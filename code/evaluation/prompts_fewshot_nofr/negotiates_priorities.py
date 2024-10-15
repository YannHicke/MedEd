NEGOTIATES_PRIORITIES_SETS_AGENDA = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student negotiates the patient’s priorities and sets the agenda for their visit. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Understanding the Task:**
    - Read the following note:
      **Note:** Learner ascertains the patient’s concerns. In negotiating priorities, a balance is struck between patient concerns and provider’s medical understanding of which problems might be more immediately important. An agenda is negotiated between learner and patient. In agenda setting and negotiating, the patient should not be told what is going to occur, but instead share in making an agreed plan. 

  **Step 2. Scoring:**
    - As you read the transcript, and using your understanding from Step 1, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student fully negotiates the priorities of patient concerns. The student lists all of the concerns, sets the agenda at the onset of the interview, and gets the patient’s agreement to the agenda.
      - **Score 4:** The student mostly negotiates the priorities of patient concerns, but not as thoroughly as in a score of 5. They set the agenda at the onset of the interview before they discuss the patient's spectrum of concerns and get the patient’s agreement to the agenda.
      - **Score 3:** The student sets the agenda but the student elicits only partial concerns and therefore does not accomplish the complete patient agenda for their visit.
      - **Score 2:** The student minimally negotiates priorities and fails to accomplish the complete patient agenda. Limited efforts are made to set an agenda.
      - **Score 1:** The student does not negotiate priorities or set an agenda. The student focuses only on the chief complaint and takes only the physician’s needs into account. 

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