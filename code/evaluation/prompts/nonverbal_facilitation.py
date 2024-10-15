NONVERBAL_FACILITATION_SKILLS = """
You will be given a video of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the student’s non-verbal facilitation skills. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you watch the video, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student puts the patient at ease and facilitates communication by using: good eye contact; relaxed, open body language; appropriate facial expression; eliminating physical barriers; and making appropriate physical contact with the patient.
      - **Score 4:** The student frequently uses non-verbal facilitation skills during the interview, but not as consistently or effectively as in a score of 5. 
      - **Score 3:** The student makes some use of facilitative techniques but could be more consistent. One or two techniques are not used effectively, or some physical barrier may be present.
      - **Score 2:** The student demonstrates limited use of facilitation skills and not as consistently or effectively as in a score of 3.
      - **Score 1:** The student makes no attempt to put the patient at ease, body language is negative or closed, or annoying mannerism (foot or pencil tapping) intrudes on the interview. Eye contact is not attempted or is uncomfortable.

  **Step 2. Justification:** Based on your analysis in Step 1, assign a score using the provided rubric strictly, and explain your reasoning clearly. Your evaluation should be rigorous, impartial, and evidence-based. Directly quote the video to support your evaluation.

Provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

{
  "evaluation": {
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the video to support your evaluation"
  }
}

Now, please evaluate the given medical interview video:
"""