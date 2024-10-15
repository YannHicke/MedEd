ASSESS_MOTIVATION_FOR_CHANGES = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student assesses the patient’s motivation for changes. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Identify Key Elements:**
    - As you read the transcript, create a list noting whether each element is present or absent:
      - Inquiry about patient's feelings towards lifestyle/behavioral change
      - Encouragement of patient 
      - Offering of options or plans tailored to patient

  **Step 2. Scoring:**
    - As you read the transcript, use your list from Step 1 and evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student inquires how the patient feels about the lifestyle/behavioral change and offers options and plans for the patient to choose from to encourage and/or support the change.
      - **Score 4:** The student shows awareness of the importance of patient buy-in and provides some support for change, but may miss opportunities to explore the patient's perspective fully or offer a complete range of options.
      - **Score 3:** The student inquires how the patient feels about changes but does not offer options or plans, or the student assumes the patient will follow the suggested change without assessing the change but does offer options and plans.
      - **Score 2:** The student makes limited attempts to address lifestyle/behavioral changes but does not offer options or plans. 
      - **Score 1:** The student fails to assess the patient’s level of motivation to change and does not offer any options or plans.

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



# ASSESS_MOTIVATION_FOR_CHANGES_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student assesses the patient's motivation for lifestyle or behavioral changes and provides appropriate information and support.
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Inquiry about patient's feelings towards lifestyle/behavioral change
#       - Assessment of patient's readiness to change
#       - Provision of information appropriate to patient's level of readiness
#       - Offering of options or plans tailored to patient's motivation level
#       - Follow-up on patient's expressed concerns or barriers

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Inquires about feelings, assesses readiness, provides appropriate information and support
#     - **Score 4:** Inquires about feelings, attempts to assess readiness, provides some appropriate support
#     - **Score 3:** Inquires about feelings but doesn't follow up appropriately
#     - **Score 2:** Limited inquiry about changes, minimal assessment of motivation or support
#     - **Score 1:** Fails to assess motivation, doesn't offer options, or assumes readiness

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"We've talked about the importance of regular exercise for your heart health. How do you feel about incorporating more physical activity into your daily routine?\"
# Patient: \"I know it's important, but I struggle to find the time with my busy work schedule.\"
# Physician: \"I understand that time can be a big challenge. On a scale of 1 to 10, how important would you say increasing your physical activity is to you right now?\"
# Patient: \"I'd say about a 7. I really do want to improve my health.\"
# Physician: \"That's great that you recognize its importance. Now, on the same scale, how confident are you that you could make some changes if we found ways to work around your schedule?\"
# Patient: \"Maybe a 4 or 5. I'm not sure how to fit it in.\"
# Physician: \"I appreciate your honesty. It sounds like you're motivated but unsure about the practical aspects. Let's brainstorm some small, manageable steps. What are your thoughts on starting with short, 10-minute walks during your lunch break or after dinner?\"
# Patient: \"That actually sounds doable.\"
# Physician: \"Excellent. Small steps can make a big difference. We can start there and gradually increase as you become more comfortable. How does that plan sound to you?\"
# Patient: \"I think I can commit to that.\"
# Physician: \"Great. Let's set a specific goal for the next week and follow up on how it goes. What other support do you think you might need to be successful with this?\"",
#       "response": {
#         "elements_present": [
#           "Inquiry about patient's feelings towards lifestyle change",
#           "Assessment of patient's readiness to change",
#           "Provision of information appropriate to patient's level of readiness",
#           "Offering of options or plans tailored to patient's motivation level",
#           "Follow-up on patient's expressed concerns or barriers"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician excels in assessing and supporting the patient's motivation for change. They begin by inquiring about the patient's feelings towards exercise (\"How do you feel about incorporating more physical activity\"). They use scaling questions to assess both importance and confidence, key components of readiness to change. The physician acknowledges the patient's concerns about time and tailors the suggestion to the patient's current motivation level (\"Let's brainstorm some small, manageable steps\"). They offer a specific, achievable plan and seek the patient's input and commitment. The physician also ensures ongoing support by planning a follow-up and asking about additional support needs. This comprehensive approach to assessing and supporting motivation warrants a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"We've discussed the benefits of quitting smoking for your health. How do you feel about the idea of quitting?\"
# Patient: \"I know I should, but I've tried before and it's really hard.\"
# Physician: \"It can certainly be challenging. What makes you feel it's important to quit?\"
# Patient: \"Well, I want to be healthier and save money.\"
# Physician: \"Those are great reasons. Have you thought about what method you might use to quit?\"
# Patient: \"Not really. I'm not sure what options are out there.\"
# Physician: \"There are several approaches we could consider, such as nicotine replacement therapy or medications. Would you like me to explain some of these options?\"
# Patient: \"Yes, that would be helpful.\"
# Physician: \"Alright, let me go over a few methods and we can discuss which might work best for you.\"",
#       "response": {
#         "elements_present": [
#           "Inquiry about patient's feelings towards lifestyle change",
#           "Some assessment of patient's readiness to change",
#           "Offering of options related to quitting smoking",
#           "Follow-up on patient's expressed challenges"
#         ],
#         "elements_absent": [
#           "Detailed assessment of confidence or readiness to change",
#           "Tailoring of plan to specific motivation level"
#         ],
#         "score": 4,
#         "justification": "The physician does a good job of inquiring about the patient's feelings towards quitting smoking and explores their motivations. They acknowledge the challenge and ask about previous attempts, showing sensitivity to the patient's experience. The physician offers to provide information about quitting methods, which is appropriate given the patient's expressed interest. However, they could have done a more detailed assessment of the patient's readiness to change, perhaps using scaling questions or exploring confidence levels. While they offer options, there's no clear tailoring of the plan to the patient's specific motivation level. This good but not comprehensive approach to assessing and supporting motivation warrants a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"Your cholesterol levels indicate that you should consider changing your diet. How do you feel about making some dietary changes?\"
# Patient: \"I'm not sure. I enjoy my current diet and I'm not confident about making changes.\"
# Physician: \"I understand it can be difficult. A healthier diet is really important for managing your cholesterol. Here's a pamphlet with some dietary guidelines you should follow.\"
# Patient: \"Okay, I'll take a look.\"
# Physician: \"Great. Do you have any questions about the diet?\"",
#       "response": {
#         "elements_present": [
#           "Inquiry about patient's feelings towards lifestyle change",
#           "Acknowledgment of difficulty"
#         ],
#         "elements_absent": [
#           "Assessment of patient's readiness to change",
#           "Provision of information appropriate to patient's level of readiness",
#           "Offering of options or plans tailored to patient's motivation level",
#           "Follow-up on patient's expressed concerns or barriers"
#         ],
#         "score": 3,
#         "justification": "The physician inquires about the patient's feelings towards dietary changes, which is positive. However, they don't follow up appropriately on the patient's expressed lack of confidence and enjoyment of their current diet. Instead of exploring these barriers or assessing readiness to change, the physician simply provides a pamphlet with guidelines. While they acknowledge that change can be difficult, they don't offer any strategies to address the patient's concerns or lack of confidence. The approach lacks tailoring to the patient's current motivation level. This limited follow-up and lack of appropriate response to the patient's expressed feelings align with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"Your blood pressure is still high. You need to reduce your salt intake and exercise more.\"
# Patient: \"I've tried to cut back on salt before, but it's hard.\"
# Physician: \"Well, it's important for your health. Do you think you can make these changes?\"
# Patient: \"I'm not sure.\"
# Physician: \"Just do your best. Here's a list of low-sodium foods you should eat.\"",
#       "response": {
#         "elements_present": [
#           "Limited inquiry about changes"
#         ],
#         "elements_absent": [
#           "Assessment of patient's readiness to change",
#           "Provision of information appropriate to patient's level of readiness",
#           "Offering of options or plans tailored to patient's motivation level",
#           "Follow-up on patient's expressed concerns or barriers"
#         ],
#         "score": 2,
#         "justification": "The physician makes a very limited attempt to assess the patient's motivation for change. They ask if the patient thinks they can make the changes, but don't explore the patient's feelings or readiness in any depth. When the patient expresses uncertainty, the physician doesn't follow up or offer any support or strategies. The advice to \"Just do your best\" doesn't address the patient's expressed difficulty with reducing salt intake. Providing a list of low-sodium foods without discussing how to incorporate these changes or addressing barriers shows a lack of tailoring to the patient's motivation level. This minimal assessment and support for motivation warrants a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"You need to lose weight and exercise more to manage your diabetes.\"
# Patient: \"I've struggled with my weight for years. It's not easy for me.\"
# Physician: \"Well, it's crucial for your health. Just eat less and move more. Do you understand?\"
# Patient: \"I guess so, but—\"
# Physician: \"Good. I'll see you for a follow-up in three months. Try to lose at least 10 pounds by then.\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Inquiry about patient's feelings towards lifestyle change",
#           "Assessment of patient's readiness to change",
#           "Provision of information appropriate to patient's level of readiness",
#           "Offering of options or plans tailored to patient's motivation level",
#           "Follow-up on patient's expressed concerns or barriers"
#         ],
#         "score": 1,
#         "justification": "The physician completely fails to assess the patient's motivation or readiness for change. They simply dictate what the patient needs to do without inquiring about the patient's feelings or past experiences. When the patient expresses that weight loss has been a struggle, the physician dismisses this concern with a simplistic \"Just eat less and move more\" advice. There's no attempt to understand the patient's barriers, assess their readiness, or offer tailored support or options. The physician assumes the patient's readiness for change and sets an arbitrary goal without discussing its feasibility. This complete lack of motivation assessment and support clearly warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# ASSESS_MOTIVATION_FOR_CHANGES2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student assesses the patient's motivation for lifestyle or behavioral changes and provides appropriate information and support. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Inquiry about patient's feelings towards lifestyle/behavioral change
#    - Assessment of patient's readiness to change
#    - Provision of information appropriate to patient's level of readiness
#    - Offering of options or plans tailored to patient's motivation level
#    - Follow-up on patient's expressed concerns or barriers

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Inquires about feelings, assesses readiness, provides appropriate information and support
#    - Score 4: Inquires about feelings, attempts to assess readiness, provides some appropriate support
#    - Score 3: Inquires about feelings but doesn't follow up appropriately
#    - Score 2: Limited inquiry about changes, minimal assessment of motivation or support
#    - Score 1: Fails to assess motivation, doesn't offer options, or assumes readiness

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
# Physician: "We've talked about the importance of regular exercise for your heart health. How do you feel about incorporating more physical activity into your daily routine?"
# Patient: "I know it's important, but I struggle to find the time with my busy work schedule."
# Physician: "I understand that time can be a big challenge. On a scale of 1 to 10, how important would you say increasing your physical activity is to you right now?"
# Patient: "I'd say about a 7. I really do want to improve my health."
# Physician: "That's great that you recognize its importance. Now, on the same scale, how confident are you that you could make some changes if we found ways to work around your schedule?"
# Patient: "Maybe a 4 or 5. I'm not sure how to fit it in."
# Physician: "I appreciate your honesty. It sounds like you're motivated but unsure about the practical aspects. Let's brainstorm some small, manageable steps. What are your thoughts on starting with short, 10-minute walks during your lunch break or after dinner?"
# Patient: "That actually sounds doable."
# Physician: "Excellent. Small steps can make a big difference. We can start there and gradually increase as you become more comfortable. How does that plan sound to you?"
# Patient: "I think I can commit to that."
# Physician: "Great. Let's set a specific goal for the next week and follow up on how it goes. What other support do you think you might need to be successful with this?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Inquiry about patient's feelings towards lifestyle change",
#       "Assessment of patient's readiness to change",
#       "Provision of information appropriate to patient's level of readiness",
#       "Offering of options or plans tailored to patient's motivation level",
#       "Follow-up on patient's expressed concerns or barriers"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician excels in assessing and supporting the patient's motivation for change. They begin by inquiring about the patient's feelings towards exercise (\"How do you feel about incorporating more physical activity\"). They use scaling questions to assess both importance and confidence, key components of readiness to change. The physician acknowledges the patient's concerns about time and tailors the suggestion to the patient's current motivation level (\"Let's brainstorm some small, manageable steps\"). They offer a specific, achievable plan and seek the patient's input and commitment. The physician also ensures ongoing support by planning a follow-up and asking about additional support needs. This comprehensive approach to assessing and supporting motivation warrants a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "We've discussed the benefits of quitting smoking for your health. How do you feel about the idea of quitting?"
# Patient: "I know I should, but I've tried before and it's really hard."
# Physician: "It can certainly be challenging. What makes you feel it's important to quit?"
# Patient: "Well, I want to be healthier and save money."
# Physician: "Those are great reasons. Have you thought about what method you might use to quit?"
# Patient: "Not really. I'm not sure what options are out there."
# Physician: "There are several approaches we could consider, such as nicotine replacement therapy or medications. Would you like me to explain some of these options?"
# Patient: "Yes, that would be helpful."
# Physician: "Alright, let me go over a few methods and we can discuss which might work best for you."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Inquiry about patient's feelings towards lifestyle change",
#       "Some assessment of patient's readiness to change",
#       "Offering of options related to quitting smoking",
#       "Follow-up on patient's expressed challenges"
#     ],
#     "elements_absent": [
#       "Detailed assessment of confidence or readiness to change",
#       "Tailoring of plan to specific motivation level"
#     ],
#     "score": 4,
#     "justification": "The physician does a good job of inquiring about the patient's feelings towards quitting smoking and explores their motivations. They acknowledge the challenge and ask about previous attempts, showing sensitivity to the patient's experience. The physician offers to provide information about quitting methods, which is appropriate given the patient's expressed interest. However, they could have done a more detailed assessment of the patient's readiness to change, perhaps using scaling questions or exploring confidence levels. While they offer options, there's no clear tailoring of the plan to the patient's specific motivation level. This good but not comprehensive approach to assessing and supporting motivation warrants a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "Your cholesterol levels indicate that you should consider changing your diet. How do you feel about making some dietary changes?"
# Patient: "I'm not sure. I enjoy my current diet and I'm not confident about making changes."
# Physician: "I understand it can be difficult. A healthier diet is really important for managing your cholesterol. Here's a pamphlet with some dietary guidelines you should follow."
# Patient: "Okay, I'll take a look."
# Physician: "Great. Do you have any questions about the diet?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Inquiry about patient's feelings towards lifestyle change",
#       "Acknowledgment of difficulty"
#     ],
#     "elements_absent": [
#       "Assessment of patient's readiness to change",
#       "Provision of information appropriate to patient's level of readiness",
#       "Offering of options or plans tailored to patient's motivation level",
#       "Follow-up on patient's expressed concerns or barriers"
#     ],
#     "score": 3,
#     "justification": "The physician inquires about the patient's feelings towards dietary changes, which is positive. However, they don't follow up appropriately on the patient's expressed lack of confidence and enjoyment of their current diet. Instead of exploring these barriers or assessing readiness to change, the physician simply provides a pamphlet with guidelines. While they acknowledge that change can be difficult, they don't offer any strategies to address the patient's concerns or lack of confidence. The approach lacks tailoring to the patient's current motivation level. This limited follow-up and lack of appropriate response to the patient's expressed feelings align with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "Your blood pressure is still high. You need to reduce your salt intake and exercise more."
# Patient: "I've tried to cut back on salt before, but it's hard."
# Physician: "Well, it's important for your health. Do you think you can make these changes?"
# Patient: "I'm not sure."
# Physician: "Just do your best. Here's a list of low-sodium foods you should eat."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Limited inquiry about changes"
#     ],
#     "elements_absent": [
#       "Assessment of patient's readiness to change",
#       "Provision of information appropriate to patient's level of readiness",
#       "Offering of options or plans tailored to patient's motivation level",
#       "Follow-up on patient's expressed concerns or barriers"
#     ],
#     "score": 2,
#     "justification": "The physician makes a very limited attempt to assess the patient's motivation for change. They ask if the patient thinks they can make the changes, but don't explore the patient's feelings or readiness in any depth. When the patient expresses uncertainty, the physician doesn't follow up or offer any support or strategies. The advice to \"Just do your best\" doesn't address the patient's expressed difficulty with reducing salt intake. Providing a list of low-sodium foods without discussing how to incorporate these changes or addressing barriers shows a lack of tailoring to the patient's motivation level. This minimal assessment and support for motivation warrants a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "You need to lose weight and exercise more to manage your diabetes."
# Patient: "I've struggled with my weight for years. It's not easy for me."
# Physician: "Well, it's crucial for your health. Just eat less and move more. Do you understand?"
# Patient: "I guess so, but—"
# Physician: "Good. I'll see you for a follow-up in three months. Try to lose at least 10 pounds by then."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Inquiry about patient's feelings towards lifestyle change",
#       "Assessment of patient's readiness to change",
#       "Provision of information appropriate to patient's level of readiness",
#       "Offering of options or plans tailored to patient's motivation level",
#       "Follow-up on patient's expressed concerns or barriers"
#     ],
#     "score": 1,
#     "justification": "The physician completely fails to assess the patient's motivation or readiness for change. They simply dictate what the patient needs to do without inquiring about the patient's feelings or past experiences. When the patient expresses that weight loss has been a struggle, the physician dismisses this concern with a simplistic \"Just eat less and move more\" advice. There's no attempt to understand the patient's barriers, assess their readiness, or offer tailored support or options. The physician assumes the patient's readiness for change and sets an arbitrary goal without discussing its feasibility. This complete lack of motivation assessment and support clearly warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
