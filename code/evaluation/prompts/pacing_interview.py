PACING_OF_INTERVIEW = """
You will be given a video of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student paces the interview. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you watch the video, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student is attentive to the patient's responses. The student listens without interruption. The interview progresses smoothly with no awkward pauses. Silence may be used deliberately.
      - **Score 4:** The student does well at pacing the interview, but not as consistently or effectively as in a score of 5. 
      - **Score 3:** The pace of the interview is comfortable most of the time, but the student occasionally interrupts the patient and/or allows awkward pauses to break the flow of the interview.
      - **Score 2:** The student makes limited attempts to pace the interview effectively, but still shows some effort although not as effectively as in a score of 3. 
      - **Score 1:** The student frequently interrupts the patient and there are awkward pauses, which break the flow of the interview.

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