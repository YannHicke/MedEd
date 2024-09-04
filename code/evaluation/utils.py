import extract_excerpts
import utils_apis
import os
import pandas as pd
from typing import Dict, List
import time
import json
import argparse
import yaml

LENGTH_MINIMUM = 100
NUM_RETRIES = 1

def get_excerpts(transcript, conversation_file, model_list):
    with open(f"./mapping_items_to_score.json", 'r') as file:
        mapping_items_to_score = json.load(file)

    # Remove .txt extension from conversation_file
    case_name = os.path.splitext(conversation_file)[0]
    # Ensure the output directory exists
    for model in model_list:
        output_dir = os.path.join("./excerpts/", model, case_name)
        os.makedirs(output_dir, exist_ok=True)

    for item_key, item_prompt in extract_excerpts.mirs_items.items():
        if item_key not in mapping_items_to_score[conversation_file]:
            print(f"Skipping item: {item_key} as it's not in mapping_items_to_score for {conversation_file}")
            continue
        print(f"\n\nItem: {item_key}")
        for model in model_list:
            print(f"Model: {model}")
            if model == "anthropic":
                api_call = utils_apis.api_call_map["anthropic_excerpt"]
            else:
                api_call = utils_apis.api_call_map[model]
            parse_response = utils_apis.parse_call_map[model]
            output_file_path = os.path.join("./excerpts/", model, case_name, f"{item_key}.txt")

            # Check if the excerpt file already exists
            if os.path.exists(output_file_path) and (excerpt_content := open(output_file_path, 'r').read()) and "Not applicable" not in excerpt_content and len(excerpt_content) > 100:
                print(f"Excerpt for {item_key}, {model} already exists. Skipping API call.")
                continue
                # print(f"\n\nExisting Excerpt: {existing_content}")
                # print("")
            else:
                if os.path.exists(output_file_path) and (excerpt_content := open(output_file_path, 'r').read()):
                    # print(excerpt_content)
                    # print("Let's retry once more")
                    # if "Not applicable" in excerpt_content or len(excerpt_content) < LENGTH_MINIMUM:
                    #     print("Move on for now ")
                        # breakpoint()
                    # time.sleep(3)
                    continue
                else:
                    excerpt_content = ""
                retry_count = 0
                while ("Not applicable" in excerpt_content or len(excerpt_content) < LENGTH_MINIMUM) and retry_count < NUM_RETRIES:
                    combined_prompt = extract_excerpts.instructions_start + item_prompt + extract_excerpts.instructions_end
                    if model == "openai":
                        response = api_call(transcript, combined_prompt, response_type=None)
                    else:
                        response = api_call(transcript, combined_prompt)
                    excerpt_content = parse_response(response)
                    if excerpt_content and "Not applicable" in excerpt_content:
                        print("Excerpt is still not applicable: ")
                        print(excerpt_content)
                        time.sleep(3)
                        retry_count += 1
                    elif excerpt_content and len(excerpt_content) < LENGTH_MINIMUM:
                        print("Excerpt is too short: ")
                        print(excerpt_content)
                        time.sleep(3)
                        retry_count += 1
                    else:
                        if retry_count > NUM_RETRIES:
                            print(f"Excerpt is still not applicable after {NUM_RETRIES} retries. Skipping API call.")
                            time.sleep(3)
                        else:
                            break

                print(f"\n\nNew Excerpt: {excerpt_content}")

                with open(output_file_path, 'w') as output_file:
                    if excerpt_content:
                        output_file.write(excerpt_content)

def create_results_dataframe(scores, explanations, model_list):
    results = pd.DataFrame.from_dict(scores[model_list[0]], orient="index", columns=[f"scores_{model_list[0]}"])
    results[f"explanations_{model_list[0]}"] = pd.Series(explanations[model_list[0]])
    for model in model_list[1:]:
        results[f"scores_{model}"] = pd.Series(scores[model])
        results[f"explanations_{model}"] = pd.Series(explanations[model])
    return results

def save_results(scores: Dict[str, Dict], explanations: Dict[str, Dict], model_list: List[str], file_name: str) -> None:
    """Save results to a CSV file, merging with existing results if the file exists."""
    results = create_results_dataframe(scores, explanations, model_list)
    
    if os.path.exists(file_name):
        existing_results = pd.read_csv(file_name, index_col=0)
        combined_results = pd.concat([existing_results, results], axis=1)
        combined_results = combined_results.loc[:, ~combined_results.columns.duplicated(keep='last')]   
        results = combined_results

    
    results.to_csv(file_name)

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def load_config():
    parser = argparse.ArgumentParser(description="Score medical interviews")
    parser.add_argument('--config', type=str, default='./config.yaml', help='Path to config file')
    parser.add_argument('--conversation_files', nargs='+', default=None, help='List of conversation files to process')
    parser.add_argument('--examples', type=str2bool, nargs='?', const=True, default=None, help='Provide examples')
    parser.add_argument('--extract_excerpts', type=str2bool, nargs='?', const=True, default=None, help='Extract excerpts')
    parser.add_argument('--score_from_excerpts', type=str2bool, nargs='?', const=True, default=None, help='Score from excerpts')
    parser.add_argument('--mirs', type=str2bool, nargs='?', const=True, default=None, help='Score conversation with Mirs rubric')
    parser.add_argument('--checklist', type=str2bool, nargs='?', const=True, default=None, help='Score conversation with checklist')
    parser.add_argument('--model_list', nargs='+', default=None, help='List of models to use')

    args = parser.parse_args()

    # Load the configuration file
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    # Override config with CLI arguments if provided
    for arg, value in vars(args).items():
        print(arg, value)
        if value is not None:
            config[arg] = value

    return config