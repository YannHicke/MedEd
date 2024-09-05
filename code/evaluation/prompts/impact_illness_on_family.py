IMPACT_OF_ILLNESS_ON_FAMILY = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student explores and addresses the impact of the illness on the patient’s family. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student inquires about the structure of the patient’s family. The student addresses the impact of the patient’s illness and/or treatment on the family. The student explores these issues.
      - **Score 4:** The student inquires about the family structure and addresses the impact of the illness/treatment on the family, but the exploration may not be as thorough as in a score of 5. Some family-related issues are discussed, but the student might miss subtle nuances or fail to delve deeply into certain aspects. The student shows a clear attempt to understand the family dynamic and its relation to the patient's health situation.
      - **Score 3:** The student addresses the impact of the illness or treatment on the family members and on family lifestyle but fails to explore these issues adequately.
      - **Score 2:** The student makes limited attempts to address family structure or the impact of illness/treatment on the family. 
      - **Score 1:** The student fails to address the impact of the illness or treatment on the family members and on family lifestyle.

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
