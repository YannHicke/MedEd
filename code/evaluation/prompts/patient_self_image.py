IMPACT_OF_ILLNESS_ON_PATIENT_AND_PATIENT_SELF_IMAGE = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student explores and addresses the impact of the illness on the patient and their self-image. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

**Step 1. Scoring:**
   - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
     - **Score 5:** The student inquires about the patient’s feelings about their illness and how it has changed their life. The student explores these issues. The student offers counseling or resources to help. 
     - **Score 4:** The student inquires about the patient's feelings regarding their illness and its impact on their life, but the exploration may not be as thorough as in a score of 5. Some counseling or resources are offered, but they might be less comprehensive or tailored. The student shows a clear attempt to address the patient’s feelings about their illness, even if not as deeply or effectively as in a top performance.
     - **Score 3:** The student partially addresses the impact of the illness on the patient’s life or self-image and/or offers no counseling or resources to help.
     - **Score 2:** The student makes limited attempts to address the impact of the illness on the patient's life or self-image. No counseling or resources are offered. The student shows some awareness of the importance of these issues but struggles to effectively address them or draw out the patient's feelings.
     - **Score 1:** The student fails to acknowledge any impact of the illness on the patient’s life or self-image.

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



# IMPACT_OF_ILLNESS_ON_PATIENT_AND_PATIENT_SELF_IMAGE_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student explores and addresses the impact of the illness on the patient's life and self-image. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Inquiry about patient's feelings regarding the illness
#       - Exploration of how the illness has changed the patient's life
#       - Discussion of impact on patient's self-image
#       - Offer of counseling or resources to help (for communication cases)
#       - Demonstration of empathy and understanding

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** Comprehensive exploration of illness impact on life and self-image, with offer of support resources
#     - **Score 4:** Good exploration of illness impact, may lack depth in some areas or offer of resources
#     - **Score 3:** Partial address of illness impact on life or self-image, limited or no offer of resources
#     - **Score 2:** Minimal acknowledgment of illness impact, no exploration or offer of support
#     - **Score 1:** No acknowledgment of illness impact on patient's life or self-image

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"I'd like to understand how this diagnosis has been affecting you. How has it impacted your daily life and the way you see yourself?\"
# Patient: \"It's been really tough. I feel like I can't do the things I used to, and sometimes I don't even recognize myself anymore.\"
# Physician: \"I can only imagine how challenging this must be for you. Many patients experience similar feelings. Can you tell me more about the specific activities that have been affected?\"
# Patient: \"Well, I used to love playing tennis with friends, but now I get tired so quickly. And at work, I worry that I'm not performing as well as I used to.\"
# Physician: \"Thank you for sharing that. It's clear this illness has had a significant impact on various aspects of your life. How are you coping with these changes emotionally?\"
# Patient: \"Some days are better than others, but often I feel frustrated and a bit depressed.\"
# Physician: \"It's completely normal to have those feelings. I want you to know that we have resources available to help you navigate these challenges. We have a support group for patients with similar experiences, and I can also refer you to a counselor who specializes in helping people adjust to chronic illnesses. Would you be interested in exploring these options?\"
# Patient: \"Yes, I think that might be helpful.\"
# Physician: \"Excellent. We'll work together to not only manage your physical symptoms but also to help you adjust to these life changes and maintain a positive self-image. Remember, you're more than your illness.\"",
#       "response": {
#         "elements_present": [
#           "Inquiry about patient's feelings regarding the illness",
#           "Exploration of how the illness has changed the patient's life",
#           "Discussion of impact on patient's self-image",
#           "Offer of counseling or resources to help",
#           "Demonstration of empathy and understanding"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician demonstrates excellent skills in exploring the impact of the illness on the patient's life and self-image. They inquire about the patient's feelings and how the illness has affected daily activities (\"How has it impacted your daily life and the way you see yourself?\"). The physician shows empathy (\"I can only imagine how challenging this must be for you\") and explores specific impacts on work and hobbies. They address the emotional aspect (\"How are you coping with these changes emotionally?\") and offer concrete support resources, including a support group and counselor referral. The physician's final statement acknowledges the whole person beyond the illness. This comprehensive approach, combining exploration, empathy, and practical support, warrants a score of 5."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"How has this diagnosis been affecting your daily life?\"
# Patient: \"It's been difficult. I can't do many things I used to enjoy.\"
# Physician: \"I'm sorry to hear that. Can you give me an example of something you can't do anymore?\"
# Patient: \"I used to go hiking every weekend, but now I get too tired.\"
# Physician: \"That must be frustrating for you. How has this change impacted how you feel about yourself?\"
# Patient: \"I feel like I'm not the same person anymore. Sometimes I get pretty down about it.\"
# Physician: \"It's understandable to feel that way. Many patients struggle with these kinds of changes. Have you considered talking to someone about these feelings?\"
# Patient: \"I hadn't really thought about it.\"
# Physician: \"It might be helpful. I can provide you with some information about support services if you're interested.\"
# Patient: \"Okay, thanks.\"",
#       "response": {
#         "elements_present": [
#           "Inquiry about patient's feelings regarding the illness",
#           "Exploration of how the illness has changed the patient's life",
#           "Some discussion of impact on patient's self-image",
#           "Mention of support services",
#           "Some demonstration of empathy and understanding"
#         ],
#         "elements_absent": [
#           "Detailed offer of specific counseling or resources"
#         ],
#         "score": 4,
#         "justification": "The physician shows good skills in exploring the impact of the illness on the patient's life and self-image. They inquire about daily life impacts (\"How has this diagnosis been affecting your daily life?\") and follow up with a request for specific examples. The physician also addresses the impact on self-image (\"How has this change impacted how you feel about yourself?\") and shows empathy (\"That must be frustrating for you\"). While they mention the possibility of support services, they don't offer specific resources or strongly encourage their use. This good but not comprehensive approach to exploring illness impact and offering support warrants a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"Has your condition affected your daily routine?\"
# Patient: \"Yes, quite a bit actually. I'm having trouble at work and at home.\"
# Physician: \"I see. It's important to try to maintain your normal activities as much as possible.\"
# Patient: \"I'm trying, but it's not easy. I feel like a different person sometimes.\"
# Physician: \"Many patients feel that way. Try to stay positive. Now, let's discuss your treatment plan.\"",
#       "response": {
#         "elements_present": [
#           "Some inquiry about illness impact on daily life",
#           "Brief acknowledgment of emotional impact"
#         ],
#         "elements_absent": [
#           "Detailed exploration of how the illness has changed the patient's life",
#           "In-depth discussion of impact on patient's self-image",
#           "Offer of counseling or resources to help",
#           "Strong demonstration of empathy and understanding"
#         ],
#         "score": 3,
#         "justification": "The physician partially addresses the impact of the illness on the patient's life by asking about effects on daily routine. However, they don't explore this in depth or follow up on the patient's mention of trouble at work and home. When the patient expresses feeling like a different person, the physician acknowledges this briefly (\"Many patients feel that way\") but doesn't explore the impact on self-image further. The advice to \"stay positive\" is given without offering any concrete support or resources. This partial address of the illness's impact without thorough exploration or offer of help aligns with a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"How often are you experiencing symptoms?\"
# Patient: \"Almost daily now. It's really affecting my life.\"
# Physician: \"Daily symptoms are concerning. We should adjust your medication.\"
# Patient: \"I'm worried about how this is changing me as a person.\"
# Physician: \"Let's focus on managing your physical symptoms for now. Have you been taking your medication as prescribed?\"",
#       "response": {
#         "elements_present": [
#           "Minimal acknowledgment of illness impact"
#         ],
#         "elements_absent": [
#           "Exploration of how the illness has changed the patient's life",
#           "Discussion of impact on patient's self-image",
#           "Inquiry about patient's feelings regarding the illness",
#           "Offer of counseling or resources to help",
#           "Demonstration of empathy and understanding"
#         ],
#         "score": 2,
#         "justification": "The physician shows minimal acknowledgment of the illness's impact on the patient's life. When the patient mentions that the condition is \"really affecting my life,\" the physician focuses solely on the physical symptoms without exploring the broader life impact. Even when the patient explicitly expresses worry about personal changes, the physician redirects to medication management, missing a clear opportunity to discuss the illness's impact on self-image. There is no offer of support resources or demonstration of empathy regarding the patient's concerns. This minimal acknowledgment without any real exploration or support warrants a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Your test results show that your condition has progressed. We need to start a new treatment regimen immediately.\"
# Patient: \"I'm feeling overwhelmed by all of this. It's really changing my life.\"
# Physician: \"The most important thing is to control the progression of the disease. Let's schedule your first treatment for next week.\"
# Patient: \"But how am I supposed to cope with all these changes?\"
# Physician: \"Just try to maintain a positive attitude. Now, about the treatment schedule...\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Inquiry about patient's feelings regarding the illness",
#           "Exploration of how the illness has changed the patient's life",
#           "Discussion of impact on patient's self-image",
#           "Offer of counseling or resources to help",
#           "Demonstration of empathy and understanding"
#         ],
#         "score": 1,
#         "justification": "The physician completely fails to acknowledge or explore the impact of the illness on the patient's life or self-image. When the patient expresses feeling overwhelmed and mentions life changes, the physician ignores these concerns, focusing solely on disease control and treatment scheduling. The patient's direct question about coping is dismissed with a platitude about maintaining a positive attitude, without any offer of support or resources. There is no demonstration of empathy or attempt to understand the patient's emotional state. This total lack of acknowledgment of the illness's impact on the patient's life and self-image clearly warrants a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]
# """

# IMPACT_OF_ILLNESS_ON_PATIENT_AND_PATIENT_SELF_IMAGE2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student explores and addresses the impact of the illness on the patient's life and self-image. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Inquiry about patient's feelings regarding the illness
#    - Exploration of how the illness has changed the patient's life
#    - Discussion of impact on patient's self-image
#    - Offer of counseling or resources to help (for communication cases)
#    - Demonstration of empathy and understanding

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: Comprehensive exploration of illness impact on life and self-image, with offer of support resources
#    - Score 4: Good exploration of illness impact, may lack depth in some areas or offer of resources
#    - Score 3: Partial address of illness impact on life or self-image, limited or no offer of resources
#    - Score 2: Minimal acknowledgment of illness impact, no exploration or offer of support
#    - Score 1: No acknowledgment of illness impact on patient's life or self-image

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
# Physician: "I'd like to understand how this diagnosis has been affecting you. How has it impacted your daily life and the way you see yourself?"
# Patient: "It's been really tough. I feel like I can't do the things I used to, and sometimes I don't even recognize myself anymore."
# Physician: "I can only imagine how challenging this must be for you. Many patients experience similar feelings. Can you tell me more about the specific activities that have been affected?"
# Patient: "Well, I used to love playing tennis with friends, but now I get tired so quickly. And at work, I worry that I'm not performing as well as I used to."
# Physician: "Thank you for sharing that. It's clear this illness has had a significant impact on various aspects of your life. How are you coping with these changes emotionally?"
# Patient: "Some days are better than others, but often I feel frustrated and a bit depressed."
# Physician: "It's completely normal to have those feelings. I want you to know that we have resources available to help you navigate these challenges. We have a support group for patients with similar experiences, and I can also refer you to a counselor who specializes in helping people adjust to chronic illnesses. Would you be interested in exploring these options?"
# Patient: "Yes, I think that might be helpful."
# Physician: "Excellent. We'll work together to not only manage your physical symptoms but also to help you adjust to these life changes and maintain a positive self-image. Remember, you're more than your illness."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Inquiry about patient's feelings regarding the illness",
#       "Exploration of how the illness has changed the patient's life",
#       "Discussion of impact on patient's self-image",
#       "Offer of counseling or resources to help",
#       "Demonstration of empathy and understanding"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician demonstrates excellent skills in exploring the impact of the illness on the patient's life and self-image. They inquire about the patient's feelings and how the illness has affected daily activities (\"How has it impacted your daily life and the way you see yourself?\"). The physician shows empathy (\"I can only imagine how challenging this must be for you\") and explores specific impacts on work and hobbies. They address the emotional aspect (\"How are you coping with these changes emotionally?\") and offer concrete support resources, including a support group and counselor referral. The physician's final statement acknowledges the whole person beyond the illness. This comprehensive approach, combining exploration, empathy, and practical support, warrants a score of 5."
#   }
# }

# Example 2:
# Input: 
# Physician: "How has this diagnosis been affecting your daily life?"
# Patient: "It's been difficult. I can't do many things I used to enjoy."
# Physician: "I'm sorry to hear that. Can you give me an example of something you can't do anymore?"
# Patient: "I used to go hiking every weekend, but now I get too tired."
# Physician: "That must be frustrating for you. How has this change impacted how you feel about yourself?"
# Patient: "I feel like I'm not the same person anymore. Sometimes I get pretty down about it."
# Physician: "It's understandable to feel that way. Many patients struggle with these kinds of changes. Have you considered talking to someone about these feelings?"
# Patient: "I hadn't really thought about it."
# Physician: "It might be helpful. I can provide you with some information about support services if you're interested."
# Patient: "Okay, thanks."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Inquiry about patient's feelings regarding the illness",
#       "Exploration of how the illness has changed the patient's life",
#       "Some discussion of impact on patient's self-image",
#       "Mention of support services",
#       "Some demonstration of empathy and understanding"
#     ],
#     "elements_absent": [
#       "Detailed offer of specific counseling or resources"
#     ],
#     "score": 4,
#     "justification": "The physician shows good skills in exploring the impact of the illness on the patient's life and self-image. They inquire about daily life impacts (\"How has this diagnosis been affecting your daily life?\") and follow up with a request for specific examples. The physician also addresses the impact on self-image (\"How has this change impacted how you feel about yourself?\") and shows empathy (\"That must be frustrating for you\"). While they mention the possibility of support services, they don't offer specific resources or strongly encourage their use. This good but not comprehensive approach to exploring illness impact and offering support warrants a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "Has your condition affected your daily routine?"
# Patient: "Yes, quite a bit actually. I'm having trouble at work and at home."
# Physician: "I see. It's important to try to maintain your normal activities as much as possible."
# Patient: "I'm trying, but it's not easy. I feel like a different person sometimes."
# Physician: "Many patients feel that way. Try to stay positive. Now, let's discuss your treatment plan."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Some inquiry about illness impact on daily life",
#       "Brief acknowledgment of emotional impact"
#     ],
#     "elements_absent": [
#       "Detailed exploration of how the illness has changed the patient's life",
#       "In-depth discussion of impact on patient's self-image",
#       "Offer of counseling or resources to help",
#       "Strong demonstration of empathy and understanding"
#     ],
#     "score": 3,
#     "justification": "The physician partially addresses the impact of the illness on the patient's life by asking about effects on daily routine. However, they don't explore this in depth or follow up on the patient's mention of trouble at work and home. When the patient expresses feeling like a different person, the physician acknowledges this briefly (\"Many patients feel that way\") but doesn't explore the impact on self-image further. The advice to \"stay positive\" is given without offering any concrete support or resources. This partial address of the illness's impact without thorough exploration or offer of help aligns with a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "How often are you experiencing symptoms?"
# Patient: "Almost daily now. It's really affecting my life."
# Physician: "Daily symptoms are concerning. We should adjust your medication."
# Patient: "I'm worried about how this is changing me as a person."
# Physician: "Let's focus on managing your physical symptoms for now. Have you been taking your medication as prescribed?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Minimal acknowledgment of illness impact"
#     ],
#     "elements_absent": [
#       "Exploration of how the illness has changed the patient's life",
#       "Discussion of impact on patient's self-image",
#       "Inquiry about patient's feelings regarding the illness",
#       "Offer of counseling or resources to help",
#       "Demonstration of empathy and understanding"
#     ],
#     "score": 2,
#     "justification": "The physician shows minimal acknowledgment of the illness's impact on the patient's life. When the patient mentions that the condition is \"really affecting my life,\" the physician focuses solely on the physical symptoms without exploring the broader life impact. Even when the patient explicitly expresses worry about personal changes, the physician redirects to medication management, missing a clear opportunity to discuss the illness's impact on self-image. There is no offer of support resources or demonstration of empathy regarding the patient's concerns. This minimal acknowledgment without any real exploration or support warrants a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "Your test results show that your condition has progressed. We need to start a new treatment regimen immediately."
# Patient: "I'm feeling overwhelmed by all of this. It's really changing my life."
# Physician: "The most important thing is to control the progression of the disease. Let's schedule your first treatment for next week."
# Patient: "But how am I supposed to cope with all these changes?"
# Physician: "Just try to maintain a positive attitude. Now, about the treatment schedule..."

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Inquiry about patient's feelings regarding the illness",
#       "Exploration of how the illness has changed the patient's life",
#       "Discussion of impact on patient's self-image",
#       "Offer of counseling or resources to help",
#       "Demonstration of empathy and understanding"
#     ],
#     "score": 1,
#     "justification": "The physician completely fails to acknowledge or explore the impact of the illness on the patient's life or self-image. When the patient expresses feeling overwhelmed and mentions life changes, the physician ignores these concerns, focusing solely on disease control and treatment scheduling. The patient's direct question about coping is dismissed with a platitude about maintaining a positive attitude, without any offer of support or resources. There is no demonstration of empathy or attempt to understand the patient's emotional state. This total lack of acknowledgment of the illness's impact on the patient's life and self-image clearly warrants a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """
