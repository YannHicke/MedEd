ORGANIZATION = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student organizes the interview. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** Questions in the body of the interview follow a logical order to the patient. Time is used effectively so that tasks are completed in time allowed.
      - **Score 4:** The student's questions mostly follow a logical order, with only occasional minor deviations. Time management is mostly effective, though some sections of the interview may be slightly rushed or extended. The overall flow is good, but not as seamless as a score of 5.
      - **Score 3:** The student seems to follow a series of topics or agenda items; however, there are a few minor disjointed questions.
      - **Score 2:** The student's questioning shows some attempt at organization, but there are frequent jumps between topics that may confuse the patient. Time management is inconsistent, with some sections of the interview being noticeably rushed or overly prolonged. While not completely disjointed, the lack of smooth transitions and logical flow is apparent.
      - **Score 1:** The student asks questions that seem disjointed and unorganized. 

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


# ORGANIZATION_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating the organization of the interview, considering if the questions follow a logical order and if the effective use of time ensures that tasks are completed within the allotted time.
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Logical order of questions
#       - Questions building on previous information
#       - Effective use of time
#       - Completion of necessary tasks
#       - Smooth flow of conversation

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Logical order of questions, effective use of time, tasks completed
#     - **Score 3:** Generally follows a series of topics, but with a few minor disjointed questions
#     - **Score 1:** Disjointed and unorganized questions, affecting interview flow

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"What's the main reason for your visit today, Mrs. Thompson?\"
# Patient: \"I've been having this persistent cough for the past two weeks.\"
# Physician: \"I see. Can you tell me more about this cough? When did it start exactly?\"
# Patient: \"It began about two weeks ago, just after I returned from a camping trip.\"
# Physician: \"Thank you for that information. Is the cough worse at any particular time of day?\"
# Patient: \"Yes, it seems to be worse at night and early in the morning.\"
# Physician: \"I see. And have you noticed any other symptoms along with the cough, such as fever or shortness of breath?\"
# Patient: \"Now that you mention it, I have been feeling a bit short of breath, especially when climbing stairs.\"
# Physician: \"Thank you for sharing that. Let's talk about your camping trip for a moment. Were you exposed to any unusual environments or substances during that time?\"
# Patient: \"We did spend a lot of time around a campfire. Could that be related?\"
# Physician: \"It's possible. Now, have you tried any over-the-counter medications or home remedies for your cough?\"
# Patient: \"I've been taking some honey and lemon tea, but it hasn't helped much.\"
# Physician: \"Alright. Based on what you've told me, I'd like to listen to your lungs and perhaps order a few tests. Before we do that, do you have any questions about what we've discussed so far?\"",
#       "response": {
#         "elements_present": [
#           "Logical order of questions",
#           "Questions building on previous information",
#           "Effective use of time",
#           "Completion of necessary tasks",
#           "Smooth flow of conversation"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician demonstrates excellent organization in this interview. They begin with an open-ended question to identify the main concern: \"What's the main reason for your visit today, Mrs. Thompson?\" Each subsequent question logically builds on the information provided by the patient. For example, after learning about the camping trip, the physician asks, \"Were you exposed to any unusual environments or substances during that time?\" The physician effectively uses the time to gather comprehensive information about the cough, its onset, associated symptoms, and potential causes. The conversation flows smoothly, with the physician summarizing and transitioning effectively: \"Based on what you've told me, I'd like to listen to your lungs and perhaps order a few tests.\" This organized approach ensures that all necessary information is gathered efficiently, justifying a score of 5."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"Good morning, Mr. Johnson. What brings you in today?\"
# Patient: \"I've been having some stomach pain lately.\"
# Physician: \"I see. When did this pain start?\"
# Patient: \"About a week ago.\"
# Physician: \"Okay. Have you had any changes in your diet recently?\"
# Patient: \"Not really, I've been eating the same as usual.\"
# Physician: \"Alright. Do you have any allergies?\"
# Patient: \"No, not that I know of.\"
# Physician: \"I see. Going back to your stomach pain, can you describe where exactly it hurts?\"
# Patient: \"It's mostly in the upper part of my stomach.\"
# Physician: \"And how would you rate the pain on a scale of 1 to 10?\"
# Patient: \"I'd say it's about a 6 or 7.\"
# Physician: \"Okay. Have you been experiencing any fatigue lately?\"
# Patient: \"Now that you mention it, yes, I have been feeling more tired than usual.\"
# Physician: \"I see. Let's go back to the stomach pain. Have you noticed if it gets worse after eating?\"",
#       "response": {
#         "elements_present": [
#           "Some logical order of questions",
#           "Partial completion of necessary tasks",
#           "Some questions building on previous information"
#         ],
#         "elements_absent": [
#           "Consistent logical flow",
#           "Optimal use of time"
#         ],
#         "score": 3,
#         "justification": "The physician demonstrates a moderate level of organization in this interview. They start with an appropriate open-ended question: \"What brings you in today?\" and follow up with relevant questions about the onset and location of the pain. However, there are a few instances where the questioning becomes disjointed. For example, asking about allergies seems out of place in the flow of the conversation about stomach pain. The physician does return to the main complaint, showing some attempt at organization: \"Going back to your stomach pain, can you describe where exactly it hurts?\" However, the question about fatigue seems somewhat unconnected to the main complaint. The physician tries to bring the focus back to the stomach pain at the end, but the overall flow is not as smooth as it could be. This mix of logical progression with occasional disjointed questions aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"Good morning. What's your name?\"
# Patient: \"I'm Sarah Jones.\"
# Physician: \"Okay, Sarah. What brings you in today?\"
# Patient: \"I've been having some chest pain lately.\"
# Physician: \"I see. Do you smoke?\"
# Patient: \"No, I don't.\"
# Physician: \"Alright. Have you had any surgeries in the past?\"
# Patient: \"Yes, I had my appendix removed when I was a teenager.\"
# Physician: \"Okay. Going back to the chest pain, when did it start?\"
# Patient: \"It started about a week ago.\"
# Physician: \"And is it constant or does it come and go?\"
# Patient: \"It comes and goes.\"
# Physician: \"I see. Do you have any family history of heart disease?\"
# Patient: \"I'm not sure. But about the pain—\"
# Physician: \"We'll get back to that. How's your sleep been lately?\"
# Patient: \"It's been okay, I guess. But I'm really worried about this chest pain.\"
# Physician: \"Right, let's talk about that. Where exactly is the pain located?\"",
#       "response": {
#         "elements_present": [
#           "Some attempt at logical order",
#           "Partial completion of necessary tasks"
#         ],
#         "elements_absent": [
#           "Consistent logical flow",
#           "Effective use of time",
#           "Questions consistently building on previous information"
#         ],
#         "score": 2,
#         "justification": "The physician's interview shows some organization but lacks consistency and effective time management. They begin appropriately by asking the patient's name and reason for the visit. However, the flow becomes disjointed when they ask about smoking and past surgeries without clear relevance to the chest pain. The physician does return to the main complaint (\"Going back to the chest pain, when did it start?\"), showing some attempt at organization. But they again diverge with questions about family history and sleep, interrupting the patient's attempt to discuss their concerns (\"But about the pain—\"). While they eventually return to the chest pain, the lack of a consistent focus and the interruption of the patient's narrative affects the interview's flow. This inconsistent organization and suboptimal use of time justify a score of 2."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# ORGANIZATION2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the organization of the interview, considering if the questions follow a logical order and if the effective use of time ensures that tasks are completed within the allotted time. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Logical order of questions
#    - Questions building on previous information
#    - Effective use of time
#    - Completion of necessary tasks
#    - Smooth flow of conversation

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Logical order of questions, effective use of time, tasks completed
#    - Score 3: Generally follows a series of topics, but with a few minor disjointed questions
#    - Score 1: Disjointed and unorganized questions, affecting interview flow

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
# Physician: "What's the main reason for your visit today, Mrs. Thompson?"
# Patient: "I've been having this persistent cough for the past two weeks."
# Physician: "I see. Can you tell me more about this cough? When did it start exactly?"
# Patient: "It began about two weeks ago, just after I returned from a camping trip."
# Physician: "Thank you for that information. Is the cough worse at any particular time of day?"
# Patient: "Yes, it seems to be worse at night and early in the morning."
# Physician: "I see. And have you noticed any other symptoms along with the cough, such as fever or shortness of breath?"
# Patient: "Now that you mention it, I have been feeling a bit short of breath, especially when climbing stairs."
# Physician: "Thank you for sharing that. Let's talk about your camping trip for a moment. Were you exposed to any unusual environments or substances during that time?"
# Patient: "We did spend a lot of time around a campfire. Could that be related?"
# Physician: "It's possible. Now, have you tried any over-the-counter medications or home remedies for your cough?"
# Patient: "I've been taking some honey and lemon tea, but it hasn't helped much."
# Physician: "Alright. Based on what you've told me, I'd like to listen to your lungs and perhaps order a few tests. Before we do that, do you have any questions about what we've discussed so far?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Logical order of questions",
#       "Questions building on previous information",
#       "Effective use of time",
#       "Completion of necessary tasks",
#       "Smooth flow of conversation"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician demonstrates excellent organization in this interview. They begin with an open-ended question to identify the main concern: \"What's the main reason for your visit today, Mrs. Thompson?\" Each subsequent question logically builds on the information provided by the patient. For example, after learning about the camping trip, the physician asks, \"Were you exposed to any unusual environments or substances during that time?\" The physician effectively uses the time to gather comprehensive information about the cough, its onset, associated symptoms, and potential causes. The conversation flows smoothly, with the physician summarizing and transitioning effectively: \"Based on what you've told me, I'd like to listen to your lungs and perhaps order a few tests.\" This organized approach ensures that all necessary information is gathered efficiently, justifying a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "Good morning, Mr. Johnson. What brings you in today?"
# Patient: "I've been having some stomach pain lately."
# Physician: "I see. When did this pain start?"
# Patient: "About a week ago."
# Physician: "Okay. Have you had any changes in your diet recently?"
# Patient: "Not really, I've been eating the same as usual."
# Physician: "Alright. Do you have any allergies?"
# Patient: "No, not that I know of."
# Physician: "I see. Going back to your stomach pain, can you describe where exactly it hurts?"
# Patient: "It's mostly in the upper part of my stomach."
# Physician: "And how would you rate the pain on a scale of 1 to 10?"
# Patient: "I'd say it's about a 6 or 7."
# Physician: "Okay. Have you been experiencing any fatigue lately?"
# Patient: "Now that you mention it, yes, I have been feeling more tired than usual."
# Physician: "I see. Let's go back to the stomach pain. Have you noticed if it gets worse after eating?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Some logical order of questions",
#       "Partial completion of necessary tasks",
#       "Some questions building on previous information"
#     ],
#     "elements_absent": [
#       "Consistent logical flow",
#       "Optimal use of time"
#     ],
#     "score": 3,
#     "justification": "The physician demonstrates a moderate level of organization in this interview. They start with an appropriate open-ended question: \"What brings you in today?\" and follow up with relevant questions about the onset and location of the pain. However, there are a few instances where the questioning becomes disjointed. For example, asking about allergies seems out of place in the flow of the conversation about stomach pain. The physician does return to the main complaint, showing some attempt at organization: \"Going back to your stomach pain, can you describe where exactly it hurts?\" However, the question about fatigue seems somewhat unconnected to the main complaint. The physician tries to bring the focus back to the stomach pain at the end, but the overall flow is not as smooth as it could be. This mix of logical progression with occasional disjointed questions aligns with a score of 3."
#   }
# }

# Example 3:
# Input: 
# Physician: "Good morning. What's your name?"
# Patient: "I'm Sarah Jones."
# Physician: "Okay, Sarah. What brings you in today?"
# Patient: "I've been having some chest pain lately."
# Physician: "I see. Do you smoke?"
# Patient: "No, I don't."
# Physician: "Alright. Have you had any surgeries in the past?"
# Patient: "Yes, I had my appendix removed when I was a teenager."
# Physician: "Okay. Going back to the chest pain, when did it start?"
# Patient: "It started about a week ago."
# Physician: "And is it constant or does it come and go?"
# Patient: "It comes and goes."
# Physician: "I see. Do you have any family history of heart disease?"
# Patient: "I'm not sure. But about the pain—"
# Physician: "We'll get back to that. How's your sleep been lately?"
# Patient: "It's been okay, I guess. But I'm really worried about this chest pain."
# Physician: "Right, let's talk about that. Where exactly is the pain located?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Some attempt at logical order",
#       "Partial completion of necessary tasks"
#     ],
#     "elements_absent": [
#       "Consistent logical flow",
#       "Effective use of time",
#       "Questions consistently building on previous information"
#     ],
#     "score": 2,
#     "justification": "The physician's interview shows some organization but lacks consistency and effective time management. They begin appropriately by asking the patient's name and reason for the visit. However, the flow becomes disjointed when they ask about smoking and past surgeries without clear relevance to the chest pain. The physician does return to the main complaint (\"Going back to the chest pain, when did it start?\"), showing some attempt at organization. But they again diverge with questions about family history and sleep, interrupting the patient's attempt to discuss their concerns (\"But about the pain—\"). While they eventually return to the chest pain, the lack of a consistent focus and the interruption of the patient's narrative affects the interview's flow. This inconsistent organization and suboptimal use of time justify a score of 2."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
