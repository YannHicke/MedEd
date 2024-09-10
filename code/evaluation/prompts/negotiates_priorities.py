NEGOTIATES_PRIORITIES_SETS_AGENDA = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student elicits the narrative thread, or the patient’s story, from the patient. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

**Step 1. Scoring:**
   - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
     - **Score 5:** The student encourages and lets the patient talk about their problem. The student does not stop the patient or introduce new information.
     - **Score 4:** The student encourages the patient to talk about their problem, but occasionally interrupts or gently redirects the conversation. The student mostly avoids introducing new information but may do so minimally.
     - **Score 3:** The student begins to let the patient talk about their problem, but either interrupts with focused questions or introduces new information into the conversation.
     - **Score 2:** The interviewer sets the pace with Q&A style, not conversation.
     - **Score 1:** The student fails to let the patient talk about their problem.

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