INFORMED_CONSENT = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student obtains informed consent for investigations and procedures. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Identify Key Elements:**
    - As you read the transcript, create a list noting whether each element is present or absent:
      - Explanation of the purpose of the investigation or procedure
      - Explanation of the risks and benefits
      - Disclosure of alternative investigations or procedures
      - Explanation that taking no action is a possible alternative

  **Step 2. Scoring:**
    - As you read the transcript, use your list from Step 1 and evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student discusses the purpose and nature of all investigations and procedures. The student reviews foreseeable risks and benefits of the proposed investigation or procedure. The student discloses alternative investigations or procedures and their relative risks and benefits. The medical student always explains to the patient that taking no action is a possible alternative.
      - **Score 4:** The student discusses most aspects of investigations and procedures, including their purpose and nature. They review most risks and benefits, but may not cover all foreseeable ones. Some alternatives are mentioned, but the discussion might not be as comprehensive as in a score of 5. The student shows a clear attempt to obtain informed consent, even if not as thoroughly as in a top performance.
      - **Score 3:** The student discusses some aspects of the investigations and procedures but omits some elements of informed consent. 
      - **Score 2:** The student makes limited attempts to discuss investigations or procedures and omits elements of informed consent. Discussion of alternatives is minimal or absent. 
      - **Score 1:** The student fails to discuss investigations or procedures.

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
