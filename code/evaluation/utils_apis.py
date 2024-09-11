import json
import os
import random
import re
import time

import anthropic
import cohere
import google.generativeai as genai
import yaml

from dotenv import load_dotenv
from fireworks.client import Fireworks
from google.api_core.exceptions import ResourceExhausted
from openai import OpenAI
from together import Together

from mirs_prompts import mirs_prompts


# Link to the root directory of the project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Maximum number of attempts for API calls
MAX_ATTEMPTS = 15


# Load the API keys
load_dotenv()


# Initialize the models
with open(os.path.join(ROOT_DIR, 'setup', 'config.yml'), 'r') as file:
    config = yaml.safe_load(file)

for model in config["model_list"]:
    if "openai" in model:
        client_openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    if "together" in model:
        client_together = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
    if "gemini" in model:
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    if "anthropic" in model:
        client_anthropic = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    if "cohere" in model:
        co = cohere.Client(os.environ["COHERE_API_KEY"])
    if "fireworks" in model:
        client_fireworks = Fireworks(api_key=os.environ["FIREWORKS_API_KEY"])


# - - - - - API CALL FUNCTIONALITY - - - - - #

def openai_api_call(transcript, prompt, response_type="json_object", temperature=1e-19):
    """
    Call the OpenAI API with the given transcript and prompt.

    Parameters:
        transcript (str):    The conversation transcript to send to the API.
        prompt (str):        The prompt to send to the API.
        response_type (str): The type of response to request from the API.
        temperature (float): The temperature to use for the API response.

    Returns:
        response_openai: The response from the OpenAI API.
    """
    if response_type:
        response_openai = client_openai.chat.completions.create(
            model="gpt-4o",
            response_format={"type": response_type},
            messages=[{"role": "system", "content": prompt},
                      {"role": "user", "content": transcript}],
            temperature=temperature  # lower for reproducibility
        )
    else:
        response_openai = client_openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt},
                      {"role": "user", "content": transcript}],
            temperature=temperature # lower for reproducibility
        )
    return response_openai


def gemini_api_call(transcript, prompt):
    """
    Call the Google Gemini API with the given transcript and prompt.

    Parameters:
        transcript (str):    The conversation transcript to send to the API.
        prompt (str):        The prompt to send to the API.

    Returns:    
        response_gemini: The response from the Google Gemini API.
    """
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


def anthropic_api_call(transcript, prompt):
    """
    Call the Anthropic API with the given transcript and prompt.

    Parameters:
        transcript (str):    The conversation transcript to send to the API.
        prompt (str):        The prompt to send to the API.

    Returns:        
        response_anthropic: The response from the Anthropic API.
    """

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
    """
    Call the Anthropic API with the given transcript and prompt.

    Parameters:
        transcript (str):    The conversation transcript to send to the API.
        prompt (str):        The prompt to send to the API.

    Returns:        
        response_anthropic: The response from the Anthropic API.
    """
    response_anthropic = client_anthropic.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system=prompt,
        messages=[{"role": "user", "content": transcript}]
    )
    return response_anthropic


def cohere_api_call(transcript, prompt):
    """
    Call the Cohere API with the given transcript and prompt.

    Parameters:
        transcript (str):    The conversation transcript to send to the API.
        prompt (str):        The prompt to send to the API.

    Returns:    
        response_cohere: The response from the Cohere API.
    """
    response_cohere = co.chat(
    model="command-r-plus",
    message=transcript,
    preamble=prompt)

    return response_cohere


def together_api_call(transcript, prompt):
    """
    Call the Together API with the given transcript and prompt.

    Parameters:
        transcript (str):    The conversation transcript to send to the API.
        prompt (str):        The prompt to send to the API.

    Returns:
        response_together: The response from the Together API.
    """
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
    """
    Call the Fireworks API with the given transcript and prompt.

    Parameters:
        transcript (str):    The conversation transcript to send to the API.
        prompt (str):        The prompt to send to the API.

    Returns:
        response_fireworks: The response from the Fireworks API
    """
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


# - - - - - RESPONSE PARSING FUNCTIONALITY - - - - - #

def parse_json(response):
    """
    Parse the JSON response from the API and extract the score and justification.

    Parameters:
        response (str): The JSON response from the API.

    Returns:    
        score:         The score extracted from the response.
        justification: The justification extracted from the response.
    """
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
    """
    Parse the string response from the API and extract the score and justification.

    Parameters:
        response (str): The string response from the API.

    Returns:
        score:           The score extracted from the response.
        justification:   The justification extracted from the response.
    """
    try:
        score = response.split("<score>")[1].split("</score>")[0]
    except:
        score = "N/A"
    try:
        justification = response.split("<reasoning>")[1].split("</reasoning>")[0]
    except:
        justification = response

    return score, justification


def parse_openai(response):
    """
    Read the OpenAI response and return the content.

    Parameters:
        response: The response from the OpenAI API.

    Returns:
        The content of the response.
    """
    return response.choices[0].message.content


def parse_together(response):
    """
    Read the Together response and return the content.

    Parameters:
        response: The response from the Together API.

    Returns:
        The content of the response.
    """
    return response.choices[0].message.content


def parse_anthropic(response):
    """
    Read the Anthropic response and return the content.

    Parameters:
        response: The response from the Anthropic API.

    Returns:
        The content of the response.
    """
    return response.content[0].text


def parse_score_justification(text):
    """
    Parse the score and justification from the text.

    Parameters:
        text (str): The text to parse.

    Returns:    
        score:         The score extracted from the text.
        justification: The justification extracted from the text.
    """
    # Extract the score
    score_match = re.search(r'Score:\s*(\d+)', text)
    score = int(score_match.group(1)) if score_match else None

    # Extract the justification
    justification_match = re.search(r'Justification:\s*(.*)', text, re.DOTALL)
    justification = justification_match.group(1).strip() if justification_match else None

    return score, justification


def parse_gemini(response):
    """
    Read the Gemini response and return the content.

    Parameters: 
        response: The response from the Gemini API.

    Returns:
        The content of the response.
    """
    if not response:
        return response
    try:
        output = response.text
    except:
        breakpoint()
        output = "The answer was blocked by Google for safety reasons."

    return output


def parse_cohere(response):
    """
    Read the Cohere response and return the content.

    Parameters:
        response: The response from the Cohere API.

    Returns:
        The content of the response.
    """
    return response.text


def parse_fireworks(response):
    """
    Read the Fireworks response and return the content.

    Parameters:
        response: The response from the Fireworks API.

    Returns:    
        The content of the response
    """
    return response.choices[0].message.content
        

# - - - - - MAPPINGS - - - - - #

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

def get_prompts_call_map(examples, prompt_type):
    return mirs_prompts