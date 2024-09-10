"""
merge_results.py
----------------
Merge the results for the selected dataset.
"""

import os
import json
import sys

import pandas as pd

from utils import get_metadata, load_mirs_items


# Link to the root directory of the project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def merge_results(data_path):
    """
    Merge the results for the selected dataset.

    Parameters:
        data_path (str): The path to the directory of conversation files.

    Returns: 
        None
    """
    # Load the mapping of MIRS items to evaluate for each case
    with open(os.path.join(data_path, 'mapping_items_to_score.json'), 'r') as f:
        mapping_items_to_score = json.load(f)

    # Load dataset information
    dataset_name = data_path.split('/')[-1]
    ground_truth_dir = os.path.join(data_path, 'ground_truth')
    columns, techniques, models, model_map = get_metadata()
    cases = os.listdir(os.path.join(data_path, 'cases'))
    questions, nontextual = load_mirs_items()

    multi_index = pd.MultiIndex.from_product([questions, cases], names=['Question', 'Casename'])
    new_results = pd.DataFrame(index=multi_index, columns=columns)
    results_scores = new_results.copy()
    results_explanations = new_results.copy()

    # Combine DataFrames
    for case in cases:
        ground_truth_df = pd.read_csv(f"{ground_truth_dir}/{case.lower()}.csv", index_col=0)
        for item in ground_truth_df.index:
            results_scores.loc[(item, case), "Consensus Answer"] = ground_truth_df.loc[item, "Consensus Answer"]
        
        # Iterate through each technique
        for technique in techniques:
            stripped_technique = technique.lower().replace(" ", "")
            results_path = os.path.join(ROOT_DIR, 'results', dataset_name, f"mirs_scores_{case.lower()}.txt_final_{stripped_technique}.csv")
            results_file = pd.read_csv(results_path)
            results_file.set_index("Unnamed: 0", inplace=True)

            # Iterate through each model
            for model in models:
                column_name = f"{model} {technique}"
                for item in questions:
                    # Fill in non-existent column data
                    if item not in mapping_items_to_score[case.lower() + ".txt"] or item in nontextual:
                        results_scores.loc[(item, case), column_name] = "-"
                        results_explanations.loc[(item, case), column_name] = "-"
                        if item not in nontextual:
                            results_scores.loc[(item, case), "Consensus Answer"] = "-"
                            results_explanations.loc[(item, case), "Consensus Answer"] = "-"
                    # Fill in existing data
                    else:
                        column_name_results_score = f"scores_{model_map[model]}"
                        column_name_results_explanation = f"explanations_{model_map[model]}"
                        score = pd.to_numeric(results_file.loc[item, column_name_results_score], errors='coerce')
                        results_scores.loc[(item, case), column_name] = score if pd.notna(score) else "-"
                        results_explanations.loc[(item, case), column_name] = results_file.loc[item, column_name_results_explanation]

    # Modify the DataFrames
    results_scores = results_scores.reset_index()
    results_explanations = results_explanations.reset_index()

    results_scores['Casename'] = pd.Categorical(results_scores['Casename'], categories=cases, ordered=True)
    results_scores['Question'] = pd.Categorical(results_scores['Question'], categories=questions, ordered=True)

    results_explanations['Casename'] = pd.Categorical(results_explanations['Casename'], categories=cases, ordered=True)
    results_explanations['Question'] = pd.Categorical(results_explanations['Question'], categories=questions, ordered=True)

    results_scores = results_scores.sort_values(by=["Casename", "Question"])
    results_explanations = results_explanations.sort_values(by=["Casename", "Question"])

    # Save the merged results
    results_scores.to_csv(os.path.join(ROOT_DIR, 'results', dataset_name, 'mirs_scores_final.csv'), index=False)
    results_explanations.to_csv(os.path.join(ROOT_DIR, 'results', dataset_name, 'mirs_explanations_final.csv'), index=False)
    print(f'\nMerged. Results saved to `results/{dataset_name}` folder.\n\n')


if __name__ == "__main__":
    # Get data path from user input
    datasets = os.listdir(os.path.join(ROOT_DIR, 'data'))

    print('\n\n- - - - - MERGING - - - - -\n\n')
    
    # Display datasets with associated numbers
    print("Please select the number corresponding to the dataset you'd like to use:\n")
    for idx, dataset in enumerate(datasets, start=1):
        print(f"\t{idx}. {dataset}")
    
    # Get the user's input
    selected_num = input("\nEnter the number of the dataset: ").strip()

    # Validate the input and convert to an integer
    try:
        selected_num = int(selected_num)
        if 1 <= selected_num <= len(datasets):
            merge_data = datasets[selected_num - 1]
        else:
            sys.exit('Invalid number selected. Exiting...')
    except ValueError:
        sys.exit('Invalid input. Exiting...')

    # Merge results for the selected dataset
    merge_results(os.path.join(ROOT_DIR, 'data', merge_data))