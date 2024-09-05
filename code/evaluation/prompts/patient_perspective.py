PATIENTS_PERSPECTIVE_BELIEFS = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student elicits the patient’s perspectives and beliefs. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student elicits the patient’s healing practices and perspectives on their illness, including their beliefs about its beginning by eliciting the patient’s Feelings about the illness, Ideas of its cause, the impact on daily Function, and their Expectations for treatment and outcomes (FIFE).
      - **Score 4:** The student elicits most aspects of the patient's perspective on their illness and healing practices. They cover several elements of FIFE, but may miss one or two components or not explore them as deeply. The student shows a clear attempt to understand the patient's viewpoint, even if not as comprehensively as in a score of 5.
      - **Score 3:** The student elicits some of the patient’s perspective on their illness and/or does not follow through with addressing their beliefs. 
      - **Score 2:** The student makes limited attempts to elicit the patient's perspective. The student shows some awareness of the importance of the patient's viewpoint but struggles to effectively draw out or address these beliefs and practices.
      - **Score 1:** The student fails to elicit the patient’s perspective.

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




# PATIENTS_PERSPECTIVE_BELIEFS_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student elicits and addresses the patient's beliefs and perspective on their illness using the FIFE (Feelings, Ideas of cause, Function, and Expectations) technique. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element of FIFE is present or absent:
#       - Feelings: Exploration of the emotional impact of the illness
#       - Ideas of cause: Investigation of patient's beliefs about the cause of their symptoms
#       - Function: Examination of how the illness affects the patient's daily life
#       - Expectations: Exploration of what the patient hopes to gain from the encounter
#    -  Also note:
#       - Incorporation of patient's perspective into the discussion
#       - Elicitation of patient's healing practices (if applicable)

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Comprehensive use of FIFE technique, addressing all four elements and incorporating findings into discussion
#     - **Score 4:** Good use of FIFE technique, addressing most elements with some incorporation into discussion
#     - **Score 3:** Partial use of FIFE technique, addressing some elements with limited incorporation into discussion
#     - **Score 2:** Minimal use of FIFE technique, addressing few elements with little to no incorporation into discussion
#     - **Score 1:** No use of FIFE technique or consideration of patient's perspective

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"Before we discuss treatment, I'd like to understand your experience with these symptoms. How have you been feeling emotionally since they started?\" (Feelings)
# Patient: \"I've been really anxious. It's affecting my mood.\"
# Physician: \"I'm sorry to hear that. It's understandable to feel anxious. What do you think might be causing these symptoms?\" (Ideas of cause)
# Patient: \"I wonder if it's related to the stress from my new job.\"
# Physician: \"That's an interesting observation. How have these symptoms affected your daily activities and work?\" (Function)
# Patient: \"I'm having trouble concentrating and I've had to cancel social plans.\"
# Physician: \"I see. That sounds challenging. What are you hoping we can accomplish today?\" (Expectations)
# Patient: \"I'm hoping to find out what's wrong and get some relief.\"
# Physician: \"Thank you for sharing that. Your perspective is very important. Let's discuss how we can address these symptoms, including looking at stress management techniques, while we investigate potential medical causes. Have you tried any remedies or practices to manage these symptoms?\"",
#       "response": {
#         "elements_present": [
#           "Feelings: Exploration of emotional impact",
#           "Ideas of cause: Investigation of patient's beliefs about cause",
#           "Function: Examination of impact on daily life",
#           "Expectations: Exploration of patient's hopes for the encounter",
#           "Incorporation of patient's perspective into the discussion",
#           "Elicitation of patient's healing practices"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician demonstrates excellent use of the FIFE technique, addressing all four elements comprehensively. They explore Feelings (\"How have you been feeling emotionally\"), Ideas of cause (\"What do you think might be causing these symptoms?\"), Function (\"How have these symptoms affected your daily activities and work?\"), and Expectations (\"What are you hoping we can accomplish today?\"). The physician also incorporates the patient's perspective into the discussion, as evidenced by their final statement about addressing symptoms and investigating causes while considering stress management. They also inquire about any remedies the patient might have tried. This comprehensive approach to understanding and incorporating the patient's perspective using FIFE warrants a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"I'd like to understand your experience with these symptoms. What do you think might be causing them?\" (Ideas of cause)
# Patient: \"I've been under a lot of stress lately, so I wonder if that's related.\"
# Physician: \"Stress can certainly affect our health. How have these symptoms been impacting your daily life?\" (Function)
# Patient: \"It's been hard to focus at work, and I'm not sleeping well.\"
# Physician: \"I see. And how are you feeling about all of this?\" (Feelings)
# Patient: \"I'm frustrated and a bit scared, to be honest.\"
# Physician: \"Those are understandable feelings. What are you hoping we can accomplish today?\" (Expectations)
# Patient: \"I'm hoping to get some answers and maybe some relief.\"
# Physician: \"Thank you for sharing that. We'll certainly look into potential causes, including how stress might be playing a role, and discuss ways to help you feel better.\"",
#       "response": {
#         "elements_present": [
#           "Feelings: Exploration of emotional impact",
#           "Ideas of cause: Investigation of patient's beliefs about cause",
#           "Function: Examination of impact on daily life",
#           "Expectations: Exploration of patient's hopes for the encounter",
#           "Some incorporation of patient's perspective into the discussion"
#         ],
#         "elements_absent": [
#           "Elicitation of patient's healing practices"
#         ],
#         "score": 4,
#         "justification": "The physician demonstrates good use of the FIFE technique, addressing all four elements. They inquire about Ideas of cause, Function, Feelings, and Expectations. The physician also shows some incorporation of the patient's perspective into the discussion, acknowledging the potential role of stress. However, the exploration of each element is not as in-depth as it could be, and they don't inquire about any healing practices the patient might have tried. While the approach is thorough, these minor limitations prevent it from reaching the comprehensive level of a score of 5, thus warranting a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"What do you think might be causing your symptoms?\" (Ideas of cause)
# Patient: \"I'm not sure, but they started after I began a new job.\"
# Physician: \"Starting a new job can be stressful. How have these symptoms affected your work?\" (Function)
# Patient: \"It's been difficult to concentrate sometimes.\"
# Physician: \"I see. How are you feeling about all this?\" (Feelings)
# Patient: \"I'm worried, to be honest.\"
# Physician: \"I understand. Well, let's run some tests to see what might be going on.\"
# Patient: \"Do you think it could be stress-related?\"
# Physician: \"It's possible. We'll consider that as we investigate.\"",
#       "response": {
#         "elements_present": [
#           "Ideas of cause: Investigation of patient's beliefs about cause",
#           "Function: Some examination of impact on daily life",
#           "Feelings: Brief exploration of emotional impact"
#         ],
#         "elements_absent": [
#           "Expectations: No exploration of patient's hopes for the encounter",
#           "Thorough incorporation of patient's perspective into the discussion",
#           "Elicitation of patient's healing practices"
#         ],
#         "score": 3,
#         "justification": "The physician makes some effort to use the FIFE technique, addressing Ideas of cause, Function, and briefly touching on Feelings. However, they miss the opportunity to explore the patient's Expectations for the encounter. While the physician acknowledges the possibility of stress playing a role, they don't fully incorporate this into the discussion or explore it further. The conversation lacks depth in addressing the patient's beliefs, and there's no inquiry into any healing practices the patient might have tried. This partial use of the FIFE technique with limited incorporation of the patient's perspective aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"How long have you been experiencing these symptoms?\"
# Patient: \"About a month now. I'm worried it might be something serious.\"
# Physician: \"I see. And where exactly is the pain located?\"
# Patient: \"In my lower back, but I've read online it could be related to my diet.\"
# Physician: \"Online information can be misleading. Let's focus on the physical symptoms for now.\"
# Patient: \"Okay, but shouldn't we consider all possibilities?\"
# Physician: \"We'll run some tests to determine the cause. Try not to worry too much.\"",
#       "response": {
#         "elements_present": [
#           "Minimal inquiry into patient's concerns"
#         ],
#         "elements_absent": [
#           "Feelings: No exploration of emotional impact",
#           "Ideas of cause: Dismissal of patient's ideas",
#           "Function: No examination of impact on daily life",
#           "Expectations: No exploration of patient's hopes for the encounter",
#           "Incorporation of patient's perspective into the discussion",
#           "Elicitation of patient's healing practices"
#         ],
#         "score": 2,
#         "justification": "The physician shows minimal effort in using the FIFE technique. While they ask about the duration and location of symptoms, they dismiss the patient's attempt to share their ideas about potential causes (\"Online information can be misleading\"). The physician doesn't explore the patient's feelings, the impact on their function, or their expectations for treatment. There's no attempt to incorporate the patient's beliefs into the discussion, and the response to the patient's concern about considering all possibilities is dismissive. This approach, which largely ignores the patient's perspective and fails to use the FIFE technique, warrants a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Your test results show high blood pressure. We need to start you on medication right away.\"
# Patient: \"I've been under a lot of stress lately. Could that be causing it?\"
# Physician: \"High blood pressure is a medical condition that requires medication. Let's focus on getting your numbers down.\"
# Patient: \"But I've read about lifestyle changes that might help...\"
# Physician: \"Those aren't as effective as medication. We'll start with a low dose and see how you respond.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Feelings: No exploration of emotional impact",
#           "Ideas of cause: Dismissal of patient's ideas",
#           "Function: No examination of impact on daily life",
#           "Expectations: No exploration of patient's hopes for the encounter",
#           "Incorporation of patient's perspective into the discussion",
#           "Elicitation of patient's healing practices"
#         ],
#         "score": 1,
#         "justification": "The physician completely fails to use the FIFE technique or consider the patient's perspective. They don't inquire about the patient's feelings, ideas about the cause, how it's affecting their function, or their expectations for treatment. When the patient attempts to share their thoughts on potential causes (stress) and treatment options (lifestyle changes), the physician dismisses these ideas without exploration. The focus is entirely on the physician's perspective and their chosen treatment plan, with no attempt to understand or incorporate the patient's beliefs or concerns. This approach, which ignores the patient's perspective entirely and shows no use of the FIFE technique, clearly warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ] 
# """

# PATIENTS_PERSPECTIVE_BELIEFS2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student elicits and addresses the patient's beliefs and perspective on their illness using the FIFE (Feelings, Ideas of cause, Function, and Expectations) technique. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element of FIFE is present or absent:
#    - Feelings: Exploration of the emotional impact of the illness
#    - Ideas of cause: Investigation of patient's beliefs about the cause of their symptoms
#    - Function: Examination of how the illness affects the patient's daily life
#    - Expectations: Exploration of what the patient hopes to gain from the encounter
#    Also note:
#    - Incorporation of patient's perspective into the discussion
#    - Elicitation of patient's healing practices (if applicable)

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Comprehensive use of FIFE technique, addressing all four elements and incorporating findings into discussion
#    - Score 4: Good use of FIFE technique, addressing most elements with some incorporation into discussion
#    - Score 3: Partial use of FIFE technique, addressing some elements with limited incorporation into discussion
#    - Score 2: Minimal use of FIFE technique, addressing few elements with little to no incorporation into discussion
#    - Score 1: No use of FIFE technique or consideration of patient's perspective

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
# Physician: "Before we discuss treatment, I'd like to understand your experience with these symptoms. How have you been feeling emotionally since they started?" (Feelings)
# Patient: "I've been really anxious. It's affecting my mood."
# Physician: "I'm sorry to hear that. It's understandable to feel anxious. What do you think might be causing these symptoms?" (Ideas of cause)
# Patient: "I wonder if it's related to the stress from my new job."
# Physician: "That's an interesting observation. How have these symptoms affected your daily activities and work?" (Function)
# Patient: "I'm having trouble concentrating and I've had to cancel social plans."
# Physician: "I see. That sounds challenging. What are you hoping we can accomplish today?" (Expectations)
# Patient: "I'm hoping to find out what's wrong and get some relief."
# Physician: "Thank you for sharing that. Your perspective is very important. Let's discuss how we can address these symptoms, including looking at stress management techniques, while we investigate potential medical causes. Have you tried any remedies or practices to manage these symptoms?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Feelings: Exploration of emotional impact",
#       "Ideas of cause: Investigation of patient's beliefs about cause",
#       "Function: Examination of impact on daily life",
#       "Expectations: Exploration of patient's hopes for the encounter",
#       "Incorporation of patient's perspective into the discussion",
#       "Elicitation of patient's healing practices"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician demonstrates excellent use of the FIFE technique, addressing all four elements comprehensively. They explore Feelings (\"How have you been feeling emotionally\"), Ideas of cause (\"What do you think might be causing these symptoms?\"), Function (\"How have these symptoms affected your daily activities and work?\"), and Expectations (\"What are you hoping we can accomplish today?\"). The physician also incorporates the patient's perspective into the discussion, as evidenced by their final statement about addressing symptoms and investigating causes while considering stress management. They also inquire about any remedies the patient might have tried. This comprehensive approach to understanding and incorporating the patient's perspective using FIFE warrants a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "I'd like to understand your experience with these symptoms. What do you think might be causing them?" (Ideas of cause)
# Patient: "I've been under a lot of stress lately, so I wonder if that's related."
# Physician: "Stress can certainly affect our health. How have these symptoms been impacting your daily life?" (Function)
# Patient: "It's been hard to focus at work, and I'm not sleeping well."
# Physician: "I see. And how are you feeling about all of this?" (Feelings)
# Patient: "I'm frustrated and a bit scared, to be honest."
# Physician: "Those are understandable feelings. What are you hoping we can accomplish today?" (Expectations)
# Patient: "I'm hoping to get some answers and maybe some relief."
# Physician: "Thank you for sharing that. We'll certainly look into potential causes, including how stress might be playing a role, and discuss ways to help you feel better."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Feelings: Exploration of emotional impact",
#       "Ideas of cause: Investigation of patient's beliefs about cause",
#       "Function: Examination of impact on daily life",
#       "Expectations: Exploration of patient's hopes for the encounter",
#       "Some incorporation of patient's perspective into the discussion"
#     ],
#     "elements_absent": [
#       "Elicitation of patient's healing practices"
#     ],
#     "score": 4,
#     "justification": "The physician demonstrates good use of the FIFE technique, addressing all four elements. They inquire about Ideas of cause, Function, Feelings, and Expectations. The physician also shows some incorporation of the patient's perspective into the discussion, acknowledging the potential role of stress. However, the exploration of each element is not as in-depth as it could be, and they don't inquire about any healing practices the patient might have tried. While the approach is thorough, these minor limitations prevent it from reaching the comprehensive level of a score of 5, thus warranting a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "What do you think might be causing your symptoms?" (Ideas of cause)
# Patient: "I'm not sure, but they started after I began a new job."
# Physician: "Starting a new job can be stressful. How have these symptoms affected your work?" (Function)
# Patient: "It's been difficult to concentrate sometimes."
# Physician: "I see. How are you feeling about all this?" (Feelings)
# Patient: "I'm worried, to be honest."
# Physician: "I understand. Well, let's run some tests to see what might be going on."
# Patient: "Do you think it could be stress-related?"
# Physician: "It's possible. We'll consider that as we investigate."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Ideas of cause: Investigation of patient's beliefs about cause",
#       "Function: Some examination of impact on daily life",
#       "Feelings: Brief exploration of emotional impact"
#     ],
#     "elements_absent": [
#       "Expectations: No exploration of patient's hopes for the encounter",
#       "Thorough incorporation of patient's perspective into the discussion",
#       "Elicitation of patient's healing practices"
#     ],
#     "score": 3,
#     "justification": "The physician makes some effort to use the FIFE technique, addressing Ideas of cause, Function, and briefly touching on Feelings. However, they miss the opportunity to explore the patient's Expectations for the encounter. While the physician acknowledges the possibility of stress playing a role, they don't fully incorporate this into the discussion or explore it further. The conversation lacks depth in addressing the patient's beliefs, and there's no inquiry into any healing practices the patient might have tried. This partial use of the FIFE technique with limited incorporation of the patient's perspective aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "How long have you been experiencing these symptoms?"
# Patient: "About a month now. I'm worried it might be something serious."
# Physician: "I see. And where exactly is the pain located?"
# Patient: "In my lower back, but I've read online it could be related to my diet."
# Physician: "Online information can be misleading. Let's focus on the physical symptoms for now."
# Patient: "Okay, but shouldn't we consider all possibilities?"
# Physician: "We'll run some tests to determine the cause. Try not to worry too much."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Minimal inquiry into patient's concerns"
#     ],
#     "elements_absent": [
#       "Feelings: No exploration of emotional impact",
#       "Ideas of cause: Dismissal of patient's ideas",
#       "Function: No examination of impact on daily life",
#       "Expectations: No exploration of patient's hopes for the encounter",
#       "Incorporation of patient's perspective into the discussion",
#       "Elicitation of patient's healing practices"
#     ],
#     "score": 2,
#     "justification": "The physician shows minimal effort in using the FIFE technique. While they ask about the duration and location of symptoms, they dismiss the patient's attempt to share their ideas about potential causes (\"Online information can be misleading\"). The physician doesn't explore the patient's feelings, the impact on their function, or their expectations for treatment. There's no attempt to incorporate the patient's beliefs into the discussion, and the response to the patient's concern about considering all possibilities is dismissive. This approach, which largely ignores the patient's perspective and fails to use the FIFE technique, warrants a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "Your test results show high blood pressure. We need to start you on medication right away."
# Patient: "I've been under a lot of stress lately. Could that be causing it?"
# Physician: "High blood pressure is a medical condition that requires medication. Let's focus on getting your numbers down."
# Patient: "But I've read about lifestyle changes that might help..."
# Physician: "Those aren't as effective as medication. We'll start with a low dose and see how you respond."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Feelings: No exploration of emotional impact",
#       "Ideas of cause: Dismissal of patient's ideas",
#       "Function: No examination of impact on daily life",
#       "Expectations: No exploration of patient's hopes for the encounter",
#       "Incorporation of patient's perspective into the discussion",
#       "Elicitation of patient's healing practices"
#     ],
#     "score": 1,
#     "justification": "The physician completely fails to use the FIFE technique or consider the patient's perspective. They don't inquire about the patient's feelings, ideas about the cause, how it's affecting their function, or their expectations for treatment. When the patient attempts to share their thoughts on potential causes (stress) and treatment options (lifestyle changes), the physician dismisses these ideas without exploration. The focus is entirely on the physician's perspective and their chosen treatment plan, with no attempt to understand or incorporate the patient's beliefs or concerns. This approach, which ignores the patient's perspective entirely and shows no use of the FIFE technique, clearly warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
