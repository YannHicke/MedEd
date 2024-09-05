QUESTIONING_SKILLS_DUPLICATION = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the student’s questioning skills, specifically looking at their duplication of information. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student does not repeat questions, seeking duplication of information that has been previously provided, unless clarification or summarization of prior information is necessary. 
      - **Score 4:** The student only rarely repeats questions that duplicate information. Questions are repeated for clarification or summarization.
      - **Score 3:** The student only rarely repeats questions. Questions are repeated not for the purpose of summarization or clarification of information, but as a result of the student’s failure to remember the data.
      - **Score 2:** The student often repeats questions. Questions are repeated due to the student’s failure to remember previously provided information. The interview flow is disrupted, but not to the extent of a score of 1. 
      - **Score 1:** The student frequently repeats questions seeking information previously provided because they fail to remember the data already obtained. The interview flow is largely disrupted.

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





# QUESTIONING_SKILLS_DUPLICATION_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student avoids unnecessary repetition of questions seeking information that has already been provided. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Unnecessary repetition of questions
#       - Repetition for clarification or summarization
#       - Attention to previously provided information
#       - Effective tracking of patient information

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** No unnecessary repetition; repetition only for clarification or summarization
#     - **Score 3:** Rare repetition due to lapses in memory, not for clarification or summarization
#     - **Score 1:** Consistent repetition showing failure to track or remember patient information

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

# Examples:
#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"What brings you in today?\"
# Patient: \"I've been having these terrible headaches for the past two weeks.\"
# Physician: \"I'm sorry to hear that. Can you tell me more about these headaches?\"
# Patient: \"They usually start in the afternoon and get worse as the day goes on. The pain is mostly on the right side of my head.\"
# Physician: \"I see. And how often do you experience these headaches?\"
# Patient: \"Almost every day now.\"
# Physician: \"Have you noticed anything that seems to trigger them?\"
# Patient: \"I'm not sure, but I think they might be worse when I'm stressed.\"
# Physician: \"Thank you for sharing that. Now, just to clarify, you mentioned the headaches started two weeks ago and occur almost daily, primarily in the afternoon and evening, correct?\"
# Patient: \"Yes, that's right.\"
# Physician: \"And they're mainly on the right side of your head, possibly exacerbated by stress?\"
# Patient: \"Exactly.\"
# Physician: \"Alright, thank you. Now, have you experienced any other symptoms along with the headaches?\"",
#       "response": {
#         "elements_present": [
#           "Repetition for clarification or summarization",
#           "Attention to previously provided information",
#           "Effective tracking of patient information"
#         ],
#         "elements_absent": [
#           "Unnecessary repetition of questions"
#         ],
#         "score": 5,
#         "justification": "The physician demonstrates excellent questioning skills without unnecessary duplication. They ask for clarification and summarize information previously provided, showing effective tracking of patient information. For example, when they say, \"Now, just to clarify, you mentioned the headaches started two weeks ago and occur almost daily, primarily in the afternoon and evening, correct?\", they're confirming and summarizing the information rather than asking for it again. This approach ensures accuracy and shows attentiveness to the patient's narrative without redundant questioning."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"What seems to be the problem?\"
# Patient: \"I've been having stomach pain for about a week now.\"
# Physician: \"Can you describe the pain?\"
# Patient: \"It's a sharp pain, mostly in my upper abdomen. It gets worse after I eat.\"
# Physician: \"I see. And how long have you been experiencing this pain?\"
# Patient: \"As I mentioned, it's been about a week.\"
# Physician: \"Oh, right, sorry about that. Are there any other symptoms accompanying the pain?\"
# Patient: \"Yes, I've been feeling nauseous, especially in the mornings.\"
# Physician: \"Alright. Have you noticed any changes in your appetite?\"
# Patient: \"Not really, but I've been avoiding large meals because they make the pain worse.\"
# Physician: \"Understood. Now, you said the pain was in your upper abdomen, correct?\"
# Patient: \"Yes, that's right.\"",
#       "response": {
#         "elements_present": [
#           "Rare repetition due to lapses in memory",
#           "Some attention to previously provided information"
#         ],
#         "elements_absent": [
#           "Consistent unnecessary repetition",
#           "Repetition for clarification or summarization"
#         ],
#         "score": 3,
#         "justification": "The physician demonstrates some lapses in memory, as seen when they ask, \"And how long have you been experiencing this pain?\" after the patient had already provided this information. The physician acknowledges this mistake, saying \"Oh, right, sorry about that.\" While there is some repetition, it's not consistent throughout the interview. The physician does show attention to previously provided information in most cases, such as confirming the location of the pain at the end of the excerpt. This performance aligns with a score of 3, where there are rare repetitions due to memory lapses rather than for clarification or summarization."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"What brings you in today?\"
# Patient: \"I've been having severe lower back pain for the past month.\"
# Physician: \"I see. And where exactly is the pain located?\"
# Patient: \"It's in my lower back, mostly on the right side.\"
# Physician: \"Okay. How long have you been experiencing this pain?\"
# Patient: \"As I said, it's been about a month now.\"
# Physician: \"Right. And is the pain constant or does it come and go?\"
# Patient: \"It's pretty constant, but gets worse when I bend or lift things.\"
# Physician: \"I understand. Now, where did you say the pain was located again?\"
# Patient: \"It's in my lower back, on the right side, as I mentioned before.\"
# Physician: \"Alright. And how long did you say you've had this pain?\"
# Patient: \"I've told you twice now, it's been a month.\"",
#       "response": {
#         "elements_present": [
#           "Consistent repetition showing failure to track or remember patient information"
#         ],
#         "elements_absent": [
#           "Attention to previously provided information",
#           "Effective tracking of patient information",
#           "Repetition for clarification or summarization"
#         ],
#         "score": 1,
#         "justification": "The physician consistently seeks information that has already been provided, showing a clear failure to track or remember patient information. They ask about the duration of the pain twice (\"How long have you been experiencing this pain?\" and later \"And how long did you say you've had this pain?\") and the location of the pain twice (\"And where exactly is the pain located?\" and later \"Now, where did you say the pain was located again?\"). This repetition is not for clarification or summarization, but appears to be due to a failure to retain the information. The patient's frustration is evident in their final response. This consistent unnecessary repetition significantly disrupts the flow of the interview and warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# QUESTIONING_SKILLS_DUPLICATION2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student avoids unnecessary repetition of questions seeking information that has already been provided. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Unnecessary repetition of questions
#    - Repetition for clarification or summarization
#    - Attention to previously provided information
#    - Effective tracking of patient information

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: No unnecessary repetition; repetition only for clarification or summarization
#    - Score 3: Rare repetition due to lapses in memory, not for clarification or summarization
#    - Score 1: Consistent repetition showing failure to track or remember patient information

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
# Physician: "What brings you in today?"
# Patient: "I've been having these terrible headaches for the past two weeks."
# Physician: "I'm sorry to hear that. Can you tell me more about these headaches?"
# Patient: "They usually start in the afternoon and get worse as the day goes on. The pain is mostly on the right side of my head."
# Physician: "I see. And how often do you experience these headaches?"
# Patient: "Almost every day now."
# Physician: "Have you noticed anything that seems to trigger them?"
# Patient: "I'm not sure, but I think they might be worse when I'm stressed."
# Physician: "Thank you for sharing that. Now, just to clarify, you mentioned the headaches started two weeks ago and occur almost daily, primarily in the afternoon and evening, correct?"
# Patient: "Yes, that's right."
# Physician: "And they're mainly on the right side of your head, possibly exacerbated by stress?"
# Patient: "Exactly."
# Physician: "Alright, thank you. Now, have you experienced any other symptoms along with the headaches?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Repetition for clarification or summarization",
#       "Attention to previously provided information",
#       "Effective tracking of patient information"
#     ],
#     "elements_absent": [
#       "Unnecessary repetition of questions"
#     ],
#     "score": 5,
#     "justification": "The physician demonstrates excellent questioning skills without unnecessary duplication. They ask for clarification and summarize information previously provided, showing effective tracking of patient information. For example, when they say, \"Now, just to clarify, you mentioned the headaches started two weeks ago and occur almost daily, primarily in the afternoon and evening, correct?\", they're confirming and summarizing the information rather than asking for it again. This approach ensures accuracy and shows attentiveness to the patient's narrative without redundant questioning."
#   }
# }

# Example 2:
# Input: 
# Physician: "What seems to be the problem?"
# Patient: "I've been having stomach pain for about a week now."
# Physician: "Can you describe the pain?"
# Patient: "It's a sharp pain, mostly in my upper abdomen. It gets worse after I eat."
# Physician: "I see. And how long have you been experiencing this pain?"
# Patient: "As I mentioned, it's been about a week."
# Physician: "Oh, right, sorry about that. Are there any other symptoms accompanying the pain?"
# Patient: "Yes, I've been feeling nauseous, especially in the mornings."
# Physician: "Alright. Have you noticed any changes in your appetite?"
# Patient: "Not really, but I've been avoiding large meals because they make the pain worse."
# Physician: "Understood. Now, you said the pain was in your upper abdomen, correct?"
# Patient: "Yes, that's right."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Rare repetition due to lapses in memory",
#       "Some attention to previously provided information"
#     ],
#     "elements_absent": [
#       "Consistent unnecessary repetition",
#       "Repetition for clarification or summarization"
#     ],
#     "score": 3,
#     "justification": "The physician demonstrates some lapses in memory, as seen when they ask, \"And how long have you been experiencing this pain?\" after the patient had already provided this information. The physician acknowledges this mistake, saying \"Oh, right, sorry about that.\" While there is some repetition, it's not consistent throughout the interview. The physician does show attention to previously provided information in most cases, such as confirming the location of the pain at the end of the excerpt. This performance aligns with a score of 3, where there are rare repetitions due to memory lapses rather than for clarification or summarization."
#   }
# }

# Example 3:
# Input: 
# Physician: "What brings you in today?"
# Patient: "I've been having severe lower back pain for the past month."
# Physician: "I see. And where exactly is the pain located?"
# Patient: "It's in my lower back, mostly on the right side."
# Physician: "Okay. How long have you been experiencing this pain?"
# Patient: "As I said, it's been about a month now."
# Physician: "Right. And is the pain constant or does it come and go?"
# Patient: "It's pretty constant, but gets worse when I bend or lift things."
# Physician: "I understand. Now, where did you say the pain was located again?"
# Patient: "It's in my lower back, on the right side, as I mentioned before."
# Physician: "Alright. And how long did you say you've had this pain?"
# Patient: "I've told you twice now, it's been a month."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Consistent repetition showing failure to track or remember patient information"
#     ],
#     "elements_absent": [
#       "Attention to previously provided information",
#       "Effective tracking of patient information",
#       "Repetition for clarification or summarization"
#     ],
#     "score": 1,
#     "justification": "The physician consistently seeks information that has already been provided, showing a clear failure to track or remember patient information. They ask about the duration of the pain twice (\"How long have you been experiencing this pain?\" and later \"And how long did you say you've had this pain?\") and the location of the pain twice (\"And where exactly is the pain located?\" and later \"Now, where did you say the pain was located again?\"). This repetition is not for clarification or summarization, but appears to be due to a failure to retain the information. The patient's frustration is evident in their final response. This consistent unnecessary repetition significantly disrupts the flow of the interview and warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
