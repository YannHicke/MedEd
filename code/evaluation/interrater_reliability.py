import pandas as pd
from sklearn.metrics import cohen_kappa_score
import numpy as np
import matplotlib.pyplot as plt
# import krippendorff
from scipy.stats import chi2_contingency
import pandas as pd

THRESHOLD = 2

def krippendorff_alpha(ratings, level_of_measurement="nominal"):
    """
    Compute Krippendorff's alpha for inter-rater reliability.
    
    :param ratings: A list of arrays representing ratings from different coders. 
                    Each array is one coder's ratings.
    :param level_of_measurement: The level of measurement: "nominal", "ordinal", "interval", or "ratio".
                                 Default is "nominal".
    :return: Krippendorff's alpha as a float.
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
    n_raters, n_items = ratings.shape

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


# Load the newly uploaded CSV file
file_path = '/Users/yannhicke/Desktop/Research/llm-med-ed-digital-platform/code/evaluation/results/v2/mirs_scores_final.csv'
data_new = pd.read_csv(file_path)

# Check the first few rows and column names
data_new.head(), data_new.columns

# columns = ["scores_anthropic", "scores_fireworks", "scores_gemini", "scores_openai"]
columns = ['Consensus Answer', 'gpt-4o zero shot',
       'gpt-4o few shot', 'gpt-4o multistep', 'Llama zero shot',
       'Llama few shot', 'Llama multistep', 'Gemini zero shot',
       'Gemini few shot', 'Gemini multistep', 'Claude zero shot',
       'Claude few shot', 'Claude multistep']

columns = ['Consensus Answer', 'gpt-4o zero shot', 'Llama zero shot', 'Gemini zero shot', 'Claude zero shot']

# for column in columns:
#     # print(column)
#     print(data_new[column].value_counts())
#     print(len(data_new[column]))
#     print("\n\n")


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

# Re-attempt the calculation after cleaning
# consensus_cleaned = data_cleaned['Consensus Answer']
# gpt4_cleaned_zero_shot = data_cleaned['gpt-4o zero shot']
# gpt4_cleaned_few_shot = data_cleaned['gpt-4o few shot']
# gpt4_cleaned_multistep = data_cleaned['gpt-4o multistep']
# claude_cleaned_zero_shot = data_cleaned['Claude zero shot']
# claude_cleaned_few_shot = data_cleaned['Claude few shot']
# claude_cleaned_multistep = data_cleaned['Claude multistep']
# llama_cleaned_zero_shot = data_cleaned['Llama zero shot']
# llama_cleaned_few_shot = data_cleaned['Llama few shot']
# llama_cleaned_multistep = data_cleaned['Llama multistep']
# gemini_cleaned_zero_shot = data_cleaned['Gemini zero shot']
# gemini_cleaned_few_shot = data_cleaned['Gemini few shot']
# gemini_cleaned_multistep = data_cleaned['Gemini multistep']


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

# models = ['gpt-4o zero shot', 'gpt-4o few shot', 'gpt-4o multistep', 
#           'Claude zero shot', 'Claude few shot', 'Claude multistep',
#           'Llama zero shot', 'Llama few shot', 'Llama multistep',
#           'Gemini zero shot', 'Gemini few shot', 'Gemini multistep']

models = ['gpt-4o zero shot', 'Llama zero shot', 'Gemini zero shot', 'Claude zero shot']

    

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

# export results
breakpoint()
results_df = pd.DataFrame(results).transpose()
results_df.to_csv("interrater_reliability_results.csv")

# chi_squared_results = pd.DataFrame(index=models, columns=models)

# for model1 in models:
#     for model2 in models:
#         # if model1 != model2:
#             # Create a contingency table for the two models
#             contingency_table = pd.crosstab(data_cleaned[model1], data_cleaned[model2])
            
#             # Perform Chi-Squared test
#             chi2, p, dof, ex = chi2_contingency(contingency_table)
            
#             # Store the Chi-Squared value in the DataFrame
#             chi_squared_results.loc[model1, model2] = chi2

# # Export the Chi-Squared results to CSV
# chi_squared_results.to_csv("chi_squared_results.csv")

# # Create a contingency table between two columns
# contingency_table = pd.crosstab(data_cleaned['gpt-4o zero shot'].dropna(), data_cleaned['Claude zero shot'].dropna())

# # Perform Chi-Squared test
# chi2, p, dof, ex = chi2_contingency(contingency_table)

# # Print the results
# print(f'Chi-Squared: {chi2}, p-value: {p}, Degrees of Freedom: {dof}')



# calculate_kappa_scores(consensus_cleaned, gpt4_cleaned_zero_shot, "GPT4 Zero Shot")
# calculate_kappa_scores(consensus_cleaned, gpt4_cleaned_few_shot, "GPT4 Few Shot")
# calculate_kappa_scores(consensus_cleaned, gpt4_cleaned_multistep, "GPT4 Multistep")
# calculate_kappa_scores(consensus_cleaned, claude_cleaned_zero_shot, "Claude Zero Shot")
# calculate_kappa_scores(consensus_cleaned, claude_cleaned_few_shot, "Claude Few Shot")
# calculate_kappa_scores(consensus_cleaned, claude_cleaned_multistep, "Claude Multistep")
# calculate_kappa_scores(consensus_cleaned, llama_cleaned_zero_shot, "Llama Zero Shot")
# calculate_kappa_scores(consensus_cleaned, llama_cleaned_few_shot, "Llama Few Shot")
# calculate_kappa_scores(consensus_cleaned, llama_cleaned_multistep, "Llama Multistep")
# calculate_kappa_scores(consensus_cleaned, gemini_cleaned_zero_shot, "Gemini Zero Shot")
# calculate_kappa_scores(consensus_cleaned, gemini_cleaned_few_shot, "Gemini Few Shot")
# calculate_kappa_scores(consensus_cleaned, gemini_cleaned_multistep, "Gemini Multistep")

# Calcualte agreement between GPT4 and other models
# calculate_kappa_scores(gpt4_cleaned_zero_shot, claude_cleaned_zero_shot, "GPT4 Zero Shot vs Claude Zero Shot", score_list=["adjusted"])
# calculate_kappa_scores(gpt4_cleaned_zero_shot, llama_cleaned_zero_shot, "GPT4 Zero Shot vs Llama Zero Shot", score_list=["adjusted"])
# calculate_kappa_scores(gpt4_cleaned_zero_shot, gemini_cleaned_zero_shot, "GPT4 Zero Shot vs Gemini Zero Shot", score_list=["adjusted"])




