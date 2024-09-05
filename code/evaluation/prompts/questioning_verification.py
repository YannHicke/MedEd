QUESTIONING_SKILLS_VERIFICATION_OF_PATIENT_INFORMATION = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the student’s questioning skills, specifically looking at their verification of patient information. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student always seeks clarification, verification, and specificity of the patient’s responses.
      - **Score 4:** The student frequently seeks clarification, verification, and specificity of the patient's responses. While not as consistent as a score of 5, the student demonstrates a clear pattern of following up on important details. Few missed opportunities for clarification may occur, but they are minor and do not significantly impact the overall understanding of the patient's situation.
      - **Score 3:** The student will seek clarification, verification, and specificity of the patient’s responses but not always. They may sometimes accept information at face value, and their overall understanding of the patient’s situation may have some minor holes.
      - **Score 2:** The student minimally seeks clarification, verification, and specificity. There are noticeable instances where important details are not followed up on, but some effort is made to clarify key points. The student shows awareness of the need for clarification but struggles to apply it consistently or effectively.
      - **Score 1:** The student fails to clarify or verify the patient's responses, accepting information at face value.

  **Step 2. Justification:** Based on your analysis in Step 1, assign a score using the provided rubric strictly, and explain your reasoning clearly. Your evaluation should be rigorous, impartial, and evidence-based. Directly quote the transcript to support your evaluation.

Provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

{
  "evaluation": {
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the transcript to support your evaluation"
  }
}

Now, please evaluate the following transcript:
"""




# QUESTIONING_SKILLS_VERIFICATION_OF_PATIENT_INFORMATION_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student seeks clarification, verification, and specificity of the patient's responses. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Seeking clarification of vague or unclear statements
#       - Verifying patient responses for accuracy
#       - Asking for specificity in patient descriptions
#       - Following up on important details

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Consistent clarification, verification, and specification of patient responses
#     - **Score 3:** Some clarification and verification, but not consistently applied
#     - **Score 1:** Failure to clarify or verify patient responses, ignoring need for accuracy

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"You mentioned experiencing headaches. Can you tell me more about when these headaches typically occur?\"
# Patient: \"They usually happen in the afternoon.\"
# Physician: \"I see. When you say 'afternoon', can you be more specific about the time?\"
# Patient: \"Usually around 2 or 3 PM.\"
# Physician: \"Thank you. And how long do these headaches typically last?\"
# Patient: \"A few hours.\"
# Physician: \"When you say 'a few hours', do you mean 2-3 hours, or longer?\"
# Patient: \"Usually about 3-4 hours.\"
# Physician: \"Alright. You've mentioned that these headaches occur around 2 or 3 PM and last for about 3-4 hours. Is that correct?\"
# Patient: \"Yes, that's right.\"
# Physician: \"And can you describe the pain? Is it a dull ache, a throbbing sensation, or something else?\"
# Patient: \"It's more of a throbbing pain.\"
# Physician: \"Thank you for clarifying. Now, have you noticed any triggers for these headaches?\"",
#       "response": {
#         "elements_present": [
#           "Seeking clarification of vague or unclear statements",
#           "Verifying patient responses for accuracy",
#           "Asking for specificity in patient descriptions",
#           "Following up on important details"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician consistently seeks clarification, verification, and specificity throughout the conversation. They ask for more specific information about timing (\"When you say 'afternoon', can you be more specific about the time?\"), duration (\"When you say 'a few hours', do you mean 2-3 hours, or longer?\"), and nature of the pain (\"Is it a dull ache, a throbbing sensation, or something else?\"). They also verify the information they've gathered (\"You've mentioned that these headaches occur around 2 or 3 PM and last for about 3-4 hours. Is that correct?\"). This thorough approach ensures accurate understanding of the patient's symptoms, warranting a score of 5."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"You mentioned having stomach pain. Can you tell me where exactly you feel this pain?\"
# Patient: \"It's in my upper stomach area.\"
# Physician: \"I see. And how long have you been experiencing this pain?\"
# Patient: \"For a few weeks now.\"
# Physician: \"Okay. Is the pain constant or does it come and go?\"
# Patient: \"It comes and goes.\"
# Physician: \"Alright. Have you noticed any other symptoms along with the pain?\"
# Patient: \"I've been feeling nauseous sometimes.\"
# Physician: \"I understand. Let's move on to discuss your medical history.\"",
#       "response": {
#         "elements_present": [
#           "Some seeking of clarification",
#           "Some asking for specificity"
#         ],
#         "elements_absent": [
#           "Consistent verification of patient responses",
#           "Thorough follow-up on important details"
#         ],
#         "score": 3,
#         "justification": "The physician demonstrates some effort to seek clarification and specificity, such as asking about the location of the pain (\"Can you tell me where exactly you feel this pain?\") and its nature (\"Is the pain constant or does it come and go?\"). However, they miss opportunities for further clarification and verification. For instance, they don't ask for more specificity when the patient says the pain has been present for \"a few weeks\" or inquire about the frequency or severity of the nausea. The physician also moves on to the next topic without verifying the information gathered about the stomach pain. This inconsistent approach to clarification and verification aligns with a score of 3."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"What brings you in today?\"
# Patient: \"I've been feeling really tired lately and I have some pain in my chest.\"
# Physician: \"I see. And how's your appetite?\"
# Patient: \"It's been okay, I guess.\"
# Physician: \"Alright. Any changes in your weight?\"
# Patient: \"Not that I've noticed.\"
# Physician: \"Okay. Let's do a physical examination now.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Seeking clarification of vague or unclear statements",
#           "Verifying patient responses for accuracy",
#           "Asking for specificity in patient descriptions",
#           "Following up on important details"
#         ],
#         "score": 1,
#         "justification": "The physician fails to seek clarification or verification on any of the patient's responses. They don't ask for more details about the fatigue or chest pain mentioned by the patient, which are potentially serious symptoms. When the patient gives vague responses like \"It's been okay, I guess\" about their appetite, the physician doesn't ask for clarification. There's no attempt to get specifics about the duration, severity, or nature of the symptoms. The physician moves on to the physical examination without gathering or verifying crucial information, demonstrating a lack of thoroughness and potentially missing important clinical details. This failure to clarify or verify patient responses consistently warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# QUESTIONING_SKILLS_VERIFICATION_OF_PATIENT_INFORMATION2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student seeks clarification, verification, and specificity of the patient's responses. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Seeking clarification of vague or unclear statements
#    - Verifying patient responses for accuracy
#    - Asking for specificity in patient descriptions
#    - Following up on important details

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Consistent clarification, verification, and specification of patient responses
#    - Score 3: Some clarification and verification, but not consistently applied
#    - Score 1: Failure to clarify or verify patient responses, ignoring need for accuracy

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
# Physician: "You mentioned experiencing headaches. Can you tell me more about when these headaches typically occur?"
# Patient: "They usually happen in the afternoon."
# Physician: "I see. When you say 'afternoon', can you be more specific about the time?"
# Patient: "Usually around 2 or 3 PM."
# Physician: "Thank you. And how long do these headaches typically last?"
# Patient: "A few hours."
# Physician: "When you say 'a few hours', do you mean 2-3 hours, or longer?"
# Patient: "Usually about 3-4 hours."
# Physician: "Alright. You've mentioned that these headaches occur around 2 or 3 PM and last for about 3-4 hours. Is that correct?"
# Patient: "Yes, that's right."
# Physician: "And can you describe the pain? Is it a dull ache, a throbbing sensation, or something else?"
# Patient: "It's more of a throbbing pain."
# Physician: "Thank you for clarifying. Now, have you noticed any triggers for these headaches?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Seeking clarification of vague or unclear statements",
#       "Verifying patient responses for accuracy",
#       "Asking for specificity in patient descriptions",
#       "Following up on important details"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician consistently seeks clarification, verification, and specificity throughout the conversation. They ask for more specific information about timing (\"When you say 'afternoon', can you be more specific about the time?\"), duration (\"When you say 'a few hours', do you mean 2-3 hours, or longer?\"), and nature of the pain (\"Is it a dull ache, a throbbing sensation, or something else?\"). They also verify the information they've gathered (\"You've mentioned that these headaches occur around 2 or 3 PM and last for about 3-4 hours. Is that correct?\"). This thorough approach ensures accurate understanding of the patient's symptoms, warranting a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "You mentioned having stomach pain. Can you tell me where exactly you feel this pain?"
# Patient: "It's in my upper stomach area."
# Physician: "I see. And how long have you been experiencing this pain?"
# Patient: "For a few weeks now."
# Physician: "Okay. Is the pain constant or does it come and go?"
# Patient: "It comes and goes."
# Physician: "Alright. Have you noticed any other symptoms along with the pain?"
# Patient: "I've been feeling nauseous sometimes."
# Physician: "I understand. Let's move on to discuss your medical history."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Some seeking of clarification",
#       "Some asking for specificity"
#     ],
#     "elements_absent": [
#       "Consistent verification of patient responses",
#       "Thorough follow-up on important details"
#     ],
#     "score": 3,
#     "justification": "The physician demonstrates some effort to seek clarification and specificity, such as asking about the location of the pain (\"Can you tell me where exactly you feel this pain?\") and its nature (\"Is the pain constant or does it come and go?\"). However, they miss opportunities for further clarification and verification. For instance, they don't ask for more specificity when the patient says the pain has been present for \"a few weeks\" or inquire about the frequency or severity of the nausea. The physician also moves on to the next topic without verifying the information gathered about the stomach pain. This inconsistent approach to clarification and verification aligns with a score of 3."
#   }
# }

# Example 3:
# Input: 
# Physician: "What brings you in today?"
# Patient: "I've been feeling really tired lately and I have some pain in my chest."
# Physician: "I see. And how's your appetite?"
# Patient: "It's been okay, I guess."
# Physician: "Alright. Any changes in your weight?"
# Patient: "Not that I've noticed."
# Physician: "Okay. Let's do a physical examination now."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Seeking clarification of vague or unclear statements",
#       "Verifying patient responses for accuracy",
#       "Asking for specificity in patient descriptions",
#       "Following up on important details"
#     ],
#     "score": 1,
#     "justification": "The physician fails to seek clarification or verification on any of the patient's responses. They don't ask for more details about the fatigue or chest pain mentioned by the patient, which are potentially serious symptoms. When the patient gives vague responses like \"It's been okay, I guess\" about their appetite, the physician doesn't ask for clarification. There's no attempt to get specifics about the duration, severity, or nature of the symptoms. The physician moves on to the physical examination without gathering or verifying crucial information, demonstrating a lack of thoroughness and potentially missing important clinical details. This failure to clarify or verify patient responses consistently warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
