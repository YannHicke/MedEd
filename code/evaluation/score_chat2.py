import sys
import os
import argparse
import json
import pandas as pd
from checklist_prompts import checklist
from utils_apis import (
    api_call_map, 
    parse_json, 
    parse_string, 
    get_prompts_call_map
)
import yaml
    
prompt_map = {
    "openai": "json",
    "gemini": "string",
    "anthropic": "string",
    "cohere": "string",
    "together": "string"
}

def score_checklist(transcript, category, items):
    pass

def score_mirs(transcript, examples, model_list):
    scores = {}
    explanations = {}
    for model in model_list:
        scores[model] = {}
        explanations[model] = {}

    json_prompts = get_prompts_call_map(examples, "json")
    for item, _ in json_prompts.items():
        print(f"\n\nItem: {item}")
        for model in model_list:
            print(f"\n\nModel: {model}")
            # Define prompt, api call, and parse response
            prompt = get_prompts_call_map(examples, prompt_map[model])[item]
            api_call = api_call_map.get(model)
            parse_response = parse_json if prompt_map[model] == "json" else parse_string

            # Call the API and parse response
            response = api_call(transcript, prompt)
            score, explanation = parse_response(response)

            # print results
            print(f"\n\nScore: {score}, \n\nExplanation: {explanation}")

            # Store in scores and explanations
            scores[model][item] = score
            explanations[model][item] = explanation


    # Store results into a dataframe
    results = pd.DataFrame(scores[model_list[0]], orient="index", columns=f"scores_{model_list[0]}")
    results[f"explanations_{model_list[0]}"] = pd.Series(explanations[model_list[0]])
    for model in model_list[1:]:
        results[f"scores_{model}"] = pd.Series(scores[model])
        results[f"explanations_{model}"] = pd.Series(explanations[model])


    # Save the dataframe to a csv file
    results.to_csv("./results/mirs_scores.csv")


if __name__ == "__main__":

    # Load the configuration file
    with open("./config.yaml", 'r') as file:
        config = yaml.safe_load(file)

    # Check if the conversation file exists
    file_path = os.path.join("../simulation/conversation_history/UConn/", config["conversation_file"])
    if not os.path.exists(file_path):
        print(f"Error: The file '{config['conversation_file']}' does not exist.")
        sys.exit(1)

    # Load the transcript
    with open(file_path, 'r') as file:
        transcript = file.read().strip()

    transcript = transcript.replace("User:", "Physician:").replace("Assistant:", "Patient:") #TODO: make it more systematic

    # Print the configuration
    print("\n\n############################################################")
    print("Scoring conversation file: ", config["conversation_file"])
    print("Examples provided: ", config["examples"])
    print("Score conversation with Mirs rubric: ", config["mirs"])
    print("Score conversation with checklist: ", config["checklist"])
    print("Model List: ", config["model_list"])
    print("############################################################\n\n")

    if config["mirs"]:
        score_mirs(transcript, config["examples"], config["model_list"])