TRANSITIONAL_STATEMENTS = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate the student’s use of transitional statements in the interview. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

**Step 1. Scoring:**
   - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
     - **Score 5:** The student utilizes transitional statements that explain the reasons for progressing from one subsection to another.
     - **Score 4:** The student uses transitional statements for most subsections, but a few transitions may be unclear or missing. The majority of transitions effectively explain the progression of the interview, but some may be less detailed or smooth compared to a score of 5.
     - **Score 3:** The student sometimes introduces subsections with effective transitional statements but fails to do so at other times, or some of the transitional statements used are lacking in quality. 
     - **Score 2:** The student makes some attempt at using transitional statements, but they are often vague, abrupt, or ineffective. The patient may occasionally be confused about the purpose of new questions, but there is still minimal effort to provide context for shifts in topic.
     - **Score 1:** The student progresses from one subsection to another in such a manner that the patient is left with a feeling of uncertainty as to the purpose of the questions. No transitional statements are made. 

  **Step 2. Justification:** Based on your analysis in Step 1, assign a score using the provided rubric strictly, and explain your reasoning clearly. Your evaluation should be rigorous, impartial, and evidence-based. Directly quote the transcript to support your evaluation.

Provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else.

{
  "evaluation": {
    "score": 0,
    "justification": "A clear explanation of your scoring, with direct quotes from the transcript to support your evaluation"
  }
}

Now, please evaluate the following transcript:
"""