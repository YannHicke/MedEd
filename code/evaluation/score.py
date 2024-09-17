"""
score.py 
--------
Evaluate the conversation transcripts using the MIRS rubric.
"""

import json
import os
import sys
import traceback

import pandas as pd

from utils import get_excerpts, save_results, load_config
from utils_apis import (
    api_call_map,
    parse_call_map, 
    parse_json, 
    get_prompts_call_map,
    prompt_map
)


# Link to the root directory of the project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def score_mirs_single_case(transcript, model_list, file_name, data_path, examples, 
                           score_from_excerpts=False, overwrite=False):
    """
    Score a single case using the MIRS rubric.

    Parameters:
        transcript (str):           The conversation transcript to score.
        model_list (list):          The list of models to score.
        file_name (str):            The name of the conversation file.
        data_path (str):            The path to the directory of conversation files.
        examples (bool):            Whether to include examples in the prompt.
        score_from_excerpts (bool): Whether to score from excerpts.
    """
    # Initialize case information
    scores = {}
    explanations = {}
    for model in model_list:
        scores[model] = {}
        explanations[model] = {}

    # Write intermediary/final file paths for storing progress
    case_name = data_path.split('/')[-1]
    eval_type = 'multistep' if score_from_excerpts else 'zeroshot' if not examples else 'fewshot'
    intermediary_file_name = f"mirs_scores_{file_name}_intermediary_{eval_type}.csv"
    intermediary_file_path = os.path.join(ROOT_DIR, 'results', case_name, intermediary_file_name)
    final_file_name = f"mirs_scores_{file_name}_final_{eval_type}.csv"
    final_file_path = os.path.join(ROOT_DIR, 'results', case_name, final_file_name)

    # Check if intermediary/final files already exist
    if os.path.exists(intermediary_file_path):
        file_path = intermediary_file_path
        df = pd.read_csv(intermediary_file_path, index_col=0)
        file_type = 'intermediary'
    elif os.path.exists(final_file_path):
        file_path = final_file_path
        df = pd.read_csv(final_file_path, index_col=0)
        file_type = 'final'
    else:
        file_path = None

    # Check if we resume from an existing file
    if file_path and not overwrite:
        print(f'Resuming from {file_type} file: {file_path}')
        for model in model_list:
            score_col = f"scores_{model}"
            explanation_col = f"explanations_{model}"
            if score_col in df.columns and explanation_col in df.columns:
                scores[model] = df[score_col].dropna().to_dict()
                explanations[model] = df[explanation_col].dropna().to_dict()
            else:
                print(f"Warning: Columns for model '{model}' not found in {file_type} file. Starting fresh for this model.")
                scores[model] = {}
                explanations[model] = {}

    if overwrite:
        print(f'Overwriting data for transcript {file_name}.')

    # Load mapping between cases and assessed MIRS items
    with open(os.path.join(data_path, 'mapping_items_to_score.json'), 'r') as f:
        mapping_items_to_score = json.load(f)
    json_prompts = get_prompts_call_map(examples, "json")
    
    # Begin scoring the case across the MIRS items
    try:
        for item, _ in json_prompts.items():
            if item not in mapping_items_to_score[file_name]:
                print(f"\n\nSkipping item: {item} as it's not in mapping_items_to_score for {file_name}")
                for model in model_list:
                    scores[model][item] = "Not scored"
                    explanations[model][item] = "Not in mapping_items_to_score"
                continue

            print(f"\n\nItem: {item}")

            for model in model_list:
                # Multistep scoring
                if score_from_excerpts:
                    case = os.path.splitext(case_name)[0]
                    output_dir = os.path.join(ROOT_DIR, 'code', 'evaluation', 'excerpts', model, case)
                    transcript_file_path = os.path.join(output_dir, f"{item}.txt")
                    with open(transcript_file_path, 'r') as file:
                        transcript = file.read().strip() 

                # Skip if the item has already been scored
                if item in scores[model] and scores[model][item] not in ["Error", "Not scored"]:
                    print(f"Skipping already processed item: {item} for model: {model}")
                    continue

                # Zero-shot and few-shot scoring
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
                save_results(scores, explanations, model_list, intermediary_file_path)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()

    finally:
        # Save final results
        save_results(scores, explanations, model_list, final_file_path)

        # Delete intermediary path after final results are saved
        if os.path.isfile(intermediary_file_path):
            os.remove(intermediary_file_path)


def score_mirs_all_cases(data_path):
    """
    Score all cases in the provided conversation files using the MIRS rubric.

    Parameters:
        data_path (str): The path to the directory conversation files.
    """ 
    # Load the configuration file
    config = load_config(verbose=False)

    # Check if the conversation file exists
    for file_name in config["conversation_files"]:
        file_path = os.path.join(data_path, 'conversation_history', file_name)
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_name}' does not exist.")
            sys.exit(1)

    overwrite = input('Do you want to overwrite existing scores? (y/n): ').strip().lower()
    if overwrite == 'y':
        overwrite = True
    else:
        overwrite = False

    # Load each transcript and evaluate it
    for file_name in config["conversation_files"]:
        file_path = os.path.join(data_path, 'conversation_history', file_name)
        with open(file_path, 'r') as file:
            transcript = file.read().strip()
            transcript = transcript.replace("User:", "Physician:").replace("Assistant:", "Patient:")

        # Print the configuration
        print("\n\n############################################################")
        print("Scoring conversation file: ", file_name)
        print("Examples provided: ", config["examples"])
        print("Extract excerpts: ", config["extract_excerpts"])
        print("Score from excerpts: ", config["score_from_excerpts"])
        print("Score conversation with MIRS rubric: ", config["mirs"])
        print("Score conversation with checklist: ", config["checklist"])
        print("Model List: ", config["model_list"])
        print("############################################################\n\n")

        if config["extract_excerpts"]:
            get_excerpts(transcript, file_name, config["model_list"], data_path)

        if config["mirs"]:
            score_mirs_single_case(transcript, config["model_list"], file_name, data_path, config["examples"], 
                                   config["score_from_excerpts"], overwrite=overwrite)

    print("\n\n- - - - -\n\nAll conversations have been scored.\n\n- - - - -\n\n")


if __name__ == "__main__":
    print('\n\n- - - - - SCORING - - - - -\n\n')

    # List all datasets in the directory
    datasets = os.listdir(os.path.join(ROOT_DIR, 'data'))

    # Display datasets with associated numbers
    print("Please select the number corresponding to the dataset you'd like to score:\n")
    for idx, dataset in enumerate(datasets, start=1):
        print(f"\t{idx}. {dataset}")
    
    # Get the user's input
    selected_num = input("\nEnter the number of the dataset: ").strip()

    # Validate the input and convert to an integer
    try:
        selected_num = int(selected_num)
        if 1 <= selected_num <= len(datasets):
            score_dataset = datasets[selected_num - 1]
        else:
            sys.exit('Invalid number selected. Exiting...')
    except ValueError:
        sys.exit('Invalid input. Please enter a number. Exiting...')

    print(f'\n\nScoring {score_dataset} dataset...\n\n')
    score_mirs_all_cases(os.path.join(ROOT_DIR, 'data', score_dataset))