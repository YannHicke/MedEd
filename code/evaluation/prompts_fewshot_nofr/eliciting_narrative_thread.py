ELICITING_NARRATIVE_THREAD = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student elicits the narrative thread, or the patient’s story, from the patient. You will then provide your evaluation in a given JSON format.
  
To ensure a thorough evaluation, follow these steps:

  **Step 1. Understanding the Task:**
    - Read the following note:
      **Note:** After the agenda is set, the learner encourages the patient to talk about the problem(s), in their own words and listens attentively without interrupting (except for encouragement to continue) until the patient has finished talking about the problem(s). This technique is an effective tool for data gathering, time-efficiency, and rapport building. It allows the patient to tell their story and can help learners gain a large amount of needed data in a short amount of time. 
      **Example:** “Tell me what’s been going on from when your symptoms first started up to today.”

  **Step 2. Scoring:**
    - As you read the transcript, and using your understanding from Step 1, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student encourages and lets the patient talk about their problem. The student does not interrupt the flow of the story.
      - **Score 4:** The student uses a "tell me about" approach.
      - **Score 3:** The student begins to let the patient talk about their problem but either interrupts with focused questions or introduces divergent topics to the history.
      - **Score 2:** The student sets the pace with Q & A style, not conversation.
      - **Score 1:** The student fails to let the patient talk about their problem.

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


# ELICITING_NARRATIVE_THREAD_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student encourages and allows the patient to talk about their problem, eliciting the 'patient's story'. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Open-ended initial question
#       - Allowing patient to speak without interruption
#       - Verbal encouragement to continue (e.g., "Go on", "I see", "Tell me more")
#       - Follow-up questions that build on patient's narrative
#       - Avoidance of unnecessary topic changes

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Complete narrative thread allowed without interruption
#     - **Score 4:** Specific problem elicited, but incomplete narrative thread
#     - **Score 3:** Patient generally allowed to talk, with occasional interruptions or topic changes
#     - **Score 2:** Frequent interruptions, Q&A style dominates
#     - **Score 1:** Physician dominates conversation, patient unable to tell their story

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"I'd like to hear about what's brought you in today. Please take your time and tell me what's been going on.\"
# Patient: \"Well, it all started about three weeks ago when I noticed...\"
# Physician: \"Mm-hmm, go on.\"
# Patient: \"...and then the pain started to spread to my lower back.\"
# Physician: \"I see. Please continue.\"
# Patient: \"...and that's why I decided I needed to come in and get this checked out.\"
# Physician: \"Thank you for sharing that with me. It sounds like you've been dealing with quite a lot. Before we dive into some specific questions, is there anything else you'd like to add about your experience?\"
# Patient: \"No, I think that covers everything.\"
# Physician: \"Alright. Now, based on what you've told me, I'd like to ask a few follow-up questions to make sure I understand everything correctly.\"",
#       "response": {
#         "elements_present": [
#           "Open-ended initial question",
#           "Allowing patient to speak without interruption",
#           "Verbal encouragement to continue",
#           "Follow-up questions that build on patient's narrative",
#           "Avoidance of unnecessary topic changes"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician excels at eliciting the patient's story. They begin with an open-ended question: \"I'd like to hear about what's brought you in today. Please take your time and tell me what's been going on.\" This invites the patient to share their narrative freely. The physician uses verbal cues like \"Mm-hmm, go on\" and \"I see. Please continue\" to encourage the patient to keep talking without interrupting the flow. After the patient finishes, the physician acknowledges the story and offers an opportunity for additions: \"Before we dive into some specific questions, is there anything else you'd like to add about your experience?\" This approach ensures a complete narrative thread and shows respect for the patient's experience."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"I see from your chart that you're here about knee pain. Can you tell me about that?\"
# Patient: \"Yes, my knee has been bothering me for a few weeks now. It started when I...\"
# Physician: \"I see.\"
# Patient: \"...and it's been getting worse, especially when I—\"
# Physician: \"Can you point to where exactly the pain is located?\"
# Patient: \"It's mainly here on the side and sometimes...\"
# Physician: \"Okay, and how would you rate the pain on a scale of 1 to 10?\"",
#       "response": {
#         "elements_present": [
#           "Specific problem elicited",
#           "Allowing patient to speak without interruption (initially)",
#           "Follow-up questions that build on patient's narrative"
#         ],
#         "elements_absent": [
#           "Open-ended initial question",
#           "Complete narrative thread allowed"
#         ],
#         "score": 4,
#         "justification": "The physician starts by focusing on a specific problem: \"I see from your chart that you're here about knee pain. Can you tell me about that?\" This allows the patient to talk about their issue, but it's not entirely open-ended. The physician initially lets the patient speak, offering a brief \"I see\" to show they're listening. However, they then start to guide the conversation with specific questions before the patient has finished their complete narrative. While the follow-up questions are relevant, they prevent a full, uninterrupted story from the patient. This approach gathers necessary information but doesn't fully allow for a complete narrative thread."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"What brings you in today?\"
# Patient: \"I've been having these terrible headaches. They started about a month ago and—\"
# Physician: \"How often do you get these headaches?\"
# Patient: \"Well, at first it was just once a week, but now it's almost daily. As I was saying, they've been getting worse and—\"
# Physician: \"And how long do they typically last?\"
# Patient: \"Usually a few hours. But the thing is, they're really affecting my work because—\"
# Physician: \"Have you taken any medication for them?\"
# Patient: \"I've tried over-the-counter painkillers, but they don't seem to help much.\"
# Physician: \"I see. Tell me more about how they're affecting your daily life.\"",
#       "response": {
#         "elements_present": [
#           "Open-ended initial question",
#           "Some allowance for patient to speak",
#           "Follow-up questions that build on patient's narrative"
#         ],
#         "elements_absent": [
#           "Allowing patient to speak without interruption",
#           "Avoidance of unnecessary topic changes"
#         ],
#         "score": 3,
#         "justification": "The physician starts with an open-ended question: \"What brings you in today?\" However, they frequently interrupt the patient's narrative with focused questions about frequency, duration, and medication. While these questions are relevant, they disrupt the flow of the patient's story. The physician does attempt to return to the patient's narrative at the end with \"Tell me more about how they're affecting your daily life.\" This approach shows some attempt to elicit the patient's story, but the frequent interruptions prevent a smooth narrative flow."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"What's the problem?\"
# Patient: \"I've been experiencing chest pain—\"
# Physician: \"Where exactly is the pain?\"
# Patient: \"It's in the center of my chest, and it—\"
# Physician: \"Is it sharp or dull?\"
# Patient: \"It's more of a sharp pain, especially when I—\"
# Physician: \"How long have you had it?\"
# Patient: \"It started about a week ago, and I've noticed—\"
# Physician: \"Have you had any shortness of breath?\"
# Patient: \"No, not really, but I am concerned because—\"
# Physician: \"Any family history of heart disease?\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Open-ended initial question",
#           "Allowing patient to speak without interruption",
#           "Verbal encouragement to continue",
#           "Follow-up questions that build on patient's narrative",
#           "Avoidance of unnecessary topic changes"
#         ],
#         "score": 2,
#         "justification": "The physician begins with a closed question: \"What's the problem?\" and then frequently interrupts the patient with a series of specific questions. This creates a rapid-fire Q&A dynamic rather than allowing for a natural conversational flow. The physician doesn't give the patient an opportunity to fully express their concerns or provide context for their symptoms. While the questions are medically relevant, this approach significantly hinders the patient's ability to tell their story and may miss important details or concerns that don't fit neatly into the physician's questioning structure."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"I see you're here for a follow-up on your blood pressure medication. Let's check your blood pressure.\"
# Patient: \"Actually, I've been having some other concerns lately—\"
# Physician: \"We'll get to that in a moment. First, let's review your medication list. Are you still taking lisinopril 10mg daily?\"
# Patient: \"Yes, but I've been experiencing some side effects that I'd like to discuss—\"
# Physician: \"Side effects are common. Are you taking it as prescribed, with food?\"
# Patient: \"Yes, but—\"
# Physician: \"Good. Now, let's schedule your next appointment and some routine blood work.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Open-ended initial question",
#           "Allowing patient to speak without interruption",
#           "Verbal encouragement to continue",
#           "Follow-up questions that build on patient's narrative",
#           "Avoidance of unnecessary topic changes"
#         ],
#         "score": 1,
#         "justification": "The physician completely fails to elicit the patient's story. They begin by making assumptions about the reason for the visit: \"I see you're here for a follow-up on your blood pressure medication.\" When the patient tries to bring up other concerns, the physician dismisses them: \"We'll get to that in a moment.\" The physician dominates the conversation, focusing on their own agenda rather than the patient's concerns. They interrupt the patient multiple times and don't allow any opportunity for the patient to express their story or concerns. This approach risks missing important health issues and can lead to patient dissatisfaction and poor health outcomes."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# ELICITING_NARRATIVE_THREAD2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student encourages and allows the patient to talk about their problem, eliciting the 'patient's story'. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Open-ended initial question
#    - Allowing patient to speak without interruption
#    - Verbal encouragement to continue (e.g., "Go on", "I see", "Tell me more")
#    - Follow-up questions that build on patient's narrative
#    - Avoidance of unnecessary topic changes

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Complete narrative thread allowed without interruption
#    - Score 4: Specific problem elicited, but incomplete narrative thread
#    - Score 3: Patient generally allowed to talk, with occasional interruptions or topic changes
#    - Score 2: Frequent interruptions, Q&A style dominates
#    - Score 1: Physician dominates conversation, patient unable to tell their story

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
# Physician: "I'd like to hear about what's brought you in today. Please take your time and tell me what's been going on."
# Patient: "Well, it all started about three weeks ago when I noticed..."
# Physician: "Mm-hmm, go on."
# Patient: "...and then the pain started to spread to my lower back."
# Physician: "I see. Please continue."
# Patient: "...and that's why I decided I needed to come in and get this checked out."
# Physician: "Thank you for sharing that with me. It sounds like you've been dealing with quite a lot. Before we dive into some specific questions, is there anything else you'd like to add about your experience?"
# Patient: "No, I think that covers everything."
# Physician: "Alright. Now, based on what you've told me, I'd like to ask a few follow-up questions to make sure I understand everything correctly."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Open-ended initial question",
#       "Allowing patient to speak without interruption",
#       "Verbal encouragement to continue",
#       "Follow-up questions that build on patient's narrative",
#       "Avoidance of unnecessary topic changes"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician excels at eliciting the patient's story. They begin with an open-ended question: \"I'd like to hear about what's brought you in today. Please take your time and tell me what's been going on.\" This invites the patient to share their narrative freely. The physician uses verbal cues like \"Mm-hmm, go on\" and \"I see. Please continue\" to encourage the patient to keep talking without interrupting the flow. After the patient finishes, the physician acknowledges the story and offers an opportunity for additions: \"Before we dive into some specific questions, is there anything else you'd like to add about your experience?\" This approach ensures a complete narrative thread and shows respect for the patient's experience."
#   }
# }

# Example 2:
# Input: 
# Physician: "I see from your chart that you're here about knee pain. Can you tell me about that?"
# Patient: "Yes, my knee has been bothering me for a few weeks now. It started when I..."
# Physician: "I see."
# Patient: "...and it's been getting worse, especially when I—"
# Physician: "Can you point to where exactly the pain is located?"
# Patient: "It's mainly here on the side and sometimes..."
# Physician: "Okay, and how would you rate the pain on a scale of 1 to 10?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Specific problem elicited",
#       "Allowing patient to speak without interruption (initially)",
#       "Follow-up questions that build on patient's narrative"
#     ],
#     "elements_absent": [
#       "Open-ended initial question",
#       "Complete narrative thread allowed"
#     ],
#     "score": 4,
#     "justification": "The physician starts by focusing on a specific problem: \"I see from your chart that you're here about knee pain. Can you tell me about that?\" This allows the patient to talk about their issue, but it's not entirely open-ended. The physician initially lets the patient speak, offering a brief \"I see\" to show they're listening. However, they then start to guide the conversation with specific questions before the patient has finished their complete narrative. While the follow-up questions are relevant, they prevent a full, uninterrupted story from the patient. This approach gathers necessary information but doesn't fully allow for a complete narrative thread."
#   }
# }

# Example 3:
# Input: 
# Physician: "What brings you in today?"
# Patient: "I've been having these terrible headaches. They started about a month ago and—"
# Physician: "How often do you get these headaches?"
# Patient: "Well, at first it was just once a week, but now it's almost daily. As I was saying, they've been getting worse and—"
# Physician: "And how long do they typically last?"
# Patient: "Usually a few hours. But the thing is, they're really affecting my work because—"
# Physician: "Have you taken any medication for them?"
# Patient: "I've tried over-the-counter painkillers, but they don't seem to help much."
# Physician: "I see. Tell me more about how they're affecting your daily life."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Open-ended initial question",
#       "Some allowance for patient to speak",
#       "Follow-up questions that build on patient's narrative"
#     ],
#     "elements_absent": [
#       "Allowing patient to speak without interruption",
#       "Avoidance of unnecessary topic changes"
#     ],
#     "score": 3,
#     "justification": "The physician starts with an open-ended question: \"What brings you in today?\" However, they frequently interrupt the patient's narrative with focused questions about frequency, duration, and medication. While these questions are relevant, they disrupt the flow of the patient's story. The physician does attempt to return to the patient's narrative at the end with \"Tell me more about how they're affecting your daily life.\" This approach shows some attempt to elicit the patient's story, but the frequent interruptions prevent a smooth narrative flow."
#   }
# }

# Example 4:
# Input: 
# Physician: "What's the problem?"
# Patient: "I've been experiencing chest pain—"
# Physician: "Where exactly is the pain?"
# Patient: "It's in the center of my chest, and it—"
# Physician: "Is it sharp or dull?"
# Patient: "It's more of a sharp pain, especially when I—"
# Physician: "How long have you had it?"
# Patient: "It started about a week ago, and I've noticed—"
# Physician: "Have you had any shortness of breath?"
# Patient: "No, not really, but I am concerned because—"
# Physician: "Any family history of heart disease?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Open-ended initial question",
#       "Allowing patient to speak without interruption",
#       "Verbal encouragement to continue",
#       "Follow-up questions that build on patient's narrative",
#       "Avoidance of unnecessary topic changes"
#     ],
#     "score": 2,
#     "justification": "The physician begins with a closed question: \"What's the problem?\" and then frequently interrupts the patient with a series of specific questions. This creates a rapid-fire Q&A dynamic rather than allowing for a natural conversational flow. The physician doesn't give the patient an opportunity to fully express their concerns or provide context for their symptoms. While the questions are medically relevant, this approach significantly hinders the patient's ability to tell their story and may miss important details or concerns that don't fit neatly into the physician's questioning structure."
#   }
# }

# Example 5:
# Input: 
# Physician: "I see you're here for a follow-up on your blood pressure medication. Let's check your blood pressure."
# Patient: "Actually, I've been having some other concerns lately—"
# Physician: "We'll get to that in a moment. First, let's review your medication list. Are you still taking lisinopril 10mg daily?"
# Patient: "Yes, but I've been experiencing some side effects that I'd like to discuss—"
# Physician: "Side effects are common. Are you taking it as prescribed, with food?"
# Patient: "Yes, but—"
# Physician: "Good. Now, let's schedule your next appointment and some routine blood work."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Open-ended initial question",
#       "Allowing patient to speak without interruption",
#       "Verbal encouragement to continue",
#       "Follow-up questions that build on patient's narrative",
#       "Avoidance of unnecessary topic changes"
#     ],
#     "score": 1,
#     "justification": "The physician completely fails to elicit the patient's story. They begin by making assumptions about the reason for the visit: \"I see you're here for a follow-up on your blood pressure medication.\" When the patient tries to bring up other concerns, the physician dismisses them: \"We'll get to that in a moment.\" The physician dominates the conversation, focusing on their own agenda rather than the patient's concerns. They interrupt the patient multiple times and don't allow any opportunity for the patient to express their story or concerns. This approach risks missing important health issues and can lead to patient dissatisfaction and poor health outcomes."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
