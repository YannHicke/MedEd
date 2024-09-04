PATIENTS_EDUCATION_AND_UNDERSTANDING = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student explores the patient’s education and understanding. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

**Step 1. Scoring:**
   - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
     - **Score 5:** The student uses deliberate techniques to check the patient’s understanding of information given during the interview including diagnosis. If English proficiency is limited, an interpreter is offered. Techniques may include asking the patient to repeat information, asking if the patient has additional questions, posing hypothetical situations, or asking the patient to demonstrate techniques. When patient education is a goal, the student determines the patient’s level of interest and provides education appropriately.
     - **Score 4:** The student makes efforts to ensure comprehension and address patient education, but might miss some opportunities or use less effective methods. The student shows awareness of the importance of patient understanding and education, even if their approach is not as refined or comprehensive as a top performance.
     - **Score 3:** The student asks the patient if they understand the information but does not use a deliberate technique to check. There is some attempt to determine the interest in patient education but could be more thorough.
     - **Score 2:** The student makes limited attempts to check the patient's understanding and does not use any specific techniques to ensure comprehension. Attempts at patient education are minimal or poorly executed. The student shows some awareness of the need to verify understanding and provide education, but struggles to implement effective strategies.
     - **Score 1:** The student fails to assess the patient's level of understanding and does not effectively correct misunderstandings when they are evident, and/or the student fails to address the issue of patient education.

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




# PATIENTS_EDUCATION_AND_UNDERSTANDING_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student educates the patient about their condition and assesses the patient's understanding. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Determination of patient's level of interest in education
#       - Provision of appropriate education
#       - Use of teach-back technique to check understanding
#       - Encouragement of additional questions
#       - Addressing of evident misunderstandings

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Determines interest, provides education, uses teach-back, encourages questions
#     - **Score 4:** Provides education, attempts to check understanding, may lack in one area
#     - **Score 3:** Provides some education, asks if patient understands but doesn't use teach-back
#     - **Score 2:** Gives information but doesn't check understanding
#     - **Score 1:** Fails to educate or check understanding, doesn't address misunderstandings

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"Before we discuss your new medication, I'd like to know how much you already understand about your condition. What do you know about hypertension?\"
# Patient: \"I know it means high blood pressure, but I'm not sure about the details.\"
# Physician: \"Thank you for sharing that. I'll explain more about hypertension and its management. Is that okay with you?\"
# Patient: \"Yes, please.\"
# Physician: [Provides explanation about hypertension and its management]
# Physician: \"Now, to make sure I've explained this clearly, could you tell me in your own words what hypertension is and why it's important to manage it?\"
# Patient: [Provides explanation]
# Physician: \"That's a good understanding. Now, regarding your new medication, it's important to take it regularly. Can you walk me through how and when you plan to take it each day?\"
# Patient: [Describes plan]
# Physician: \"Excellent. One last thing - what would you do if you experience any side effects?\"
# Patient: \"I'm not sure. What should I do?\"
# Physician: \"Good question. If you experience [lists potential side effects], you should [provides instructions]. Can you repeat that back to me?\"
# Patient: [Repeats instructions]
# Physician: \"Perfect. Do you have any other questions about your condition or the medication?\"",
#       "response": {
#         "elements_present": [
#           "Determination of patient's level of interest in education",
#           "Provision of appropriate education",
#           "Use of teach-back technique to check understanding",
#           "Encouragement of additional questions",
#           "Addressing of evident misunderstandings"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician excels in patient education and understanding assessment. They start by determining the patient's current knowledge and interest in learning more (\"What do you know about hypertension?\"). They provide appropriate education and use the teach-back technique multiple times (\"Could you tell me in your own words...\", \"Can you walk me through...\", \"Can you repeat that back to me?\"). The physician also encourages questions and addresses misunderstandings or gaps in knowledge, such as what to do about side effects. This comprehensive approach to education and understanding assessment warrants a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"I'd like to explain your new medication for diabetes. Is that okay with you?\"
# Patient: \"Yes, please.\"
# Physician: [Provides explanation about the medication and its importance]
# Physician: \"Now, can you tell me how you'll take this medication?\"
# Patient: [Provides explanation]
# Physician: \"That's correct. It's also important to monitor your blood sugar. Do you know how to do that?\"
# Patient: \"I'm not entirely sure.\"
# Physician: \"Okay, let me explain the process.\" [Explains blood sugar monitoring]
# Physician: \"Do you have any questions about what we've discussed?\"",
#       "response": {
#         "elements_present": [
#           "Determination of patient's interest in education",
#           "Provision of appropriate education",
#           "Partial use of teach-back technique",
#           "Encouragement of additional questions"
#         ],
#         "elements_absent": [
#           "Consistent use of teach-back for all important information"
#         ],
#         "score": 4,
#         "justification": "The physician does a good job of educating the patient and checking understanding. They ask for permission to explain, provide appropriate information, and use a teach-back technique for medication usage (\"Can you tell me how you'll take this medication?\"). They also identify and address a knowledge gap about blood sugar monitoring. However, they don't use the teach-back method for the blood sugar monitoring explanation, which would have ensured full understanding. The physician encourages questions at the end. This approach is strong but not as comprehensive as a score of 5 would require, thus warranting a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"I'm going to explain your new blood pressure medication. Is that alright?\"
# Patient: \"Yes, go ahead.\"
# Physician: [Provides explanation about the medication]
# Physician: \"Do you understand everything I've told you about the medication?\"
# Patient: \"I think so.\"
# Physician: \"Okay, good. Do you have any questions?\"
# Patient: \"Not right now.\"
# Physician: \"Alright, if you think of any later, feel free to call the office.\"",
#       "response": {
#         "elements_present": [
#           "Determination of patient's interest in education",
#           "Provision of some education",
#           "Asking if patient understands",
#           "Encouragement of additional questions"
#         ],
#         "elements_absent": [
#           "Use of teach-back technique",
#           "Thorough checking of understanding"
#         ],
#         "score": 3,
#         "justification": "The physician provides some patient education and makes an attempt to check understanding. They ask for permission to explain and provide information about the medication. However, their method of checking understanding is superficial, asking \"Do you understand everything I've told you?\" without using a teach-back technique. The physician encourages questions but doesn't probe further when the patient says they have none. This approach shows some effort towards patient education but lacks the depth and thoroughness required for a higher score, aligning with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"You need to start taking this new medication for your cholesterol.\"
# Patient: \"Okay.\"
# Physician: [Provides basic information about dosage and timing]
# Physician: \"It's important to take it regularly. Do you need me to write down the instructions?\"
# Patient: \"No, I think I've got it.\"
# Physician: \"Alright then, let's schedule your next appointment.\"",
#       "response": {
#         "elements_present": [
#           "Provision of basic information"
#         ],
#         "elements_absent": [
#           "Determination of patient's interest in education",
#           "Use of teach-back technique",
#           "Thorough checking of understanding",
#           "Encouragement of additional questions"
#         ],
#         "score": 2,
#         "justification": "The physician provides basic information about the new medication but does not make any real effort to check the patient's understanding. They offer to write down instructions but don't use any teach-back techniques or ask the patient to repeat the information. There's no encouragement for questions or attempt to ensure the patient truly understands the importance of the medication. The quick move to scheduling the next appointment without further discussion indicates a lack of thoroughness in patient education. This minimal approach to education without checking understanding warrants a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Your test results show high cholesterol. You need to start this medication.\"
# Patient: \"What exactly is cholesterol? Is it dangerous?\"
# Physician: \"It can be if it's too high. Just take the medication as prescribed.\"
# Patient: \"But how does the medication work?\"
# Physician: \"It lowers your cholesterol. Take one pill daily. Any other questions?\"
# Patient: \"I'm not sure...\"
# Physician: \"Okay, we're done for today then. The nurse will schedule your next appointment.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Determination of patient's interest in education",
#           "Provision of appropriate education",
#           "Use of teach-back technique",
#           "Encouragement of additional questions",
#           "Addressing of evident misunderstandings"
#         ],
#         "score": 1,
#         "justification": "The physician fails to provide adequate patient education or assess understanding. They ignore the patient's clear request for more information about cholesterol and its dangers, providing only minimal, dismissive responses. When the patient asks about how the medication works, the physician gives a superficial answer without explaining further. There's no attempt to use teach-back techniques or ensure the patient understands the importance of the medication. The physician also fails to address the patient's evident confusion and uncertainty. This complete lack of effective education and disregard for the patient's understanding clearly warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# PATIENTS_EDUCATION_AND_UNDERSTANDING2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student educates the patient about their condition and assesses the patient's understanding. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Determination of patient's level of interest in education
#    - Provision of appropriate education
#    - Use of teach-back technique to check understanding
#    - Encouragement of additional questions
#    - Addressing of evident misunderstandings

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Determines interest, provides education, uses teach-back, encourages questions
#    - Score 4: Provides education, attempts to check understanding, may lack in one area
#    - Score 3: Provides some education, asks if patient understands but doesn't use teach-back
#    - Score 2: Gives information but doesn't check understanding
#    - Score 1: Fails to educate or check understanding, doesn't address misunderstandings

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
# Physician: "Before we discuss your new medication, I'd like to know how much you already understand about your condition. What do you know about hypertension?"
# Patient: "I know it means high blood pressure, but I'm not sure about the details."
# Physician: "Thank you for sharing that. I'll explain more about hypertension and its management. Is that okay with you?"
# Patient: "Yes, please."
# Physician: [Provides explanation about hypertension and its management]
# Physician: "Now, to make sure I've explained this clearly, could you tell me in your own words what hypertension is and why it's important to manage it?"
# Patient: [Provides explanation]
# Physician: "That's a good understanding. Now, regarding your new medication, it's important to take it regularly. Can you walk me through how and when you plan to take it each day?"
# Patient: [Describes plan]
# Physician: "Excellent. One last thing - what would you do if you experience any side effects?"
# Patient: "I'm not sure. What should I do?"
# Physician: "Good question. If you experience [lists potential side effects], you should [provides instructions]. Can you repeat that back to me?"
# Patient: [Repeats instructions]
# Physician: "Perfect. Do you have any other questions about your condition or the medication?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Determination of patient's level of interest in education",
#       "Provision of appropriate education",
#       "Use of teach-back technique to check understanding",
#       "Encouragement of additional questions",
#       "Addressing of evident misunderstandings"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician excels in patient education and understanding assessment. They start by determining the patient's current knowledge and interest in learning more (\"What do you know about hypertension?\"). They provide appropriate education and use the teach-back technique multiple times (\"Could you tell me in your own words...\", \"Can you walk me through...\", \"Can you repeat that back to me?\"). The physician also encourages questions and addresses misunderstandings or gaps in knowledge, such as what to do about side effects. This comprehensive approach to education and understanding assessment warrants a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "I'd like to explain your new medication for diabetes. Is that okay with you?"
# Patient: "Yes, please."
# Physician: [Provides explanation about the medication and its importance]
# Physician: "Now, can you tell me how you'll take this medication?"
# Patient: [Provides explanation]
# Physician: "That's correct. It's also important to monitor your blood sugar. Do you know how to do that?"
# Patient: "I'm not entirely sure."
# Physician: "Okay, let me explain the process." [Explains blood sugar monitoring]
# Physician: "Do you have any questions about what we've discussed?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Determination of patient's interest in education",
#       "Provision of appropriate education",
#       "Partial use of teach-back technique",
#       "Encouragement of additional questions"
#     ],
#     "elements_absent": [
#       "Consistent use of teach-back for all important information"
#     ],
#     "score": 4,
#     "justification": "The physician does a good job of educating the patient and checking understanding. They ask for permission to explain, provide appropriate information, and use a teach-back technique for medication usage (\"Can you tell me how you'll take this medication?\"). They also identify and address a knowledge gap about blood sugar monitoring. However, they don't use the teach-back method for the blood sugar monitoring explanation, which would have ensured full understanding. The physician encourages questions at the end. This approach is strong but not as comprehensive as a score of 5 would require, thus warranting a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "I'm going to explain your new blood pressure medication. Is that alright?"
# Patient: "Yes, go ahead."
# Physician: [Provides explanation about the medication]
# Physician: "Do you understand everything I've told you about the medication?"
# Patient: "I think so."
# Physician: "Okay, good. Do you have any questions?"
# Patient: "Not right now."
# Physician: "Alright, if you think of any later, feel free to call the office."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Determination of patient's interest in education",
#       "Provision of some education",
#       "Asking if patient understands",
#       "Encouragement of additional questions"
#     ],
#     "elements_absent": [
#       "Use of teach-back technique",
#       "Thorough checking of understanding"
#     ],
#     "score": 3,
#     "justification": "The physician provides some patient education and makes an attempt to check understanding. They ask for permission to explain and provide information about the medication. However, their method of checking understanding is superficial, asking \"Do you understand everything I've told you?\" without using a teach-back technique. The physician encourages questions but doesn't probe further when the patient says they have none. This approach shows some effort towards patient education but lacks the depth and thoroughness required for a higher score, aligning with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "You need to start taking this new medication for your cholesterol."
# Patient: "Okay."
# Physician: [Provides basic information about dosage and timing]
# Physician: "It's important to take it regularly. Do you need me to write down the instructions?"
# Patient: "No, I think I've got it."
# Physician: "Alright then, let's schedule your next appointment."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Provision of basic information"
#     ],
#     "elements_absent": [
#       "Determination of patient's interest in education",
#       "Use of teach-back technique",
#       "Thorough checking of understanding",
#       "Encouragement of additional questions"
#     ],
#     "score": 2,
#     "justification": "The physician provides basic information about the new medication but does not make any real effort to check the patient's understanding. They offer to write down instructions but don't use any teach-back techniques or ask the patient to repeat the information. There's no encouragement for questions or attempt to ensure the patient truly understands the importance of the medication. The quick move to scheduling the next appointment without further discussion indicates a lack of thoroughness in patient education. This minimal approach to education without checking understanding warrants a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "Your test results show high cholesterol. You need to start this medication."
# Patient: "What exactly is cholesterol? Is it dangerous?"
# Physician: "It can be if it's too high. Just take the medication as prescribed."
# Patient: "But how does the medication work?"
# Physician: "It lowers your cholesterol. Take one pill daily. Any other questions?"
# Patient: "I'm not sure..."
# Physician: "Okay, we're done for today then. The nurse will schedule your next appointment."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Determination of patient's interest in education",
#       "Provision of appropriate education",
#       "Use of teach-back technique",
#       "Encouragement of additional questions",
#       "Addressing of evident misunderstandings"
#     ],
#     "score": 1,
#     "justification": "The physician fails to provide adequate patient education or assess understanding. They ignore the patient's clear request for more information about cholesterol and its dangers, providing only minimal, dismissive responses. When the patient asks about how the medication works, the physician gives a superficial answer without explaining further. There's no attempt to use teach-back techniques or ensure the patient understands the importance of the medication. The physician also fails to address the patient's evident confusion and uncertainty. This complete lack of effective education and disregard for the patient's understanding clearly warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """