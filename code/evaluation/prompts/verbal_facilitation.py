VERBAL_FACILITATION_SKILLS = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the student’s verbal facilitation skills. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student uses facilitation skills throughout the interview. Verbal encouragement, use of short statements, and echoing are used regularly when appropriate. The student provides the patient with intermittent verbal encouragement, such as verbally praising the patient for proper health care technique.
      - **Score 4:** The student frequently uses facilitation skills during the interview, but not as consistently or effectively as in a score of 5. Verbal encouragement, short statements, and echoing are present, but there may be only a few missed opportunities or inappropriate applications. The student provides some verbal encouragement, though it may not always be as timely or specific as in a top performance.
      - **Score 3:** The student uses some facilitative skills but not consistently or at inappropriate times. Verbal encouragement could be used more effectively.
      - **Score 2:** The student demonstrates limited use of facilitation skills. There are occasional instances of verbal encouragement, short statements, or echoing, but these are infrequent and often poorly timed or executed. The student shows some awareness of the need for facilitation but struggles to implement these skills effectively, resulting in a less fluid conversation with the patient.
      - **Score 1:** The student fails to use facilitative skills to encourage the patient to tell their story. 

  **Step 2. Justification:** Based on your analysis in Step 1, assign a score using the provided rubric strictly, and explain your reasoning clearly. Your evaluation should be rigorous, impartial, and evidence-based. Directly quote the transcript to support your evaluation.

Provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

{
  "evaluation": {
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the transcript to support your evaluation"
  }
}

Now, please evaluate the following medical interview transcript:
"""


# VERBAL_FACILITATION_SKILLS_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student uses verbal encouragement and facilitation skills to engage the patient. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Use of verbal encouragement
#       - Short statements to facilitate conversation
#       - Echoing patient's words
#       - Praising patient for proper health care techniques
#       - Drawing out information from the patient

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Consistent, highly effective use of encouragement and facilitation skills throughout the interview
#     - **Score 4:** Frequent use of facilitation skills, but with occasional missed opportunities
#     - **Score 3:** Some use of facilitative skills, but not consistently or at appropriate times
#     - **Score 2:** Limited use of facilitation skills, with many missed opportunities
#     - **Score 1:** Failure to use facilitative skills to encourage the patient's narrative

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"So, you mentioned you've been working on managing your diabetes. That's really commendable. Can you tell me more about what you've been doing?\"
# Patient: \"Well, I've been checking my blood sugar regularly and trying to eat better.\"
# Physician: \"Checking your blood sugar regularly and improving your diet - that's excellent! How often are you checking your levels?\"
# Patient: \"Usually twice a day, morning and evening.\"
# Physician: \"Twice a day is a great routine. You're doing a wonderful job staying on top of your health. How has this been affecting your blood sugar readings?\"
# Patient: \"They seem to be more stable now.\"
# Physician: \"More stable readings - that's fantastic progress! It really shows how your efforts are paying off. How are you feeling with these changes?\"
# Patient: \"I think I have more energy, and I'm not as worried about my health.\"
# Physician: \"It's wonderful to hear you're feeling better both physically and emotionally. Your dedication to managing your diabetes is truly impressive. Is there anything you find particularly challenging about your new routine?\"",
#       "response": {
#         "elements_present": [
#           "Use of verbal encouragement",
#           "Short statements to facilitate conversation",
#           "Echoing patient's words",
#           "Praising patient for proper health care techniques",
#           "Drawing out information from the patient"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician consistently and effectively uses all aspects of verbal facilitation throughout the conversation. They provide frequent verbal encouragement (\"That's really commendable\", \"that's excellent!\", \"You're doing a wonderful job\"), use short statements to facilitate conversation, echo the patient's words (\"Checking your blood sugar regularly and improving your diet\", \"More stable readings\"), praise the patient for proper health care techniques, and effectively draw out information by asking specific follow-up questions. This approach not only encourages the patient to share more details but also reinforces their positive health behaviors and builds rapport, fully warranting a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"I understand you've been working on your blood pressure management. That's great. What steps have you been taking?\"
# Patient: \"I've been trying to reduce my salt intake and exercise more.\"
# Physician: \"Reducing salt and increasing exercise are excellent strategies. How often are you exercising?\"
# Patient: \"I try to walk for 30 minutes, three times a week.\"
# Physician: \"That's a good start. Have you noticed any changes since you began this routine?\"
# Patient: \"I think my blood pressure readings at home have been a bit lower.\"
# Physician: \"Lower readings are a positive sign. It shows your efforts are making a difference. Are you having any difficulties with these lifestyle changes?\"
# Patient: \"Sometimes it's hard to find time to exercise.\"
# Physician: \"I see. Let's talk about your medication adherence now.\"",
#       "response": {
#         "elements_present": [
#           "Use of verbal encouragement",
#           "Short statements to facilitate conversation",
#           "Some praising of patient for proper health care techniques",
#           "Drawing out information from the patient"
#         ],
#         "elements_absent": [
#           "Consistent echoing of patient's words"
#         ],
#         "score": 4,
#         "justification": "The physician frequently uses facilitation skills, providing verbal encouragement (\"That's great\", \"That's a good start\") and praising the patient's efforts. They use short statements and questions to draw out information effectively. However, there are some missed opportunities. For instance, when the patient mentions difficulty finding time to exercise, the physician could have explored this challenge further instead of moving to a new topic. Additionally, while they do some echoing (\"Lower readings are a positive sign\"), it's not consistent throughout. Overall, the physician demonstrates good facilitation skills with room for minor improvements, aligning with a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"You mentioned you've started a new medication. How's that going?\"
# Patient: \"It's okay, I guess. I'm remembering to take it most days.\"
# Physician: \"Good. Any side effects?\"
# Patient: \"I've been feeling a bit tired.\"
# Physician: \"I see. Is the tiredness affecting your daily activities?\"
# Patient: \"Sometimes it's hard to get through the workday.\"
# Physician: \"Okay. Are you taking the medication as prescribed?\"
# Patient: \"Yes, I think so.\"
# Physician: \"Alright. Let's move on to discuss your diet.\"",
#       "response": {
#         "elements_present": [
#           "Some use of short statements to facilitate conversation",
#           "Some attempts to draw out information"
#         ],
#         "elements_absent": [
#           "Consistent use of verbal encouragement",
#           "Echoing patient's words",
#           "Praising patient for proper health care techniques"
#         ],
#         "score": 3,
#         "justification": "The physician uses some facilitative skills, but not consistently or always effectively. They attempt to draw out information with follow-up questions about side effects and medication adherence. However, they miss several opportunities for encouragement and deeper exploration. For instance, when the patient mentions tiredness affecting work, the physician could have explored this impact further. The use of \"Good\" and \"Okay\" provides minimal encouragement. There's no echoing of the patient's words or substantial praise for their efforts in medication adherence. This inconsistent use of facilitation skills, with some present but others notably absent, aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"What brings you in today?\"
# Patient: \"I've been having some stomach pain. I'm a bit worried about it.\"
# Physician: \"How long have you had this pain?\"
# Patient: \"It started about two weeks ago. At first I thought—\"
# Physician: \"Is the pain constant or does it come and go?\"
# Patient: \"It comes and goes. Lately it seems to be happening more often.\"
# Physician: \"Any nausea or vomiting?\"
# Patient: \"No, but I have been feeling more tired than usual.\"
# Physician: \"Okay. I'm going to order some tests to investigate this further.\"",
#       "response": {
#         "elements_present": [
#           "Limited attempts to draw out information"
#         ],
#         "elements_absent": [
#           "Use of verbal encouragement",
#           "Short statements to facilitate conversation",
#           "Echoing patient's words",
#           "Praising patient for proper health care techniques"
#         ],
#         "score": 2,
#         "justification": "The physician demonstrates very limited use of facilitation skills. They ask direct questions to gather information but fail to provide any verbal encouragement or acknowledgment of the patient's concerns. When the patient attempts to elaborate (\"At first I thought—\"), the physician interrupts rather than allowing the patient to continue. There's no echoing of the patient's words, no praise or encouragement, and minimal attempt to draw out more detailed information about the patient's experience. The physician's final statement provides some reassurance but doesn't encourage further dialogue. This limited use of facilitation skills, with many missed opportunities, warrants a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"What's the problem?\"
# Patient: \"I've been having headaches and feeling dizzy.\"
# Physician: \"When did this start?\"
# Patient: \"About a month ago. It's been getting worse and I'm worried—\"
# Physician: \"Frequency of headaches?\"
# Patient: \"Almost daily now.\"
# Physician: \"Any visual changes?\"
# Patient: \"No, but sometimes I feel nauseous.\"
# Physician: \"I'll refer you for a CT scan.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Use of verbal encouragement",
#           "Short statements to facilitate conversation",
#           "Echoing patient's words",
#           "Praising patient for proper health care techniques",
#           "Drawing out information from the patient"
#         ],
#         "score": 1,
#         "justification": "The physician fails to use any significant facilitative skills to encourage the patient to tell their story. The interview consists entirely of brief, direct questions without any verbal encouragement or acknowledgment of the patient's concerns. When the patient tries to express worry, the physician interrupts with another question. There's no echoing of the patient's words, no empathy expressed, and no attempt to draw out more detailed information about the patient's experience or concerns. The abrupt conclusion with a referral for a CT scan without any explanation or reassurance further demonstrates the lack of facilitation. This complete absence of verbal facilitation skills warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# VERBAL_FACILITATION_SKILLS2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student uses verbal encouragement and facilitation skills to engage the patient. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Use of verbal encouragement
#    - Short statements to facilitate conversation
#    - Echoing patient's words
#    - Praising patient for proper health care techniques
#    - Drawing out information from the patient

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Consistent, highly effective use of encouragement and facilitation skills throughout the interview
#    - Score 4: Frequent use of facilitation skills, but with occasional missed opportunities
#    - Score 3: Some use of facilitative skills, but not consistently or at appropriate times
#    - Score 2: Limited use of facilitation skills, with many missed opportunities
#    - Score 1: Failure to use facilitative skills to encourage the patient's narrative

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
# Physician: "So, you mentioned you've been working on managing your diabetes. That's really commendable. Can you tell me more about what you've been doing?"
# Patient: "Well, I've been checking my blood sugar regularly and trying to eat better."
# Physician: "Checking your blood sugar regularly and improving your diet - that's excellent! How often are you checking your levels?"
# Patient: "Usually twice a day, morning and evening."
# Physician: "Twice a day is a great routine. You're doing a wonderful job staying on top of your health. How has this been affecting your blood sugar readings?"
# Patient: "They seem to be more stable now."
# Physician: "More stable readings - that's fantastic progress! It really shows how your efforts are paying off. How are you feeling with these changes?"
# Patient: "I think I have more energy, and I'm not as worried about my health."
# Physician: "It's wonderful to hear you're feeling better both physically and emotionally. Your dedication to managing your diabetes is truly impressive. Is there anything you find particularly challenging about your new routine?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Use of verbal encouragement",
#       "Short statements to facilitate conversation",
#       "Echoing patient's words",
#       "Praising patient for proper health care techniques",
#       "Drawing out information from the patient"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician consistently and effectively uses all aspects of verbal facilitation throughout the conversation. They provide frequent verbal encouragement (\"That's really commendable\", \"that's excellent!\", \"You're doing a wonderful job\"), use short statements to facilitate conversation, echo the patient's words (\"Checking your blood sugar regularly and improving your diet\", \"More stable readings\"), praise the patient for proper health care techniques, and effectively draw out information by asking specific follow-up questions. This approach not only encourages the patient to share more details but also reinforces their positive health behaviors and builds rapport, fully warranting a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "I understand you've been working on your blood pressure management. That's great. What steps have you been taking?"
# Patient: "I've been trying to reduce my salt intake and exercise more."
# Physician: "Reducing salt and increasing exercise are excellent strategies. How often are you exercising?"
# Patient: "I try to walk for 30 minutes, three times a week."
# Physician: "That's a good start. Have you noticed any changes since you began this routine?"
# Patient: "I think my blood pressure readings at home have been a bit lower."
# Physician: "Lower readings are a positive sign. It shows your efforts are making a difference. Are you having any difficulties with these lifestyle changes?"
# Patient: "Sometimes it's hard to find time to exercise."
# Physician: "I see. Let's talk about your medication adherence now."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Use of verbal encouragement",
#       "Short statements to facilitate conversation",
#       "Some praising of patient for proper health care techniques",
#       "Drawing out information from the patient"
#     ],
#     "elements_absent": [
#       "Consistent echoing of patient's words"
#     ],
#     "score": 4,
#     "justification": "The physician frequently uses facilitation skills, providing verbal encouragement (\"That's great\", \"That's a good start\") and praising the patient's efforts. They use short statements and questions to draw out information effectively. However, there are some missed opportunities. For instance, when the patient mentions difficulty finding time to exercise, the physician could have explored this challenge further instead of moving to a new topic. Additionally, while they do some echoing (\"Lower readings are a positive sign\"), it's not consistent throughout. Overall, the physician demonstrates good facilitation skills with room for minor improvements, aligning with a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "You mentioned you've started a new medication. How's that going?"
# Patient: "It's okay, I guess. I'm remembering to take it most days."
# Physician: "Good. Any side effects?"
# Patient: "I've been feeling a bit tired."
# Physician: "I see. Is the tiredness affecting your daily activities?"
# Patient: "Sometimes it's hard to get through the workday."
# Physician: "Okay. Are you taking the medication as prescribed?"
# Patient: "Yes, I think so."
# Physician: "Alright. Let's move on to discuss your diet."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Some use of short statements to facilitate conversation",
#       "Some attempts to draw out information"
#     ],
#     "elements_absent": [
#       "Consistent use of verbal encouragement",
#       "Echoing patient's words",
#       "Praising patient for proper health care techniques"
#     ],
#     "score": 3,
#     "justification": "The physician uses some facilitative skills, but not consistently or always effectively. They attempt to draw out information with follow-up questions about side effects and medication adherence. However, they miss several opportunities for encouragement and deeper exploration. For instance, when the patient mentions tiredness affecting work, the physician could have explored this impact further. The use of \"Good\" and \"Okay\" provides minimal encouragement. There's no echoing of the patient's words or substantial praise for their efforts in medication adherence. This inconsistent use of facilitation skills, with some present but others notably absent, aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "What brings you in today?"
# Patient: "I've been having some stomach pain. I'm a bit worried about it."
# Physician: "How long have you had this pain?"
# Patient: "It started about two weeks ago. At first I thought—"
# Physician: "Is the pain constant or does it come and go?"
# Patient: "It comes and goes. Lately it seems to be happening more often."
# Physician: "Any nausea or vomiting?"
# Patient: "No, but I have been feeling more tired than usual."
# Physician: "Okay. I'm going to order some tests to investigate this further."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Limited attempts to draw out information"
#     ],
#     "elements_absent": [
#       "Use of verbal encouragement",
#       "Short statements to facilitate conversation",
#       "Echoing patient's words",
#       "Praising patient for proper health care techniques"
#     ],
#     "score": 2,
#     "justification": "The physician demonstrates very limited use of facilitation skills. They ask direct questions to gather information but fail to provide any verbal encouragement or acknowledgment of the patient's concerns. When the patient attempts to elaborate (\"At first I thought—\"), the physician interrupts rather than allowing the patient to continue. There's no echoing of the patient's words, no praise or encouragement, and minimal attempt to draw out more detailed information about the patient's experience. The physician's final statement provides some reassurance but doesn't encourage further dialogue. This limited use of facilitation skills, with many missed opportunities, warrants a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "What's the problem?"
# Patient: "I've been having headaches and feeling dizzy."
# Physician: "When did this start?"
# Patient: "About a month ago. It's been getting worse and I'm worried—"
# Physician: "Frequency of headaches?"
# Patient: "Almost daily now."
# Physician: "Any visual changes?"
# Patient: "No, but sometimes I feel nauseous."
# Physician: "I'll refer you for a CT scan."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Use of verbal encouragement",
#       "Short statements to facilitate conversation",
#       "Echoing patient's words",
#       "Praising patient for proper health care techniques",
#       "Drawing out information from the patient"
#     ],
#     "score": 1,
#     "justification": "The physician fails to use any significant facilitative skills to encourage the patient to tell their story. The interview consists entirely of brief, direct questions without any verbal encouragement or acknowledgment of the patient's concerns. When the patient tries to express worry, the physician interrupts with another question. There's no echoing of the patient's words, no empathy expressed, and no attempt to draw out more detailed information about the patient's experience or concerns. The abrupt conclusion with a referral for a CT scan without any explanation or reassurance further demonstrates the lack of facilitation. This complete absence of verbal facilitation skills warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
