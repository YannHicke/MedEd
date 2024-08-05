from together import Together
from openai import OpenAI
import google.generativeai as genai
from fireworks.client import Fireworks
import anthropic
import cohere
import time
from google.api_core.exceptions import ResourceExhausted
import os
import json
import random
from mirs_prompts import mirs_prompts
from nojson_mirs_prompts import nojson_mirs_prompts
from mirs_prompts_noExamples import mirs_prompts_noExamples
from nojson_mirs_prompts_noExamples import nojson_mirs_prompts_noExamples

from dotenv import load_dotenv
load_dotenv()

# initialize models
client_openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client_together = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
client_anthropic = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
co = cohere.Client(os.environ["COHERE_API_KEY"])
client_fireworks = Fireworks(api_key=os.environ["FIREWORKS_API_KEY"])


def openai_api_call(transcript, prompt):
    response_openai = client_openai.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": prompt},
                {"role": "user", "content": transcript}]
    )
    # print(prompt)
    return response_openai


def gemini_api_call(transcript, prompt):
    model_gemini = genai.GenerativeModel(
        "models/gemini-1.5-pro-latest",
        system_instruction=prompt,
    )
    attempt = 0
    while attempt < 5:
        try:
            response_gemini = model_gemini.generate_content(transcript)
            break
        except ResourceExhausted:
            print(f"Resource exhausted on attempt {attempt + 1}")
            time.sleep((2 ** attempt) + (random.randint(0, 1000) / 1000))  # Exponential backoff with jitter
            attempt += 1

    if attempt == 5:
        response_gemini.text = None  # or handle as appropriate if max retries exceeded

    return response_gemini


claude_sys_prompt = """
You are an expert evaluator of medical interviews conducted by medical students. 
Your task is to analyze interview transcripts and provide detailed assessments on various aspects of the interview process. 
For each evaluation task, you will:

1. Carefully read the provided transcript.
2. Analyze specific aspects of the interview as requested.
3. Provide a detailed reasoning for your evaluation, citing specific examples from the transcript.
4. Assign a score based on the given rubric.
"""

def anthropic_api_call(transcript, prompt):
    # print("system prompt\n\n", claude_sys_prompt)
    # print("messages\n\n", prompt.replace("{TRANSCRIPT}", transcript))
    # print("Start Assistant message\n\n", "I've carefully reviewed the provided medical interview transcript. Based on the evaluation criteria outlined in the prompt, I'll now provide a detailed analysis and scoring. Let's begin with the reasoning for my evaluation:")
    breakpoint()
    response_anthropic = client_anthropic.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system=claude_sys_prompt,
        messages=[
            {"role": "user", "content": prompt.replace("{TRANSCRIPT}", transcript)},
            {"role": "assistant", "content": "I've carefully reviewed the provided medical interview transcript. Based on the evaluation criteria outlined in the prompt, I'll now provide a detailed analysis and scoring. Let's begin with the reasoning for my evaluation:"} 
        ]
    )
    return response_anthropic


def cohere_api_call(transcript, prompt):
    response_cohere = co.chat(
    model="command-r-plus",
    message=transcript,
    preamble=prompt)

    return response_cohere


def together_api_call(transcript, prompt):
    response_together = client_together.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[{"role": "system", "content": prompt},
            {"role": "user", "content": transcript}],
        )
    
    return response_together

def fireworks_api_call(transcript, prompt):
    response_fireworks = client_fireworks.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p1-405b-instruct",
        messages=[{"role": "user", "content": prompt},
        {"role": "user", "content": transcript}]
    )
    return response_fireworks


def parse_json(response):
    try:
        score = json.loads(response)["score"]
    except:
        score = "N/A"
    try:
        explanation = json.loads(response)["justification"]
    except:
        explanation = response

    return score, explanation


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

def parse_gemini(response):
    return response.text

def parse_cohere(response):
    return response.text

def parse_fireworks(response):
    return response.choices[0].message.content



api_call_map = {
    "openai": openai_api_call,
    "gemini": gemini_api_call,
    "anthropic": anthropic_api_call,
    "cohere": cohere_api_call,
    "together": together_api_call,
    "fireworks": fireworks_api_call
}

parse_call_map = {
    "openai": parse_openai,
    "gemini": parse_gemini,
    "anthropic": parse_anthropic,
    "cohere": parse_cohere,
    "together": parse_together,
    "fireworks": parse_fireworks
}

def get_prompts_call_map(examples, prompt_type):
    if examples:
        if prompt_type == "json":
            return mirs_prompts
        elif prompt_type == "string":
            return nojson_mirs_prompts
    else:
        if prompt_type == "json":
            return mirs_prompts_noExamples
        elif prompt_type == "string":
            return nojson_mirs_prompts_noExamples