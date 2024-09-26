"""
utils.py
--------
Various utility functions for scoring and evaluating conversations.
"""

import argparse
import json
import os
import time

import pandas as pd
import yaml

from typing import Dict, List

import extract_excerpts
import utils_apis


# Link to the root directory of the project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Constants for obtaining excerpts
LENGTH_MINIMUM = 100
NUM_RETRIES = 1


def get_metadata():
    """
    Get the columns, techniques, and models to use for scoring.

    Parameters:
        None

    Returns:
        columns (List[str]):        List of columns to use
        techniques (List[str]):     List of techniques to use
        models (List[str]):         List of models to use
        model_map (Dict[str, str]): Mapping of model names to their API names
    """

    # Load the configuration file information
    config = load_config(verbose=False)

    model_list = config['model_list']
    zero_shot = not config['examples']
    few_shot = config['examples'] and not config['score_from_excerpts']
    multistep = config['examples'] and config['score_from_excerpts']

    openai = "openai" in model_list
    fireworks = "fireworks" in model_list
    anthropic = "anthropic" in model_list
    gemini = "gemini" in model_list
    cohere = "cohere" in model_list
    together = "together" in model_list 

    # Determine dataset columns 
    columns = {
        'Consensus Answer': True,
        'GPT Zero Shot': openai and zero_shot, 'GPT Few Shot': openai and few_shot, 'GPT Multistep': openai and multistep,
        'Llama Zero Shot': fireworks and zero_shot, 'Llama Few Shot': fireworks and few_shot, 'Llama Multistep': fireworks and multistep,
        'Claude Zero Shot': anthropic and zero_shot, 'Claude Few Shot': anthropic and few_shot, 'Claude Multistep': anthropic and multistep,
        'Gemini Zero Shot': gemini and zero_shot, 'Gemini Few Shot': gemini and few_shot, 'Gemini Multistep': gemini and multistep,
        'Cohere Zero Shot': cohere and zero_shot, 'Cohere Few Shot': cohere and few_shot, 'Cohere Multistep': cohere and multistep,
        'Together Zero Shot': together and zero_shot, 'Together Few Shot': together and few_shot, 'Together Multistep': together and multistep
    }
    columns = [column for column in columns if columns[column]]

    # Determine techniques to use
    techniques = {
        'Zero Shot': zero_shot, 'Few Shot': few_shot, 'Multistep': multistep
    }
    techniques = [technique for technique in techniques if techniques[technique]]

    # Determine models to use
    models = {
        'GPT': openai, 'Llama': fireworks, 'Claude': anthropic, 'Gemini': gemini, 'Cohere': cohere, 'Together': together
    }
    models = [model for model in models if models[model]]
    model_map = {
        'GPT': 'openai', 'Llama': 'fireworks', 'Claude': 'anthropic', 'Gemini': 'gemini', 'Cohere': 'cohere', 'Together': 'together'
    }

    return columns, techniques, models, model_map 


def load_mirs_items():
    """
    Load the MIRS item names.

    Parameters:
        None

    Returns:
        items (List[str]): List of MIRS item names
        nontextual (List[str]): List of MIRS items that are nontextual
    """

    items = [
        "OPENING", "ELICITS SPECTRUM OF CONCERNS", "NEGOTIATES PRIORITIES & SETS AGENDA", 
        "ELICITING THE NARRATIVE THREAD or the PATIENT_S STORY", "TIMELINE", "ORGANIZATION", 
        "TRANSITIONAL STATEMENTS", "PACING OF INTERVIEW", "QUESTIONING SKILLS TYPES OF QUESTIONS", 
        "QUESTIONING SKILLS SUMMARIZING", "QUESTIONING SKILLS DUPLICATION", "QUESTIONING SKILLS LACK OF JARGON", 
        "QUESTIONING SKILLS VERIFICATION OF PATIENT INFORMATION", "INTERACTIVE TECHNIQUES", "VERBAL FACILITATION SKILLS", 
        "NON-VERBAL FACILITATION SKILLS", "EMPATHY AND ACKNOWLEDGING PATIENT CUES", "PATIENTS PERSPECTIVE & BELIEFS", 
        "IMPACT OF ILLNESS ON PATIENT AND PATIENT_S SELF-IMAGE", "IMPACT OF ILLNESS ON FAMILY", "SUPPORT SYSTEMS", 
        "PATIENTS EDUCATION AND UNDERSTANDING", "ASSESS MOTIVATION FOR CHANGES", "ADMITTING LACK OF KNOWLEDGE", 
        "INFORMED CONSENT FOR INVESTIGATIONS & PROCEDURES", "ACHIEVE A SHARED PLAN", "ENCOURAGEMENT OF QUESTIONS", "CLOSURE"
    ]
    nontextual = ["PACING OF INTERVIEW", "NON-VERBAL FACILITATION SKILLS"]

    return items, nontextual


def get_excerpts(transcript, conversation_file, model_list, dataset_path):
    """
    Get excerpts relevant to each item in the MIRS rubric for a given conversation transcript.

    Parameters:
        transcript (str):           The conversation transcript to score.
        conversation_file (str):    The name of the conversation file.
        model_list (list):          The list of models to score.

    Returns:
        None
    """
    with open(os.path.join(dataset_path, 'mapping_items_to_score.json'), 'r') as file:
        mapping_items_to_score = json.load(file)

    # Remove .txt extension from conversation_file
    dataset = dataset_path.split('/')[-1]
    case_name = os.path.splitext(conversation_file)[0]

    # Ensure the output directories exist
    for model in model_list:
        output_dir = os.path.join(ROOT_DIR, 'results', dataset, 'excerpts', model, case_name)
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
            output_file_path = os.path.join(ROOT_DIR, 'results', dataset, 'excerpts', model, case_name, f"{item_key}.txt")

            # Check if the excerpt file already exists
            if os.path.exists(output_file_path) and (excerpt_content := open(output_file_path, 'r').read()) and "Not applicable" not in excerpt_content and len(excerpt_content) > 100:
                print(f"Excerpt for {item_key}, {model} already exists. Skipping API call.")
                continue
            else:
                if os.path.exists(output_file_path) and (excerpt_content := open(output_file_path, 'r').read()):
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
    """
    Create a DataFrame from the scores and explanations dictionaries.

    Parameters:
        scores (Dict[str, Dict]):       Dictionary of scores for each model
        explanations (Dict[str, Dict]): Dictionary of explanations for each model
        model_list (List[str]):         List of models used

    Returns:
        results (pd.DataFrame):         DataFrame containing scores and explanations for each model
    """
    results = pd.DataFrame.from_dict(scores[model_list[0]], orient="index", columns=[f"scores_{model_list[0]}"])
    results[f"explanations_{model_list[0]}"] = pd.Series(explanations[model_list[0]])
    for model in model_list[1:]:
        results[f"scores_{model}"] = pd.Series(scores[model])
        results[f"explanations_{model}"] = pd.Series(explanations[model])
    return results


def save_results(scores: Dict[str, Dict], explanations: Dict[str, Dict], model_list: List[str], file_name: str) -> None:
    """
    Save results to a CSV file, merging with existing results if the file exists.

    Parameters:
        scores (Dict[str, Dict]):       Dictionary of scores for each model
        explanations (Dict[str, Dict]): Dictionary of explanations for each model
        model_list (List[str]):         List of models used
        file_name (str):                Path to the file to save

    Returns: 
        None
    """
    results = create_results_dataframe(scores, explanations, model_list)

    path_components = file_name.split('/')[:-1]
    root_dir = '/'.join(path_components)
    if not os.path.isdir(root_dir): 
        os.makedirs(root_dir)

    if os.path.exists(file_name):
        existing_results = pd.read_csv(file_name, index_col=0)
        combined_results = pd.concat([existing_results, results], axis=1)
        combined_results = combined_results.loc[:, ~combined_results.columns.duplicated(keep='last')]   
        results = combined_results

    results.to_csv(file_name)


def str2bool(v):
    """
    Convert string to boolean.

    Parameters:
        v (str): String to convert to boolean

    Returns:
        bool: Converted boolean value
    """
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def load_config(verbose=True):
    """
    Load the configuration file and override with CLI arguments if provided.

    Parameters:
        None    

    Returns:
        config (Dict): Configuration
    """
    parser = argparse.ArgumentParser(description="Score medical interviews")
    parser.add_argument('--config', type=str, default='../../setup/config.yml', help='Path to config file')
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
        if verbose:
            print(arg, value)
        if value is not None:
            config[arg] = value

    return config