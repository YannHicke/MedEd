ACHIEVE_A_SHARED_PLAN = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student achieves a shared plan with the patient. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Identify Key Elements:**
    - As you read the transcript, create a list noting whether each element is present or absent:
      - Discussion of the diagnosis/prognosis
      - Inviting patient to contribute
      - Negotiating a plan with the patient

  **Step 2. Scoring:**
    - As you read the transcript, use your list from Step 1 and evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student discusses the diagnosis and/or prognosis and negotiates a plan with the patient. The student invites the patient to contribute their own thoughts, ideas, suggestions, and preferences.
      - **Score 4:** The student discusses the diagnosis and/or prognosis and attempts to negotiate a plan with the patient. They invite some patient input, but may not explore the patient's thoughts, ideas, suggestions, and preferences as thoroughly as in a score of 5. The student shows a clear attempt to involve the patient in decision-making, even if not as comprehensively as in a top performance.
      - **Score 3:** The student discusses the diagnosis and/or prognosis and plan but does not allow the patient to contribute. The discussion lacks full quality. 
      - **Score 2:** The student makes limited attempts to discuss the diagnosis and/or prognosis with no opportunity for patient input. 
      - **Score 1:** The student fails to discuss the diagnosis and/or prognosis. 

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




# ACHIEVE_A_SHARED_PLAN_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student discusses the diagnosis or prognosis and negotiates a plan collaboratively with the patient.
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Clear discussion of diagnosis and/or prognosis
#       - Invitation for patient to contribute thoughts, ideas, suggestions, and preferences
#       - Negotiation of a plan with the patient
#       - Incorporation of patient's preferences into the plan
#       - Explanation of treatment options and their implications

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Discusses diagnosis/prognosis, invites patient contribution, negotiates plan collaboratively
#     - **Score 4:** Discusses diagnosis/prognosis, some patient contribution, mostly collaborative plan
#     - **Score 3:** Discusses diagnosis/prognosis and plan, limited patient contribution
#     - **Score 2:** Limited discussion of diagnosis/prognosis, minimal patient involvement in planning
#     - **Score 1:** Fails to discuss diagnosis/prognosis or involve patient in planning

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"Based on your symptoms and test results, it appears you have Type 2 diabetes. How much do you know about this condition?\"
# Patient: \"I know it affects blood sugar, but I'm not sure about the details.\"
# Physician: \"You're right, it does affect blood sugar. Let me explain a bit more about what this means for you, and then we can discuss how to manage it. Is that okay?\"
# Patient: \"Yes, please.\"
# [Physician provides explanation]
# Physician: \"Now that we've discussed what diabetes is, I'd like to hear your thoughts. What concerns do you have about this diagnosis?\"
# Patient: \"I'm worried about how it will affect my life. Will I need to change everything?\"
# Physician: \"Those are valid concerns. There are several ways we can approach managing your diabetes. Some people prefer to start with lifestyle changes, while others combine that with medication. What are your thoughts on these options?\"
# Patient: \"I'd like to try lifestyle changes first if possible.\"
# Physician: \"That's certainly an option. Let's discuss some specific changes you could make. What do you think would be most manageable for you to start with?\"
# Patient: \"Maybe I could start by changing my diet?\"
# Physician: \"That's a great place to start. Let's outline a diet plan that works for you. We'll also set some goals for physical activity. How does that sound?\"
# Patient: \"That sounds good. I appreciate being involved in the decision.\"
# Physician: \"Absolutely. It's important that this plan works for you. Let's set up a follow-up appointment to see how these changes are working and adjust our plan if needed. Do you have any other questions or concerns about our plan?\"",
#       "response": {
#         "elements_present": [
#           "Clear discussion of diagnosis and prognosis",
#           "Invitation for patient to contribute thoughts, ideas, suggestions, and preferences",
#           "Negotiation of a plan with the patient",
#           "Incorporation of patient's preferences into the plan",
#           "Explanation of treatment options and their implications"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician excels in achieving a shared plan. They clearly discuss the diagnosis of Type 2 diabetes and its implications. The physician actively invites the patient's input throughout the conversation, asking \"What concerns do you have about this diagnosis?\" and \"What are your thoughts on these options?\" They present treatment options and allow the patient to express a preference for lifestyle changes. The physician then incorporates this preference into the plan, saying \"Let's outline a diet plan that works for you.\" They also ensure ongoing collaboration by scheduling a follow-up to adjust the plan if needed. This comprehensive approach to discussing the diagnosis and collaboratively creating a plan warrants a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"Your test results indicate that you have high blood pressure, also known as hypertension. Do you know much about this condition?\"
# Patient: \"I know it can be serious, but I'm not sure of the details.\"
# Physician: \"You're right, it can be serious if left untreated. Let me explain what it means and how we can manage it.\"
# [Physician provides explanation]
# Physician: \"There are two main approaches we can take: lifestyle changes and medication. What are your thoughts on these options?\"
# Patient: \"I'd prefer to avoid medication if possible.\"
# Physician: \"Alright, we can certainly start with lifestyle changes. I recommend reducing salt intake, increasing exercise, and managing stress. How do you feel about making these changes?\"
# Patient: \"I can try, but I'm not sure how to start.\"
# Physician: \"That's understandable. Let's focus on one change at a time. Perhaps we can start with reducing salt intake. I'll give you some guidelines on how to do this. We'll monitor your progress and consider medication if these changes aren't sufficient. Does this plan work for you?\"
# Patient: \"Yes, I think I can manage that.\"
# Physician: \"Great. We'll schedule a follow-up in a month to see how you're doing.\"",
#       "response": {
#         "elements_present": [
#           "Clear discussion of diagnosis",
#           "Some invitation for patient to contribute thoughts and preferences",
#           "Partial negotiation of a plan with the patient",
#           "Incorporation of patient's preferences into the plan",
#           "Explanation of treatment options"
#         ],
#         "elements_absent": [
#           "Comprehensive exploration of patient's ideas and suggestions"
#         ],
#         "score": 4,
#         "justification": "The physician does a good job of discussing the diagnosis and treatment options for hypertension. They invite some patient input, asking \"What are your thoughts on these options?\" and incorporate the patient's preference to avoid medication. However, when the patient expresses uncertainty about how to start making changes, the physician could have explored this more thoroughly or asked for the patient's ideas. While they do adjust the plan to focus on one change at a time, there's room for more collaborative problem-solving. The approach is largely collaborative but falls slightly short of the comprehensive shared decision-making seen in a score of 5, thus warranting a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"Your test results show that you have high cholesterol. This can increase your risk of heart disease.\"
# Patient: \"Oh, I see. What does that mean for me?\"
# Physician: \"It means we need to work on lowering your cholesterol. The main treatments are dietary changes, exercise, and medication. I think we should start you on a statin medication.\"
# Patient: \"I'm not sure about taking medication. Are there other options?\"
# Physician: \"Medication is usually the most effective approach. But if you prefer, we can try diet and exercise first. Here's a diet plan you should follow. Do you have any questions about it?\"
# Patient: \"Not right now.\"
# Physician: \"Okay. Follow this plan and we'll check your cholesterol again in three months.\"",
#       "response": {
#         "elements_present": [
#           "Discussion of diagnosis and prognosis",
#           "Brief mention of treatment options",
#           "Limited response to patient's preference"
#         ],
#         "elements_absent": [
#           "Invitation for patient to contribute thoughts, ideas, and suggestions",
#           "Thorough negotiation of a plan with the patient",
#           "Comprehensive incorporation of patient's preferences into the plan"
#         ],
#         "score": 3,
#         "justification": "The physician discusses the diagnosis of high cholesterol and briefly mentions its implications. They present treatment options but initially recommend medication without exploring the patient's preferences. When the patient expresses reluctance about medication, the physician does adjust the plan, showing some flexibility. However, they don't invite the patient to contribute their own thoughts or ideas about managing their condition. The diet plan is presented without discussion or negotiation. While there is some attempt to accommodate the patient's preference, the overall approach lacks the collaborative quality required for a higher score. This limited patient involvement in the planning process aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"Your blood tests show that you have diabetes.\"
# Patient: \"Diabetes? What does that mean exactly?\"
# Physician: \"It means your blood sugar is too high. You'll need to watch your diet and probably take medication.\"
# Patient: \"I'm not sure I understand. Can you explain more?\"
# Physician: \"Diabetes is a chronic condition that affects how your body processes sugar. Here's a pamphlet about diabetes and a diet plan you should follow. Do you have any other questions?\"
# Patient: \"Well, I'm not sure—\"
# Physician: \"If you think of any later, you can ask at your next appointment. For now, just try to follow the diet plan.\"",
#       "response": {
#         "elements_present": [
#           "Brief mention of diagnosis",
#           "Limited explanation of condition and treatment"
#         ],
#         "elements_absent": [
#           "Clear discussion of prognosis",
#           "Invitation for patient to contribute thoughts, ideas, suggestions, and preferences",
#           "Negotiation of a plan with the patient",
#           "Incorporation of patient's preferences into the plan",
#           "Thorough explanation of treatment options and their implications"
#         ],
#         "score": 2,
#         "justification": "The physician provides a very limited discussion of the diagnosis, offering only a brief explanation when prompted by the patient. They mention the need for dietary changes and possibly medication but don't explain the options or their implications in detail. The physician doesn't invite the patient to contribute their thoughts or preferences, instead providing a pamphlet and diet plan without discussion. When the patient begins to express uncertainty, the physician cuts off the conversation, deferring further questions to the next appointment. This approach shows minimal patient involvement in the planning process and a lack of shared decision-making, warranting a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Your test results are back. You'll need to start on this medication right away.\"
# Patient: \"Medication? What's wrong with me?\"
# Physician: \"It's to manage your condition. Take one pill twice a day with food.\"
# Patient: \"But what condition do I have? And are there any side effects?\"
# Physician: \"The nurse will give you an information sheet about the medication. Make sure to schedule a follow-up appointment in one month.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Clear discussion of diagnosis and prognosis",
#           "Invitation for patient to contribute thoughts, ideas, suggestions, and preferences",
#           "Negotiation of a plan with the patient",
#           "Incorporation of patient's preferences into the plan",
#           "Explanation of treatment options and their implications"
#         ],
#         "score": 1,
#         "justification": "The physician completely fails to discuss the diagnosis or prognosis with the patient. When the patient directly asks what's wrong, the physician avoids answering, referring only to \"your condition\" without any explanation. There's no discussion of treatment options or their implications, and the patient's questions about side effects are deflected. The physician prescribes medication without explaining why it's needed or considering the patient's preferences. There is no attempt to involve the patient in the decision-making process or to create a shared plan. This complete lack of diagnostic discussion and patient involvement clearly warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# ACHIEVED_SHARED_PLAN2_OLD = """
#   You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student discusses the diagnosis or prognosis and negotiates a plan collaboratively with the patient. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Clear discussion of diagnosis and/or prognosis
#    - Invitation for patient to contribute thoughts, ideas, suggestions, and preferences
#    - Negotiation of a plan with the patient
#    - Incorporation of patient's preferences into the plan
#    - Explanation of treatment options and their implications

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Discusses diagnosis/prognosis, invites patient contribution, negotiates plan collaboratively
#    - Score 4: Discusses diagnosis/prognosis, some patient contribution, mostly collaborative plan
#    - Score 3: Discusses diagnosis/prognosis and plan, limited patient contribution
#    - Score 2: Limited discussion of diagnosis/prognosis, minimal patient involvement in planning
#    - Score 1: Fails to discuss diagnosis/prognosis or involve patient in planning

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
# Physician: "Based on your symptoms and test results, it appears you have Type 2 diabetes. How much do you know about this condition?"
# Patient: "I know it affects blood sugar, but I'm not sure about the details."
# Physician: "You're right, it does affect blood sugar. Let me explain a bit more about what this means for you, and then we can discuss how to manage it. Is that okay?"
# Patient: "Yes, please."
# [Physician provides explanation]
# Physician: "Now that we've discussed what diabetes is, I'd like to hear your thoughts. What concerns do you have about this diagnosis?"
# Patient: "I'm worried about how it will affect my life. Will I need to change everything?"
# Physician: "Those are valid concerns. There are several ways we can approach managing your diabetes. Some people prefer to start with lifestyle changes, while others combine that with medication. What are your thoughts on these options?"
# Patient: "I'd like to try lifestyle changes first if possible."
# Physician: "That's certainly an option. Let's discuss some specific changes you could make. What do you think would be most manageable for you to start with?"
# Patient: "Maybe I could start by changing my diet?"
# Physician: "That's a great place to start. Let's outline a diet plan that works for you. We'll also set some goals for physical activity. How does that sound?"
# Patient: "That sounds good. I appreciate being involved in the decision."
# Physician: "Absolutely. It's important that this plan works for you. Let's set up a follow-up appointment to see how these changes are working and adjust our plan if needed. Do you have any other questions or concerns about our plan?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Clear discussion of diagnosis and prognosis",
#       "Invitation for patient to contribute thoughts, ideas, suggestions, and preferences",
#       "Negotiation of a plan with the patient",
#       "Incorporation of patient's preferences into the plan",
#       "Explanation of treatment options and their implications"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician excels in achieving a shared plan. They clearly discuss the diagnosis of Type 2 diabetes and its implications. The physician actively invites the patient's input throughout the conversation, asking \"What concerns do you have about this diagnosis?\" and \"What are your thoughts on these options?\" They present treatment options and allow the patient to express a preference for lifestyle changes. The physician then incorporates this preference into the plan, saying \"Let's outline a diet plan that works for you.\" They also ensure ongoing collaboration by scheduling a follow-up to adjust the plan if needed. This comprehensive approach to discussing the diagnosis and collaboratively creating a plan warrants a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "Your test results indicate that you have high blood pressure, also known as hypertension. Do you know much about this condition?"
# Patient: "I know it can be serious, but I'm not sure of the details."
# Physician: "You're right, it can be serious if left untreated. Let me explain what it means and how we can manage it."
# [Physician provides explanation]
# Physician: "There are two main approaches we can take: lifestyle changes and medication. What are your thoughts on these options?"
# Patient: "I'd prefer to avoid medication if possible."
# Physician: "Alright, we can certainly start with lifestyle changes. I recommend reducing salt intake, increasing exercise, and managing stress. How do you feel about making these changes?"
# Patient: "I can try, but I'm not sure how to start."
# Physician: "That's understandable. Let's focus on one change at a time. Perhaps we can start with reducing salt intake. I'll give you some guidelines on how to do this. We'll monitor your progress and consider medication if these changes aren't sufficient. Does this plan work for you?"
# Patient: "Yes, I think I can manage that."
# Physician: "Great. We'll schedule a follow-up in a month to see how you're doing."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Clear discussion of diagnosis",
#       "Some invitation for patient to contribute thoughts and preferences",
#       "Partial negotiation of a plan with the patient",
#       "Incorporation of patient's preferences into the plan",
#       "Explanation of treatment options"
#     ],
#     "elements_absent": [
#       "Comprehensive exploration of patient's ideas and suggestions"
#     ],
#     "score": 4,
#     "justification": "The physician does a good job of discussing the diagnosis and treatment options for hypertension. They invite some patient input, asking \"What are your thoughts on these options?\" and incorporate the patient's preference to avoid medication. However, when the patient expresses uncertainty about how to start making changes, the physician could have explored this more thoroughly or asked for the patient's ideas. While they do adjust the plan to focus on one change at a time, there's room for more collaborative problem-solving. The approach is largely collaborative but falls slightly short of the comprehensive shared decision-making seen in a score of 5, thus warranting a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "Your test results show that you have high cholesterol. This can increase your risk of heart disease."
# Patient: "Oh, I see. What does that mean for me?"
# Physician: "It means we need to work on lowering your cholesterol. The main treatments are dietary changes, exercise, and medication. I think we should start you on a statin medication."
# Patient: "I'm not sure about taking medication. Are there other options?"
# Physician: "Medication is usually the most effective approach. But if you prefer, we can try diet and exercise first. Here's a diet plan you should follow. Do you have any questions about it?"
# Patient: "Not right now."
# Physician: "Okay. Follow this plan and we'll check your cholesterol again in three months."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Discussion of diagnosis and prognosis",
#       "Brief mention of treatment options",
#       "Limited response to patient's preference"
#     ],
#     "elements_absent": [
#       "Invitation for patient to contribute thoughts, ideas, and suggestions",
#       "Thorough negotiation of a plan with the patient",
#       "Comprehensive incorporation of patient's preferences into the plan"
#     ],
#     "score": 3,
#     "justification": "The physician discusses the diagnosis of high cholesterol and briefly mentions its implications. They present treatment options but initially recommend medication without exploring the patient's preferences. When the patient expresses reluctance about medication, the physician does adjust the plan, showing some flexibility. However, they don't invite the patient to contribute their own thoughts or ideas about managing their condition. The diet plan is presented without discussion or negotiation. While there is some attempt to accommodate the patient's preference, the overall approach lacks the collaborative quality required for a higher score. This limited patient involvement in the planning process aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "Your blood tests show that you have diabetes."
# Patient: "Diabetes? What does that mean exactly?"
# Physician: "It means your blood sugar is too high. You'll need to watch your diet and probably take medication."
# Patient: "I'm not sure I understand. Can you explain more?"
# Physician: "Diabetes is a chronic condition that affects how your body processes sugar. Here's a pamphlet about diabetes and a diet plan you should follow. Do you have any other questions?"
# Patient: "Well, I'm not sure—"
# Physician: "If you think of any later, you can ask at your next appointment. For now, just try to follow the diet plan."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Brief mention of diagnosis",
#       "Limited explanation of condition and treatment"
#     ],
#     "elements_absent": [
#       "Clear discussion of prognosis",
#       "Invitation for patient to contribute thoughts, ideas, suggestions, and preferences",
#       "Negotiation of a plan with the patient",
#       "Incorporation of patient's preferences into the plan",
#       "Thorough explanation of treatment options and their implications"
#     ],
#     "score": 2,
#     "justification": "The physician provides a very limited discussion of the diagnosis, offering only a brief explanation when prompted by the patient. They mention the need for dietary changes and possibly medication but don't explain the options or their implications in detail. The physician doesn't invite the patient to contribute their thoughts or preferences, instead providing a pamphlet and diet plan without discussion. When the patient begins to express uncertainty, the physician cuts off the conversation, deferring further questions to the next appointment. This approach shows minimal patient involvement in the planning process and a lack of shared decision-making, warranting a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "Your test results are back. You'll need to start on this medication right away."
# Patient: "Medication? What's wrong with me?"
# Physician: "It's to manage your condition. Take one pill twice a day with food."
# Patient: "But what condition do I have? And are there any side effects?"
# Physician: "The nurse will give you an information sheet about the medication. Make sure to schedule a follow-up appointment in one month."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Clear discussion of diagnosis and prognosis",
#       "Invitation for patient to contribute thoughts, ideas, suggestions, and preferences",
#       "Negotiation of a plan with the patient",
#       "Incorporation of patient's preferences into the plan",
#       "Explanation of treatment options and their implications"
#     ],
#     "score": 1,
#     "justification": "The physician completely fails to discuss the diagnosis or prognosis with the patient. When the patient directly asks what's wrong, the physician avoids answering, referring only to \"your condition\" without any explanation. There's no discussion of treatment options or their implications, and the patient's questions about side effects are deflected. The physician prescribes medication without explaining why it's needed or considering the patient's preferences. There is no attempt to involve the patient in the decision-making process or to create a shared plan. This complete lack of diagnostic discussion and patient involvement clearly warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
