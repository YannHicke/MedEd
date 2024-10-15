SUPPORT_SYSTEMS = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student explores the patient’s support systems. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Understanding the Task:**
    - Read the following note:
      **Note:** Learner should explore the patient’s means of financial, social, and emotional support. Support systems might include other family members, friends, and the patient’s workplace. These are current resources which could be employed immediately. Learners may suggest other community resources including charitable organizations, self-help groups, etc., not yet thought of or known to the patient. 
      **Examples:** “These tests can be expensive; are you concerned about this?” “It sounds like you’ve been through a difficult time. Do you have someone you can talk to?” “Is there anyone that can help with the children until you’re feeling better?” “You told me that you are involved in your church, could they be a source of help?”

  **Step 2. Scoring:**
    - As you read the transcript, and using your understanding from Step 1, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student determines (1) what emotional support the patient has, (2) what financial support the patient has and learns about health care access, (3) other resources available to the patient and family and suggests appropriate community resources. In focused histories (a patient history that concentrates solely on the details surrounding the patient's current chief complaint), one of the three items is sufficient.
      - **Score 4:** The student addresses most aspects of patient support, covering at least two of the three main areas (emotional, financial, and other resources) or one item in a focused history. The exploration may not be as comprehensive as in a score of 5, but there's a clear attempt to understand the patient's support systems.
      - **Score 3:** The student determines some of the available support.
      - **Score 2:** The student makes limited attempts to determine the patient's available support. They may briefly touch on one aspect of support (emotional, financial, or other resources) but fail to explore it thoroughly or miss significant areas. The student shows some awareness of the importance of patient support but struggles to effectively gather comprehensive information or provide relevant suggestions.
      - **Score 1:** The student fails to determine what support is currently available to the patient. 

  **Step 3. Justification:** Based on your analysis in Steps 1 and 2, assign a score using the provided rubric strictly, and explain your reasoning clearly. Your evaluation should be rigorous, impartial, and evidence-based. Directly quote the transcript to support your evaluation.

Provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

{
  "evaluation": {
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the transcript to support your evaluation"
  }
}

Now, please evaluate the following medical interview transcript:
"""




# SUPPORT_SYSTEMS_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student explores the patient's support systems. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether the physician thoroughly explores at least one of these aspects:
#       - Emotional support
#       - Financial support
#       - Access to healthcare
#       - Other relevant support needs

# **2.  Self-Consistency Check:** Ensure your evaluation aligns with the criteria for each score level:
#     - **Score 5:** Thorough exploration of at least one support aspect, with appropriate follow-up or resource suggestions
#     - **Score 4:** Good exploration of at least one support aspect, may lack some depth or follow-up
#     - **Score 3:** Some exploration of a support aspect, but limited in depth or follow-up
#     - **Score 2:** Minimal exploration of support, lacking depth and follow-up
#     - **Score 1:** No meaningful exploration of any support aspect

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"I'd like to understand your support system for managing your diabetes. Who helps you with your day-to-day care?\"
# Patient: \"Well, I live alone, but my daughter visits regularly.\"
# Physician: \"That's good that your daughter is involved. How often does she visit, and what kind of support does she provide?\"
# Patient: \"She comes by twice a week. She helps me organize my medications and sometimes cooks meals.\"
# Physician: \"That's excellent. Is your daughter familiar with your diabetes management needs?\"
# Patient: \"Not really, she's trying to learn but it's all new to her too.\"
# Physician: \"I see. Would you and your daughter be interested in attending a diabetes education session together? We could go over dietary needs, medication management, and signs of complications to watch for.\"
# Patient: \"Yes, I think that would be very helpful.\"
# Physician: \"Great, I'll arrange that for you. I'll also provide information about local diabetes support groups. These groups can offer both emotional support and practical advice from others managing the same condition. They often have resources for family members too. How does that sound?\"
# Patient: \"That sounds really good. I've been feeling a bit overwhelmed, so that extra support would be great.\"
# Physician: \"I'm glad to hear you're open to these resources. Is there anything else you're concerned about regarding your support for managing diabetes?\"",
#       "response": {
#         "elements_present": [
#           "Thorough exploration of emotional and practical support for diabetes management",
#           "Inquiry about family involvement and support",
#           "Offer of educational resources for both patient and family",
#           "Suggestion of community support resources",
#           "Follow-up on patient's feelings and additional concerns"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician thoroughly explores the patient's support system for diabetes management. They inquire about who provides support, the frequency and type of support, and the supporter's knowledge level. The physician then offers concrete resources to enhance this support, including education sessions and support groups. They also follow up on the patient's emotional state and offer an opportunity to express additional concerns. This comprehensive exploration of one support aspect (diabetes management support) with appropriate follow-up and resource suggestions warrants a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"You mentioned you're having trouble affording your medications. Can you tell me more about that?\"
# Patient: \"Yes, with my recent job loss, it's been hard to keep up with the costs.\"
# Physician: \"I'm sorry to hear about your job loss. That must be stressful. Are you aware of any prescription assistance programs or financial support options?\"
# Patient: \"No, I didn't know those existed.\"
# Physician: \"There are several programs that might be able to help. I can give you information about patient assistance programs from pharmaceutical companies and local organizations that offer financial support for medications. Would that be helpful?\"
# Patient: \"Yes, that would be great.\"
# Physician: \"Excellent. I'll get that information for you. In the meantime, have you discussed your situation with your pharmacist? Sometimes they can suggest cheaper alternatives or discount programs.\"
# Patient: \"I haven't, but I'll do that.\"
# Physician: \"Good idea. If you're still having trouble after exploring these options, please let me know, and we can discuss adjusting your treatment plan if necessary.\"",
#       "response": {
#         "elements_present": [
#           "Exploration of financial support for medication",
#           "Acknowledgment of patient's situation",
#           "Offer of information about assistance programs",
#           "Suggestion to explore options with pharmacist",
#           "Openness to adjust treatment plan if needed"
#         ],
#         "elements_absent": [
#           "Detailed discussion of specific programs or immediate action to enroll patient"
#         ],
#         "score": 4,
#         "justification": "The physician does a good job of exploring the patient's financial support needs regarding medication. They inquire about the specific challenge, offer information about assistance programs, and suggest additional resources (pharmacist). The physician also shows willingness to adjust the treatment plan if necessary. However, the exploration could have been more thorough by discussing specific programs or taking immediate action to enroll the patient in assistance programs. This good but not comprehensive exploration of one support aspect (financial support for medications) aligns with a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"Do you have someone who can drive you to your appointments?\"
# Patient: \"Usually my neighbor helps, but she's been busy lately.\"
# Physician: \"I see. Is there anyone else who might be able to assist you?\"
# Patient: \"Not really. I'm worried about making it to all my appointments.\"
# Physician: \"It's important to attend all your scheduled visits. Have you considered using a taxi or ride-sharing service?\"
# Patient: \"I hadn't thought of that. It might be expensive though.\"
# Physician: \"I understand. Well, try to find a reliable way to get here. Let's move on to discussing your treatment plan.\"",
#       "response": {
#         "elements_present": [
#           "Inquiry about transportation support",
#           "Follow-up question about alternative support options",
#           "Suggestion of alternative transportation methods"
#         ],
#         "elements_absent": [
#           "Exploration of financial aspect of transportation",
#           "Offer of resources or assistance for transportation issues",
#           "Addressing patient's expressed worry"
#         ],
#         "score": 3,
#         "justification": "The physician makes some effort to explore the patient's transportation support. They inquire about the current situation and ask about alternatives. However, the exploration is limited in depth. When the patient expresses worry and hints at financial concerns, the physician doesn't delve deeper or offer any resources or assistance. The suggestion to use a taxi or ride-sharing service is not followed up when the patient mentions potential cost issues. This surface-level exploration of one support aspect (transportation) without thorough follow-up or resource offering aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"It's important to have someone help you after the surgery. Do you live with family?\"
# Patient: \"No, I live alone.\"
# Physician: \"Oh, okay. Well, try to arrange for someone to stay with you for a few days after the procedure.\"
# Patient: \"I'm not sure who I can ask. I don't have many people nearby.\"
# Physician: \"I see. Well, it's really important to have support. Let's go over the post-operative instructions now.\"",
#       "response": {
#         "elements_present": [
#           "Minimal inquiry about post-operative support"
#         ],
#         "elements_absent": [
#           "Exploration of patient's support network",
#           "Offer of resources or assistance for post-operative care",
#           "Addressing patient's expressed difficulty in finding support"
#         ],
#         "score": 2,
#         "justification": "The physician shows minimal exploration of the patient's support system. They ask about living with family and mention the need for post-operative support, but when the patient expresses difficulty in arranging this, the physician doesn't explore further or offer any suggestions or resources. The conversation quickly moves on to post-operative instructions without addressing the support issue. This very limited exploration of one support aspect (post-operative care) without any meaningful follow-up or assistance warrants a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Your blood pressure is still high. I'm increasing your medication dosage.\"
# Patient: \"I've been having trouble remembering to take my pills regularly.\"
# Physician: \"It's crucial to take your medication as prescribed. The new dosage should help bring your blood pressure down.\"
# Patient: \"But I'm not sure how to manage this new schedule—\"
# Physician: \"Just make sure to take it every day. Do you have any other questions about the medication itself?\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Exploration of reasons for medication adherence issues",
#           "Inquiry about support for medication management",
#           "Offer of strategies or resources to improve adherence",
#           "Addressing patient's expressed concerns"
#         ],
#         "score": 1,
#         "justification": "The physician completely fails to explore any aspect of the patient's support needs. When the patient mentions having trouble remembering to take medications, which is a clear opportunity to discuss support systems for medication management, the physician ignores this information. There is no attempt to understand why the patient is having difficulties, no exploration of potential support systems, and no offer of strategies or resources to help. The physician's focus on the medication itself, without addressing the adherence issue raised by the patient, demonstrates a total lack of engagement with the patient's support needs. This failure to explore any support aspect, even when directly mentioned by the patient, clearly warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# SUPPORT_SYSTEMS2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student explores the patient's support systems. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether the physician thoroughly explores at least one of these aspects:
#    - Emotional support
#    - Financial support
#    - Access to healthcare
#    - Other relevant support needs

# 2. Self-Consistency Check: Ensure your evaluation aligns with the criteria for each score level:
#    - Score 5: Thorough exploration of at least one support aspect, with appropriate follow-up or resource suggestions
#    - Score 4: Good exploration of at least one support aspect, may lack some depth or follow-up
#    - Score 3: Some exploration of a support aspect, but limited in depth or follow-up
#    - Score 2: Minimal exploration of support, lacking depth and follow-up
#    - Score 1: No meaningful exploration of any support aspect

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
# Physician: "I'd like to understand your support system for managing your diabetes. Who helps you with your day-to-day care?"
# Patient: "Well, I live alone, but my daughter visits regularly."
# Physician: "That's good that your daughter is involved. How often does she visit, and what kind of support does she provide?"
# Patient: "She comes by twice a week. She helps me organize my medications and sometimes cooks meals."
# Physician: "That's excellent. Is your daughter familiar with your diabetes management needs?"
# Patient: "Not really, she's trying to learn but it's all new to her too."
# Physician: "I see. Would you and your daughter be interested in attending a diabetes education session together? We could go over dietary needs, medication management, and signs of complications to watch for."
# Patient: "Yes, I think that would be very helpful."
# Physician: "Great, I'll arrange that for you. I'll also provide information about local diabetes support groups. These groups can offer both emotional support and practical advice from others managing the same condition. They often have resources for family members too. How does that sound?"
# Patient: "That sounds really good. I've been feeling a bit overwhelmed, so that extra support would be great."
# Physician: "I'm glad to hear you're open to these resources. Is there anything else you're concerned about regarding your support for managing diabetes?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Thorough exploration of emotional and practical support for diabetes management",
#       "Inquiry about family involvement and support",
#       "Offer of educational resources for both patient and family",
#       "Suggestion of community support resources",
#       "Follow-up on patient's feelings and additional concerns"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician thoroughly explores the patient's support system for diabetes management. They inquire about who provides support, the frequency and type of support, and the supporter's knowledge level. The physician then offers concrete resources to enhance this support, including education sessions and support groups. They also follow up on the patient's emotional state and offer an opportunity to express additional concerns. This comprehensive exploration of one support aspect (diabetes management support) with appropriate follow-up and resource suggestions warrants a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "You mentioned you're having trouble affording your medications. Can you tell me more about that?"
# Patient: "Yes, with my recent job loss, it's been hard to keep up with the costs."
# Physician: "I'm sorry to hear about your job loss. That must be stressful. Are you aware of any prescription assistance programs or financial support options?"
# Patient: "No, I didn't know those existed."
# Physician: "There are several programs that might be able to help. I can give you information about patient assistance programs from pharmaceutical companies and local organizations that offer financial support for medications. Would that be helpful?"
# Patient: "Yes, that would be great."
# Physician: "Excellent. I'll get that information for you. In the meantime, have you discussed your situation with your pharmacist? Sometimes they can suggest cheaper alternatives or discount programs."
# Patient: "I haven't, but I'll do that."
# Physician: "Good idea. If you're still having trouble after exploring these options, please let me know, and we can discuss adjusting your treatment plan if necessary."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Exploration of financial support for medication",
#       "Acknowledgment of patient's situation",
#       "Offer of information about assistance programs",
#       "Suggestion to explore options with pharmacist",
#       "Openness to adjust treatment plan if needed"
#     ],
#     "elements_absent": [
#       "Detailed discussion of specific programs or immediate action to enroll patient"
#     ],
#     "score": 4,
#     "justification": "The physician does a good job of exploring the patient's financial support needs regarding medication. They inquire about the specific challenge, offer information about assistance programs, and suggest additional resources (pharmacist). The physician also shows willingness to adjust the treatment plan if necessary. However, the exploration could have been more thorough by discussing specific programs or taking immediate action to enroll the patient in assistance programs. This good but not comprehensive exploration of one support aspect (financial support for medications) aligns with a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "Do you have someone who can drive you to your appointments?"
# Patient: "Usually my neighbor helps, but she's been busy lately."
# Physician: "I see. Is there anyone else who might be able to assist you?"
# Patient: "Not really. I'm worried about making it to all my appointments."
# Physician: "It's important to attend all your scheduled visits. Have you considered using a taxi or ride-sharing service?"
# Patient: "I hadn't thought of that. It might be expensive though."
# Physician: "I understand. Well, try to find a reliable way to get here. Let's move on to discussing your treatment plan."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Inquiry about transportation support",
#       "Follow-up question about alternative support options",
#       "Suggestion of alternative transportation methods"
#     ],
#     "elements_absent": [
#       "Exploration of financial aspect of transportation",
#       "Offer of resources or assistance for transportation issues",
#       "Addressing patient's expressed worry"
#     ],
#     "score": 3,
#     "justification": "The physician makes some effort to explore the patient's transportation support. They inquire about the current situation and ask about alternatives. However, the exploration is limited in depth. When the patient expresses worry and hints at financial concerns, the physician doesn't delve deeper or offer any resources or assistance. The suggestion to use a taxi or ride-sharing service is not followed up when the patient mentions potential cost issues. This surface-level exploration of one support aspect (transportation) without thorough follow-up or resource offering aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "It's important to have someone help you after the surgery. Do you live with family?"
# Patient: "No, I live alone."
# Physician: "Oh, okay. Well, try to arrange for someone to stay with you for a few days after the procedure."
# Patient: "I'm not sure who I can ask. I don't have many people nearby."
# Physician: "I see. Well, it's really important to have support. Let's go over the post-operative instructions now."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Minimal inquiry about post-operative support"
#     ],
#     "elements_absent": [
#       "Exploration of patient's support network",
#       "Offer of resources or assistance for post-operative care",
#       "Addressing patient's expressed difficulty in finding support"
#     ],
#     "score": 2,
#     "justification": "The physician shows minimal exploration of the patient's support system. They ask about living with family and mention the need for post-operative support, but when the patient expresses difficulty in arranging this, the physician doesn't explore further or offer any suggestions or resources. The conversation quickly moves on to post-operative instructions without addressing the support issue. This very limited exploration of one support aspect (post-operative care) without any meaningful follow-up or assistance warrants a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "Your blood pressure is still high. I'm increasing your medication dosage."
# Patient: "I've been having trouble remembering to take my pills regularly."
# Physician: "It's crucial to take your medication as prescribed. The new dosage should help bring your blood pressure down."
# Patient: "But I'm not sure how to manage this new schedule—"
# Physician: "Just make sure to take it every day. Do you have any other questions about the medication itself?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Exploration of reasons for medication adherence issues",
#       "Inquiry about support for medication management",
#       "Offer of strategies or resources to improve adherence",
#       "Addressing patient's expressed concerns"
#     ],
#     "score": 1,
#     "justification": "The physician completely fails to explore any aspect of the patient's support needs. When the patient mentions having trouble remembering to take medications, which is a clear opportunity to discuss support systems for medication management, the physician ignores this information. There is no attempt to understand why the patient is having difficulties, no exploration of potential support systems, and no offer of strategies or resources to help. The physician's focus on the medication itself, without addressing the adherence issue raised by the patient, demonstrates a total lack of engagement with the patient's support needs. This failure to explore any support aspect, even when directly mentioned by the patient, clearly warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
