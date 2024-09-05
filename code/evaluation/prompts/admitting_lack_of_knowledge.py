ADMITTING_LACK_OF_KNOWLEDGE = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student admits a lack of knowledge. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

**Step 1. Scoring:**
   - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
     - **Score 5:** The student, when asked for information or advice that they are not equipped to provide, admits to their lack of knowledge in that area but immediately offers to seek resources to answer the question(s).
     - **Score 4:** The student admits to their lack of knowledge when asked for information or advice they can't provide. They often offer to seek resources for answers, but may not do so as consistently or immediately as in a score of 5. The student shows a clear understanding of their limitations and a willingness to find information, even if their approach is slightly less proactive.
     - **Score 3:** The student, when asked for information or advice that they are not equipped to provide, admits lack of knowledge, but rarely seeks other resources for answers.
     - **Score 2:** The student inconsistently admits to lack of knowledge when faced with questions they can't answer. They do not seek other resources for answers.
     - **Score 1:** The student, when asked for information, which they are not equipped to provide, makes up answers in an attempt to satisfy the patient’s questions and never refers to other resources.

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
