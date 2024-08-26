import sys
import os
import argparse
import json
import pandas as pd
import traceback
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
    "anthropic": "json_score_justification",
    "cohere": "json",
    "together": "json",
    "fireworks": "json"
}

def score_checklist(transcript, category, items):
    pass

def create_results_dataframe(scores, explanations, model_list):
    results = pd.DataFrame.from_dict(scores[model_list[0]], orient="index", columns=[f"scores_{model_list[0]}"])
    results[f"explanations_{model_list[0]}"] = pd.Series(explanations[model_list[0]])
    for model in model_list[1:]:
        results[f"scores_{model}"] = pd.Series(scores[model])
        results[f"explanations_{model}"] = pd.Series(explanations[model])
    return results

def save_intermediary_results(scores, explanations, model_list, file_name):
    results = create_results_dataframe(scores, explanations, model_list)
    intermediary_file = f"./results/mirs_scores_{file_name}_intermediary.csv"
    
    if os.path.exists(intermediary_file):
        existing_results = pd.read_csv(intermediary_file, index_col=0)
        combined_results = pd.concat([existing_results, results], axis=1)
        combined_results = combined_results.loc[:, ~combined_results.columns.duplicated(keep='last')]   
        results = combined_results
    
    results.to_csv(intermediary_file)
    

def save_final_results(scores, explanations, model_list, file_name):
    results = create_results_dataframe(scores, explanations, model_list)
    final_file = f"./results/mirs_scores_{file_name}_final.csv"
    
    if os.path.exists(final_file):
        existing_results = pd.read_csv(final_file, index_col=0)
        combined_results = pd.concat([existing_results, results], axis=1)
        combined_results = combined_results.loc[:, ~combined_results.columns.duplicated(keep='last')]
        results = combined_results
    
    results.to_csv(final_file)

def score_mirs(transcript, examples, model_list, file_name):
    scores = {}
    explanations = {}
    for model in model_list:
        scores[model] = {}
        explanations[model] = {}

    intermediary_file = f"./results/mirs_scores_{file_name}_intermediary.csv"
    
    # Check if intermediary file exists and load it
    if os.path.exists(intermediary_file):
        print(f"Resuming from intermediary file: {intermediary_file}")
        intermediary_df = pd.read_csv(intermediary_file, index_col=0)
        for model in model_list:
            score_col = f"scores_{model}"
            explanation_col = f"explanations_{model}"
            if score_col in intermediary_df.columns and explanation_col in intermediary_df.columns:
                scores[model] = intermediary_df[score_col].dropna().to_dict()
                explanations[model] = intermediary_df[explanation_col].dropna().to_dict()
            else:
                print(f"Warning: Columns for model '{model}' not found in intermediary file. Starting fresh for this model.")
                scores[model] = {}
                explanations[model] = {}

    with open(f"./mapping_items_to_score.json", 'r') as file:
        mapping_items_to_score = json.load(file)

    json_prompts = get_prompts_call_map(examples, "json")
    
    try:
        for item, _ in json_prompts.items():
            if item not in mapping_items_to_score[file_name]:
                print(f"Skipping item: {item} as it's not in mapping_items_to_score for {file_name}")
                for model in model_list:
                    scores[model][item] = "Not scored"
                    explanations[model][item] = "Not in mapping_items_to_score"
                continue

            print(f"\n\nItem: {item}")
            for model in model_list:
                # Skip if this item-model pair has already been processed
                if item in scores[model] and scores[model][item] not in ["Error", "Not scored"]:
                    print(f"Skipping already processed item: {item} for model: {model}")
                    continue

                print(f"\n\nModel: {model}")
                prompt = get_prompts_call_map(examples, prompt_map[model])[item]
                api_call = api_call_map.get(model)
                parse_response_model = parse_call_map.get(model)
                parse_response = (
                    (lambda response: parse_json(parse_response_model(response)))
                    if prompt_map[model] == "json"
                    else (lambda response: response)
                )            

                try:
                    response = api_call(transcript, prompt)
                    score, explanation = parse_response(response)
                    if score == "N/A":
                        raise ValueError("Score is N/A")
                    
                    print(f"\n\nScore: {score}, \n\nExplanation: {explanation}")
                    
                    scores[model][item] = score
                    explanations[model][item] = explanation
                except Exception as e:
                    print(f"Error processing item {item} for model {model}: {str(e)}")
                    scores[model][item] = "Error"
                    explanations[model][item] = str(e)

                
                # Save intermediary results after each item-model pair
                save_intermediary_results(scores, explanations, model_list, file_name)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()
    finally:
        # Save final results
        save_final_results(scores, explanations, model_list, file_name)


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