QUESTIONING_SKILLS_SUMMARIZING = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the student’s questioning skills, specifically looking at their ability to summarize. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Identify Key Elements:**
    - As you read the transcript, create a list noting whether each element is present or absent:
      - Summarizes patient's concerns
      - Verifies information with the patient
      - Clarifies details

  **Step 2. Scoring:**
    - As you read the transcript, use your list from Step 1 and evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student summarizes the data obtained at the end of each major line of inquiry or subsection to verify and/or clarify the information for a complete Hx (History). One summary is sufficient for a focused history (a patient history that concentrates solely on the details surrounding the patient's current chief complaint) either at the end of the HPI (History of Present Illness) or by the end of the interview. 
      - **Score 4:** The student summarizes data at the end of most major lines of inquiry or subsections, but may miss one or two opportunities. Summaries are mostly accurate but may occasionally lack some detail. For a focused history, the summary is present but might be slightly incomplete or occur at a less optimal time.
      - **Score 3:** The student summarizes the data at the end of some lines of inquiry but not consistently or completely, or attempts to summarize at the end of the interview and it is incomplete.
      - **Score 2:** The student makes some attempts at summarizing, but these are infrequent, often incomplete, or occur at inappropriate times. There may be one or two adequate summaries, but the majority of opportunities for summarization are missed. The student shows awareness of the need to summarize but struggles to execute it effectively.
      - **Score 1:** The student fails to summarize any of the data obtained. 

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

Now, please evaluate the following transcript:
"""


# QUESTIONING_SKILLS_SUMMARIZING_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student summarizes the data obtained during the interview. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Summarization at the end of major lines of inquiry or subsections
#       - Verification of information with the patient
#       - Clarification of details
#       - Completeness of summaries

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Consistent, complete summaries at the end of each major line of inquiry or subsection
#     - **Score 3:** Some summaries present, but inconsistent or incomplete
#     - **Score 1:** No summaries of data obtained

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

# Examples:
#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"What brings you in today?\"
# Patient: \"I've been having these terrible headaches.\"
# Physician: \"I'm sorry to hear that. Can you tell me more about these headaches?\"
# Patient: \"They started about two weeks ago. At first, they were just annoying, but now they're really intense.\"
# Physician: \"Where exactly do you feel the pain?\"
# Patient: \"It's mostly on the right side of my head, behind my eye.\"
# Physician: \"And how often do you get these headaches?\"
# Patient: \"Now it's almost every day. They usually start in the afternoon and get worse in the evening.\"
# Physician: \"Have you noticed anything that seems to trigger them?\"
# Patient: \"I'm not sure, but I think they might be worse when I'm stressed or haven't slept well.\"
# Physician: \"Have you tried anything to relieve the pain?\"
# Patient: \"I've been taking over-the-counter painkillers, but they don't help much.\"
# Physician: \"Alright, thank you for sharing all of that. Let me summarize what you've told me about your headaches to make sure I've understood correctly. You've been experiencing headaches for about two weeks now. They started as mild annoyances but have become more intense over time. The pain is primarily on the right side of your head, behind your eye. You're now having these headaches almost daily, typically starting in the afternoon and worsening in the evening. You've noticed they might be exacerbated by stress or lack of sleep. Over-the-counter painkillers haven't been very effective in managing the pain. Is this an accurate summary of what you've told me?\"
# Patient: \"Yes, that's exactly right.\"
# Physician: \"Thank you for confirming. Now, let's talk about any other symptoms you might be experiencing...\"",
#       "response": {
#         "elements_present": [
#           "Summarization at the end of major lines of inquiry or subsections",
#           "Verification of information with the patient",
#           "Clarification of details",
#           "Completeness of summaries"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician provides an excellent summary of the patient's headache symptoms. They cover all key points discussed: onset (\"experiencing headaches for about two weeks\"), progression (\"started as mild annoyances but have become more intense\"), location (\"right side of your head, behind your eye\"), frequency (\"almost daily\"), timing (\"starting in the afternoon and worsening in the evening\"), potential triggers (\"exacerbated by stress or lack of sleep\"), and attempted remedies (\"Over-the-counter painkillers haven't been very effective\"). The physician then verifies the information with the patient by asking, \"Is this an accurate summary of what you've told me?\" This comprehensive summary at the end of this line of inquiry ensures all information is accurate and complete before moving on to the next topic."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"What seems to be the problem?\"
# Patient: \"I've been having trouble sleeping lately.\"
# Physician: \"How long has this been going on?\"
# Patient: \"It's been about a month now.\"
# Physician: \"And what exactly is the trouble? Falling asleep, staying asleep, or both?\"
# Patient: \"Mostly falling asleep. I toss and turn for hours.\"
# Physician: \"Have you noticed any changes in your daily routine or stress levels?\"
# Patient: \"Well, I started a new job about six weeks ago. It's been pretty stressful.\"
# Physician: \"I see. Have you tried anything to help you sleep?\"
# Patient: \"I've tried some herbal tea and melatonin supplements, but they don't seem to help much.\"
# Physician: \"Okay, so you've been having trouble falling asleep for about a month now. This started around the time you began a new job. Is that right?\"
# Patient: \"Yes, that's correct.\"
# Physician: \"Alright, let's talk about your typical daily routine...\"",
#       "response": {
#         "elements_present": [
#           "Some summarization at the end of lines of inquiry",
#           "Partial verification of information with the patient"
#         ],
#         "elements_absent": [
#           "Consistent summarization",
#           "Completeness of summaries",
#           "Clarification of details"
#         ],
#         "score": 3,
#         "justification": "The physician attempts to summarize some of the information obtained about the patient's sleep issues: \"Okay, so you've been having trouble falling asleep for about a month now. This started around the time you began a new job.\" They also verify this information with the patient. However, the summary is incomplete, missing details such as the patient's difficulty in falling asleep, the tossing and turning, and the ineffective remedies tried (herbal tea and melatonin). The physician doesn't provide a comprehensive summary of all aspects discussed before moving on to the next topic. This inconsistent and incomplete summarization warrants a score of 3."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"What brings you in today?\"
# Patient: \"I've been experiencing some chest pain.\"
# Physician: \"Can you describe the pain?\"
# Patient: \"It's a sharp pain, right in the center of my chest.\"
# Physician: \"How long have you been experiencing this?\"
# Patient: \"It started about a week ago.\"
# Physician: \"Does anything seem to trigger the pain?\"
# Patient: \"I've noticed it's worse when I exert myself, like climbing stairs.\"
# Physician: \"Have you experienced any shortness of breath?\"
# Patient: \"Yes, especially when the pain is bad.\"
# Physician: \"I see. Do you have any other symptoms you're concerned about?\"
# Patient: \"No, those are the main things.\"
# Physician: \"Alright, let's move on to your medical history. Have you ever been diagnosed with any heart conditions?\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Summarization at the end of major lines of inquiry or subsections",
#           "Verification of information with the patient",
#           "Clarification of details",
#           "Completeness of summaries"
#         ],
#         "score": 1,
#         "justification": "The physician fails to summarize any of the data obtained during the discussion about the patient's symptoms. Despite gathering significant information about the chest pain (description, duration, triggers) and associated symptoms (shortness of breath), the physician moves directly to the next line of inquiry about medical history without summarizing or clarifying the information about the current symptoms. This complete lack of summarization results in a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]

# """

# QUESTIONING_SKILLS_SUMMARIZING2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student summarizes the data obtained during the interview. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Summarization at the end of major lines of inquiry or subsections
#    - Verification of information with the patient
#    - Clarification of details
#    - Completeness of summaries

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Consistent, complete summaries at the end of each major line of inquiry or subsection
#    - Score 3: Some summaries present, but inconsistent or incomplete
#    - Score 1: No summaries of data obtained

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
# Patient: "I've been having these terrible headaches."
# Physician: "I'm sorry to hear that. Can you tell me more about these headaches?"
# Patient: "They started about two weeks ago. At first, they were just annoying, but now they're really intense."
# Physician: "Where exactly do you feel the pain?"
# Patient: "It's mostly on the right side of my head, behind my eye."
# Physician: "And how often do you get these headaches?"
# Patient: "Now it's almost every day. They usually start in the afternoon and get worse in the evening."
# Physician: "Have you noticed anything that seems to trigger them?"
# Patient: "I'm not sure, but I think they might be worse when I'm stressed or haven't slept well."
# Physician: "Have you tried anything to relieve the pain?"
# Patient: "I've been taking over-the-counter painkillers, but they don't help much."
# Physician: "Alright, thank you for sharing all of that. Let me summarize what you've told me about your headaches to make sure I've understood correctly. You've been experiencing headaches for about two weeks now. They started as mild annoyances but have become more intense over time. The pain is primarily on the right side of your head, behind your eye. You're now having these headaches almost daily, typically starting in the afternoon and worsening in the evening. You've noticed they might be exacerbated by stress or lack of sleep. Over-the-counter painkillers haven't been very effective in managing the pain. Is this an accurate summary of what you've told me?"
# Patient: "Yes, that's exactly right."
# Physician: "Thank you for confirming. Now, let's talk about any other symptoms you might be experiencing..."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Summarization at the end of major lines of inquiry or subsections",
#       "Verification of information with the patient",
#       "Clarification of details",
#       "Completeness of summaries"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician provides an excellent summary of the patient's headache symptoms. They cover all key points discussed: onset (\"experiencing headaches for about two weeks\"), progression (\"started as mild annoyances but have become more intense\"), location (\"right side of your head, behind your eye\"), frequency (\"almost daily\"), timing (\"starting in the afternoon and worsening in the evening\"), potential triggers (\"exacerbated by stress or lack of sleep\"), and attempted remedies (\"Over-the-counter painkillers haven't been very effective\"). The physician then verifies the information with the patient by asking, \"Is this an accurate summary of what you've told me?\" This comprehensive summary at the end of this line of inquiry ensures all information is accurate and complete before moving on to the next topic."
#   }
# }

# Example 2:
# Input: 
# Physician: "What seems to be the problem?"
# Patient: "I've been having trouble sleeping lately."
# Physician: "How long has this been going on?"
# Patient: "It's been about a month now."
# Physician: "And what exactly is the trouble? Falling asleep, staying asleep, or both?"
# Patient: "Mostly falling asleep. I toss and turn for hours."
# Physician: "Have you noticed any changes in your daily routine or stress levels?"
# Patient: "Well, I started a new job about six weeks ago. It's been pretty stressful."
# Physician: "I see. Have you tried anything to help you sleep?"
# Patient: "I've tried some herbal tea and melatonin supplements, but they don't seem to help much."
# Physician: "Okay, so you've been having trouble falling asleep for about a month now. This started around the time you began a new job. Is that right?"
# Patient: "Yes, that's correct."
# Physician: "Alright, let's talk about your typical daily routine..."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Some summarization at the end of lines of inquiry",
#       "Partial verification of information with the patient"
#     ],
#     "elements_absent": [
#       "Consistent summarization",
#       "Completeness of summaries",
#       "Clarification of details"
#     ],
#     "score": 3,
#     "justification": "The physician attempts to summarize some of the information obtained about the patient's sleep issues: \"Okay, so you've been having trouble falling asleep for about a month now. This started around the time you began a new job.\" They also verify this information with the patient. However, the summary is incomplete, missing details such as the patient's difficulty in falling asleep, the tossing and turning, and the ineffective remedies tried (herbal tea and melatonin). The physician doesn't provide a comprehensive summary of all aspects discussed before moving on to the next topic. This inconsistent and incomplete summarization warrants a score of 3."
#   }
# }

# Example 3:
# Input: 
# Physician: "What brings you in today?"
# Patient: "I've been experiencing some chest pain."
# Physician: "Can you describe the pain?"
# Patient: "It's a sharp pain, right in the center of my chest."
# Physician: "How long have you been experiencing this?"
# Patient: "It started about a week ago."
# Physician: "Does anything seem to trigger the pain?"
# Patient: "I've noticed it's worse when I exert myself, like climbing stairs."
# Physician: "Have you experienced any shortness of breath?"
# Patient: "Yes, especially when the pain is bad."
# Physician: "I see. Do you have any other symptoms you're concerned about?"
# Patient: "No, those are the main things."
# Physician: "Alright, let's move on to your medical history. Have you ever been diagnosed with any heart conditions?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Summarization at the end of major lines of inquiry or subsections",
#       "Verification of information with the patient",
#       "Clarification of details",
#       "Completeness of summaries"
#     ],
#     "score": 1,
#     "justification": "The physician fails to summarize any of the data obtained during the discussion about the patient's symptoms. Despite gathering significant information about the chest pain (description, duration, triggers) and associated symptoms (shortness of breath), the physician moves directly to the next line of inquiry about medical history without summarizing or clarifying the information about the current symptoms. This complete lack of summarization results in a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
