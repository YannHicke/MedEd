QUESTIONING_SKILLS_TYPES_OF_QUESTIONS = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the student’s questioning skills, specifically looking at the types of questions they ask. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Understanding the Task:**
    - Read the following note:
      **Note:** Learners should follow a line of inquiry that progresses from open-ended to specific followed with specific questions. 
      - Open-ended questions: Allow the learner to obtain a large amount of information about a particular area. It allows the patient to tell their story. This should be used to begin a line of inquiry then follow up with more focused and direct questions. Example: "What brings you here today?" or "Tell me about your general health.”
      - Direct or specific questions: Gather specific pertinent information. Example: “How old were you when you had your tonsils removed?" or "When did your pain begin?" or "How long have you had the pain?"
      Other types of direct questions elicit a "yes" or "no" answer from the patient, or a response to a choice that the learner has provided.   
      Example various types of questions: Learner (L): "Tell me about your problem." (Open-ended) Patient (P): "For two weeks, I've had a constant pain in my stomach, right here (points), above my navel." L: "Tell me about the pain." (Open-ended) P: "It's a burning sensation." L: "Is it a deep pain?" (Direct) P: "Yes, a deep one." L: "Does the pain move around?" (Direct) P: "No."  L: "What makes the pain feel worse?" (Open-ended)
      Learners should avoid using direct or (particularly) forced choice questions in beginning a line of inquiry because it restricts the possible flow of information and makes obtaining the necessary information a tedious task. Example: if NOT beginning with an open-ended question such as: "Tell me about the pain.” they must ask several direct questions: L: "Is the pain an ache?" P: "No."  L: "Is it a stabbing pain?" P: "No."  L: "Is it a dull pain?" P: "No."
      Learners should avoid these poor question types: 
      - Leading Questions supply a particular answer for the patient, desired answer is implied by how the question is phrased. This should also be avoided because some patients may agree with the leading questions rather than contradicting the learner. Example: "No headaches? Right?"
      - "Why" Questions: put the patient on the defensive and should be avoided. Example: "Why didn’t you come in sooner, you've had the problem for six weeks?"
      - Multiple Questions: a series of short questions asked in succession without allowing the patient to answer each individually. The patient may be confused about which question to answer. Example: “Does the pain feel like it’s as sharp after dinner or is it different than before dinner? Multiple questions may also be one question listing many options. Example: "Has anyone in your family ever had cancer, diabetes, heart disease, or high blood pressure?"  

  **Step 2. Scoring:**
    - As you read the transcript, and using your understanding from Step 1, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student begins information gathering with an open-ended question. This is followed up by more specific or direct questions. Each major line of questioning is begun with an open-ended question. No poor question types are used.
      - **Score 4:** The student mostly uses open-ended questions to begin information gathering and major lines of inquiry, but occasionally starts with more specific or direct questions. Follow-up questions are mostly appropriate. Very few, if any, poor question types (leading, why, or multiple questions) are used.
      - **Score 3:** The student often fails to begin a line of inquiry with open-ended questions but rather employs specific or direct questions to gather information, or the student uses a few leading questions, why questions, or multiple questions.
      - **Score 2:** The student frequently uses open-ended questions, often relying on specific or direct questions to gather information. There is a noticeable presence of poor question types (leading, why, or multiple questions), but not to the extent of a score of 1. Some attempts at open-ended questioning are evident, but they are infrequent or poorly executed.
      - **Score 1:** The student asks many why questions, multiple questions, or leading questions.

  **Step 3. Justification:** Based on your analysis in Steps 1 and 2, assign a score using the provided rubric strictly, and explain your reasoning clearly. Your evaluation should be rigorous, impartial, and evidence-based. Directly quote the transcript to support your evaluation.
  
Provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

{
  "evaluation": {
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the transcript to support your evaluation"
  }
}

Now, please evaluate the following transcript:
"""

# QUESTIONING_SKILLS_TYPES_OF_QUESTIONS_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating the types of questions used by the interviewer, considering the sequence and appropriateness of open-ended versus specific questions.
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Use of open-ended questions to begin new topics or lines of inquiry
#       - Appropriate follow-up with more specific or direct questions within a topic
#       - Avoidance of poor question types (leading, why, or multiple questions)

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Open-ended questions begin each new topic, followed by appropriate specific questions. No poor question types used.
#     - **Score 4:** Mostly open-ended questions to begin new topics, with occasional use of specific questions to start a new topic. Rare use of poor question types.
#     - **Score 3:** Mix of open-ended and specific questions to begin new topics. Occasional use of poor question types.
#     - **Score 2:** Primarily specific questions used, even to start new topics. More frequent use of poor question types.
#     - **Score 1:** Frequent use of poor question types (why, multiple, or leading questions), especially when starting new topics.

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

# Examples:
#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"Can you tell me about what brought you in today?\"
# Patient: \"I've been having these terrible headaches lately.\"
# Physician: \"I see. Could you describe these headaches for me?\"
# Patient: \"They're really intense, like a throbbing pain behind my eyes.\"
# Physician: \"How often have you been experiencing these headaches?\"
# Patient: \"Almost daily for the past two weeks.\"
# Physician: \"What treatments have you tried for these headaches?\"
# Patient: \"I've been taking over-the-counter painkillers, but they don't help much.\"
# Physician: \"I'd like to ask about a different topic now. How has your sleep been recently?\"
# Patient: \"Actually, I've been having trouble sleeping lately.\"
# Physician: \"Could you tell me more about that?\"
# Patient: \"Well, I'm having difficulty falling asleep and I often wake up in the middle of the night.\"
# Physician: \"How many hours of sleep do you usually get?\"",
#       "response": {
#         "elements_present": [
#           "Use of open-ended questions to begin new topics or lines of inquiry",
#           "Appropriate follow-up with more specific or direct questions within a topic",
#           "Avoidance of poor question types"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician demonstrates excellent questioning skills. They begin with an open-ended question: \"Can you tell me about what brought you in today?\" This allows the patient to freely express their main concern. Within the topic of headaches, they use a mix of open-ended questions (\"Could you describe these headaches for me?\") and specific questions (\"How often have you been experiencing these headaches?\"). When transitioning to a new topic, sleep, the physician uses another open-ended question: \"How has your sleep been recently?\" and follows up with \"Could you tell me more about that?\" before asking more specific questions. There are no instances of poor question types such as leading, why, or multiple questions. This approach allows for a comprehensive gathering of information while maintaining a patient-centered focus."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"What's the main reason for your visit today?\"
# Patient: \"I've been having some stomach issues.\"
# Physician: \"Can you tell me more about these stomach issues?\"
# Patient: \"I've been having a lot of pain and discomfort after eating.\"
# Physician: \"How long has this been going on?\"
# Patient: \"For about two weeks now.\"
# Physician: \"What kinds of foods seem to trigger this discomfort?\"
# Patient: \"Mostly spicy or fatty foods, I think.\"
# Physician: \"I'd like to ask about your general health now. Do you have any chronic medical conditions?\"
# Patient: \"I have high blood pressure.\"
# Physician: \"How long have you been managing your high blood pressure?\"
# Patient: \"For about five years now.\"
# Physician: \"What medications are you currently taking for it?\"",
#       "response": {
#         "elements_present": [
#           "Use of open-ended questions to begin new topics or lines of inquiry",
#           "Appropriate follow-up with more specific or direct questions within a topic",
#           "Avoidance of poor question types"
#         ],
#         "elements_absent": [],
#         "score": 4,
#         "justification": "The physician demonstrates good questioning skills. They start with an open-ended question: \"What's the main reason for your visit today?\" and follow up with another open-ended question within the same topic: \"Can you tell me more about these stomach issues?\" When transitioning to a new topic about general health, the physician uses a somewhat specific question: \"Do you have any chronic medical conditions?\" This is why the score is 4 instead of 5. It would have been better to use an open-ended question to introduce this new topic. However, once the patient mentions high blood pressure, the physician asks appropriate follow-up questions. There are no instances of poor question types, making this a strong performance overall."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"What seems to be the problem today?\"
# Patient: \"I've been having trouble sleeping.\"
# Physician: \"How many hours of sleep are you getting each night?\"
# Patient: \"Usually about 4 or 5 hours.\"
# Physician: \"Do you have trouble falling asleep or staying asleep?\"
# Patient: \"Mostly falling asleep.\"
# Physician: \"Have you been feeling stressed lately?\"
# Patient: \"Yes, work has been quite stressful.\"
# Physician: \"What do you think might be causing your stress at work?\"
# Patient: \"We've had a lot of deadlines and I'm worried about meeting them.\"
# Physician: \"Are you exercising regularly?\"
# Patient: \"Not as much as I should be.\"
# Physician: \"How often do you exercise in a typical week?\"",
#       "response": {
#         "elements_present": [
#           "Use of open-ended questions to begin inquiry",
#           "Appropriate use of specific questions within a topic"
#         ],
#         "elements_absent": [
#           "Consistent use of open-ended questions to begin new topics",
#           "Complete avoidance of poor question types"
#         ],
#         "score": 3,
#         "justification": "The physician starts with an open-ended question: \"What seems to be the problem today?\" However, they often fail to start new topics with open-ended questions. When transitioning to the topic of stress, they use a closed question: \"Have you been feeling stressed lately?\" Similarly, when introducing the topic of exercise, they ask \"Are you exercising regularly?\" rather than using an open-ended question. There's one instance of a 'why' question: \"What do you think might be causing your stress at work?\" While this doesn't severely detract from the information gathering, it could potentially lead the patient to speculate rather than report facts. The mix of question types when starting new topics and the occasional use of a poor question type aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"What's bothering you?\"
# Patient: \"I've been having chest pain.\"
# Physician: \"Is the pain sharp or dull?\"
# Patient: \"It's more of a sharp pain.\"
# Physician: \"Do you have the pain all the time or does it come and go?\"
# Patient: \"It comes and goes.\"
# Physician: \"Does it get worse when you exercise?\"
# Patient: \"Yes, it does.\"
# Physician: \"Do you smoke?\"
# Patient: \"No, I don't.\"
# Physician: \"Have you had any shortness of breath, dizziness, or nausea with the pain?\"
# Patient: \"I've felt a bit dizzy at times.\"
# Physician: \"Do you have a family history of heart disease?\"",
#       "response": {
#         "elements_present": [
#           "Use of specific questions to gather information"
#         ],
#         "elements_absent": [
#           "Use of open-ended questions to begin new topics",
#           "Avoidance of poor question types"
#         ],
#         "score": 2,
#         "justification": "The physician begins with a somewhat open-ended question: \"What's bothering you?\" However, they quickly switch to using primarily specific questions, such as \"Is the pain sharp or dull?\" and \"Do you have the pain all the time or does it come and go?\" When transitioning to new topics like smoking history or family history, the physician continues to use closed questions: \"Do you smoke?\" and \"Do you have a family history of heart disease?\" rather than open-ended questions. There's also an instance of a multiple question: \"Have you had any shortness of breath, dizziness, or nausea with the pain?\" While these questions gather necessary information, they don't allow the patient to fully express their experience and may miss important details. This frequent use of specific questions, even when starting new topics, and the presence of a poor question type aligns with a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Why are you here today?\"
# Patient: \"I've been feeling really tired lately.\"
# Physician: \"Why do you think you're so tired? Is it because you're not sleeping well, or are you working too much, or maybe you're not eating right?\"
# Patient: \"Um, I'm not sure. Maybe all of those?\"
# Physician: \"Don't you think you should be getting more sleep?\"
# Patient: \"I guess so...\"
# Physician: \"And why haven't you tried to eat better or cut back on work?\"
# Patient: \"I've been trying, but it's difficult.\"
# Physician: \"Do you drink alcohol? How much do you drink per day?\"
# Patient: \"I have a glass of wine with dinner sometimes.\"
# Physician: \"Well, don't you want to feel better? Maybe you should stop drinking altogether.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Use of open-ended questions to begin new topics",
#           "Appropriate follow-up with more specific or direct questions within a topic",
#           "Avoidance of poor question types"
#         ],
#         "score": 1,
#         "justification": "The physician demonstrates poor questioning skills throughout this interaction. They begin with a 'why' question: \"Why are you here today?\" which is generally considered a poor way to start a medical interview. They frequently use other poor question types, including multiple questions (\"Why do you think you're so tired? Is it because you're not sleeping well, or are you working too much, or maybe you're not eating right?\") and leading questions (\"Don't you think you should be getting more sleep?\" and \"Well, don't you want to feel better?\"). When introducing a new topic about alcohol consumption, they use a multiple question again: \"Do you drink alcohol? How much do you drink per day?\" These questions can confuse the patient, lead to speculation rather than reporting of symptoms, and may make the patient feel judged or defensive. There are no instances of open-ended questions that would allow the patient to freely express their concerns, even when starting new topics. This frequent use of poor question types severely detracts from the quality of information gathered, aligning with a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]

# """

# QUESTIONING_SKILLS_TYPES_OF_QUESTIONS2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the types of questions used by the interviewer, considering the sequence and appropriateness of open-ended versus specific questions. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Use of open-ended questions to begin new topics or lines of inquiry
#    - Appropriate follow-up with more specific or direct questions within a topic
#    - Avoidance of poor question types (leading, why, or multiple questions)

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Open-ended questions begin each new topic, followed by appropriate specific questions. No poor question types used.
#    - Score 4: Mostly open-ended questions to begin new topics, with occasional use of specific questions to start a new topic. Rare use of poor question types.
#    - Score 3: Mix of open-ended and specific questions to begin new topics. Occasional use of poor question types.
#    - Score 2: Primarily specific questions used, even to start new topics. More frequent use of poor question types.
#    - Score 1: Frequent use of poor question types (why, multiple, or leading questions), especially when starting new topics.

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
# Physician: "Can you tell me about what brought you in today?"
# Patient: "I've been having these terrible headaches lately."
# Physician: "I see. Could you describe these headaches for me?"
# Patient: "They're really intense, like a throbbing pain behind my eyes."
# Physician: "How often have you been experiencing these headaches?"
# Patient: "Almost daily for the past two weeks."
# Physician: "What treatments have you tried for these headaches?"
# Patient: "I've been taking over-the-counter painkillers, but they don't help much."
# Physician: "I'd like to ask about a different topic now. How has your sleep been recently?"
# Patient: "Actually, I've been having trouble sleeping lately."
# Physician: "Could you tell me more about that?"
# Patient: "Well, I'm having difficulty falling asleep and I often wake up in the middle of the night."
# Physician: "How many hours of sleep do you usually get?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Use of open-ended questions to begin new topics or lines of inquiry",
#       "Appropriate follow-up with more specific or direct questions within a topic",
#       "Avoidance of poor question types"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician demonstrates excellent questioning skills. They begin with an open-ended question: \"Can you tell me about what brought you in today?\" This allows the patient to freely express their main concern. Within the topic of headaches, they use a mix of open-ended questions (\"Could you describe these headaches for me?\") and specific questions (\"How often have you been experiencing these headaches?\"). When transitioning to a new topic, sleep, the physician uses another open-ended question: \"How has your sleep been recently?\" and follows up with \"Could you tell me more about that?\" before asking more specific questions. There are no instances of poor question types such as leading, why, or multiple questions. This approach allows for a comprehensive gathering of information while maintaining a patient-centered focus."
#   }
# }

# Example 2:
# Input: 
# Physician: "What's the main reason for your visit today?"
# Patient: "I've been having some stomach issues."
# Physician: "Can you tell me more about these stomach issues?"
# Patient: "I've been having a lot of pain and discomfort after eating."
# Physician: "How long has this been going on?"
# Patient: "For about two weeks now."
# Physician: "What kinds of foods seem to trigger this discomfort?"
# Patient: "Mostly spicy or fatty foods, I think."
# Physician: "I'd like to ask about your general health now. Do you have any chronic medical conditions?"
# Patient: "I have high blood pressure."
# Physician: "How long have you been managing your high blood pressure?"
# Patient: "For about five years now."
# Physician: "What medications are you currently taking for it?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Use of open-ended questions to begin new topics or lines of inquiry",
#       "Appropriate follow-up with more specific or direct questions within a topic",
#       "Avoidance of poor question types"
#     ],
#     "elements_absent": [],
#     "score": 4,
#     "justification": "The physician demonstrates good questioning skills. They start with an open-ended question: \"What's the main reason for your visit today?\" and follow up with another open-ended question within the same topic: \"Can you tell me more about these stomach issues?\" When transitioning to a new topic about general health, the physician uses a somewhat specific question: \"Do you have any chronic medical conditions?\" This is why the score is 4 instead of 5. It would have been better to use an open-ended question to introduce this new topic. However, once the patient mentions high blood pressure, the physician asks appropriate follow-up questions. There are no instances of poor question types, making this a strong performance overall."
#   }
# }

# Example 3:
# Input: 
# Physician: "What seems to be the problem today?"
# Patient: "I've been having trouble sleeping."
# Physician: "How many hours of sleep are you getting each night?"
# Patient: "Usually about 4 or 5 hours."
# Physician: "Do you have trouble falling asleep or staying asleep?"
# Patient: "Mostly falling asleep."
# Physician: "Have you been feeling stressed lately?"
# Patient: "Yes, work has been quite stressful."
# Physician: "What do you think might be causing your stress at work?"
# Patient: "We've had a lot of deadlines and I'm worried about meeting them."
# Physician: "Are you exercising regularly?"
# Patient: "Not as much as I should be."
# Physician: "How often do you exercise in a typical week?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Use of open-ended questions to begin inquiry",
#       "Appropriate use of specific questions within a topic"
#     ],
#     "elements_absent": [
#       "Consistent use of open-ended questions to begin new topics",
#       "Complete avoidance of poor question types"
#     ],
#     "score": 3,
#     "justification": "The physician starts with an open-ended question: \"What seems to be the problem today?\" However, they often fail to start new topics with open-ended questions. When transitioning to the topic of stress, they use a closed question: \"Have you been feeling stressed lately?\" Similarly, when introducing the topic of exercise, they ask \"Are you exercising regularly?\" rather than using an open-ended question. There's one instance of a 'why' question: \"What do you think might be causing your stress at work?\" While this doesn't severely detract from the information gathering, it could potentially lead the patient to speculate rather than report facts. The mix of question types when starting new topics and the occasional use of a poor question type aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "What's bothering you?"
# Patient: "I've been having chest pain."
# Physician: "Is the pain sharp or dull?"
# Patient: "It's more of a sharp pain."
# Physician: "Do you have the pain all the time or does it come and go?"
# Patient: "It comes and goes."
# Physician: "Does it get worse when you exercise?"
# Patient: "Yes, it does."
# Physician: "Do you smoke?"
# Patient: "No, I don't."
# Physician: "Have you had any shortness of breath, dizziness, or nausea with the pain?"
# Patient: "I've felt a bit dizzy at times."
# Physician: "Do you have a family history of heart disease?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Use of specific questions to gather information"
#     ],
#     "elements_absent": [
#       "Use of open-ended questions to begin new topics",
#       "Avoidance of poor question types"
#     ],
#     "score": 2,
#     "justification": "The physician begins with a somewhat open-ended question: \"What's bothering you?\" However, they quickly switch to using primarily specific questions, such as \"Is the pain sharp or dull?\" and \"Do you have the pain all the time or does it come and go?\" When transitioning to new topics like smoking history or family history, the physician continues to use closed questions: \"Do you smoke?\" and \"Do you have a family history of heart disease?\" rather than open-ended questions. There's also an instance of a multiple question: \"Have you had any shortness of breath, dizziness, or nausea with the pain?\" While these questions gather necessary information, they don't allow the patient to fully express their experience and may miss important details. This frequent use of specific questions, even when starting new topics, and the presence of a poor question type aligns with a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "Why are you here today?"
# Patient: "I've been feeling really tired lately."
# Physician: "Why do you think you're so tired? Is it because you're not sleeping well, or are you working too much, or maybe you're not eating right?"
# Patient: "Um, I'm not sure. Maybe all of those?"
# Physician: "Don't you think you should be getting more sleep?"
# Patient: "I guess so..."
# Physician: "And why haven't you tried to eat better or cut back on work?"
# Patient: "I've been trying, but it's difficult."
# Physician: "Do you drink alcohol? How much do you drink per day?"
# Patient: "I have a glass of wine with dinner sometimes."
# Physician: "Well, don't you want to feel better? Maybe you should stop drinking altogether."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Use of open-ended questions to begin new topics",
#       "Appropriate follow-up with more specific or direct questions within a topic",
#       "Avoidance of poor question types"
#     ],
#     "score": 1,
#     "justification": "The physician demonstrates poor questioning skills throughout this interaction. They begin with a 'why' question: \"Why are you here today?\" which is generally considered a poor way to start a medical interview. They frequently use other poor question types, including multiple questions (\"Why do you think you're so tired? Is it because you're not sleeping well, or are you working too much, or maybe you're not eating right?\") and leading questions (\"Don't you think you should be getting more sleep?\" and \"Well, don't you want to feel better?\"). When introducing a new topic about alcohol consumption, they use a multiple question again: \"Do you drink alcohol? How much do you drink per day?\" These questions can confuse the patient, lead to speculation rather than reporting of symptoms, and may make the patient feel judged or defensive. There are no instances of open-ended questions that would allow the patient to freely express their concerns, even when starting new topics. This frequent use of poor question types severely detracts from the quality of information gathered, aligning with a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
