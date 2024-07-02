from together import Together
from openai import OpenAI
import google.generativeai as genai
import anthropic
import cohere
import time
from google.api_core.exceptions import ResourceExhausted
import os
import json
import random
from mirs_prompts import mirs_prompts
from mirs_prompts_opro import mirs_prompts_opro
from nojson_mirs_prompts import nojson_mirs_prompts
from mirs_prompts_noExamples import mirs_prompts_noExamples
from nojson_mirs_prompts_noExamples import nojson_mirs_prompts_noExamples

# initialize models
client_openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
#client_together = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
#genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
#client_anthropic = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
#co = cohere.Client(os.environ["COHERE_API_KEY"])


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


def anthropic_api_call(transcript, prompt):
    response_anthropic = client_anthropic.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system=prompt,
        messages=[
            {"role": "user", "content": transcript} 
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


def parse_json(response):
    try:
        score = json.loads(response.choices[0].message.content)["score"]
        score = score.replace('"', '').strip() # remove additional quotations if present
        explanation = json.loads(response.choices[0].message.content)["explanation"]
    except:
        score = "N/A"
        explanation = response.choices[0].message.content

    return score, explanation

def parse_string(response):
    try:
        score = response.text.split("Score: ")[1].split("\n")[0]
        explanation = response.text.split("Explanation: ")[1].split("\n")[0]
    except:
        score = "N/A"
        explanation = response.text

    return score, explanation


api_call_map = {
    "openai": openai_api_call,
    "gemini": gemini_api_call,
    "anthropic": anthropic_api_call,
    "cohere": cohere_api_call,
    "together": together_api_call
}

def get_prompts_call_map(examples, prompt_type):
    if examples:
        if prompt_type == "json":
            return mirs_prompts_opro
        elif prompt_type == "string":
            return nojson_mirs_prompts
    else:
        if prompt_type == "json":
            return mirs_prompts_noExamples
        elif prompt_type == "string":
            return nojson_mirs_prompts_noExamples
