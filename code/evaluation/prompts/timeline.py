TIMELINE = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student establishes a timeline of the chief concern and history of the present illness. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student obtains sufficient information so that a chronology of the chief complaint and history of the present illness can be established. The chronology of all associated symptoms is also established.
      - **Score 4:** The student obtains most of the information necessary to establish a chronology of the chief complaint and history of the present illness. The chronology of most, but not all, associated symptoms is established. Minor gaps in the timeline may exist.
      - **Score 3:** The student obtains some of the information necessary to establish a chronology. They may fail to establish a chronology for all associated symptoms. 
      - **Score 2:** The student obtains limited information about the chronology of the chief complaint and history of the present illness. Significant gaps exist in the timeline, and the chronology of most associated symptoms is not established. 
      - **Score 1:** The student fails to obtain information necessary to establish a chronology. 

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



# TIMELINE_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student establishes a timeline of the chief concern and history of the present illness. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Identification of when symptoms first appeared
#       - Sequence of associated symptoms and/or events
#       - Progression or changes in symptoms over time
#       - Inquiry about recent developments or current status

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Clear chronology established for all symptoms and events
#     - **Score 4:** Most information obtained, but minor details in chronology missing
#     - **Score 3:** Some necessary information obtained, but incomplete chronology
#     - **Score 2:** Limited timeline information gathered, major gaps in chronology
#     - **Score 1:** No meaningful timeline or chronology established

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"When did you first notice something wasn't right?\"
# Patient: \"About a month ago, I started feeling unusually tired.\"
# Physician: \"And what happened next? How did things progress from there?\"
# Patient: \"Well, after about a week of fatigue, I started getting headaches.\"
# Physician: \"I see. And how often were these headaches occurring?\"
# Patient: \"At first, maybe once every couple of days. But by week three, they were daily.\"
# Physician: \"Thank you for that detail. Have you noticed any other symptoms developing since then?\"
# Patient: \"Yes, in the past week, I've also been feeling dizzy occasionally.\"
# Physician: \"And how would you describe your symptoms now, compared to when they first started?\"
# Patient: \"The fatigue is about the same, but the headaches are more intense, and the dizziness is new.\"
# Physician: \"Thank you for walking me through that. Just to confirm, the sequence was fatigue, then headaches, and most recently dizziness, correct?\"
# Patient: \"That's right.\"",
#       "response": {
#         "elements_present": [
#           "Identification of when symptoms first appeared",
#           "Sequence of associated symptoms and/or events",
#           "Progression or changes in symptoms over time",
#           "Inquiry about recent developments or current status"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician thoroughly establishes a clear chronology of the patient's symptoms. They start with \"When did you first notice something wasn't right?\" to pinpoint the onset. They then use questions like \"And what happened next? How did things progress from there?\" to establish the sequence of events. The physician inquires about the progression of symptoms over time, asking \"And how often were these headaches occurring?\" They also check for recent developments with \"Have you noticed any other symptoms developing since then?\" Finally, they confirm the timeline by summarizing the sequence of symptoms. This approach provides a comprehensive understanding of the patient's condition over time."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"When did your symptoms begin?\"
# Patient: \"I started feeling short of breath about two weeks ago.\"
# Physician: \"And how has that progressed since then?\"
# Patient: \"It's gotten worse, especially when I climb stairs.\"
# Physician: \"Have you noticed any other symptoms along with the shortness of breath?\"
# Patient: \"Yes, I've also been feeling very tired lately.\"
# Physician: \"I see. And when did the fatigue start in relation to the shortness of breath?\"
# Patient: \"I'm not sure exactly, but I think around the same time.\"
# Physician: \"Okay. How would you describe your symptoms now compared to two weeks ago?\"
# Patient: \"They're definitely worse now.\"",
#       "response": {
#         "elements_present": [
#           "Identification of when symptoms first appeared",
#           "Sequence of associated symptoms and/or events",
#           "Progression or changes in symptoms over time",
#           "Inquiry about recent developments or current status"
#         ],
#         "elements_absent": [],
#         "score": 4,
#         "justification": "The physician establishes a good timeline of the patient's symptoms, starting with \"When did your symptoms begin?\" They inquire about progression and additional symptoms. However, they miss the opportunity to clarify the exact onset of fatigue in relation to shortness of breath, which would have provided a more precise chronology. The physician does ask about current status compared to initial onset, but could have probed for more specific details about the progression of symptoms over the two-week period."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"How long have you been experiencing these symptoms?\"
# Patient: \"The pain in my knee started about a month ago.\"
# Physician: \"I see. And has it gotten worse since then?\"
# Patient: \"Yes, it's definitely more painful now.\"
# Physician: \"Are you having any other symptoms besides the knee pain?\"
# Patient: \"Well, I've also noticed some swelling.\"
# Physician: \"Okay. Let's take a look at your knee.\"",
#       "response": {
#         "elements_present": [
#           "Identification of when symptoms first appeared",
#           "Progression or changes in symptoms over time"
#         ],
#         "elements_absent": [
#           "Sequence of associated symptoms and/or events",
#           "Inquiry about recent developments or current status"
#         ],
#         "score": 3,
#         "justification": "The physician obtains some necessary information to establish a timeline, starting with \"How long have you been experiencing these symptoms?\" and inquiring about progression. However, they fail to establish a complete chronology. They don't explore the onset of the swelling in relation to the pain, missing an opportunity to understand the sequence of symptoms. They also don't inquire about any recent developments or the current status of the symptoms beyond a general statement of worsening."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"What seems to be the problem today?\"
# Patient: \"I've been having terrible migraines.\"
# Physician: \"How often do these migraines occur?\"
# Patient: \"Almost daily now.\"
# Physician: \"And how long do they usually last?\"
# Patient: \"A few hours, sometimes the whole day.\"
# Physician: \"Okay, let's discuss treatment options.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Identification of when symptoms first appeared",
#           "Sequence of associated symptoms and/or events",
#           "Progression or changes in symptoms over time",
#           "Inquiry about recent developments or current status"
#         ],
#         "score": 2,
#         "justification": "The physician gathers very limited timeline information. They fail to ask when the migraines first started or how they've progressed over time. While they ask about frequency and duration, they don't establish any chronology of the symptoms or explore any associated events or additional symptoms. The phrase \"Almost daily now\" suggests a change in frequency, but the physician doesn't follow up on this. This leaves major gaps in understanding the timeline of the patient's condition."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"I see you're here for abdominal pain. On a scale of 1 to 10, how would you rate your pain right now?\"
# Patient: \"It's about a 7.\"
# Physician: \"And where exactly is the pain located?\"
# Patient: \"Mostly in my lower right side.\"
# Physician: \"Okay, I'm going to perform a physical examination now.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Identification of when symptoms first appeared",
#           "Sequence of associated symptoms and/or events",
#           "Progression or changes in symptoms over time",
#           "Inquiry about recent developments or current status"
#         ],
#         "score": 1,
#         "justification": "The physician fails to establish any meaningful timeline or chronology of the patient's symptoms. They don't ask when the pain started, how it has progressed, or if there are any associated symptoms. The questions focus only on the current state of the pain (intensity and location) without any attempt to understand its history or development over time. This lack of temporal information severely limits the ability to understand the nature and progression of the patient's condition."
#       }
#     }
#   ],
# "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
#   """

# TIMELINE2 = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student establishes a timeline of the chief concern and history of the present illness. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Identification of when symptoms first appeared
#    - Sequence of associated symptoms and/or events
#    - Progression or changes in symptoms over time
#    - Inquiry about recent developments or current status

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Clear chronology established for all symptoms and events
#    - Score 4: Most information obtained, but minor details in chronology missing
#    - Score 3: Some necessary information obtained, but incomplete chronology
#    - Score 2: Limited timeline information gathered, major gaps in chronology
#    - Score 1: No meaningful timeline or chronology established

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
# Physician: "When did you first notice something wasn't right?"
# Patient: "About a month ago, I started feeling unusually tired."
# Physician: "And what happened next? How did things progress from there?"
# Patient: "Well, after about a week of fatigue, I started getting headaches."
# Physician: "I see. And how often were these headaches occurring?"
# Patient: "At first, maybe once every couple of days. But by week three, they were daily."
# Physician: "Thank you for that detail. Have you noticed any other symptoms developing since then?"
# Patient: "Yes, in the past week, I've also been feeling dizzy occasionally."
# Physician: "And how would you describe your symptoms now, compared to when they first started?"
# Patient: "The fatigue is about the same, but the headaches are more intense, and the dizziness is new."
# Physician: "Thank you for walking me through that. Just to confirm, the sequence was fatigue, then headaches, and most recently dizziness, correct?"
# Patient: "That's right."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Identification of when symptoms first appeared",
#       "Sequence of associated symptoms and/or events",
#       "Progression or changes in symptoms over time",
#       "Inquiry about recent developments or current status"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician thoroughly establishes a clear chronology of the patient's symptoms. They start with \"When did you first notice something wasn't right?\" to pinpoint the onset. They then use questions like \"And what happened next? How did things progress from there?\" to establish the sequence of events. The physician inquires about the progression of symptoms over time, asking \"And how often were these headaches occurring?\" They also check for recent developments with \"Have you noticed any other symptoms developing since then?\" Finally, they confirm the timeline by summarizing the sequence of symptoms. This approach provides a comprehensive understanding of the patient's condition over time."
#   }
# }

# Example 2:
# Input: 
# Physician: "When did your symptoms begin?"
# Patient: "I started feeling short of breath about two weeks ago."
# Physician: "And how has that progressed since then?"
# Patient: "It's gotten worse, especially when I climb stairs."
# Physician: "Have you noticed any other symptoms along with the shortness of breath?"
# Patient: "Yes, I've also been feeling very tired lately."
# Physician: "I see. And when did the fatigue start in relation to the shortness of breath?"
# Patient: "I'm not sure exactly, but I think around the same time."
# Physician: "Okay. How would you describe your symptoms now compared to two weeks ago?"
# Patient: "They're definitely worse now."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Identification of when symptoms first appeared",
#       "Sequence of associated symptoms and/or events",
#       "Progression or changes in symptoms over time",
#       "Inquiry about recent developments or current status"
#     ],
#     "elements_absent": [],
#     "score": 4,
#     "justification": "The physician establishes a good timeline of the patient's symptoms, starting with \"When did your symptoms begin?\" They inquire about progression and additional symptoms. However, they miss the opportunity to clarify the exact onset of fatigue in relation to shortness of breath, which would have provided a more precise chronology. The physician does ask about current status compared to initial onset, but could have probed for more specific details about the progression of symptoms over the two-week period."
#   }
# }

# Example 3:
# Input: 
# Physician: "How long have you been experiencing these symptoms?"
# Patient: "The pain in my knee started about a month ago."
# Physician: "I see. And has it gotten worse since then?"
# Patient: "Yes, it's definitely more painful now."
# Physician: "Are you having any other symptoms besides the knee pain?"
# Patient: "Well, I've also noticed some swelling."
# Physician: "Okay. Let's take a look at your knee."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Identification of when symptoms first appeared",
#       "Progression or changes in symptoms over time"
#     ],
#     "elements_absent": [
#       "Sequence of associated symptoms and/or events",
#       "Inquiry about recent developments or current status"
#     ],
#     "score": 3,
#     "justification": "The physician obtains some necessary information to establish a timeline, starting with \"How long have you been experiencing these symptoms?\" and inquiring about progression. However, they fail to establish a complete chronology. They don't explore the onset of the swelling in relation to the pain, missing an opportunity to understand the sequence of symptoms. They also don't inquire about any recent developments or the current status of the symptoms beyond a general statement of worsening."
#   }
# }

# Example 4:
# Input: 
# Physician: "What seems to be the problem today?"
# Patient: "I've been having terrible migraines."
# Physician: "How often do these migraines occur?"
# Patient: "Almost daily now."
# Physician: "And how long do they usually last?"
# Patient: "A few hours, sometimes the whole day."
# Physician: "Okay, let's discuss treatment options."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Identification of when symptoms first appeared",
#       "Sequence of associated symptoms and/or events",
#       "Progression or changes in symptoms over time",
#       "Inquiry about recent developments or current status"
#     ],
#     "score": 2,
#     "justification": "The physician gathers very limited timeline information. They fail to ask when the migraines first started or how they've progressed over time. While they ask about frequency and duration, they don't establish any chronology of the symptoms or explore any associated events or additional symptoms. The phrase \"Almost daily now\" suggests a change in frequency, but the physician doesn't follow up on this. This leaves major gaps in understanding the timeline of the patient's condition."
#   }
# }

# Example 5:
# Input: 
# Physician: "I see you're here for abdominal pain. On a scale of 1 to 10, how would you rate your pain right now?"
# Patient: "It's about a 7."
# Physician: "And where exactly is the pain located?"
# Patient: "Mostly in my lower right side."
# Physician: "Okay, I'm going to perform a physical examination now."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Identification of when symptoms first appeared",
#       "Sequence of associated symptoms and/or events",
#       "Progression or changes in symptoms over time",
#       "Inquiry about recent developments or current status"
#     ],
#     "score": 1,
#     "justification": "The physician fails to establish any meaningful timeline or chronology of the patient's symptoms. They don't ask when the pain started, how it has progressed, or if there are any associated symptoms. The questions focus only on the current state of the pain (intensity and location) without any attempt to understand its history or development over time. This lack of temporal information severely limits the ability to understand the nature and progression of the patient's condition."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
