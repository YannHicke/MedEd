import json
import pandas as pd

mapping = {"openai": "gpt-4o", 
           "fireworks": "Llama",
           "anthropic": "Claude",
           "gemini": "Gemini"}

# conversation_files = ["case1.txt", "case2.txt", "case3.txt", "case4.txt", "dental1.txt", "dental2.txt", "dental3.txt", "behavioral1.txt", "behavioral2.txt", "behavioral3.txt"]

with open(f"./mapping_items_to_score.json", 'r') as file:
        mapping_items_to_score = json.load(file)

ground_truth_dir = "/Users/yannhicke/Desktop/Research/llm-med-ed-digital-platform/code/evaluation/results/ground_truth"
columns = ["Casename", "Question", "Consensus Answer", "gpt-4o zero shot", "gpt-4o few shot", "gpt-4o multistep", "Llama zero shot", "Llama few shot", "Llama multistep", "Gemini zero shot", "Gemini few shot", "Gemini multistep", "Claude zero shot", "Claude few shot", "Claude multistep"]
cases = ["Case1", "Case2", "Case3", "Case4", "Dental1", "Dental2", "Dental3", "Behavioral1", "Behavioral2", "Behavioral3"]
questions = ["OPENING", "ELICITS SPECTRUM OF CONCERNS", "NEGOTIATES PRIORITIES & SETS AGENDA", "ELICITING THE NARRATIVE THREAD or the PATIENT_S STORY", "TIMELINE", "ORGANIZATION", "TRANSITIONAL STATEMENTS", "PACING OF INTERVIEW", "QUESTIONING SKILLS - TYPES OF QUESTIONS", "QUESTIONING SKILLS - SUMMARIZING", "QUESTIONING SKILLS - DUPLICATION", "QUESTIONING SKILLS - LACK OF JARGON", "QUESTIONING SKILLS - VERIFICATION OF PATIENT INFORMATION", "INTERACTIVE TECHNIQUES", "VERBAL FACILITATION SKILLS", "NON-VERBAL FACILITATION SKILLS", "EMPATHY AND ACKNOWLEDGING PATIENT CUES", "PATIENTS PERSPECTIVE & BELIEFS", "IMPACT OF ILLNESS ON PATIENT AND PATIENT_S SELF-IMAGE", "IMPACT OF ILLNESS ON FAMILY", "SUPPORT SYSTEMS", "PATIENTS EDUCATION AND UNDERSTANDING", "ASSESS MOTIVATION FOR CHANGES", "ADMITTING LACK OF KNOWLEDGE", "INFORMED CONSENT FOR INVESTIGATIONS & PROCEDURES", "ACHIEVE A SHARED PLAN", "ENCOURAGEMENT OF QUESTIONS", "CLOSURE"]
multi_index = pd.MultiIndex.from_product([questions, cases], names=['Question', 'Casename'])
new_results = pd.DataFrame(index=multi_index, columns=columns)

results_scores = new_results.copy()
results_explanations = new_results.copy()

# Techniques = ["few shot", "zero shot", "multistep"]
Techniques = ["zero shot"]
Techniques_mapping = {"few shot": "", "zero shot": "_noExamples", "multistep": "_multi_step"}

for case in cases:
    ground_truth_df = pd.read_csv(f"{ground_truth_dir}/{case.lower()}.csv", index_col=0)
    for item in ground_truth_df.index:
        results_scores.loc[(item, case), "Consensus Answer"] = ground_truth_df.loc[item, "Consensus Answer"]
    
    for technique in Techniques:
        results_file = pd.read_csv(f"./results/v2/mirs_scores_{case.lower()}.txt_final{Techniques_mapping[technique]}.csv")
        results_file.set_index("Unnamed: 0", inplace=True)

        for model in mapping.keys():
            column_name = f"{mapping[model]} {technique}"
            for item in questions:
                if item not in mapping_items_to_score[case.lower() + ".txt"] or item in ["PACING OF INTERVIEW", "NON-VERBAL FACILITATION SKILLS"]:
                    results_scores.loc[(item, case), column_name] = "-"
                    results_explanations.loc[(item, case), column_name] = "-"
                    if not item in ["PACING OF INTERVIEW", "NON-VERBAL FACILITATION SKILLS"]:
                        results_scores.loc[(item, case), "Consensus Answer"] = "-"
                        results_explanations.loc[(item, case), "Consensus Answer"] = "-"
                else:
                    column_name_results_score = f"scores_{model}"
                    column_name_results_explanation = f"explanations_{model}"
                    score = pd.to_numeric(results_file.loc[item, column_name_results_score], errors='coerce')
                    results_scores.loc[(item, case), column_name] = score if pd.notna(score) else "-"
                    results_explanations.loc[(item, case), column_name] = results_file.loc[item, column_name_results_explanation]


breakpoint()
results_scores = results_scores.reset_index()
results_explanations = results_explanations.reset_index()
breakpoint()