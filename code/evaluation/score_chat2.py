import sys
import os
import argparse
import json
import pandas as pd
from checklist_prompts import checklist
from utils_apis import (
    api_call_map,
    parse_call_map, 
    parse_json, 
    parse_string, 
    get_prompts_call_map
)
import yaml
    
prompt_map = {
    "openai": "json",
    "gemini": "json",
    "anthropic": "string",
    "cohere": "string",
    "together": "json",
    "fireworks": "json"
}

def score_checklist(transcript, category, items):
    pass

def score_mirs(transcript, examples, model_list, file_name):
    scores = {}
    explanations = {}
    for model in model_list:
        scores[model] = {}
        explanations[model] = {}

    with open(f"./mapping_items_to_score.json", 'r') as file:
        mapping_items_to_score = json.load(file)

    json_prompts = get_prompts_call_map(examples, "json")
    for item, _ in json_prompts.items():
        # if item not in mapping_items_to_score[file_name]:
        #     for model in model_list:
        #         scores[model][item] = "Not scored"
        #         explanations[model][item] = "Not scored"
        #         print(f"Skipping item: {item} for model: {model}")
        #     continue
        print(f"\n\nItem: {item}")
        for model in model_list:
            print(f"\n\nModel: {model}")
            # Define prompt, api call, and parse response
            prompt = get_prompts_call_map(examples, prompt_map[model])[item]
            # prompt = get_prompts_call_map(examples, "json")[item]
            api_call = api_call_map.get(model)
            parse_response_model = parse_call_map.get(model)
            parse_response = (
                (lambda response: parse_json(parse_response_model(response)))
                if prompt_map[model] == "json"
                else (lambda response: parse_string(parse_response_model(response)))
            )            

            # Call the API and parse response
            response = api_call(transcript, prompt)
            score, explanation = parse_response(response)
            breakpoint()

            # print results
            print(f"\n\nScore: {score}, \n\nExplanation: {explanation}")
            # print(f"\n\nPrompt: {prompt}")

            # Store in scores and explanations
            scores[model][item] = score
            explanations[model][item] = explanation
            breakpoint()


    # Store results into a dataframe
    results = pd.DataFrame.from_dict(scores[model_list[0]], orient="index", columns=[f"scores_{model_list[0]}"])
    results[f"explanations_{model_list[0]}"] = pd.Series(explanations[model_list[0]])
    for model in model_list[1:]:
        results[f"scores_{model}"] = pd.Series(scores[model])
        results[f"explanations_{model}"] = pd.Series(explanations[model])


    # Save the dataframe to a csv file
    results.to_csv(f"./results/mirs_scores_{file_name}_test_gemini.csv")


if __name__ == "__main__":

    # Load the configuration file
    with open("./config.yaml", 'r') as file:
        config = yaml.safe_load(file)

    # Check if the conversation file exists
    for file_name in config["conversation_files"]:
        file_path = os.path.join("../simulation/conversation_history/UConn/", file_name)
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_name}' does not exist.")
            sys.exit(1)

    # Load the transcript
    for file_name in config["conversation_files"]:
        file_path = os.path.join("../simulation/conversation_history/UConn/", file_name)
        with open(file_path, 'r') as file:
            transcript = file.read().strip()

        transcript = transcript.replace("User:", "Physician:").replace("Assistant:", "Patient:") #TODO: make it more systematic

        # Print the configuration
        print("\n\n############################################################")
        print("Scoring conversation file: ", file_name)
        print("Examples provided: ", config["examples"])
        print("Score conversation with Mirs rubric: ", config["mirs"])
        print("Score conversation with checklist: ", config["checklist"])
        print("Model List: ", config["model_list"])
        print("############################################################\n\n")

        if config["mirs"]:
            score_mirs(transcript, config["examples"], config["model_list"], file_name)

    print("All conversations have been scored.")