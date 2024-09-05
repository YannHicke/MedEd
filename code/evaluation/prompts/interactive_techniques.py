INTERACTIVE_TECHNIQUES = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the student’s interactive techniques with the patient. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The interviewer consistently uses the patient-centered technique, prioritizing the patient's needs and involving them in decisions. They also mix patient-centered and physician-centered styles, balancing patient involvement with the doctor's expertise to promote a collaborative partnership between patient and doctor.
      - **Score 4:** The student mostly uses a patient-centered approach, with frequent attempts to involve the patient in decisions. There is a noticeable effort to balance patient-centered and physician-centered styles, though the balance may not be as seamless as in a score of 5. Occasional lapses into a more physician-centered approach occur, but the student usually recognizes and corrects these, maintaining a largely collaborative partnership.
      - **Score 3:** The student initially uses a patient-centered style, but reverts to a physician-centered approach at the end, rarely giving control back to the patient. Alternatively, the student may use only a patient-centered style, neglecting the physician-centered approach, which prevents them from effectively accomplishing the negotiated agenda.
      - **Score 2:** The student shows some awareness of patient-centered techniques but struggles to implement them consistently. The interview is predominantly physician-centered, with occasional attempts at patient involvement that are often cut short or ineffective. While not entirely neglecting the patient's perspective, the student fails to establish a truly collaborative partnership. There are more instances of patient involvement than in a score of 1, but these are limited and often superficial.
      - **Score 1:** The student does not follow the patient’s lead. They only use physician-centered technique, halting the collaborative partnership.

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
