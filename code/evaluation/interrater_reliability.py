"""
interrater_reliability.py 
-------------------------
This script calculates the inter-rater reliability between the consensus answer and the models' predictions.
"""

import os
import sys

import krippendorff
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


from utils import get_metadata


# Link to the root directory of the project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Threshold for the maximum permissible difference between the consensus answer and the prediction
THRESHOLD = [2,3]


def krippendorff_alpha(ratings, level_of_measurement="ordinal"):
    """
    Calculate Krippendorff's alpha for given ratings, considering missing values.

    Parameters:
    - ratings: A 2D list or array-like structure where rows represent different raters and columns represent items.
    - level_of_measurement: The level of measurement for the ratings. Options include:
        - "nominal"
        - "ordinal"
        - "interval"
        - "ratio"
    
    Returns:
    - alpha: The Krippendorff's alpha coefficient.
    """
    # Convert ratings to a numpy array for compatibility
    ratings_array = np.array(ratings, dtype=np.float64)

    # Ensure that missing values are represented as np.nan (if they are not already)
    ratings_array = np.where(np.isnan(ratings_array), np.nan, ratings_array)

    # Calculate Krippendorff's alpha with the chosen level of measurement
    alpha = krippendorff.alpha(reliability_data=ratings_array, level_of_measurement=level_of_measurement)

    return alpha
    

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

    # kappa_cleaned = cohen_kappa_score(consensus, gpt4)
    # kappa_weighted = cohen_kappa_score(consensus, gpt4, weights='linear')
    # kappa_weighted_quadratic = cohen_kappa_score(consensus, gpt4, weights='quadratic')

    adjusted_gpt4 = measure_scores(consensus, gpt4)
    # kappa_adjusted = cohen_kappa_score(consensus, adjusted_gpt4)

    accuracy = np.mean(consensus == gpt4)
    accuracy_off_by_one = np.mean(abs(consensus - gpt4) <= 1)

    kappa_thresholded = {}
    accuracy_thresholded = {}
    for threshold in THRESHOLD:
        consensus_thresholded = (consensus > threshold).astype(int)
        gpt4_thresholded = (gpt4 > threshold).astype(int)
        # kappa_thresholded[threshold] = cohen_kappa_score(consensus_thresholded, gpt4_thresholded)
        accuracy_thresholded[threshold] = np.mean(consensus_thresholded == gpt4_thresholded)

    ratings = np.array([consensus, gpt4])
    # krippendorff_alpha_nominal = krippendorff_alpha(ratings, level_of_measurement="nominal")
    krippendorff_alpha_ordinal = krippendorff_alpha(ratings, level_of_measurement="ordinal")
    # krippendorff_alpha_interval = krippendorff_alpha(ratings, level_of_measurement="interval")
    # krippendorff_alpha_ratio = krippendorff_alpha(ratings, level_of_measurement="ratio")

    results = {
        # 'Cohen\'s kappa': kappa_cleaned,
        # 'Weighted kappa (linear)': kappa_weighted,
        # 'Weighted kappa (quadratic)': kappa_weighted_quadratic,
        # 'Adjusted kappa': kappa_adjusted,
        # f'Thresholded kappa {THRESHOLD[0]}': kappa_thresholded[THRESHOLD[0]],
        # f'Thresholded kappa {THRESHOLD[1]}': kappa_thresholded[THRESHOLD[1]],
        f'Accuracy thresholded {THRESHOLD[0]}': accuracy_thresholded[THRESHOLD[0]],
        # f'Accuracy thresholded {THRESHOLD[1]}': accuracy_thresholded[THRESHOLD[1]],
        'Accuracy': accuracy,
        'Accuracy off by 1': accuracy_off_by_one,
        # 'Krippendorff\'s alpha (nominal)': krippendorff_alpha_nominal,
        # 'Krippendorff\'s alpha (interval)': krippendorff_alpha_interval,
        # 'Krippendorff\'s alpha (ratio)': krippendorff_alpha_ratio,
        'Krippendorff\'s alpha (ordinal)': krippendorff_alpha_ordinal
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
        # 'Cohen\'s kappa', 'Weighted kappa (linear)', 'Weighted kappa (quadratic)', 
        # 'Adjusted kappa', f'Thresholded kappa {THRESHOLD[0]}', f'Thresholded kappa {THRESHOLD[1]}',
        # 'Krippendorff\'s alpha (nominal)', 'Krippendorff\'s alpha (interval)', 
        'Krippendorff\'s alpha (ordinal)',
        # 'Krippendorff\'s alpha (ratio)', 
        'Accuracy', f'Accuracy thresholded {THRESHOLD[0]}', 
        # f'Accuracy thresholded {THRESHOLD[1]}', 
        'Accuracy off by 1'
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