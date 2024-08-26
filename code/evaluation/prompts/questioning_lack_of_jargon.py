QUESTIONING_SKILLS_LACK_OF_JARGON = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
You will be evaluating how well the medical student avoids using medical jargon and communicates clearly with the patient. 
To ensure a thorough evaluation, follow these steps:

**1. Identify Key Elements:**
   -  As you read the excerpt, create a list noting whether each element is present or absent:
      - Use of patient-friendly language
      - Avoidance of medical jargon
      - Immediate explanation of medical terms when used
      - Clear communication of medical concepts

**2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
    - **Score 5:** Consistent use of easily understood language, avoidance of jargon, or immediate explanation of terms
    - **Score 3:** Occasional use of medical terms without definition, clarified upon patient request
    - **Score 1:** Frequent use of unexplained medical jargon, making conversation inaccessible to the patient

**3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

  "examples": [
    {
      "score": 5,
      "excerpt": "Physician: \"Can you tell me more about the pain you're experiencing in your stomach?\"
Patient: \"It's a burning sensation, right here in the middle of my upper belly.\"
Physician: \"I see. What you're describing sounds like it could be related to stomach acid. Sometimes, when stomach acid moves up into the food pipe - that's the tube that connects your mouth to your stomach - it can cause a burning feeling. This is often called heartburn or acid reflux. Have you ever heard of these terms?\"
Patient: \"Yes, I've heard of heartburn before.\"
Physician: \"Great. Now, does this pain get worse after eating certain foods or when you lie down?\"
Patient: \"Yes, especially after spicy meals and when I go to bed.\"
Physician: \"That's helpful information. These symptoms are common with a condition called acid reflux. It's when the muscle at the bottom of your food pipe doesn't close properly, allowing stomach acid to flow back up. Does this explanation make sense to you?\"
Patient: \"Yes, it does. Thank you for explaining it so clearly.\"",
      "response": {
        "elements_present": [
          "Use of patient-friendly language",
          "Avoidance of medical jargon",
          "Immediate explanation of medical terms when used",
          "Clear communication of medical concepts"
        ],
        "elements_absent": [],
        "score": 5,
        "justification": "The physician consistently uses patient-friendly language and avoids medical jargon throughout the conversation. When introducing medical concepts, they provide immediate, clear explanations. For example, they describe the esophagus as \"the tube that connects your mouth to your stomach\" and explain acid reflux as \"when stomach acid moves up into the food pipe\". They also check for patient understanding, asking \"Have you ever heard of these terms?\" and \"Does this explanation make sense to you?\". This approach ensures clear communication and patient comprehension, warranting a score of 5."
      }
    },
    {
      "score": 3,
      "excerpt": "Physician: \"Based on your symptoms, it sounds like you might have gastritis.\"
Patient: \"Gastritis? What's that?\"
Physician: \"Oh, I'm sorry. Gastritis is inflammation of the stomach lining. It can cause pain and discomfort in your upper abdomen. Have you been experiencing any nausea or vomiting?\"
Patient: \"Yes, I've felt nauseous, especially in the mornings.\"
Physician: \"I see. And have you noticed any changes in your bowel movements?\"
Patient: \"What do you mean by that?\"
Physician: \"I'm asking if you've had any diarrhea or constipation, or if your stools look different than usual.\"
Patient: \"Oh, I see. No, everything seems normal in that regard.\"
Physician: \"Alright. Now, I'd like to perform a physical examination to check for any abdominal tenderness.\"",
      "response": {
        "elements_present": [
          "Some use of patient-friendly language",
          "Clarification of terms upon patient request"
        ],
        "elements_absent": [
          "Consistent avoidance of medical jargon",
          "Immediate explanation of all medical terms used"
        ],
        "score": 3,
        "justification": "The physician occasionally uses medical terms without immediate definition, such as \"gastritis\" and \"bowel movements\". However, they do provide explanations when the patient asks for clarification. For instance, when the patient questions the term \"gastritis\", the physician explains it as \"inflammation of the stomach lining\". Similarly, they clarify \"bowel movements\" when the patient seems confused. While the physician does use some patient-friendly language, the initial use of unexplained terms and the need for patient-prompted clarifications align with a score of 3."
      }
    },
    {
      "score": 1,
      "excerpt": "Physician: \"Your symptoms suggest possible cholecystitis with concomitant cholelithiasis.\"
Patient: \"I'm sorry, I don't understand what you're saying.\"
Physician: \"Ah, well, cholecystitis is inflammation of the gallbladder, often caused by cholelithiasis, which are gallstones. Have you been experiencing any epigastric pain radiating to your right upper quadrant?\"
Patient: \"I'm not sure what you mean by epigastric or right upper quadrant.\"
Physician: \"Right, epigastric refers to the area right below your sternum, and the right upper quadrant is the upper right part of your abdomen. We'll need to do an ultrasound to confirm the diagnosis and rule out any hepatic involvement.\"
Patient: \"I'm feeling quite lost with all these terms. Can you explain in simpler words?\"
Physician: \"Of course, my apologies. We think there might be a problem with your gallbladder, possibly stones. We need to do a special scan to check it out.\"",
      "response": {
        "elements_present": [],
        "elements_absent": [
          "Use of patient-friendly language",
          "Avoidance of medical jargon",
          "Immediate explanation of medical terms when used",
          "Clear communication of medical concepts"
        ],
        "score": 1,
        "justification": "The physician's conversation is dominated by medical jargon, making it largely inaccessible to the patient. They begin with complex terms like \"cholecystitis\" and \"cholelithiasis\" without providing immediate explanations. Even when attempting to clarify, they introduce more jargon such as \"epigastric pain\" and \"right upper quadrant\". The patient's repeated requests for clarification demonstrate their struggle to understand. While the physician eventually provides a simplified explanation, it comes only after multiple instances of confusion. This excessive use of unexplained medical terminology significantly impedes effective communication, warranting a score of 1."
      }
    }
  ],
"response_format": [
    {
      "score": "json_object"
    }
  ]
"""

QUESTIONING_SKILLS_LACK_OF_JARGON2 = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student avoids using medical jargon and communicates clearly with the patient. Provide your assessment in a specific JSON format.

Evaluation Process:
1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
   - Use of patient-friendly language
   - Avoidance of medical jargon
   - Immediate explanation of medical terms when used
   - Clear communication of medical concepts

2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
   - Score 5: Consistent use of easily understood language, avoidance of jargon, or immediate explanation of terms
   - Score 3: Occasional use of medical terms without definition, clarified upon patient request
   - Score 1: Frequent use of unexplained medical jargon, making conversation inaccessible to the patient

3. Provide Justification: Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

Please provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else:

{
  "evaluation": {
    "elements_present": [
      "List of elements present in the interview"
    ],
    "elements_absent": [
      "List of elements missing from the interview"
    ],
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the excerpt to support your evaluation"
  }
}

Examples:
The following examples illustrate how to apply the evaluation criteria and format the response:

Example 1:
Input: 
Physician: "Can you tell me more about the pain you're experiencing in your stomach?"
Patient: "It's a burning sensation, right here in the middle of my upper belly."
Physician: "I see. What you're describing sounds like it could be related to stomach acid. Sometimes, when stomach acid moves up into the food pipe - that's the tube that connects your mouth to your stomach - it can cause a burning feeling. This is often called heartburn or acid reflux. Have you ever heard of these terms?"
Patient: "Yes, I've heard of heartburn before."
Physician: "Great. Now, does this pain get worse after eating certain foods or when you lie down?"
Patient: "Yes, especially after spicy meals and when I go to bed."
Physician: "That's helpful information. These symptoms are common with a condition called acid reflux. It's when the muscle at the bottom of your food pipe doesn't close properly, allowing stomach acid to flow back up. Does this explanation make sense to you?"
Patient: "Yes, it does. Thank you for explaining it so clearly."

Output:
{
  "evaluation": {
    "elements_present": [
      "Use of patient-friendly language",
      "Avoidance of medical jargon",
      "Immediate explanation of medical terms when used",
      "Clear communication of medical concepts"
    ],
    "elements_absent": [],
    "score": 5,
    "justification": "The physician consistently uses patient-friendly language and avoids medical jargon throughout the conversation. When introducing medical concepts, they provide immediate, clear explanations. For example, they describe the esophagus as \"the tube that connects your mouth to your stomach\" and explain acid reflux as \"when stomach acid moves up into the food pipe\". They also check for patient understanding, asking \"Have you ever heard of these terms?\" and \"Does this explanation make sense to you?\". This approach ensures clear communication and patient comprehension, warranting a score of 5."
  }
}

Example 2:
Input: 
Physician: "Based on your symptoms, it sounds like you might have gastritis."
Patient: "Gastritis? What's that?"
Physician: "Oh, I'm sorry. Gastritis is inflammation of the stomach lining. It can cause pain and discomfort in your upper abdomen. Have you been experiencing any nausea or vomiting?"
Patient: "Yes, I've felt nauseous, especially in the mornings."
Physician: "I see. And have you noticed any changes in your bowel movements?"
Patient: "What do you mean by that?"
Physician: "I'm asking if you've had any diarrhea or constipation, or if your stools look different than usual."
Patient: "Oh, I see. No, everything seems normal in that regard."
Physician: "Alright. Now, I'd like to perform a physical examination to check for any abdominal tenderness."

Output:
{
  "evaluation": {
    "elements_present": [
      "Some use of patient-friendly language",
      "Clarification of terms upon patient request"
    ],
    "elements_absent": [
      "Consistent avoidance of medical jargon",
      "Immediate explanation of all medical terms used"
    ],
    "score": 3,
    "justification": "The physician occasionally uses medical terms without immediate definition, such as \"gastritis\" and \"bowel movements\". However, they do provide explanations when the patient asks for clarification. For instance, when the patient questions the term \"gastritis\", the physician explains it as \"inflammation of the stomach lining\". Similarly, they clarify \"bowel movements\" when the patient seems confused. While the physician does use some patient-friendly language, the initial use of unexplained terms and the need for patient-prompted clarifications align with a score of 3."
  }
}

Example 3:
Input: 
Physician: "Your symptoms suggest possible cholecystitis with concomitant cholelithiasis."
Patient: "I'm sorry, I don't understand what you're saying."
Physician: "Ah, well, cholecystitis is inflammation of the gallbladder, often caused by cholelithiasis, which are gallstones. Have you been experiencing any epigastric pain radiating to your right upper quadrant?"
Patient: "I'm not sure what you mean by epigastric or right upper quadrant."
Physician: "Right, epigastric refers to the area right below your sternum, and the right upper quadrant is the upper right part of your abdomen. We'll need to do an ultrasound to confirm the diagnosis and rule out any hepatic involvement."
Patient: "I'm feeling quite lost with all these terms. Can you explain in simpler words?"
Physician: "Of course, my apologies. We think there might be a problem with your gallbladder, possibly stones. We need to do a special scan to check it out."

Output:
{
  "evaluation": {
    "elements_present": [],
    "elements_absent": [
      "Use of patient-friendly language",
      "Avoidance of medical jargon",
      "Immediate explanation of medical terms when used",
      "Clear communication of medical concepts"
    ],
    "score": 1,
    "justification": "The physician's conversation is dominated by medical jargon, making it largely inaccessible to the patient. They begin with complex terms like \"cholecystitis\" and \"cholelithiasis\" without providing immediate explanations. Even when attempting to clarify, they introduce more jargon such as \"epigastric pain\" and \"right upper quadrant\". The patient's repeated requests for clarification demonstrate their struggle to understand. While the physician eventually provides a simplified explanation, it comes only after multiple instances of confusion. This excessive use of unexplained medical terminology significantly impedes effective communication, warranting a score of 1."
  }
}

Now, please evaluate the following medical interview transcript:
"""