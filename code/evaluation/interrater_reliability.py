"""
interrater_reliability.py 
-------------------------
This script calculates the inter-rater reliability between the consensus answer and the models' predictions.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import yaml

from sklearn.metrics import cohen_kappa_score


# Link to the root directory of the project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Threshold for the maximum permissible difference between the consensus answer and the prediction
THRESHOLD = 2


def krippendorff_alpha(ratings, level_of_measurement="nominal"):
    """
    Compute Krippendorff's alpha for inter-rater reliability.
    
    Parameters:
    - ratings:              A list of arrays representing ratings from different coders. 
                            Each array is one coder's ratings.
    - level_of_measurement: The level of measurement: "nominal", "ordinal", "interval", or "ratio".
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
    

def model_metadata():
    # Load in model information
    config_file = os.path.join(ROOT_DIR, 'setup', 'config.yml')
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    # Determine models 
    openai = True if 'openai' in config['model_list'] else False
    llama = True if 'llama' in config['model_list'] else False
    gemini = True if 'gemini' in config['model_list'] else False
    claude = True if 'claude' in config['model_list'] else False
    cohere = True if 'cohere' in config['model_list'] else False
    together = True if 'together' in config['model_list'] else False

    # Determine evaluation type
    zero_shot = ~config['examples']
    few_shot = config['examples']
    multistep = config['extract_excerpts'] and config['score_from_excerpts']

    column_data = {
        'Consensus Answer': True,
        'GPT Zero-Shot': openai and zero_shot, 'GPT Few-Shot': openai and few_shot, 'GPT Multi-Step': openai and multistep,
        'Llama Zero-Shot': llama and zero_shot, 'Llama Few-Shot': llama and few_shot, 'Llama Multi-Step': llama and multistep,
        'Gemini Zero-Shot': gemini and zero_shot, 'Gemini Few-Shot': gemini and few_shot, 'Gemini Multi-Step': gemini and multistep,
        'Claude Zero-Shot': claude and zero_shot, 'Claude Few-Shot': claude and few_shot, 'Claude Multi-Step': claude and multistep,
        'Cohere Zero-Shot': cohere and zero_shot, 'Cohere Few-Shot': cohere and few_shot, 'Cohere Multi-Step': cohere and multistep,
        'Together Zero-Shot': together and zero_shot, 'Together Few-Shot': together and few_shot, 'Together Multi-Step': together and multistep
    }

    columns = [column for column in column_data if column_data[column]]
    models = [column for column in columns if column != 'Consensus Answer']

    return columns, models


def evaluate():
    file_path = os.path.join(ROOT_DIR, 'results')


columns, models = model_metadata()


# Load the newly uploaded CSV file
# TODO: Fix results path
file_path = '/Users/yannhicke/Desktop/Research/llm-med-ed-digital-platform/code/evaluation/results/v2/mirs_scores_final.csv'
data_new = pd.read_csv(file_path)

# Check the first few rows and column names
data_new.head(), data_new.columns



# Define a function to adjust ratings
def adjust_scores(consensus, model):
    """Consider scores that are one unit apart as agreeing."""
    return np.where(abs(consensus - model) <= 1, consensus, model)


# Check for NaN values in both columns
missing_values = data_new[columns + ["Consensus Answer"]].isnull().sum()
print("Missing values in the columns: ", missing_values.iloc[0], missing_values.iloc[1])

# Remove rows with NaN values
data_cleaned = data_new.dropna(subset=columns + ["Consensus Answer"])

for column in columns:
    data_cleaned[column] = pd.to_numeric(data_cleaned[column], errors='coerce')

data_cleaned = data_cleaned.dropna(subset=columns)

def calculate_kappa_scores(consensus, gpt4, evaluator_name, comparand, score_list=["kappa", "linear", "quadratic", "adjusted", "thresholded", "krippendorff", "accuracy"]):

    kappa_cleaned = cohen_kappa_score(consensus, gpt4)
    kappa_weighted = cohen_kappa_score(consensus, gpt4, weights='linear')
    kappa_weighted_quadratic = cohen_kappa_score(consensus, gpt4, weights='quadratic')

    adjusted_gpt4 = adjust_scores(consensus, gpt4)
    kappa_adjusted = cohen_kappa_score(consensus, adjusted_gpt4)

    accuracy = np.mean(consensus == gpt4)
    accuracy_off_by_one = np.mean(abs(consensus - gpt4) <= 1)

    consensus_thresholded = (consensus > THRESHOLD).astype(int)
    gpt4_thresholded = (gpt4 > THRESHOLD).astype(int)
    kappa_thresholded = cohen_kappa_score(consensus_thresholded, gpt4_thresholded)
    accuracy_thresholded = np.mean(consensus_thresholded == gpt4_thresholded)
   
    ratings = np.array([consensus, gpt4])
    krippendorff_alpha_nominal = krippendorff_alpha(ratings, level_of_measurement="nominal")
    krippendorff_alpha_ordinal = krippendorff_alpha(ratings, level_of_measurement="ordinal")
    krippendorff_alpha_interval = krippendorff_alpha(ratings, level_of_measurement="interval")
    krippendorff_alpha_ratio = krippendorff_alpha(ratings, level_of_measurement="ratio")

    return {
        'Cohen\'s kappa': kappa_cleaned,
        'Weighted kappa (linear)': kappa_weighted,
        'Weighted kappa (quadratic)': kappa_weighted_quadratic,
        'Adjusted kappa': kappa_adjusted,
        'Thresholded kappa': kappa_thresholded,
        'Accuracy': accuracy,
        'Accuracy thresholded': accuracy_thresholded,
        'Accuracy off by 1': accuracy_off_by_one,
        'Krippendorff\'s alpha (nominal)': krippendorff_alpha_nominal,
        'Krippendorff\'s alpha (ordinal)': krippendorff_alpha_ordinal,
        'Krippendorff\'s alpha (interval)': krippendorff_alpha_interval,
        'Krippendorff\'s alpha (ratio)': krippendorff_alpha_ratio
    }

    

results = {}
for metric in ['Cohen\'s kappa', 'Weighted kappa (linear)', 'Weighted kappa (quadratic)', 
               'Adjusted kappa', 'Thresholded kappa', 'Accuracy', 'Accuracy thresholded', 
               'Accuracy off by 1', 'Krippendorff\'s alpha (nominal)', 
               'Krippendorff\'s alpha (ordinal)', 'Krippendorff\'s alpha (interval)', 
               'Krippendorff\'s alpha (ratio)']:
    results[metric] = pd.DataFrame(index=models, columns=models)

# for model1 in models:
#     for model2 in models:
#         if model1 != model2:
#             scores = calculate_kappa_scores(data_cleaned[model1], data_cleaned[model2], model1, model2, score_list=["adjusted"])
#             for metric, value in scores.items():
#                 results[metric].loc[model1, model2] = value

# # export results to csv (only the accuracy off by 1)
# results['Accuracy off by 1'].to_csv("interrater_reliability_results.csv")

# Calculate the agreement between the consensus and each model
results = {}
for metric in ['Cohen\'s kappa', 'Weighted kappa (linear)', 'Weighted kappa (quadratic)', 
               'Adjusted kappa', 'Thresholded kappa', 'Accuracy', 'Accuracy thresholded', 
               'Accuracy off by 1', 'Krippendorff\'s alpha (nominal)', 
               'Krippendorff\'s alpha (ordinal)', 'Krippendorff\'s alpha (interval)', 
               'Krippendorff\'s alpha (ratio)']:
    results[metric] = {}

for model in models:
    scores = calculate_kappa_scores(data_cleaned["Consensus Answer"], data_cleaned[model], model, "Consensus Answer")
    for metric, value in scores.items():
        results[metric][model] = value

# export results to csv
results_df = pd.DataFrame(results).transpose()
results_df.to_csv("interrater_reliability_results.csv")



