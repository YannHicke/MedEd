OPENING = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student conducts the opening of this medical interview. You will then provide your evaluation in a given JSON format. 

To ensure a thorough evaluation, follow these steps:

  **Step 1. Understanding the Task:**
    - Read the following note:
      **Note:** Learner begins with the introduction of self, clarification of roles, and inquiry of how to address patient. The opening question identifies the problems or issues that the patient wishes to address. 
      **Example:** “Hello, I’m Carol Redding, (shaking patient’s hand) a student working with the team. Would you prefer I call you, Ms. Black or Phyllis? Are you comfortable right now? What brings you in today?”

  **Step 2. Identify Key Elements:**
    - As you read the opening of the transcript, and using your understanding from Step 1, note whether the student:
      - Introduces self
      - Clarifies their role
      - Inquires how to address the patient
      - Uses patient’s name 

  **Step 3. Scoring:** Compare your findings from Step 2 to the following scoring criteria:
    - **Score 5:** All elements are present
    - **Score 4:** Student’s introduction is missing one element
    - **Score 3:** Student’s introduction is missing two elements
    - **Score 2:** Student's introduction is missing three or all four elements, and only a basic greeting (e.g. \"Hello\") is present.
    - **Score 1:** There is no introduction

  **Step 4. Justification:** Based on your analysis in Steps 1, 2, and 3, assign a score using the provided rubric strictly, and explain your reasoning clearly. Your evaluation should be rigorous, impartial, and evidence-based. Directly quote the transcript to support your evaluation.

Provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

{
  "evaluation": {
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the transcript to support your evaluation"
  }
}

Now, please evaluate the following transcript:
"""






# OPENING_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating the opening of this medical interview based on a provided full transcript. 
# Your goal is to assess how well the medical student initiates the conversation with the patient. 
# To ensure a thorough evaluation, follow these steps:
  
#   **1. Identify Key Elements:**
#     -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Self-introduction
#       - Role clarification
#       - Polite patient address inquiry

#   **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** All three key elements are present.
#     - **Score 4:** Two key elements are present.
#     - **Score 3:** One key element is present. 
#     - **Score 2:** Only a basic greeting (e.g., \"Hello\") is provided.
#     - **Score 1:** No introduction or greeting is given.

#   **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.
  
#   "examples": [
#     {
#       "excerpt": "\"Good morning, I'm Dr. Smith, a resident assigned to your case today. May I know how you'd like to be addressed?\"",
#       "response": {
#         "elements_present": [
#           "Self-introduction (\"Good morning, I'm Dr. Smith\")",
#           "Role clarification (\"a resident assigned to your case today\")",
#           "Polite patient address inquiry (\"May I know how you'd like to be addressed?\")"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "This introduction includes all three key elements, demonstrating a complete and respectful opening."
#       }
#     },
#     {
#       "excerpt": "\"Hi, I'm Dr. Jones, one of the physicians here. What brings you in?\"",
#       "response": {
#         "elements_present": [
#           "Self-introduction (\"Hi, I'm Dr. Jones\")",
#           "Role clarification (\"one of the physicians here\")"
#         ],
#         "elements_absent": [
#           "Polite patient address inquiry"
#         ],
#         "score": 4,
#         "justification": "This introduction is missing a patient address inquiry. While the physician introduces themselves and their role, they don't ask how the patient prefers to be addressed."
#       }
#     },
#     {
#       "excerpt": "\"I'm covering for Dr. Lee today. What's your name?\"",
#       "response": {
#         "elements_present": [
#           "Role clarification (\"covering for Dr. Lee today\")"
#         ],
#         "elements_absent": [
#           "Self-introduction",
#           "Polite patient address inquiry"
#         ], 
#         "score": 3,
#         "justification": "This introduction lacks a self-introduction and uses a less polite way to ask for the patient's name. It relies on the context of covering for another doctor." 
#       }
#     },
#     {
#       "excerpt": "\"Hello there.  What seems to be the issue?\"",
#       "response":{
#         "elements_present": [],
#         "elements_absent": [
#           "Self-introduction",
#           "Role clarification",
#           "Polite patient address inquiry"
#         ],
#         "score": 2,
#         "justification": "While there is a greeting, this opening jumps into the medical issue without introducing themselves or their role."
#       }
#     },
#     {
#       "excerpt": "\"Tell me about your pain.\"",
#       "response":{
#         "elements_present": [],
#         "elements_absent": [
#           "Self-introduction",
#           "Role clarification",
#           "Polite patient address inquiry"
#         ],
#         "score": 1,
#         "justification": "This opening lacks any form of introduction and immediately focuses on the patient's symptoms, which can feel abrupt and impersonal." 
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
#   """

# OPENING_ANTHROPIC_OLD = f"""
# You will be evaluating the opening of a medical interview between a medical student (referred to as the physician) and a patient. Your task is to assess how well the medical student initiates the conversation based on the provided transcript.

# Here is the full transcript of the medical interview:

# <transcript>
# {{TRANSCRIPT}}
# </transcript>

# Carefully analyze the opening of the interview, focusing on the following elements:
# 1. Self-introduction by the medical student
# 2. Role clarification
# 3. Polite patient address inquiry using the patient's name

# Use this rubric to evaluate the opening:
# - Score 5: Complete introduction with self-introduction, role clarification, and polite patient address inquiry using the patient's name.
# - Score 4: One element missing from the introduction.
# - Score 3: Two elements missing from the introduction.
# - Score 2: Only a basic greeting, such as 'hello', with most elements missing.
# - Score 1: No introduction provided.

# First, provide your reasoning for the score you will assign. Consider which elements of the introduction are present or missing, and how well they were executed. Write your reasoning inside <reasoning> tags.

# Then, based on your analysis and the rubric, assign a score from 1 to 5. Write your score inside <score> tags.

# Present your evaluation in the following format:
# <evaluation>
# <reasoning>
# [Your detailed reasoning here]
# </reasoning>
# <score>
# [Your score here]
# </score>
# </evaluation>
# """

# OPENING2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the opening of this medical interview and provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Self-introduction
#    - Role clarification
#    - Polite patient address inquiry

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: All three key elements are present.
#    - Score 4: Two key elements are present.
#    - Score 3: One key element is present. 
#    - Score 2: Only a basic greeting (e.g., "Hello") is provided.
#    - Score 1: No introduction or greeting is given.

# 3. Provide Justification: Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

# Please provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

# {
#   "evaluation": {
#     "elements_present": [
#       "List of elements present in the opening"
#     ],
#     "elements_absent": [
#       "List of elements missing from the opening"
#     ],
#     "score": 0,
#     "justification": "A clear explanation of your scoring, with direct quotes from the excerpt to support your evaluation"
#   }
# }

# Examples:
# The following examples illustrate how to apply the evaluation criteria and format the response:

# Example 1:
# Input: "Good morning, I'm Dr. Smith, a resident assigned to your case today. May I know how you'd like to be addressed?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Self-introduction (\"Good morning, I'm Dr. Smith\")",
#       "Role clarification (\"a resident assigned to your case today\")",
#       "Polite patient address inquiry (\"May I know how you'd like to be addressed?\")"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "This introduction includes all three key elements, demonstrating a complete and respectful opening. The physician provides a self-introduction (\"I'm Dr. Smith\"), clarifies their role (\"a resident assigned to your case today\"), and politely inquires about the patient's preferred form of address (\"May I know how you'd like to be addressed?\")."
#   }
# }

# Example 2:
# Input: "Hi, I'm Dr. Jones, one of the physicians here. What brings you in?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Self-introduction (\"Hi, I'm Dr. Jones\")",
#       "Role clarification (\"one of the physicians here\")"
#     ],
#     "elements_absent": [
#       "Polite patient address inquiry"
#     ],
#     "score": 4,
#     "justification": "This introduction is missing a patient address inquiry. The physician introduces themselves (\"I'm Dr. Jones\") and clarifies their role (\"one of the physicians here\"), but they don't ask how the patient prefers to be addressed. Instead, they directly ask about the reason for the visit (\"What brings you in?\")."
#   }
# }

# Example 3:
# Input: "I'm covering for Dr. Lee today. What's your name?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Role clarification (\"covering for Dr. Lee today\")"
#     ],
#     "elements_absent": [
#       "Self-introduction",
#       "Polite patient address inquiry"
#     ],
#     "score": 3,
#     "justification": "This introduction lacks a self-introduction and uses a less polite way to ask for the patient's name. It provides role clarification (\"I'm covering for Dr. Lee today\"), but doesn't include the physician's name. The question \"What's your name?\" is direct but not as polite as inquiring about the patient's preferred form of address."
#   }
# }

# Example 4:
# Input: "Hello there. What seems to be the issue?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Self-introduction",
#       "Role clarification",
#       "Polite patient address inquiry"
#     ],
#     "score": 2,
#     "justification": "While there is a basic greeting (\"Hello there\"), this opening jumps into the medical issue without the physician introducing themselves or their role, or asking how the patient prefers to be addressed. The greeting alone is not sufficient for a higher score, as it lacks all three key elements of a proper medical interview opening."
#   }
# }

# Example 5:
# Input: "Tell me about your pain."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Self-introduction",
#       "Role clarification",
#       "Polite patient address inquiry"
#     ],
#     "score": 1,
#     "justification": "This opening lacks any form of introduction or greeting and immediately focuses on the patient's symptoms. There is no self-introduction, role clarification, or patient address inquiry. The abrupt nature of \"Tell me about your pain\" can feel impersonal and fails to establish any rapport with the patient."
#   }
# }

# Now, please evaluate the following transcript:
# """