"""
interrater_reliability.py 
-------------------------
This script calculates the inter-rater reliability between the consensus answer and the models' predictions.
"""

import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.metrics import cohen_kappa_score

from utils import get_metadata


# Link to the root directory of the project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Threshold for the maximum permissible difference between the consensus answer and the prediction
THRESHOLD = [2,3]


def krippendorff_alpha(ratings, level_of_measurement="nominal"):
    """
    Compute Krippendorff's alpha for inter-rater reliability.
    
    Parameters:
        ratings:              A list of arrays representing ratings from different coders. 
                              Each array is one coder's ratings.
        level_of_measurement: The level of measurement: "nominal", "ordinal", "interval", or "ratio".
                              Default is "nominal".

    Returns: 
        Krippendorff's alpha as a float.
    """
    def nominal_metric(a, b):
        return a != b

    def ordinal_metric(a, b):
        a_rank = np.argsort(np.argsort(a))
        b_rank = np.argsort(np.argsort(b))
        return (a_rank - b_rank) ** 2

    def interval_metric(a, b):
        return (a - b) ** 2

    def ratio_metric(a, b):
        return ((a - b) / (a + b)) ** 2 if (a + b) != 0 else 0

    metric = {
        "nominal": nominal_metric,
        "ordinal": ordinal_metric,
        "interval": interval_metric,
        "ratio": ratio_metric,
    }[level_of_measurement]

    ratings = np.asarray(ratings)
    _, n_items = ratings.shape

    # Mask the missing values with np.nan
    ratings = np.where(np.isnan(ratings), np.nan, ratings)

    # Calculate observed disagreement
    observed_disagreement = 0
    n_pairable = 0
    for i in range(n_items):
        item_ratings = ratings[:, i][~np.isnan(ratings[:, i])]
        n_pairable += len(item_ratings) * (len(item_ratings) - 1)
        observed_disagreement += sum(metric(ri, rj) for ri in item_ratings for rj in item_ratings if ri != rj)

    if n_pairable == 0:
        raise ValueError("No pairable values found.")

    Do = observed_disagreement / n_pairable

    # Calculate expected disagreement
    all_ratings = ratings[~np.isnan(ratings)]
    De = sum(metric(ri, rj) for ri in all_ratings for rj in all_ratings if ri != rj) / (len(all_ratings) * (len(all_ratings) - 1))

    # Calculate alpha
    if Do == De == 0:
        return 1.0
    else:
        return 1 - (Do / De)
    

def calculate_kappa_scores(consensus, gpt4):
    """
    Calculate the Cohen's kappa, weighted kappa, accuracy, and adjusted kappa scores 
    between the consensus and GPT-4 predictions.

    Parameters:
        consensus (array): The consensus answers.
        gpt4 (array):      The GPT-4 predictions.    

    Returns:
        results (dict): A dictionary of the calculated scores.
    """

    kappa_cleaned = cohen_kappa_score(consensus, gpt4)
    kappa_weighted = cohen_kappa_score(consensus, gpt4, weights='linear')
    kappa_weighted_quadratic = cohen_kappa_score(consensus, gpt4, weights='quadratic')

    adjusted_gpt4 = measure_scores(consensus, gpt4)
    kappa_adjusted = cohen_kappa_score(consensus, adjusted_gpt4)

    accuracy = np.mean(consensus == gpt4)
    accuracy_off_by_one = np.mean(abs(consensus - gpt4) <= 1)

    kappa_thresholded = {}
    accuracy_thresholded = {}
    for threshold in THRESHOLD:
        consensus_thresholded = (consensus > threshold).astype(int)
        gpt4_thresholded = (gpt4 > threshold).astype(int)
        kappa_thresholded[threshold] = cohen_kappa_score(consensus_thresholded, gpt4_thresholded)
        accuracy_thresholded[threshold] = np.mean(consensus_thresholded == gpt4_thresholded)

    ratings = np.array([consensus, gpt4])
    krippendorff_alpha_nominal = krippendorff_alpha(ratings, level_of_measurement="nominal")
    krippendorff_alpha_interval = krippendorff_alpha(ratings, level_of_measurement="interval")
    krippendorff_alpha_ratio = krippendorff_alpha(ratings, level_of_measurement="ratio")

    results = {
        'Cohen\'s kappa': kappa_cleaned,
        'Weighted kappa (linear)': kappa_weighted,
        'Weighted kappa (quadratic)': kappa_weighted_quadratic,
        'Adjusted kappa': kappa_adjusted,
        f'Thresholded kappa {THRESHOLD[0]}': kappa_thresholded[THRESHOLD[0]],
        f'Thresholded kappa {THRESHOLD[1]}': kappa_thresholded[THRESHOLD[1]],
        f'Accuracy thresholded {THRESHOLD[0]}': accuracy_thresholded[THRESHOLD[0]],
        f'Accuracy thresholded {THRESHOLD[1]}': accuracy_thresholded[THRESHOLD[1]],
        'Accuracy': accuracy,
        'Accuracy off by 1': accuracy_off_by_one,
        'Krippendorff\'s alpha (nominal)': krippendorff_alpha_nominal,
        'Krippendorff\'s alpha (interval)': krippendorff_alpha_interval,
        'Krippendorff\'s alpha (ratio)': krippendorff_alpha_ratio
    }

    return results
    

def measure_scores(consensus, model):
    """
    Measure the difference between scores.
    Consider scores that are one unit apart as agreeing.

    Parameters:
        consensus (array): The consensus answers.
        model (array):      The model predictions.

    Returns:
        The adjusted model predictions as an array.
    """
    return np.where(abs(consensus - model) <= 1, consensus, model)


def evaluate(file_path):
    """
    Evaluate and save the inter-rater reliability between the consensus answer 
    and the models' predictions.

    Parameters: 
        file_path (str): The path to the CSV file containing the data.
    
    Returns:
        None
    """
    # Load in the data
    columns, _, _, _  = get_metadata()
    models = columns[1:]
    data_new = pd.read_csv(file_path)

    # Check for and remove NaN values 
    data_cleaned = data_new.dropna(subset=columns + ["Consensus Answer"])
    for column in columns:
        data_cleaned[column] = pd.to_numeric(data_cleaned[column], errors='coerce')
    data_cleaned = data_cleaned.dropna(subset=columns)

    # Calculate the agreement between the consensus and each model
    results = {}
    for metric in [
        'Cohen\'s kappa', 'Weighted kappa (linear)', 'Weighted kappa (quadratic)', 
        'Adjusted kappa', f'Thresholded kappa {THRESHOLD[0]}', f'Thresholded kappa {THRESHOLD[1]}',
        'Krippendorff\'s alpha (nominal)', 'Krippendorff\'s alpha (interval)', 
        'Krippendorff\'s alpha (ratio)', 'Accuracy', f'Accuracy thresholded {THRESHOLD[0]}', 
        f'Accuracy thresholded {THRESHOLD[1]}', 'Accuracy off by 1'
    ]:
        results[metric] = {}

    for model in models:
        scores = calculate_kappa_scores(data_cleaned["Consensus Answer"], data_cleaned[model])
        for metric, value in scores.items():
            results[metric][model] = value

    # Export results to CSV
    results_df = pd.DataFrame(results).transpose()
    case_name = file_path.split('/')[-2]
    results_path = os.path.join(ROOT_DIR, 'results', case_name, 'interrater_reliability_results.csv')
    results_df.to_csv(results_path)

    print(f'\nEvaluation complete. Results saved under `results/{case_name}`.\n\n')


if __name__ == "__main__":
    # Get data path from user input
    datasets = os.listdir(os.path.join(ROOT_DIR, 'data'))

    print('\n\n- - - - - EVALUATING - - - - -\n\n')
    
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
            eval_data = datasets[selected_num - 1]
        else:
            sys.exit('Invalid number selected. Exiting...')
    except ValueError:
        sys.exit('Invalid input. Exiting...')

    # Evaluate the inter-rater reliability
    evaluate(os.path.join(ROOT_DIR, 'results', eval_data, 'mirs_scores_final.csv'))
