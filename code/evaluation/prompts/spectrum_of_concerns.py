SPECTRUM_OF_CONCERNS = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student elicits the patient's full spectrum of concerns within the first 3-5 minutes of the interview. You will then provide your evaluation in a given JSON format. 

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student elicits the patient’s full spectrum of concerns within the first 3-5 minutes of the interview. The student asks a final “Anything else?” or an equivalent to the patient to make sure all concerns have been raised.
      - **Score 4:** The student elicits the patient’s chief complaint and secondary concerns but fails to ask the final 'Anything else?' question.
      - **Score 3:** The student elicits some of the patient’s concerns on their chief complaint.
      - **Score 2:** The student only states the chief complaint without eliciting the patient’s concerns.
      - **Score 1:** The student fails to elicit the patient’s chief complaint.

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



# SPECTRUM_OF_CONCERNS_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student elicits the patient's full spectrum of concerns within the first 3-5 minutes of the interview. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Elicitation of main concern
#       - Probing for additional concerns
#       - Use of "what else" questions
#       - Confirmation of no further concerns

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Full spectrum of concerns elicited, multiple "what else" questions asked until no additional concerns raised.
#     - **Score 4:** Secondary concerns addressed, only one final "what else" missing.
#     - **Score 3:** Only main concern elicited without probing for additional concerns.
#     - **Score 2:** Concern merely stated without any elicitation.
#     - **Score 1:** No concerns elicited at all.

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

# "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"Good morning, I'm Dr. Smith. What brings you in today?\"
# Patient: \"I've been having terrible headaches.\"
# Physician: \"I'm sorry to hear that. Can you tell me more about these headaches?\"
# Patient: \"They're really painful and happen almost daily.\"
# Physician: \"I see. Is there anything else bothering you, apart from the headaches?\"
# Patient: \"Well, I've also been feeling quite tired lately.\"
# Physician: \"Thank you for sharing that. Is there anything else on your mind health-wise that you'd like us to address today?\"
# Patient: \"No, I think that covers everything.\"
# Physician: \"Alright. Just to make sure, is there anything else at all you'd like to discuss?\"
# Patient: \"No, that's really all.\"",
#       "response": {
#         "elements_present": [
#           "Elicitation of main concern",
#           "Probing for additional concerns",
#           "Use of multiple \"what else\" questions",
#           "Confirmation of no further concerns"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician thoroughly elicits the patient's concerns. They start with \"What brings you in today?\", then probe deeper with \"Can you tell me more about these headaches?\". They explicitly ask for additional concerns twice with \"Is there anything else bothering you, apart from the headaches?\" and \"Is there anything else on your mind health-wise that you'd like us to address today?\". Finally, they confirm no further concerns with a last check: \"Just to make sure, is there anything else at all you'd like to discuss?\". This approach ensures a comprehensive understanding of the patient's issues."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"Hello, I'm Dr. Johnson. What's the main reason for your visit today?\"
# Patient: \"I've been experiencing shortness of breath.\"
# Physician: \"I see. Can you tell me more about that?\"
# Patient: \"It's been happening for about a week, especially when I climb stairs.\"
# Physician: \"Thank you for sharing that. Is there anything else you're concerned about today?\"
# Patient: \"Yes, I've also noticed some swelling in my ankles.\"
# Physician: \"Alright, I'll make sure to examine that as well. Let's start with your breathing issues.\"",
#       "response": {
#         "elements_present": [
#           "Elicitation of main concern",
#           "Probing for additional concerns",
#           "Use of one \"what else\" question"
#         ],
#         "elements_absent": [
#           "Final confirmation of no further concerns"
#         ],
#         "score": 4,
#         "justification": "The physician effectively elicits the main concern and probes for additional issues. They ask \"What's the main reason for your visit today?\" and follow up with \"Can you tell me more about that?\". They also ask about additional concerns with \"Is there anything else you're concerned about today?\". However, they miss the opportunity for a final \"what else\" question after the patient mentions ankle swelling, which would have ensured no other concerns were left unaddressed."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"Good afternoon. What seems to be the problem today?\"
# Patient: \"I've been having this persistent cough that won't go away.\"
# Physician: \"How long have you had this cough?\"
# Patient: \"It's been about three weeks now.\"
# Physician: \"I see. And is it a dry cough or are you coughing up anything?\"
# Patient: \"It's mostly dry, but sometimes I cough up a little mucus.\"
# Physician: \"Alright, let's take a closer look at that cough then.\"",
#       "response": {
#         "elements_present": [
#           "Elicitation of main concern"
#         ],
#         "elements_absent": [
#           "Probing for additional concerns",
#           "Use of \"what else\" questions",
#           "Confirmation of no further concerns"
#         ],
#         "score": 3,
#         "justification": "The physician adequately elicits information about the patient's main concern, starting with \"What seems to be the problem today?\" and following up with specific questions about the cough. However, they fail to ask about any additional concerns or use any \"what else\" questions. This approach risks missing other health issues the patient might have."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"Your chart says you're here for a rash. Where is it located?\"
# Patient: \"Yes, it's on my arm and it's really itchy.\"
# Physician: \"How long have you had it?\"
# Patient: \"About a week now.\"
# Physician: \"Okay, let me take a look at it.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Elicitation of main concern",
#           "Probing for additional concerns",
#           "Use of \"what else\" questions",
#           "Confirmation of no further concerns"
#         ],
#         "score": 2,
#         "justification": "The physician doesn't actually elicit the patient's concern, instead stating it based on the chart: \"Your chart says you're here for a rash.\" They ask follow-up questions about the rash but don't explore if this is indeed the patient's main concern or if there are any other issues. There's no attempt to probe for additional concerns or use any \"what else\" questions."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"I see you're scheduled for a check-up today. I'm going to start by checking your blood pressure.\"
# Patient: \"Actually, I've been having some chest pain lately.\"
# Physician: \"Okay, I'll make a note of that. Please roll up your sleeve for the blood pressure cuff.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Elicitation of main concern",
#           "Probing for additional concerns",
#           "Use of \"what else\" questions",
#           "Confirmation of no further concerns"
#         ],
#         "score": 1,
#         "justification": "The physician completely fails to elicit the patient's concerns. They assume the visit is for a routine check-up without asking the patient's reason for the visit. Even when the patient volunteers information about chest pain, the physician merely acknowledges it without exploring further. There's no attempt to understand the patient's concerns or check for additional issues."
#       }
#     }
#   ],
# "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# SPECTRUM_OF_CONCERNS2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student elicits the patient's full spectrum of concerns within the first 3-5 minutes of the interview. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Elicitation of main concern
#    - Probing for additional concerns
#    - Use of "what else" questions
#    - Confirmation of no further concerns

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Full spectrum of concerns elicited, multiple "what else" questions asked until no additional concerns raised.
#    - Score 4: Secondary concerns addressed, only one final "what else" missing.
#    - Score 3: Only main concern elicited without probing for additional concerns.
#    - Score 2: Concern merely stated without any elicitation.
#    - Score 1: No concerns elicited at all.

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
# Physician: "Good morning, I'm Dr. Smith. What brings you in today?"
# Patient: "I've been having terrible headaches."
# Physician: "I'm sorry to hear that. Can you tell me more about these headaches?"
# Patient: "They're really painful and happen almost daily."
# Physician: "I see. Is there anything else bothering you, apart from the headaches?"
# Patient: "Well, I've also been feeling quite tired lately."
# Physician: "Thank you for sharing that. Is there anything else on your mind health-wise that you'd like us to address today?"
# Patient: "No, I think that covers everything."
# Physician: "Alright. Just to make sure, is there anything else at all you'd like to discuss?"
# Patient: "No, that's really all."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Elicitation of main concern",
#       "Probing for additional concerns",
#       "Use of multiple \"what else\" questions",
#       "Confirmation of no further concerns"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician thoroughly elicits the patient's concerns. They start with \"What brings you in today?\", then probe deeper with \"Can you tell me more about these headaches?\". They explicitly ask for additional concerns twice with \"Is there anything else bothering you, apart from the headaches?\" and \"Is there anything else on your mind health-wise that you'd like us to address today?\". Finally, they confirm no further concerns with a last check: \"Just to make sure, is there anything else at all you'd like to discuss?\". This approach ensures a comprehensive understanding of the patient's issues."
#   }
# }

# Example 2:
# Input: 
# Physician: "Hello, I'm Dr. Johnson. What's the main reason for your visit today?"
# Patient: "I've been experiencing shortness of breath."
# Physician: "I see. Can you tell me more about that?"
# Patient: "It's been happening for about a week, especially when I climb stairs."
# Physician: "Thank you for sharing that. Is there anything else you're concerned about today?"
# Patient: "Yes, I've also noticed some swelling in my ankles."
# Physician: "Alright, I'll make sure to examine that as well. Let's start with your breathing issues."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Elicitation of main concern",
#       "Probing for additional concerns",
#       "Use of one \"what else\" question"
#     ],
#     "elements_absent": [
#       "Final confirmation of no further concerns"
#     ],
#     "score": 4,
#     "justification": "The physician effectively elicits the main concern and probes for additional issues. They ask \"What's the main reason for your visit today?\" and follow up with \"Can you tell me more about that?\". They also ask about additional concerns with \"Is there anything else you're concerned about today?\". However, they miss the opportunity for a final \"what else\" question after the patient mentions ankle swelling, which would have ensured no other concerns were left unaddressed."
#   }
# }

# Example 3:
# Input: 
# Physician: "Good afternoon. What seems to be the problem today?"
# Patient: "I've been having this persistent cough that won't go away."
# Physician: "How long have you had this cough?"
# Patient: "It's been about three weeks now."
# Physician: "I see. And is it a dry cough or are you coughing up anything?"
# Patient: "It's mostly dry, but sometimes I cough up a little mucus."
# Physician: "Alright, let's take a closer look at that cough then."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Elicitation of main concern"
#     ],
#     "elements_absent": [
#       "Probing for additional concerns",
#       "Use of \"what else\" questions",
#       "Confirmation of no further concerns"
#     ],
#     "score": 3,
#     "justification": "The physician adequately elicits information about the patient's main concern, starting with \"What seems to be the problem today?\" and following up with specific questions about the cough. However, they fail to ask about any additional concerns or use any \"what else\" questions. This approach risks missing other health issues the patient might have."
#   }
# }

# Example 4:
# Input: 
# Physician: "Your chart says you're here for a rash. Where is it located?"
# Patient: "Yes, it's on my arm and it's really itchy."
# Physician: "How long have you had it?"
# Patient: "About a week now."
# Physician: "Okay, let me take a look at it."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Elicitation of main concern",
#       "Probing for additional concerns",
#       "Use of \"what else\" questions",
#       "Confirmation of no further concerns"
#     ],
#     "score": 2,
#     "justification": "The physician doesn't actually elicit the patient's concern, instead stating it based on the chart: \"Your chart says you're here for a rash.\" They ask follow-up questions about the rash but don't explore if this is indeed the patient's main concern or if there are any other issues. There's no attempt to probe for additional concerns or use any \"what else\" questions."
#   }
# }

# Example 5:
# Input: 
# Physician: "I see you're scheduled for a check-up today. I'm going to start by checking your blood pressure."
# Patient: "Actually, I've been having some chest pain lately."
# Physician: "Okay, I'll make a note of that. Please roll up your sleeve for the blood pressure cuff."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Elicitation of main concern",
#       "Probing for additional concerns",
#       "Use of \"what else\" questions",
#       "Confirmation of no further concerns"
#     ],
#     "score": 1,
#     "justification": "The physician completely fails to elicit the patient's concerns. They assume the visit is for a routine check-up without asking the patient's reason for the visit. Even when the patient volunteers information about chest pain, the physician merely acknowledges it without exploring further. There's no attempt to understand the patient's concerns or check for additional issues."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
