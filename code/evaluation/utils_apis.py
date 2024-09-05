from together import Together
from openai import OpenAI
import google.generativeai as genai
from fireworks.client import Fireworks
import anthropic
import cohere
import time
from google.api_core.exceptions import ResourceExhausted
import re
import os
import json
import random
from mirs_prompts import mirs_prompts

from dotenv import load_dotenv
load_dotenv()

MAX_ATTEMPTS = 15

# initialize models
client_openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client_together = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
client_anthropic = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
co = cohere.Client(os.environ["COHERE_API_KEY"])
client_fireworks = Fireworks(api_key=os.environ["FIREWORKS_API_KEY"])
print("GOOGLE_API_KEY", os.environ.get("GOOGLE_API_KEY"))


def openai_api_call(transcript, prompt, response_type="json_object"):
    if response_type:
        response_openai = client_openai.chat.completions.create(
            model="gpt-4o",
            response_format={"type": response_type},
            messages=[{"role": "system", "content": prompt},
                      {"role": "user", "content": transcript}],
            temperature=0  # for reproducibility
        )
    else:
        response_openai = client_openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt},
                      {"role": "user", "content": transcript}],
            temperature=0 #for reproducibility
        )
    return response_openai


def gemini_api_call(transcript, prompt):
    model_gemini = genai.GenerativeModel(
        "models/gemini-1.5-pro-exp-0801",
        system_instruction=prompt,
    )
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            response_gemini = model_gemini.generate_content(transcript)
            break
        except ResourceExhausted:
            print(f"Resource exhausted on attempt {attempt + 1}")
            backoff_time = (2 ** attempt) * 2  # Doubled the base time
            jitter = random.uniform(0, backoff_time / 2)  # Increased jitter range
            sleep_time = backoff_time + jitter
            print(f"Retrying in {sleep_time:.2f} seconds")
            time.sleep(sleep_time)
            attempt += 1

    if attempt == MAX_ATTEMPTS:
        response_gemini = None  # or handle as appropriate if max retries exceeded

    return response_gemini


# claude_sys_prompt = """
# You are an expert evaluator of medical interviews conducted by medical students. 
# Your task is to analyze interview transcripts and provide detailed assessments on various aspects of the interview process. 
# For each evaluation task, you will:

# 1. Carefully read the provided transcript.
# 2. Analyze specific aspects of the interview as requested.
# 3. Provide a detailed reasoning for your evaluation, citing specific examples from the transcript.
# 4. Assign a score based on the given rubric.
# """

def anthropic_api_call(transcript, prompt):
    response_anthropic = client_anthropic.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system=prompt,
        messages=[
            {"role": "user", "content": transcript},
            {"role": "assistant", "content": """Here is the json output formatted the following way: 
{
  "evaluation": {
    "elements_present": [
      "List of relevant elements present in the transcript"
    ],
    "elements_absent": [
      "List of relevant elements missing from the transcript"
    ],
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the excerpt to support your evaluation"
  }
}"""}
        ]
    )
    if "Not applicable" in transcript and not response_anthropic.content:
        return 1, "Not applicable"
    response_anthropic = client_anthropic.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system="Now parse the following output and return the score and justification only",
        messages=[{"role": "user", "content": response_anthropic.content[0].text}]
    )
    return parse_score_justification(response_anthropic.content[0].text)

def anthropic_api_call_excerpt(transcript, prompt):
    response_anthropic = client_anthropic.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system=prompt,
        messages=[{"role": "user", "content": transcript}]
    )
    return response_anthropic


def cohere_api_call(transcript, prompt):
    response_cohere = co.chat(
    model="command-r-plus",
    message=transcript,
    preamble=prompt)

    return response_cohere


def together_api_call(transcript, prompt):
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            response_together = client_together.chat.completions.create(
                model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
                messages=[{"role": "system", "content": prompt},
                {"role": "user", "content": transcript}],
            )
            break
        except ResourceExhausted:
            print(f"Resource exhausted on attempt {attempt + 1}")
            backoff_time = (2 ** attempt) * 2  # Doubled the base time
            jitter = random.uniform(0, backoff_time / 2)  # Increased jitter range
            sleep_time = backoff_time + jitter
            print(f"Retrying in {sleep_time:.2f} seconds")
            time.sleep(sleep_time)
            attempt += 1

    return response_together

def fireworks_api_call(transcript, prompt):
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            response_fireworks = client_fireworks.chat.completions.create(
                model="accounts/fireworks/models/llama-v3p1-405b-instruct",
                messages=[{"role": "user", "content": prompt},
                {"role": "user", "content": transcript}]
            )
            break
        except ResourceExhausted:
            print(f"Resource exhausted on attempt {attempt + 1}")
            backoff_time = (2 ** attempt) * 2  # Doubled the base time
            jitter = random.uniform(0, backoff_time / 2)  # Increased jitter range
            sleep_time = backoff_time + jitter
            print(f"Retrying in {sleep_time:.2f} seconds")
            time.sleep(sleep_time)
            attempt += 1

    return response_fireworks


def parse_json(response):
    # Extract the JSON part from the response
    json_start = re.search(r'\{', response)
    if json_start:
        response = response[json_start.start():]
    
    # Attempt to load the JSON data while handling possible extra data after the JSON
    try:
        # Find the end of the JSON object
        json_end = re.search(r'\}\n```', response)
        if json_end:
            response = response[:json_end.end() - 3]
        
        data = json.loads(response)
    except (json.JSONDecodeError, ValueError):
        return "N/A", response

    # Function to safely extract a value from a dictionary
    def safe_get(dct, key, default="N/A"):
        try:
            return dct.get(key, default)
        except (AttributeError, KeyError):
            return default

    # Extract evaluation section
    evaluation = safe_get(data, "evaluation", {})

    # Extract score and justification safely
    score = safe_get(evaluation, "score", "N/A")
    justification = safe_get(evaluation, "justification", response)

    return score, justification


    


def parse_string(response):
    try:
        score = response.split("<score>")[1].split("</score>")[0]
    except:
        score = "N/A"
    try:
        explanation = response.split("<reasoning>")[1].split("</reasoning>")[0]
    except:
        explanation = response

    return score, explanation


def parse_openai(response):
    return response.choices[0].message.content

def parse_together(response):
    return response.choices[0].message.content

def parse_anthropic(response):
    return response.content[0].text

def parse_score_justification(text):
    # Extract the score
    score_match = re.search(r'Score:\s*(\d+)', text)
    score = int(score_match.group(1)) if score_match else None

    # Extract the justification
    justification_match = re.search(r'Justification:\s*(.*)', text, re.DOTALL)
    justification = justification_match.group(1).strip() if justification_match else None

    return score, justification

def parse_gemini(response):
    if not response:
        return response
    try:
        output = response.text
    except:
        breakpoint()
        output = "The answer was blocked by Google for safety reasons."

    return output

def parse_cohere(response):
    return response.text

def parse_fireworks(response):
    return response.choices[0].message.content


def get_prompts_call_map(examples, prompt_type):
    return mirs_prompts
    # if examples:
    #     if prompt_type == "json" or prompt_type == "json_score_justification":
    #         return mirs_prompts
    #     elif prompt_type == "string":
    #         return nojson_mirs_prompts
    # else:
    #     if prompt_type == "json" or prompt_type == "json_score_justification":
    #         return mirs_prompts_noExamples
    #     elif prompt_type == "string":
    #         return nojson_mirs_prompts_noExamples
        

api_call_map = {
    "openai": openai_api_call,
    "gemini": gemini_api_call,
    "anthropic": anthropic_api_call,
    "cohere": cohere_api_call,
    "together": together_api_call,
    "fireworks": fireworks_api_call,
    "anthropic_excerpt": anthropic_api_call_excerpt
}

parse_call_map = {
    "openai": parse_openai,
    "gemini": parse_gemini,
    "anthropic": parse_anthropic,
    "cohere": parse_cohere,
    "together": parse_together,
    "fireworks": parse_fireworks
}

prompt_map = {
    "openai": "json",
    "gemini": "json",
    "anthropic": "json_score_justification",
    "cohere": "json",
    "together": "json",
    "fireworks": "json"
}