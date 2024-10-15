EMPATHY_AND_ACKNOWLEDGING_PATIENT_CUES = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student demonstrates empathy and acknowledges patient cues. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Identify Key Elements:**
    - As you read the transcript, create a list noting whether each element is present or absent:
      - Supportive comments regarding patient's emotions
      - Empathy demonstrated through specific techniques

  **Step 2. Scoring:**
    - As you read the transcript, use your list from Step 1 and evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student uses supportive comments regarding the patient’s emotions. The student uses NURS (Name the emotion, Understand the patient's perspective, Respect the patient's experience, and Support the patient) or specific techniques for demonstrating empathy. 
      - **Score 4:** NURS or equivalent techniques are mostly employed by the student, but they may not be as well-executed or as frequent. The student shows clear attempts to connect emotionally with the patient, even if occasionally missing opportunities for deeper empathy.
      - **Score 3:** The student is neutral, neither overly positive nor negative in demonstrating empathy. 
      - **Score 2:** The student shows limited attempts at empathy, but these are infrequent or sometimes poorly executed. There may be moments of connection, but they are overshadowed by missed opportunities or occasional insensitive comments. The student's approach is inconsistent, sometimes seeming detached or unresponsive to the patient's emotions.
      - **Score 1:** No empathy is demonstrated. The student uses a negative emphasis or openly criticizes the patient. 

  **Step 3. Justification:** Based on your analysis in Steps 1 and 2, assign a score using the provided rubric strictly, and explain your reasoning clearly. Your evaluation should be rigorous, impartial, and evidence-based. Directly quote the transcript to support your evaluation.

Provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

{
  "evaluation": {
    "elements_present": [
      "List of key elements present"
    ],
    "elements_absent": [
      "List of key elements missing"
    ],
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the transcript to support your evaluation"
  }
}

Now, please evaluate the following medical interview transcript:
"""




# EMPATHY_AND_ACKNOWLEDGING_PATIENT_CUES_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student uses supportive comments regarding the patient's emotions and demonstrates empathy. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Use of supportive comments regarding patient's emotions
#       - Demonstration of empathy 
#       - Acknowledgment of patient's emotional state
#       - Use of NURS techniques (Naming, Understanding, Respecting, Supporting)
#       - Absence of criticism or negative emphasis

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Consistent use of supportive comments, strong demonstration of empathy, and effective use of NURS techniques
#     - **Score 4:** Good use of empathetic statements and some NURS techniques, but may miss some opportunities or lack consistency
#     - **Score 3:** Neutral approach, some empathy shown but limited use of supportive comments or NURS techniques
#     - **Score 2:** Limited empathy, with some dismissive comments and no use of NURS techniques
#     - **Score 1:** No empathy demonstrated, with negative emphasis or open criticism

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Patient: \"I'm really worried about these test results. I can't stop thinking about what they might mean.\"
# Physician: \"It sounds like you're experiencing a lot of anxiety about the test results. Can you tell me more about what worries you the most?\" (Naming and Understanding)
# Patient: \"I'm scared they'll show something serious. I have a family to take care of.\"
# Physician: \"I can see why you'd be concerned, especially given your family responsibilities. It's completely understandable to feel this way when facing uncertainty.\" (Respecting)
# Patient: \"Yes, it's been overwhelming.\"
# Physician: \"You're showing a lot of strength in dealing with this uncertainty. Let's discuss some strategies that might help you manage this anxiety while we wait for the results. What has helped you cope with stressful situations in the past?\" (Supporting)",
#       "response": {
#         "elements_present": [
#           "Use of supportive comments regarding patient's emotions",
#           "Strong demonstration of empathy",
#           "Acknowledgment of patient's emotional state",
#           "Effective use of NURS techniques",
#           "Absence of criticism or negative emphasis"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician demonstrates excellent empathy skills and effectively uses NURS techniques. They Name the emotion (\"It sounds like you're experiencing a lot of anxiety\"), seek to Understand (\"Can you tell me more about what worries you the most?\"), show Respect (\"It's completely understandable to feel this way\"), and offer Support (\"Let's discuss some strategies that might help you manage this anxiety\"). The physician acknowledges the patient's emotional state without criticism and offers reassurance. This comprehensive display of empathy and use of NURS techniques warrants a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Patient: \"I've been having trouble sleeping because of this pain. I'm exhausted.\"
# Physician: \"I'm sorry to hear you're in pain and having difficulty sleeping. That must be really tough for you. Can you describe how the pain affects your sleep?\" (Understanding)
# Patient: \"It's hard to fall asleep, and I keep waking up. I'm worried it's affecting my work.\"
# Physician: \"It sounds like you're concerned about how this is impacting your daily life. That's a valid concern.\" (Naming and Respecting)
# Patient: \"I hope something helps.\"
# Physician: \"We'll work on this together to find a solution that works for you. Have you tried any strategies to manage the pain or improve your sleep so far?\" (Supporting)",
#       "response": {
#         "elements_present": [
#           "Use of supportive comments regarding patient's emotions",
#           "Good demonstration of empathy",
#           "Acknowledgment of patient's emotional state",
#           "Some use of NURS techniques",
#           "Absence of criticism or negative emphasis"
#         ],
#         "elements_absent": [
#           "Consistent use of all NURS techniques"
#         ],
#         "score": 4,
#         "justification": "The physician shows good empathy skills and uses some NURS techniques. They seek to Understand (\"Can you describe how the pain affects your sleep?\"), Name and Respect the patient's concerns (\"It sounds like you're concerned about how this is impacting your daily life. That's a valid concern.\"), and offer Support (\"We'll work on this together to find a solution\"). However, they could have explored the patient's emotions more deeply, particularly regarding work concerns. While they provide reassurance and use some NURS techniques, the approach is not as comprehensive as a score of 5 would require, thus warranting a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Patient: \"I'm feeling really nervous about this procedure.\"
# Physician: \"Many patients feel nervous before procedures. Can you tell me what specifically concerns you?\" (Understanding)
# Patient: \"I'm not sure I can go through with it.\"
# Physician: \"The procedure is important for your health. We'll do our best to make you comfortable. Have you had any negative experiences with medical procedures before?\"
# Patient: \"I guess so.\"
# Physician: \"Do you have any specific questions about the procedure that might help ease your concerns?\"",
#       "response": {
#         "elements_present": [
#           "Some acknowledgment of patient's emotional state",
#           "Limited use of NURS techniques"
#         ],
#         "elements_absent": [
#           "Strong use of supportive comments regarding patient's emotions",
#           "Consistent demonstration of empathy",
#           "Criticism or negative emphasis"
#         ],
#         "score": 3,
#         "justification": "The physician takes a somewhat neutral approach, showing some empathy but not consistently. They acknowledge the patient's nervousness and attempt to understand the specific concerns, which aligns with the Understanding aspect of NURS. However, they miss opportunities to Name the emotion explicitly or Respect the patient's feelings. The focus is more on providing information and reassurance about the procedure rather than exploring and validating the patient's emotions. While not dismissive, they could have demonstrated more empathy, particularly when the patient expresses doubt about going through with the procedure. This neutral approach, with limited use of empathetic statements and NURS techniques, aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Patient: \"I'm really struggling with the side effects of this medication.\"
# Physician: \"Side effects are common with this medication. Are you taking it as prescribed?\"
# Patient: \"Yes, but it's making me feel awful.\"
# Physician: \"Well, it's important to continue the medication. The benefits outweigh the side effects. What specific side effects are you experiencing?\"
# Patient: \"I don't know if I can keep this up.\"
# Physician: \"You need to try to tolerate it. Let's schedule a follow-up in a month to see how you're doing.\"",
#       "response": {
#         "elements_present": [
#           "Limited inquiry about patient's experience"
#         ],
#         "elements_absent": [
#           "Use of supportive comments regarding patient's emotions",
#           "Demonstration of empathy",
#           "Acknowledgment of patient's emotional state",
#           "Use of NURS techniques",
#           "Absence of dismissive comments"
#         ],
#         "score": 2,
#         "justification": "The physician demonstrates limited empathy and makes some dismissive comments. They do not acknowledge the patient's emotional struggle or offer supportive statements. There is no use of NURS techniques - the physician doesn't Name the patient's emotions, doesn't seek to Understand the full impact of the side effects, doesn't Respect the patient's difficulty in coping, and offers limited Support. Instead, they focus on the medical aspect, emphasizing the importance of continuing the medication without addressing the patient's distress. The response \"You need to try to tolerate it\" dismisses the patient's concerns rather than showing understanding or support. This lack of empathy and the presence of dismissive comments align with a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Patient: \"I've been feeling really down lately. I think I might be depressed.\"
# Physician: \"Everyone feels sad sometimes. You just need to try harder to be positive.\"
# Patient: \"I've tried, but it's not that simple.\"
# Physician: \"Well, if you don't make an effort, you won't get better. You need to exercise more and eat healthier.\"
# Patient: \"I don't have the energy to do those things.\"
# Physician: \"That's just an excuse. You have to take responsibility for your health.\"",
#       "response": {
#         "elements_present": [
#           "Negative emphasis",
#           "Open criticism of the patient"
#         ],
#         "elements_absent": [
#           "Use of supportive comments regarding patient's emotions",
#           "Demonstration of empathy",
#           "Acknowledgment of patient's emotional state",
#           "Use of NURS techniques"
#         ],
#         "score": 1,
#         "justification": "The physician demonstrates a complete lack of empathy and openly criticizes the patient. There is no use of NURS techniques - the physician fails to Name the patient's emotions, doesn't attempt to Understand their experience, shows no Respect for their struggles, and offers no meaningful Support. They dismiss the patient's concerns about depression with \"Everyone feels sad sometimes,\" showing a lack of understanding of the condition. The physician's responses are consistently negative and unsupportive, such as \"You just need to try harder\" and \"That's just an excuse.\" There is no acknowledgment of the patient's emotional state or the difficulty they're experiencing. The physician's approach could be harmful, potentially discouraging the patient from seeking further help. This total absence of empathy, lack of NURS techniques, and presence of criticism clearly warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# EMPATHY_AND_ACKNOWLEDGING_PATIENT_CUES2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student uses supportive comments regarding the patient's emotions and demonstrates empathy. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Use of supportive comments regarding patient's emotions
#    - Demonstration of empathy 
#    - Acknowledgment of patient's emotional state
#    - Use of NURS techniques (Naming, Understanding, Respecting, Supporting)
#    - Absence of criticism or negative emphasis

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Consistent use of supportive comments, strong demonstration of empathy, and effective use of NURS techniques
#    - Score 4: Good use of empathetic statements and some NURS techniques, but may miss some opportunities or lack consistency
#    - Score 3: Neutral approach, some empathy shown but limited use of supportive comments or NURS techniques
#    - Score 2: Limited empathy, with some dismissive comments and no use of NURS techniques
#    - Score 1: No empathy demonstrated, with negative emphasis or open criticism

# 3. Provide Justification: Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

# Please provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else:

# {
#   "evaluation": {
#     "elements_present": [
#       "List of elements present in the interview"
#     ],
#     "elements_absent": [
#       "List of elements missing from the interview"
#     ],
#     "score": 0,
#     "justification": "A clear explanation of your scoring, with direct quotes from the excerpt to support your evaluation"
#   }
# }

# Examples:
# The following examples illustrate how to apply the evaluation criteria and format the response:

# Example 1:
# Input: 
# Patient: "I'm really worried about these test results. I can't stop thinking about what they might mean."
# Physician: "It sounds like you're experiencing a lot of anxiety about the test results. Can you tell me more about what worries you the most?" (Naming and Understanding)
# Patient: "I'm scared they'll show something serious. I have a family to take care of."
# Physician: "I can see why you'd be concerned, especially given your family responsibilities. It's completely understandable to feel this way when facing uncertainty." (Respecting)
# Patient: "Yes, it's been overwhelming."
# Physician: "You're showing a lot of strength in dealing with this uncertainty. Let's discuss some strategies that might help you manage this anxiety while we wait for the results. What has helped you cope with stressful situations in the past?" (Supporting)

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Use of supportive comments regarding patient's emotions",
#       "Strong demonstration of empathy",
#       "Acknowledgment of patient's emotional state",
#       "Effective use of NURS techniques",
#       "Absence of criticism or negative emphasis"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician demonstrates excellent empathy skills and effectively uses NURS techniques. They Name the emotion (\"It sounds like you're experiencing a lot of anxiety\"), seek to Understand (\"Can you tell me more about what worries you the most?\"), show Respect (\"It's completely understandable to feel this way\"), and offer Support (\"Let's discuss some strategies that might help you manage this anxiety\"). The physician acknowledges the patient's emotional state without criticism and offers reassurance. This comprehensive display of empathy and use of NURS techniques warrants a score of 5."
#   }
# }

# Example 2:
# Input: 
# Patient: "I've been having trouble sleeping because of this pain. I'm exhausted."
# Physician: "I'm sorry to hear you're in pain and having difficulty sleeping. That must be really tough for you. Can you describe how the pain affects your sleep?" (Understanding)
# Patient: "It's hard to fall asleep, and I keep waking up. I'm worried it's affecting my work."
# Physician: "It sounds like you're concerned about how this is impacting your daily life. That's a valid concern." (Naming and Respecting)
# Patient: "I hope something helps."
# Physician: "We'll work on this together to find a solution that works for you. Have you tried any strategies to manage the pain or improve your sleep so far?" (Supporting)

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Use of supportive comments regarding patient's emotions",
#       "Good demonstration of empathy",
#       "Acknowledgment of patient's emotional state",
#       "Some use of NURS techniques",
#       "Absence of criticism or negative emphasis"
#     ],
#     "elements_absent": [
#       "Consistent use of all NURS techniques"
#     ],
#     "score": 4,
#     "justification": "The physician shows good empathy skills and uses some NURS techniques. They seek to Understand (\"Can you describe how the pain affects your sleep?\"), Name and Respect the patient's concerns (\"It sounds like you're concerned about how this is impacting your daily life. That's a valid concern.\"), and offer Support (\"We'll work on this together to find a solution\"). However, they could have explored the patient's emotions more deeply, particularly regarding work concerns. While they provide reassurance and use some NURS techniques, the approach is not as comprehensive as a score of 5 would require, thus warranting a score of 4."
#   }
# }

# Example 3:
# Input: 
# Patient: "I'm feeling really nervous about this procedure."
# Physician: "Many patients feel nervous before procedures. Can you tell me what specifically concerns you?" (Understanding)
# Patient: "I'm not sure I can go through with it."
# Physician: "The procedure is important for your health. We'll do our best to make you comfortable. Have you had any negative experiences with medical procedures before?"
# Patient: "I guess so."
# Physician: "Do you have any specific questions about the procedure that might help ease your concerns?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Some acknowledgment of patient's emotional state",
#       "Limited use of NURS techniques"
#     ],
#     "elements_absent": [
#       "Strong use of supportive comments regarding patient's emotions",
#       "Consistent demonstration of empathy",
#       "Criticism or negative emphasis"
#     ],
#     "score": 3,
#     "justification": "The physician takes a somewhat neutral approach, showing some empathy but not consistently. They acknowledge the patient's nervousness and attempt to understand the specific concerns, which aligns with the Understanding aspect of NURS. However, they miss opportunities to Name the emotion explicitly or Respect the patient's feelings. The focus is more on providing information and reassurance about the procedure rather than exploring and validating the patient's emotions. While not dismissive, they could have demonstrated more empathy, particularly when the patient expresses doubt about going through with the procedure. This neutral approach, with limited use of empathetic statements and NURS techniques, aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Patient: "I'm really struggling with the side effects of this medication."
# Physician: "Side effects are common with this medication. Are you taking it as prescribed?"
# Patient: "Yes, but it's making me feel awful."
# Physician: "Well, it's important to continue the medication. The benefits outweigh the side effects. What specific side effects are you experiencing?"
# Patient: "I don't know if I can keep this up."
# Physician: "You need to try to tolerate it. Let's schedule a follow-up in a month to see how you're doing."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Limited inquiry about patient's experience"
#     ],
#     "elements_absent": [
#       "Use of supportive comments regarding patient's emotions",
#       "Demonstration of empathy",
#       "Acknowledgment of patient's emotional state",
#       "Use of NURS techniques",
#       "Absence of dismissive comments"
#     ],
#     "score": 2,
#     "justification": "The physician demonstrates limited empathy and makes some dismissive comments. They do not acknowledge the patient's emotional struggle or offer supportive statements. There is no use of NURS techniques - the physician doesn't Name the patient's emotions, doesn't seek to Understand the full impact of the side effects, doesn't Respect the patient's difficulty in coping, and offers limited Support. Instead, they focus on the medical aspect, emphasizing the importance of continuing the medication without addressing the patient's distress. The response \"You need to try to tolerate it\" dismisses the patient's concerns rather than showing understanding or support. This lack of empathy and the presence of dismissive comments align with a score of 2."
#   }
# }

# Example 5:
# Input: 
# Patient: "I've been feeling really down lately. I think I might be depressed."
# Physician: "Everyone feels sad sometimes. You just need to try harder to be positive."
# Patient: "I've tried, but it's not that simple."
# Physician: "Well, if you don't make an effort, you won't get better. You need to exercise more and eat healthier."
# Patient: "I don't have the energy to do those things."
# Physician: "That's just an excuse. You have to take responsibility for your health."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Negative emphasis",
#       "Open criticism of the patient"
#     ],
#     "elements_absent": [
#       "Use of supportive comments regarding patient's emotions",
#       "Demonstration of empathy",
#       "Acknowledgment of patient's emotional state",
#       "Use of NURS techniques"
#     ],
#     "score": 1,
#     "justification": "The physician demonstrates a complete lack of empathy and openly criticizes the patient. There is no use of NURS techniques - the physician fails to Name the patient's emotions, doesn't attempt to Understand their experience, shows no Respect for their struggles, and offers no meaningful Support. They dismiss the patient's concerns about depression with \"Everyone feels sad sometimes,\" showing a lack of understanding of the condition. The physician's responses are consistently negative and unsupportive, such as \"You just need to try harder\" and \"That's just an excuse.\" There is no acknowledgment of the patient's emotional state or the difficulty they're experiencing. The physician's approach could be harmful, potentially discouraging the patient from seeking further help. This total absence of empathy, lack of NURS techniques, and presence of criticism clearly warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
