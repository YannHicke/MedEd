ENCOURAGEMENT_OF_QUESTIONS = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student encourages questions from the patient. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Identify Key Elements:**
    - As you read the transcript, create a list noting whether each element is present or absent:
      - Encourages questions from the patient
      - Creates an open and supportive environment for questions

  **Step 2. Scoring:**
    - As you read the transcript, use your list from Step 1 and evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student encourages the patient to ask questions at the end of a major subsection. The student gives the patient the opportunity to bring up additional topics or points not covered in the interview.
      - **Score 4:** The student encourages opportunities for the patient to ask questions, though not consistently at the end of every major subsection. They mostly allow for additional topics to be brought up, but may not actively encourage this as thoroughly as in a score of 5. The student shows a clear attempt to be open to patient input, even if not as proactively as in a top performance.
      - **Score 3:** The student provides the patient with the opportunity to discuss any additional points or ask any additional questions but neither encourages or discourages them. 
      - **Score 2:** The student makes limited attempts to allow for patient questions or additional topics. The opportunity for the patient to discuss additional topics is minimal. 
      - **Score 1:** The student fails to provide the patient with the opportunity to ask questions or discuss additional points. The student may discourage the patient’s questions. 

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




# ENCOURAGEMENT_OF_QUESTIONS_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student encourages the patient to ask questions throughout the interview.
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Encouragement to ask questions at the end of major subsections
#       - Opportunity for patient to bring up additional topics
#       - Final opportunity for questions at the end of the interview
#       - Climate and pace allowing for questions
#       - Active discouragement of questions

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Multiple opportunities for questions, including one at the end
#     - **Score 4:** One opportunity for questions at the end of the interview
#     - **Score 3:** One opportunity for questions, but not near the end
#     - **Score 2:** No specific invitation for questions, but climate allows them
#     - **Score 1:** No opportunity for questions, or active discouragement

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"We've covered a lot about your diagnosis. Do you have any questions about what we've discussed so far?\"
# Patient: \"Yes, I was wondering about the side effects of the medication.\"
# Physician: \"That's a great question. Let's go through the potential side effects...\"
# [Physician answers the question]
# Physician: \"Does that clarify things for you?\"
# Patient: \"Yes, thank you.\"
# [Later in the interview, after discussing treatment options]
# Physician: \"Before we move on, do you have any questions about the treatment options we've discussed?\"
# Patient: \"No, I think I understand.\"
# [At the end of the interview]
# Physician: \"We've covered a lot today. Is there anything else you'd like to ask or any other concerns you want to discuss that we haven't touched on?\"
# Patient: \"Actually, I was wondering about...\"
# [Physician addresses the final questions]
# Physician: \"I'm glad you brought that up. Are there any other questions or concerns?\"
# Patient: \"No, I think that covers everything.\"
# Physician: \"Alright. Remember, if you think of anything else later, don't hesitate to call or bring it up at our next appointment.\"",
#       "response": {
#         "elements_present": [
#           "Encouragement to ask questions at the end of major subsections",
#           "Opportunity for patient to bring up additional topics",
#           "Final opportunity for questions at the end of the interview",
#           "Climate and pace allowing for questions"
#         ],
#         "elements_absent": [
#           "Active discouragement of questions"
#         ],
#         "score": 5,
#         "justification": "The physician excels in encouraging questions throughout the interview. They provide multiple opportunities for the patient to ask questions, first after discussing the diagnosis (\"Do you have any questions about what we've discussed so far?\"), then after treatment options (\"Before we move on, do you have any questions about the treatment options we've discussed?\"), and finally at the end of the interview (\"Is there anything else you'd like to ask or any other concerns you want to discuss that we haven't touched on?\"). The physician also creates a climate that encourages questions by responding positively to the patient's inquiries and explicitly inviting additional concerns. This comprehensive approach to encouraging questions throughout the interview warrants a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"So based on your symptoms and test results, it looks like you have high blood pressure. We'll need to start treatment to manage this condition.\"
# Patient: \"Okay...\"
# Physician: \"There are several treatment options we can consider, including lifestyle changes and medication. I think a combination of both would be best in your case.\"
# Patient: \"I see.\"
# [Physician continues explaining the treatment plan]
# Physician: \"So that's the plan moving forward. Now, before we wrap up, do you have any questions about anything we've discussed today or anything else you'd like to bring up?\"
# Patient: \"Actually, yes. I was wondering about...\"
# [Physician answers the question]
# Physician: \"I'm glad you asked. Any other questions or concerns?\"
# Patient: \"No, I think that covers it.\"
# Physician: \"Alright. If you think of anything else later, feel free to call the office.\"",
#       "response": {
#         "elements_present": [
#           "Final opportunity for questions at the end of the interview",
#           "Opportunity for patient to bring up additional topics",
#           "Climate and pace allowing for questions"
#         ],
#         "elements_absent": [
#           "Encouragement to ask questions at the end of major subsections",
#           "Active discouragement of questions"
#         ],
#         "score": 4,
#         "justification": "The physician provides a clear opportunity for questions at the end of the interview, saying \"Now, before we wrap up, do you have any questions about anything we've discussed today or anything else you'd like to bring up?\" This invitation is open-ended, allowing the patient to ask about any topic. The physician also responds positively when the patient does ask a question and offers a second chance for additional questions. However, there are no earlier opportunities for questions during the interview, such as after explaining the diagnosis or treatment options. The climate seems open to questions, but the lack of multiple opportunities throughout the interview prevents this from scoring a 5. This aligns with a score of 4, where there is one good opportunity for questions at the end of the encounter."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"Your test results show elevated blood sugar levels, which indicates diabetes. We'll need to start treatment to manage this condition.\"
# Patient: \"Diabetes? I wasn't expecting that.\"
# Physician: \"Do you have any questions about the diagnosis?\"
# Patient: \"Well, yes. What exactly does this mean for my health?\"
# [Physician answers the question]
# Physician: \"Now, let's discuss your treatment options. We'll start with dietary changes and possibly medication.\"
# [Physician explains treatment plan]
# Physician: \"So, that's what we'll do. I'll see you for a follow-up in a month to check your progress.\"
# Patient: \"Okay, but I was wondering...\"
# Physician: \"We're out of time for today, but we can discuss any other concerns at your next appointment.\"",
#       "response": {
#         "elements_present": [
#           "One opportunity for questions, but not near the end"
#         ],
#         "elements_absent": [
#           "Encouragement to ask questions at the end of major subsections",
#           "Final opportunity for questions at the end of the interview",
#           "Opportunity for patient to bring up additional topics"
#         ],
#         "score": 3,
#         "justification": "The physician provides one clear opportunity for questions early in the interview, asking \"Do you have any questions about the diagnosis?\" This shows some effort to encourage patient questions. However, there are no further opportunities for questions throughout the rest of the interview, including at the end. When the patient tries to ask a question at the end, the physician cuts them off, citing time constraints. This approach, where there is one opportunity for questions but not near the end of the encounter, aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"Your blood pressure is higher than it should be. We need to work on bringing it down.\"
# Patient: \"I see...\"
# Physician: \"I'm going to prescribe a medication to help lower your blood pressure. You'll need to take it once daily.\"
# Patient: \"Okay.\"
# Physician: \"It's also important to make some lifestyle changes. Try to reduce your salt intake and get regular exercise.\"
# Patient: \"Alright.\"
# Physician: \"Do you understand everything I've told you?\"
# Patient: \"I think so.\"
# Physician: \"Good. I'll see you for a follow-up in two months.\"",
#       "response": {
#         "elements_present": [
#           "Climate and pace potentially allowing for questions"
#         ],
#         "elements_absent": [
#           "Encouragement to ask questions at the end of major subsections",
#           "Opportunity for patient to bring up additional topics",
#           "Final opportunity for questions at the end of the interview",
#           "Active discouragement of questions"
#         ],
#         "score": 2,
#         "justification": "The physician does not specifically invite the patient to ask questions at any point during the interview. However, the pace of the conversation and the physician's pauses after providing information could potentially allow the patient to ask questions if they wanted to. The physician's question \"Do you understand everything I've told you?\" provides a slight opening for the patient to express confusion or ask for clarification, but it's not a direct invitation for questions. While the physician doesn't actively discourage questions, they also don't create an environment that explicitly encourages them. This aligns with a score of 2, where the climate and pace of the interview allow for questions, but there's no specific invitation to ask them."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Your cholesterol is too high. You need to start taking this medication immediately.\"
# Patient: \"But I—\"
# Physician: \"It's essential for your health. Take one pill every morning.\"
# Patient: \"I was wondering if—\"
# Physician: \"Just follow the instructions on the bottle. Any other questions will have to wait until your next appointment. We're running behind schedule.\"
# Patient: \"Okay...\"
# Physician: \"Good. The nurse will schedule your follow-up on your way out.\"",
#       "response": {
#         "elements_present": [
#           "Active discouragement of questions"
#         ],
#         "elements_absent": [
#           "Encouragement to ask questions at the end of major subsections",
#           "Opportunity for patient to bring up additional topics",
#           "Final opportunity for questions at the end of the interview",
#           "Climate and pace allowing for questions"
#         ],
#         "score": 1,
#         "justification": "The physician not only fails to provide any opportunities for questions but actively discourages them. When the patient attempts to speak or ask questions, the physician interrupts them and continues with their own agenda. The statement \"Any other questions will have to wait until your next appointment. We're running behind schedule\" clearly shows that the physician is not open to questions during this encounter. This approach creates a climate where the patient may feel their concerns and questions are not valued. The complete lack of opportunity for questions and the active discouragement of patient input clearly warrant a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# ENCOURAGEMENT_OF_QUESTIONS2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student encourages the patient to ask questions throughout the interview. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Encouragement to ask questions at the end of major subsections
#    - Opportunity for patient to bring up additional topics
#    - Final opportunity for questions at the end of the interview
#    - Climate and pace allowing for questions
#    - Active discouragement of questions

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Multiple opportunities for questions, including one at the end
#    - Score 4: One opportunity for questions at the end of the interview
#    - Score 3: One opportunity for questions, but not near the end
#    - Score 2: No specific invitation for questions, but climate allows them
#    - Score 1: No opportunity for questions, or active discouragement

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
# Physician: "We've covered a lot about your diagnosis. Do you have any questions about what we've discussed so far?"
# Patient: "Yes, I was wondering about the side effects of the medication."
# Physician: "That's a great question. Let's go through the potential side effects..."
# [Physician answers the question]
# Physician: "Does that clarify things for you?"
# Patient: "Yes, thank you."
# [Later in the interview, after discussing treatment options]
# Physician: "Before we move on, do you have any questions about the treatment options we've discussed?"
# Patient: "No, I think I understand."
# [At the end of the interview]
# Physician: "We've covered a lot today. Is there anything else you'd like to ask or any other concerns you want to discuss that we haven't touched on?"
# Patient: "Actually, I was wondering about..."
# [Physician addresses the final questions]
# Physician: "I'm glad you brought that up. Are there any other questions or concerns?"
# Patient: "No, I think that covers everything."
# Physician: "Alright. Remember, if you think of anything else later, don't hesitate to call or bring it up at our next appointment."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Encouragement to ask questions at the end of major subsections",
#       "Opportunity for patient to bring up additional topics",
#       "Final opportunity for questions at the end of the interview",
#       "Climate and pace allowing for questions"
#     ],
#     "elements_absent": [
#       "Active discouragement of questions"
#     ],
#     "score": 5,
#     "justification": "The physician excels in encouraging questions throughout the interview. They provide multiple opportunities for the patient to ask questions, first after discussing the diagnosis (\"Do you have any questions about what we've discussed so far?\"), then after treatment options (\"Before we move on, do you have any questions about the treatment options we've discussed?\"), and finally at the end of the interview (\"Is there anything else you'd like to ask or any other concerns you want to discuss that we haven't touched on?\"). The physician also creates a climate that encourages questions by responding positively to the patient's inquiries and explicitly inviting additional concerns. This comprehensive approach to encouraging questions throughout the interview warrants a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "So based on your symptoms and test results, it looks like you have high blood pressure. We'll need to start treatment to manage this condition."
# Patient: "Okay..."
# Physician: "There are several treatment options we can consider, including lifestyle changes and medication. I think a combination of both would be best in your case."
# Patient: "I see."
# [Physician continues explaining the treatment plan]
# Physician: "So that's the plan moving forward. Now, before we wrap up, do you have any questions about anything we've discussed today or anything else you'd like to bring up?"
# Patient: "Actually, yes. I was wondering about..."
# [Physician answers the question]
# Physician: "I'm glad you asked. Any other questions or concerns?"
# Patient: "No, I think that covers it."
# Physician: "Alright. If you think of anything else later, feel free to call the office."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Final opportunity for questions at the end of the interview",
#       "Opportunity for patient to bring up additional topics",
#       "Climate and pace allowing for questions"
#     ],
#     "elements_absent": [
#       "Encouragement to ask questions at the end of major subsections",
#       "Active discouragement of questions"
#     ],
#     "score": 4,
#     "justification": "The physician provides a clear opportunity for questions at the end of the interview, saying \"Now, before we wrap up, do you have any questions about anything we've discussed today or anything else you'd like to bring up?\" This invitation is open-ended, allowing the patient to ask about any topic. The physician also responds positively when the patient does ask a question and offers a second chance for additional questions. However, there are no earlier opportunities for questions during the interview, such as after explaining the diagnosis or treatment options. The climate seems open to questions, but the lack of multiple opportunities throughout the interview prevents this from scoring a 5. This aligns with a score of 4, where there is one good opportunity for questions at the end of the encounter."
#   }
# }

# Example 3:
# Input: 
# Physician: "Your test results show elevated blood sugar levels, which indicates diabetes. We'll need to start treatment to manage this condition."
# Patient: "Diabetes? I wasn't expecting that."
# Physician: "Do you have any questions about the diagnosis?"
# Patient: "Well, yes. What exactly does this mean for my health?"
# [Physician answers the question]
# Physician: "Now, let's discuss your treatment options. We'll start with dietary changes and possibly medication."
# [Physician explains treatment plan]
# Physician: "So, that's what we'll do. I'll see you for a follow-up in a month to check your progress."
# Patient: "Okay, but I was wondering..."
# Physician: "We're out of time for today, but we can discuss any other concerns at your next appointment."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "One opportunity for questions, but not near the end"
#     ],
#     "elements_absent": [
#       "Encouragement to ask questions at the end of major subsections",
#       "Final opportunity for questions at the end of the interview",
#       "Opportunity for patient to bring up additional topics"
#     ],
#     "score": 3,
#     "justification": "The physician provides one clear opportunity for questions early in the interview, asking \"Do you have any questions about the diagnosis?\" This shows some effort to encourage patient questions. However, there are no further opportunities for questions throughout the rest of the interview, including at the end. When the patient tries to ask a question at the end, the physician cuts them off, citing time constraints. This approach, where there is one opportunity for questions but not near the end of the encounter, aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "Your blood pressure is higher than it should be. We need to work on bringing it down."
# Patient: "I see..."
# Physician: "I'm going to prescribe a medication to help lower your blood pressure. You'll need to take it once daily."
# Patient: "Okay."
# Physician: "It's also important to make some lifestyle changes. Try to reduce your salt intake and get regular exercise."
# Patient: "Alright."
# Physician: "Do you understand everything I've told you?"
# Patient: "I think so."
# Physician: "Good. I'll see you for a follow-up in two months."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Climate and pace potentially allowing for questions"
#     ],
#     "elements_absent": [
#       "Encouragement to ask questions at the end of major subsections",
#       "Opportunity for patient to bring up additional topics",
#       "Final opportunity for questions at the end of the interview",
#       "Active discouragement of questions"
#     ],
#     "score": 2,
#     "justification": "The physician does not specifically invite the patient to ask questions at any point during the interview. However, the pace of the conversation and the physician's pauses after providing information could potentially allow the patient to ask questions if they wanted to. The physician's question \"Do you understand everything I've told you?\" provides a slight opening for the patient to express confusion or ask for clarification, but it's not a direct invitation for questions. While the physician doesn't actively discourage questions, they also don't create an environment that explicitly encourages them. This aligns with a score of 2, where the climate and pace of the interview allow for questions, but there's no specific invitation to ask them."
#   }
# }

# Example 5:
# Input: 
# Physician: "Your cholesterol is too high. You need to start taking this medication immediately."
# Patient: "But I—"
# Physician: "It's essential for your health. Take one pill every morning."
# Patient: "I was wondering if—"
# Physician: "Just follow the instructions on the bottle. Any other questions will have to wait until your next appointment. We're running behind schedule."
# Patient: "Okay..."
# Physician: "Good. The nurse will schedule your follow-up on your way out."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Active discouragement of questions"
#     ],
#     "elements_absent": [
#       "Encouragement to ask questions at the end of major subsections",
#       "Opportunity for patient to bring up additional topics",
#       "Final opportunity for questions at the end of the interview",
#       "Climate and pace allowing for questions"
#     ],
#     "score": 1,
#     "justification": "The physician not only fails to provide any opportunities for questions but actively discourages them. When the patient attempts to speak or ask questions, the physician interrupts them and continues with their own agenda. The statement \"Any other questions will have to wait until your next appointment. We're running behind schedule\" clearly shows that the physician is not open to questions during this encounter. This approach creates a climate where the patient may feel their concerns and questions are not valued. The complete lack of opportunity for questions and the active discouragement of patient input clearly warrant a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
