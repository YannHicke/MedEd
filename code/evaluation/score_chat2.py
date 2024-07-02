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
import extract_excerpts, mirs_prompts_opro
import utils_apis
    
prompt_map = {
    "openai": "json"#,
    #"gemini": "string",
    #"anthropic": "string",
    #"cohere": "string",
    #"together": "string"
}

def score_checklist(transcript, category, items):
    pass

def get_excerpts(transcript, conversation_file):

    # Remove .txt extension from conversation_file
    case_name = os.path.splitext(conversation_file)[0]
    # Ensure the output directory exists
    output_dir = os.path.join("./excerpts/", case_name)
    os.makedirs(output_dir, exist_ok=True)

    for item_key, item_prompt in extract_excerpts.mirs_items.items():
        print(f"\n\nItem: {item_key}")

        combined_prompt = extract_excerpts.instructions_start + item_prompt + extract_excerpts.instructions_end
        response = utils_apis.openai_api_call(combined_prompt, transcript, response_type=None)
        print(f"\n\nExcerpt: {response.choices[0].message.content}")

        output_file_path = os.path.join(output_dir, f"{item_key}.txt")
        with open(output_file_path, 'w') as output_file:
            output_file.write(response.choices[0].message.content)

def score_mirs(transcript, examples, model_list, score_from_excerpts=False, case_name=None):
    scores = {}
    explanations = {}
    for model in model_list:
        scores[model] = {}
        explanations[model] = {}

    json_prompts = get_prompts_call_map(examples, "json")
    for item, _ in json_prompts.items():
        print(f"\n\nItem: {item}")

        if score_from_excerpts:
            # Remove .txt extension from conversation_file
            case = os.path.splitext(case_name)[0]
            # Ensure the directory exists
            output_dir = os.path.join("./excerpts/", case)
            os.makedirs(output_dir, exist_ok=True)

            # Read the transcript from the appropriate .txt file
            transcript_file_path = os.path.join(output_dir, f"{item}.txt")
            with open(transcript_file_path, 'r') as file:
                transcript = file.read().strip()

        for model in model_list:
            print(f"\n\nModel: {model}")
            # Define prompt, api call, and parse response
            prompt = get_prompts_call_map(examples, prompt_map[model])[item]
            api_call = api_call_map.get(model)
            parse_response = parse_json if prompt_map[model] == "json" else parse_string

            # Call the API and parse response
            #response = api_call(transcript, prompt)
            combined_prompt = mirs_prompts_opro.instructions_start + prompt + mirs_prompts_opro.instructions_end
            response = utils_apis.openai_api_call(combined_prompt, transcript, response_type=None)
            score, explanation = parse_response(response)

            # print results
            print(f"\n\nScore: {score}, \n\nExplanation: {explanation}")

            # Store in scores and explanations
            scores[model][item] = score
            explanations[model][item] = explanation


    # Store results into a dataframe
    results = pd.DataFrame.from_dict(scores[model_list[0]], orient="index", columns=[f"scores_{model_list[0]}"])
    results[f"explanations_{model_list[0]}"] = pd.Series(explanations[model_list[0]])
    for model in model_list[1:]:
        results[f"scores_{model}"] = pd.Series(scores[model])
        results[f"explanations_{model}"] = pd.Series(explanations[model])

    # Save the dataframe to a csv file
    case_name = case_name.removesuffix(".txt")
    csv_file_name = f"./results/mirs_scores_{case_name}.csv" if case_name else "./results/mirs_scores_opro.csv"
    results.to_csv(csv_file_name)


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
    print("Extract excerpts: ", config["extract_excerpts"])
    print("Score from excerpts: ", config["score_from_excerpts"])
    print("Score conversation with MIRS rubric: ", config["mirs"])
    print("Score conversation with checklist: ", config["checklist"])
    print("Model List: ", config["model_list"])
    print("############################################################\n\n")

    if config["extract_excerpts"]:
        get_excerpts(transcript, config["conversation_file"])

    if config["mirs"]:
        score_mirs(transcript, config["examples"], config["model_list"], config["score_from_excerpts"], config["conversation_file"])
