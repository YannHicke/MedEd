import openai
import sys
import os
from openai import OpenAI
from mirs_prompts import mirs_prompts
import json
import pandas as pd
import time
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from together import Together


client = OpenAI(api_key="OPENAI_API_KEY")

client_together = Together(api_key=os.environ.get("TOGETHER_API_KEY"))


checklist = {
    "PAST MEDICAL HISTORY": [
        {"past illnesses (childhood adult)": "Determine if there was any discussion about past illnesses, including childhood and adult illnesses in the following conversation between a physician and a patient. Provide your answer in a json format with {past illnesses (childhood adult): 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"operations/injuries/accidents": "Determine if there was any discussion about operations, injuries, or accidents in the following conversation between a physician and a patient. Provide your answer in a json format with {operations/injuries/accidents: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"hospitalizations":"Determine if there was any discussion about hospitalizations in the following conversation between a physician and a patient. Provide your answer in a json format with {hospitalizations: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"immunizations":"Determine if there was any discussion about immunizations in the following conversation between a physician and a patient. Provide your answer in a json format with {immunizations: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"age-appropriate screening tests": "Determine if there was any discussion about age-appropriate screening tests in the following conversation between a physician and a patient. Provide your answer in a json format with {age-appropriate screening tests: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"OB history": "Determine if there was any discussion about OB history in the following conversation between a physician and a patient. Provide your answer in a json format with {OB history: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"psychiatric history": "Determine if there was any discussion about psychiatric history in the following conversation between a physician and a patient. Provide your answer in a json format with {psychiatric history: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
    ],
    "MEDICATIONS": [
        {"taking medications": "Determine if there was any discussion about taking medications in the following conversation between a physician and a patient. Provide your answer in a json format with {taking medications: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
    ],
    "ALLERGIES": [
        {"allergies": "Determine if there was any discussion about allergies in the following conversation between a physician and a patient. Provide your answer in a json format with {allergies: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
    ],
    "SOCIAL HISTORY": [
        {"education":"Determine if there was any discussion about the patient's education in the following conversation between a physician and a patient. Provide your answer in a json format with {education: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"social background (family household)":"Determine if there was any discussion about the patient's social background, including family and household, in the following conversation between a physician and a patient. Provide your answer in a json format with {social background (family household): 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"occupational history":"Determine if there was any discussion about the patient's occupational history in the following conversation between a physician and a patient. Provide your answer in a json format with {occupational history: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"habits (recreational drugs alcohol tobacco)":"Determine if there was any discussion about the patient's habits, including recreational drugs, alcohol, and tobacco, in the following conversation between a physician and a patient. Provide your answer in a json format with {habits (recreational drugs alcohol tobacco): 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"support systems":"Determine if there was any discussion about the patient's support systems in the following conversation between a physician and a patient. Provide your answer in a json format with {support systems: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"sexual history":"Determine if there was any discussion about the patient's sexual history in the following conversation between a physician and a patient. Provide your answer in a json format with {sexual history: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"diet history":"Determine if there was any discussion about the patient's diet history in the following conversation between a physician and a patient. Provide your answer in a json format with {diet history: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"exercise":"Determine if there was any discussion about the patient's exercise in the following conversation between a physician and a patient. Provide your answer in a json format with {exercise: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"religious or spiritual beliefs":"Determine if there was any discussion about the patient's religious or spiritual beliefs in the following conversation between a physician and a patient. Provide your answer in a json format with {religious or spiritual beliefs: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"safety (car gun fire)":"Determine if there was any discussion about the patient's safety, including car, gun, and fire safety, in the following conversation between a physician and a patient. Provide your answer in a json format with {safety (car gun fire): 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"financial concerns":"Determine if there was any discussion about the patient's financial concerns in the following conversation between a physician and a patient. Provide your answer in a json format with {financial concerns: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
    ],
    "FAMILY HISTORY": [
        {"age/health status of siblings":"Determine if there was any discussion about the age/health status of siblings in the following conversation between a physician and a patient. Provide your answer in a json format with {age/health status of siblings: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"age/health status of parents":"Determine if there was any discussion about the age/health status of parents in the following conversation between a physician and a patient. Provide your answer in a json format with {age/health status of parents: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"age/health status of grandparents":"Determine if there was any discussion about the age/health status of grandparents in the following conversation between a physician and a patient. Provide your answer in a json format with {age/health status of grandparents: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"age/health status of children":"Determine if there was any discussion about the age/health status of children in the following conversation between a physician and a patient. Provide your answer in a json format with {age/health status of children: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"check for other FH of DM HTN CA stroke or heart disease":"Determine if there was any discussion about checking for other family history of diabetes, hypertension, cancer, stroke, or heart disease in the following conversation between a physician and a patient. Provide your answer in a json format with {check for other FH of DM HTN CA stroke or heart disease: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
    ],
    "REVIEW OF SYSTEMS": [
        {"General Health":"Determine if there was any discussion about general health, including recent weight loss/gain, fever, fatigue, or other general health concerns in the following conversation between a physician and a patient. Provide your answer in a json format with {General Health: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Head, Eyes, Ears, Nose, Throat":"Determine if there was any discussion about head, eyes, ears, nose, and throat, including vision changes, hearing loss, sinus problems, sore throat, or other related concerns in the following conversation between a physician and a patient. Provide your answer in a json format with {Head, Eyes, Ears, Nose, Throat: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Pulmonary":"Determine if there was any discussion about pulmonary concerns, including breathing, cough, wheezing, shortness of breath, or other related concerns in the following conversation between a physician and a patient. Provide your answer in a json format with {Pulmonary: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Cardiovascular":"Determine if there was any discussion about cardiovascular concerns, including chest pain, palpitations, hypertension, past heart conditions, or other related concerns in the following conversation between a physician and a patient. Provide your answer in a json format with {Cardiovascular: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Gastrointestinal":"Determine if there was any discussion about gastrointestinal concerns, including stomach, liver, intestines, pain, indigestion, diarrhea, constipation, or other related concerns in the following conversation between a physician and a patient. Provide your answer in a json format with {Gastrointestinal: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Neuromuscular":"Determine if there was any discussion about neuromuscular concerns, including headaches, seizures, numbness, tingling, weakness, or other neurological symptoms in the following conversation between a physician and a patient. Provide your answer in a json format with {Neuromuscular: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Hematologic":"Determine if there was any discussion about hematologic concerns, including blood-related concerns such as history of anemia, bleeding or clotting disorders in the following conversation between a physician and a patient. Provide your answer in a json format with {Hematologic: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Genitourinary":"Determine if there was any discussion about genitourinary concerns, including kidney functions, urinary changes, reproductive health issues in the following conversation between a physician and a patient. Provide your answer in a json format with {Genitourinary: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Endocrine":"Determine if there was any discussion about endocrine concerns, including thyroid, diabetes, or other hormonal issues in the following conversation between a physician and a patient. Provide your answer in a json format with {Endocrine: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
        {"Psychiatric":"Determine if there was any discussion about psychiatric concerns, including depression, anxiety, sleep disturbances, and other mental health issues in the following conversation between a physician and a patient. Provide your answer in a json format with {Psychiatric: 'discussed' or 'not discussed', explanation: 'where it was discussed in the conversation' or 'not discussed'}."},
    ],
}

def were_category_items_discussed(transcript, category, items):
    conversation = load_context(os.path.join("../conversation_history/", transcript))

    # replace User: in the conversation with Physician: and replace Assistant: with Patient:
    conversation = conversation.replace("User:", "Physician:").replace("Assistant:", "Patient:") #TODO: make it more systematic

    item_checklist = {}

    for item in items:
        system_prompt = list(item.values())[0]
        response = client.chat.completions.create(
            model="gpt-4-0125-preview", 
            response_format={"type": "json_object"},
            messages=[{"role": "system", "content": system_prompt},
                    {"role": "user", "content": conversation}]
        )
        try:
            is_discussed = json.loads(response.choices[0].message.content)[list(item.keys())[0]]
            explanation = json.loads(response.choices[0].message.content)["explanation"]
        except:
            is_discussed = "not discussed"
            explanation = "not discussed"
        item_checklist[list(item.keys())[0]] = {"discussed": is_discussed, "explanation": explanation}




    return item_checklist


def load_context(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def score_conversation(filename):

    # Read in scorer context
    # scoring_context = load_context('../context/context_scorer2.txt')

    # Read in convo
    conversation = load_context(os.path.join("../simulation/conversation_history/UConn/", filename))

    # replace User: in the conversation with Physician: and replace Assistant: with Patient:
    conversation = conversation.replace("User:", "Physician:").replace("Assistant:", "Patient:") #TODO: make it more systematic

    def get_mirs_scores(transcript, mirs_prompts):

        scores = {}
        explanations = {}
        for item, prompt in mirs_prompts.items():
            
            # Call the OpenAI API (assuming a simplified use case)
            response = client.chat.completions.create(
            model="gpt-4-0125-preview", 
            response_format={"type": "json_object"},
            messages=[{"role": "system", "content": prompt},
                    {"role": "user", "content": transcript}]
        )
            
            # Process the response from GPT-4 (you might need to adjust based on the expected output format)
            try:
                score = json.loads(response.choices[0].message.content)["score"]
                explanation = json.loads(response.choices[0].message.content)["explanation"]
            except:
                breakpoint()
            print(f"\nItem: {item}, \nScore: {score}, \n\nExplanation:\n {explanation}")
            # Store the score with the item
            scores[item] = score
            explanations[item] = explanation
            
        return scores, explanations
    
    mirs_scores, mirs_explanations = get_mirs_scores(conversation, mirs_prompts)

    # Append the conversation to the scoring context
    # full_context = scoring_context + "\n" + conversation

    # response = client.chat.completions.create(
    #         model="gpt-4-0125-preview",
    #         messages=[{"role": "system", "content": full_context}]
    #     )
    # output_text = response.choices[0].message.content
    output_text = None

    # Ensure the results/ directory exists
    os.makedirs("../results", exist_ok=True)
    breakpoint()
    # with open(os.path.join("../results", filename), "w") as file:
    #     file.write(output_text)

    # output to csv
    df = pd.DataFrame.from_dict(mirs_scores, orient='index', columns=['score'])
    for item, score in mirs_scores.items():
        df.loc[item, 'explanation'] = mirs_explanations[item]

    df.to_csv(os.path.join("../results", filename.replace(".txt", ".csv")))

    return output_text

if __name__ == "__main__":

    conversation_file = sys.argv[1]

    # Check if the conversation file exists
    if not os.path.exists(os.path.join("../simulation/conversation_history/UConn/", conversation_file)):
        print(f"Error: The file '{conversation_file}' does not exist.")
        sys.exit(1)

    results = score_conversation(conversation_file)
    breakpoint()

    discussed_items = {category: [] for category in checklist.keys()}
    for category, items in checklist.items():
        response = were_category_items_discussed(conversation_file, category, items)
        discussed_items[category] = response

    # save the results to a json file
    with open(os.path.join("../results", conversation_file.replace(".txt", "_results.json")), "w") as file:
        json.dump(discussed_items, file, indent=4)

    # print(results)
