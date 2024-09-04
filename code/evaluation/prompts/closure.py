CLOSURE = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student closes the interview. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

**Step 1. Scoring:**
   - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
     - **Score 5:** At the end of the interview, the student clearly specifies the future plans: (1) What the student will do (leave and consult, make referrals), (2) What the patient will do (wait, make diet changes, go to Physical Therapy), and (3) When (the time of the next communication or appointment). 
     - **Score 4:** The student specifies most aspects of the future plans at the end of the interview, but may not cover all three areas (student actions, patient actions, and timing) as comprehensively as in a score of 5. The plans are mostly clear, but some details might be vague or omitted. The student shows a clear attempt to provide closure and future direction, even if not as thoroughly as in a top performance.
     - **Score 3:** At the end of the interview, the student partially details the plans for the future.
     - **Score 2:** The student makes limited attempts to specify future plans at the end of the interview. The information provided is vague or incomplete, leaving the patient with an unclear sense of what to expect. The student shows some awareness of the need for closure but struggles to provide a comprehensive plan or clear next steps.
     - **Score 1:** At the end of the interview, the student fails to specify the plans for the future and the patient leaves the interview without a sense of what to expect. There is no closure whatsoever. 

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


# CLOSURE_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how effectively the physician concludes the interview, focusing on the clarity and completeness of future plans.
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Specification of what the physician will do
#       - Specification of what the patient will do
#       - Clear timeline for next communication or appointment
#       - Summary of key points discussed
#       - Opportunity for final questions or concerns

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Clear and complete specification of future plans for both physician and patient, with timeline
#     - **Score 4:** Good specification of future plans, may lack some detail or clarity
#     - **Score 3:** Partial detailing of future plans, some elements missing or unclear
#     - **Score 2:** Minimal closure, vague plans with little detail
#     - **Score 1:** No specification of future plans, lack of any meaningful closure

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"Alright, let's summarize our plan moving forward. I will consult with Dr. Johnson, our cardiologist, about your case this week and arrange for you to have an echocardiogram. You should expect a call from our office by Friday to schedule that.\"
# Patient: \"Okay, that sounds good.\"
# Physician: \"As for what you need to do, please start the new blood pressure medication we discussed - one pill each morning with breakfast. Also, begin the low-sodium diet we talked about, and aim for a 30-minute walk at least five days a week.\"
# Patient: \"Got it. Medication in the morning, watch my salt, and regular walks.\"
# Physician: \"Exactly. I'd like to see you back here in three weeks to check your progress. Sarah at the front desk will schedule that appointment for you on your way out. Do you have any questions about what we've discussed or the plan going forward?\"
# Patient: \"No, I think I understand everything.\"
# Physician: \"Excellent. If you think of any questions later or have any concerns before our next appointment, please don't hesitate to call the office. We're here to support you.\"",
#       "response": {
#         "elements_present": [
#           "Specification of what the physician will do",
#           "Specification of what the patient will do",
#           "Clear timeline for next communication or appointment",
#           "Summary of key points discussed",
#           "Opportunity for final questions or concerns"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician provides an excellent closure to the interview. They clearly specify what they will do (\"I will consult with Dr. Johnson, our cardiologist, about your case this week and arrange for you to have an echocardiogram\") and what the patient should do (\"start the new blood pressure medication... begin the low-sodium diet... aim for a 30-minute walk at least five days a week\"). The timeline for next communication is clear (\"expect a call from our office by Friday\") and a follow-up appointment is scheduled (\"I'd like to see you back here in three weeks\"). The physician summarizes key points and provides an opportunity for final questions. This comprehensive closure ensures the patient leaves with a clear understanding of the next steps, warranting a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"Okay, so here's what we're going to do. I'll refer you to a specialist for further evaluation of your symptoms. In the meantime, I want you to start taking this medication daily.\"
# Patient: \"Alright, when will I see the specialist?\"
# Physician: \"The referral office will call you within the next week to schedule that appointment. As for the medication, take one pill every morning. Can you remind me what lifestyle changes we discussed?\"
# Patient: \"Um, I think it was about diet and exercise?\"
# Physician: \"That's right. Try to reduce your sugar intake and aim for at least 20 minutes of exercise three times a week. Do you have any other questions about what we've discussed today?\"
# Patient: \"No, I think I'm good.\"
# Physician: \"Great. If you have any concerns before your specialist appointment, don't hesitate to call us.\"",
#       "response": {
#         "elements_present": [
#           "Specification of what the physician will do",
#           "Specification of what the patient will do",
#           "Some timeline for next communication",
#           "Partial summary of key points",
#           "Opportunity for final questions"
#         ],
#         "elements_absent": [
#           "Clear timeline for follow-up with primary physician"
#         ],
#         "score": 4,
#         "justification": "The physician provides a good closure to the interview, covering most key elements. They specify their action (referral to a specialist) and the patient's actions (taking medication, dietary changes, and exercise). There's a timeline for the specialist contact (\"within the next week\") and an opportunity for final questions. However, the closure lacks some detail and clarity. The lifestyle changes are not as clearly stated as they could be, and there's no specific follow-up planned with this physician. While the closure is generally effective, these minor shortcomings prevent it from reaching the comprehensive level of a score of 5, thus warranting a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"So, we've discussed your condition and treatment options. Do you have any questions?\"
# Patient: \"Not really, but what should I do next?\"
# Physician: \"You should start the new medication we talked about. Take it once daily.\"
# Patient: \"Okay, and when do I come back?\"
# Physician: \"We'll need to see you for a follow-up. Stop by the front desk and they'll schedule your next appointment.\"
# Patient: \"Alright, thanks.\"
# Physician: \"Take care, and call if you have any problems.\"",
#       "response": {
#         "elements_present": [
#           "Some specification of what the patient will do",
#           "Mention of follow-up appointment",
#           "Opportunity for questions"
#         ],
#         "elements_absent": [
#           "Specification of what the physician will do",
#           "Clear timeline for next communication or appointment",
#           "Summary of key points discussed"
#         ],
#         "score": 3,
#         "justification": "The physician provides a partial closure to the interview. They mention the new medication and instruct the patient to take it daily, which is good. They also indicate that a follow-up appointment is needed. However, the closure lacks detail in several areas. There's no clear timeline for the follow-up, no summary of key points discussed, and no specification of what the physician will do next. The patient has to prompt for information about next steps. While there is some closure, the lack of detail and completeness aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"Well, that covers everything for today.\"
# Patient: \"So, what happens now?\"
# Physician: \"Just continue with the treatment we discussed. If you have any issues, give us a call.\"
# Patient: \"Okay, but when should I come back?\"
# Physician: \"We'll let you know if we need to see you again. Any other questions?\"
# Patient: \"No, I guess not.\"
# Physician: \"Alright then, take care.\"",
#       "response": {
#         "elements_present": [
#           "Minimal opportunity for questions"
#         ],
#         "elements_absent": [
#           "Specification of what the physician will do",
#           "Clear specification of what the patient will do",
#           "Timeline for next communication or appointment",
#           "Summary of key points discussed"
#         ],
#         "score": 2,
#         "justification": "The physician provides minimal closure to the interview. They don't specify any clear plans for the future, either for themselves or for the patient. When the patient asks about next steps, the physician's response is vague (\"Just continue with the treatment we discussed\"). There's no summary of key points, no clear timeline for follow-up, and no specific instructions for the patient. The physician does provide an opportunity for questions, but this is the only element of good closure present. This lack of clear plans and details leaves the patient without a sense of what to expect, aligning with a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Okay, we're done here.\"
# Patient: \"Wait, what should I do next?\"
# Physician: \"Just follow the instructions I gave you earlier.\"
# Patient: \"But I'm not sure I remember everything...\"
# Physician: \"You'll be fine. I have another patient waiting. Goodbye.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Specification of what the physician will do",
#           "Specification of what the patient will do",
#           "Timeline for next communication or appointment",
#           "Summary of key points discussed",
#           "Opportunity for final questions or concerns"
#         ],
#         "score": 1,
#         "justification": "The physician fails to provide any meaningful closure to the interview. They don't specify any future plans, either for themselves or for the patient. When the patient expresses uncertainty and asks for clarification, the physician dismisses their concerns without providing any additional information. There's no summary of key points, no timeline for follow-up, and no opportunity for questions. The abrupt ending (\"I have another patient waiting. Goodbye.\") leaves the patient without any clear sense of what to expect or do next. This complete lack of closure and failure to address the patient's expressed confusion clearly warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# CLOSURE2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how effectively the physician concludes the interview, focusing on the clarity and completeness of future plans. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Specification of what the physician will do
#    - Specification of what the patient will do
#    - Clear timeline for next communication or appointment
#    - Summary of key points discussed
#    - Opportunity for final questions or concerns

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Clear and complete specification of future plans for both physician and patient, with timeline
#    - Score 4: Good specification of future plans, may lack some detail or clarity
#    - Score 3: Partial detailing of future plans, some elements missing or unclear
#    - Score 2: Minimal closure, vague plans with little detail
#    - Score 1: No specification of future plans, lack of any meaningful closure

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
# Physician: "Alright, let's summarize our plan moving forward. I will consult with Dr. Johnson, our cardiologist, about your case this week and arrange for you to have an echocardiogram. You should expect a call from our office by Friday to schedule that."
# Patient: "Okay, that sounds good."
# Physician: "As for what you need to do, please start the new blood pressure medication we discussed - one pill each morning with breakfast. Also, begin the low-sodium diet we talked about, and aim for a 30-minute walk at least five days a week."
# Patient: "Got it. Medication in the morning, watch my salt, and regular walks."
# Physician: "Exactly. I'd like to see you back here in three weeks to check your progress. Sarah at the front desk will schedule that appointment for you on your way out. Do you have any questions about what we've discussed or the plan going forward?"
# Patient: "No, I think I understand everything."
# Physician: "Excellent. If you think of any questions later or have any concerns before our next appointment, please don't hesitate to call the office. We're here to support you."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Specification of what the physician will do",
#       "Specification of what the patient will do",
#       "Clear timeline for next communication or appointment",
#       "Summary of key points discussed",
#       "Opportunity for final questions or concerns"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician provides an excellent closure to the interview. They clearly specify what they will do (\"I will consult with Dr. Johnson, our cardiologist, about your case this week and arrange for you to have an echocardiogram\") and what the patient should do (\"start the new blood pressure medication... begin the low-sodium diet... aim for a 30-minute walk at least five days a week\"). The timeline for next communication is clear (\"expect a call from our office by Friday\") and a follow-up appointment is scheduled (\"I'd like to see you back here in three weeks\"). The physician summarizes key points and provides an opportunity for final questions. This comprehensive closure ensures the patient leaves with a clear understanding of the next steps, warranting a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "Okay, so here's what we're going to do. I'll refer you to a specialist for further evaluation of your symptoms. In the meantime, I want you to start taking this medication daily."
# Patient: "Alright, when will I see the specialist?"
# Physician: "The referral office will call you within the next week to schedule that appointment. As for the medication, take one pill every morning. Can you remind me what lifestyle changes we discussed?"
# Patient: "Um, I think it was about diet and exercise?"
# Physician: "That's right. Try to reduce your sugar intake and aim for at least 20 minutes of exercise three times a week. Do you have any other questions about what we've discussed today?"
# Patient: "No, I think I'm good."
# Physician: "Great. If you have any concerns before your specialist appointment, don't hesitate to call us."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Specification of what the physician will do",
#       "Specification of what the patient will do",
#       "Some timeline for next communication",
#       "Partial summary of key points",
#       "Opportunity for final questions"
#     ],
#     "elements_absent": [
#       "Clear timeline for follow-up with primary physician"
#     ],
#     "score": 4,
#     "justification": "The physician provides a good closure to the interview, covering most key elements. They specify their action (referral to a specialist) and the patient's actions (taking medication, dietary changes, and exercise). There's a timeline for the specialist contact (\"within the next week\") and an opportunity for final questions. However, the closure lacks some detail and clarity. The lifestyle changes are not as clearly stated as they could be, and there's no specific follow-up planned with this physician. While the closure is generally effective, these minor shortcomings prevent it from reaching the comprehensive level of a score of 5, thus warranting a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "So, we've discussed your condition and treatment options. Do you have any questions?"
# Patient: "Not really, but what should I do next?"
# Physician: "You should start the new medication we talked about. Take it once daily."
# Patient: "Okay, and when do I come back?"
# Physician: "We'll need to see you for a follow-up. Stop by the front desk and they'll schedule your next appointment."
# Patient: "Alright, thanks."
# Physician: "Take care, and call if you have any problems."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Some specification of what the patient will do",
#       "Mention of follow-up appointment",
#       "Opportunity for questions"
#     ],
#     "elements_absent": [
#       "Specification of what the physician will do",
#       "Clear timeline for next communication or appointment",
#       "Summary of key points discussed"
#     ],
#     "score": 3,
#     "justification": "The physician provides a partial closure to the interview. They mention the new medication and instruct the patient to take it daily, which is good. They also indicate that a follow-up appointment is needed. However, the closure lacks detail in several areas. There's no clear timeline for the follow-up, no summary of key points discussed, and no specification of what the physician will do next. The patient has to prompt for information about next steps. While there is some closure, the lack of detail and completeness aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "Well, that covers everything for today."
# Patient: "So, what happens now?"
# Physician: "Just continue with the treatment we discussed. If you have any issues, give us a call."
# Patient: "Okay, but when should I come back?"
# Physician: "We'll let you know if we need to see you again. Any other questions?"
# Patient: "No, I guess not."
# Physician: "Alright then, take care."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Minimal opportunity for questions"
#     ],
#     "elements_absent": [
#       "Specification of what the physician will do",
#       "Clear specification of what the patient will do",
#       "Timeline for next communication or appointment",
#       "Summary of key points discussed"
#     ],
#     "score": 2,
#     "justification": "The physician provides minimal closure to the interview. They don't specify any clear plans for the future, either for themselves or for the patient. When the patient asks about next steps, the physician's response is vague (\"Just continue with the treatment we discussed\"). There's no summary of key points, no clear timeline for follow-up, and no specific instructions for the patient. The physician does provide an opportunity for questions, but this is the only element of good closure present. This lack of clear plans and details leaves the patient without a sense of what to expect, aligning with a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "Okay, we're done here."
# Patient: "Wait, what should I do next?"
# Physician: "Just follow the instructions I gave you earlier."
# Patient: "But I'm not sure I remember everything..."
# Physician: "You'll be fine. I have another patient waiting. Goodbye."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Specification of what the physician will do",
#       "Specification of what the patient will do",
#       "Timeline for next communication or appointment",
#       "Summary of key points discussed",
#       "Opportunity for final questions or concerns"
#     ],
#     "score": 1,
#     "justification": "The physician fails to provide any meaningful closure to the interview. They don't specify any future plans, either for themselves or for the patient. When the patient expresses uncertainty and asks for clarification, the physician dismisses their concerns without providing any additional information. There's no summary of key points, no timeline for follow-up, and no opportunity for questions. The abrupt ending (\"I have another patient waiting. Goodbye.\") leaves the patient without any clear sense of what to expect or do next. This complete lack of closure and failure to address the patient's expressed confusion clearly warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """