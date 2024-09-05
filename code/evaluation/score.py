import sys
import os
import json
import pandas as pd
import traceback
# from checklist_prompts import checklist
from utils_apis import (
    api_call_map,
    parse_call_map, 
    parse_json, 
    get_prompts_call_map,
    prompt_map
)
from utils import get_excerpts, save_results, load_config

def score_checklist(transcript, category, items):
    pass

def score_mirs(transcript, examples, model_list, file_name, score_from_excerpts=False):
    case_name = os.path.splitext(file_name)[0]
    scores = {}
    explanations = {}
    for model in model_list:
        scores[model] = {}
        explanations[model] = {}

    intermediary_file_name = f"./results/v2/mirs_scores_{file_name}_intermediary{'_multi_step' if score_from_excerpts else '_noExamples' if not examples else ''}.csv"

    # Check if intermediary file exists and load it
    if os.path.exists(intermediary_file_name):
        print(f"Resuming from intermediary file: {intermediary_file_name}")
        intermediary_df = pd.read_csv(intermediary_file_name, index_col=0)
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
                if score_from_excerpts:
                    # Remove .txt extension from conversation_file
                    case = os.path.splitext(case_name)[0]
                    # Ensure the directory exists
                    output_dir = os.path.join("./excerpts/", model, case)
                    # Read the transcript from the appropriate .txt file
                    transcript_file_path = os.path.join(output_dir, f"{item}.txt")
                    with open(transcript_file_path, 'r') as file:
                        transcript = file.read().strip() 
                # Skip if this item-model pair has already been processed
                if item in scores[model] and scores[model][item] not in ["Error", "Not scored"]:
                    print(f"Skipping already processed item: {item} for model: {model}")
                    continue

                print(f"\n\nModel: {model}")
                prompt = get_prompts_call_map(examples, prompt_map[model])[item]
                if not examples:
                    if len(prompt.split("Examples:")) > 1:
                        prompt = prompt.split("Examples:")[0].strip() + '\n\nNow, please evaluate the following medical interview transcript:\n'
                    else:
                        prompt = prompt.strip()
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
                save_results(scores, explanations, model_list, intermediary_file_name)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()
    finally:
        # Save final results
        final_file_name = f"./results/v2/mirs_scores_{file_name}_final{'_multi_step' if score_from_excerpts else '_noExamples' if not examples else ''}.csv"
        save_results(scores, explanations, model_list, final_file_name)


if __name__ == "__main__":

    # Load the configuration file
    config = load_config()

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
        print("Extract excerpts: ", config["extract_excerpts"])
        print("Score from excerpts: ", config["score_from_excerpts"])
        print("Score conversation with Mirs rubric: ", config["mirs"])
        print("Score conversation with checklist: ", config["checklist"])
        print("Model List: ", config["model_list"])
        print("############################################################\n\n")

        if config["extract_excerpts"]:
            get_excerpts(transcript, file_name, config["model_list"])

        if config["mirs"]:
            score_mirs(transcript, config["examples"], config["model_list"], file_name, config["score_from_excerpts"])


    print("All conversations have been scored.")