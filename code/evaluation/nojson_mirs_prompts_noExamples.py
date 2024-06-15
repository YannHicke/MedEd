# nojson_mirs_prompts.py

nojson_mirs_prompts_noExamples = {
    "OPENING": """
Consider the following criteria for evaluating the opening of a medical interview. Assign a score from 1 to 5 based on the criteria provided:

Score 5: The interviewer introduces themselves, clarifies their role, and inquires how to address the patient, using the patient’s name.
Score 4: Only one element of the full introduction criteria is missing.
Score 3: The interviewer’s introduction is missing two elements.
Score 2: The introduction consists only of a basic 'hello', lacking most elements of a full introduction.
Score 1: There is no introduction at all.

Task:
Based on the above criteria, analyze the opening of the following conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
    """,

    "ELICITS SPECTRUM OF CONCERNS": """
Consider the following criteria for evaluating how effectively an interviewer elicits the patient's full spectrum of concerns within the first 3-5 minutes of the medical interview. Assign a score from 1 to 5 based on the criteria provided:

Score 5: The interviewer elicits the patient’s full spectrum of concerns, asking 'what else' repeatedly until no additional concerns are raised.
Score 4: The interviewer addresses secondary concerns but misses one final 'what else'.
Score 3: The interviewer only elicits the patient’s main concern, without probing for additional concerns.
Score 2: The interviewer merely acknowledges the concern without actively eliciting further information.
Score 1: The interviewer fails to elicit any of the patient’s concerns.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "NEGOTIATES PRIORITIES & SETS AGENDA": """
Consider the following criteria for evaluating how the interviewer negotiates priorities of patient concerns, lists all of the concerns, and sets the agenda at the onset of the interview with the patient’s agreement:

Score 5: The interviewer negotiates priorities of patient concerns as gathered, listing all of the concerns, and sets the agenda at the onset of the interview, obtaining the patient’s agreement.
Score 4: The full agenda is set before all concerns are completely elicited.
Score 3: The interviewer sets an agenda but does not negotiate priorities with the patient.
Score 2: The interviewer lists some concerns but does not set an agenda or negotiate priorities.
Score 1: The interviewer does not negotiate priorities or set an agenda, focusing only on the chief concern and considering only the physician’s needs.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

"ELICITING THE NARRATIVE THREAD or the ‘PATIENT’S STORY’": """
Evaluate the interviewer's effectiveness in allowing the patient to discuss their health concerns in a narrative format. Use the following criteria for scoring:

Score 5: The interviewer encourages the patient to share their entire story without interrupting, allowing for a complete narrative thread.
Score 4: The interviewer asks the patient to tell them about a specific problem but does not allow for a complete narrative thread.
Score 3: The interviewer generally allows the patient to talk but occasionally interrupts with focused questions or introduces unrelated topics.
Score 2: The interviewer frequently interrupts the patient's narrative with questions, creating a Q&A style rather than a conversational flow.
Score 1: The interviewer dominates the conversation, not allowing the patient to talk about their problem.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "TIMELINE": """
Consider how well the interviewer establishes a timeline of the chief concern and history of the present illness, including the following scoring criteria:

Score 5: The interviewer obtains sufficient information to establish a clear chronology of the chief concern and history of the present illness, including the sequence of associated symptoms and/or events.
Score 3: The interviewer obtains some of the necessary information but fails to establish a complete chronology for all associated symptoms and events.
Score 1: The interviewer fails to obtain any information necessary to establish a timeline or chronology of the patient’s concerns.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ORGANIZATION": """
Assess the organization of the interview, considering if the questions follow a logical order and if the effective use of time ensures that tasks are completed within the allotted time. Use the following criteria for scoring:

Score 5: Questions in the body of the interview follow a logical order to the patient, with effective use of time so tasks are completed within the time allowed.
Score 3: The interviewer seems to follow a series of topics or agenda items, but there are a few minor disjointed questions.
Score 1: The interviewer asks questions that seem disjointed and unorganized, affecting the interview's flow.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "TRANSITIONAL STATEMENTS (only for complete histories)": """
Evaluate the use of transitional statements by the interviewer, which explain the reasons for progressing from one section to another, with the following scoring guidelines:

Score 5: The interviewer utilizes transitional statements effectively throughout the interview, clarifying the interview's structure for the patient.
Score 3: The interviewer sometimes uses effective transitional statements but fails to do so consistently or some statements lack clarity.
Score 1: The interviewer progresses from one subsection to another in such a manner that the patient is left with a feeling of uncertainty as to the purpose of the questions. No transitional statements are made.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "PACING OF INTERVIEW (not based on finishing on time)": """
Consider the pacing of the interview, focusing on the interviewer's attentiveness, the smooth progression of the interview, and the deliberate use of silence, scoring as follows:

Score 5: The interviewer is fully attentive to the patient’s responses, listens without interruption, and the interview progresses smoothly without awkward pauses. Silence is used deliberately.
Score 3: The pace of the interview is generally comfortable, but there are occasional interruptions or awkward pauses.
Score 1: The interviewer frequently interrupts the patient, with several awkward pauses breaking the flow of the interview.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "QUESTIONING SKILLS – TYPES OF QUESTIONS": """
Analyze the types of questions used by the interviewer, considering the sequence and appropriateness of open-ended versus specific questions, and score as follows:

Score 5: The interviewer begins information gathering with an open-ended question, follows up with more specific or direct questions, and each major line of questioning is begun with an open-ended question. No poor question types are used.
Score 3: The interviewer often fails to start a line of inquiry with open-ended questions, relying instead on specific or direct questions, or occasionally uses leading, why, or multiple questions.
Score 1: The interviewer frequently uses why questions, multiple questions, or leading questions, detracting from the quality of information gathered.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

   "QUESTIONING SKILLS - SUMMARIZING": """
Evaluate how the interviewer summarizes the data obtained during the interview, using the following criteria for scoring:

Score 5: The interviewer summarizes the data obtained at the end of each major line of inquiry or subsection to verify and/or clarify the information. For a focused history, one summary at the end is sufficient.
Score 3: The interviewer summarizes data at the end of some lines of inquiry but not consistently, or the summary attempts are incomplete.
Score 1: The interviewer fails to summarize any of the data obtained.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",    


    "QUESTIONING SKILLS - DUPLICATION": """
Assess the interviewer's tendency to repeat questions seeking information that has already been provided, unless clarification or summarization is necessary, with scoring as follows:

Score 5: The interviewer does not repeat questions unnecessarily and only seeks repetition for clarification or summarization.
Score 3: The interviewer rarely repeats questions, and when questions are repeated, it is not for summarization or clarification but due to a lapse in memory.
Score 1: The interviewer consistently seeks information previously provided, showing a clear failure to track or remember patient information.

Task:
Based on the criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "QUESTIONING SKILLS - LACK OF JARGON": """
Evaluate the interviewer's use of language, focusing on how well they avoid medical jargon and ensure clarity of communication. Use the following criteria for scoring:

Score 5: The interviewer uses language that is easily understood by the patient, avoiding medical jargon entirely or explaining any technical terms immediately.
Score 3: The interviewer occasionally uses medical terms without definition, which may require clarification upon patient request.
Score 1: The conversation is dominated by medical jargon, making it inaccessible to the patient without definitions provided.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "QUESTIONING SKILLS - VERIFICATION OF PATIENT INFORMATION (in vignette)": """
Evaluate how effectively the interviewer clarifies, verifies, and seeks specificity of the patient's responses during the interview. Use the following criteria for scoring:

Score 5: The interviewer consistently seeks to clarify, verify, and specify patient responses, ensuring an accurate understanding of the patient’s statements.
Score 3: Clarification, verification, and specificity are sought but not consistently, leading to some gaps in understanding.
Score 1: The interviewer fails to clarify or verify patient responses consistently, largely ignoring the need for accuracy.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "INTERACTIVE TECHNIQUES": """
Evaluate the balance between patient-centered and physician-centered interviewing styles used by the interviewer. Use the following criteria for scoring:

Score 5: The interviewer consistently uses a patient-centered technique while effectively incorporating physician-centered elements that promote a collaborative partnership between patient and doctor.
Score 3: The interviewer initially uses a patient-centered style but reverts to a physician-centered approach at the end, rarely returning the lead to the patient. Alternatively, the interviewer uses only patient-centered interviewing without effectively incorporating physician-centered elements, failing to accomplish the negotiated agenda.
Score 1: The interview is dominated by a physician-centered approach, not following the patient’s lead, which halts the collaborative partnership.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "VERBAL FACILITATION SKILLS": """
Evaluate the interviewer's verbal facilitation skills, focusing on how effectively they encourage the patient to share their story and participate in the conversation. Use the following criteria for scoring:

Score 5: The interviewer consistently encourages the patient throughout the interview by drawing out information using verbal encouragement, short statements, and echoing techniques. Praises are intermittently given for patient engagement or correct healthcare practices.
Score 3: The interviewer uses some verbal facilitation skills but not consistently or sometimes at inappropriate times. There is room for more effective use of verbal encouragement.
Score 1: The interviewer fails to use verbal facilitation skills to encourage the patient to tell their story or contribute to the conversation.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "NON-VERBAL FACILITATION SKILLS": """
Evaluate the interviewer's use of non-verbal communication skills to put the patient at ease and facilitate engagement. Use the following criteria for scoring:

Score 5: The interviewer puts the patient at ease and facilitates effective communication using good eye contact, relaxed and open body language, appropriate facial expressions, eliminating physical barriers, and making appropriate physical contact.
Score 3: The interviewer utilizes some facilitative non-verbal techniques effectively, but could be more consistent. One or two techniques are not utilized effectively, or some physical barrier may still be present.
Score 1: The interviewer makes no attempt to put the patient at ease. The body language is negative or closed, annoying mannerisms such as foot or pencil tapping are present, or eye contact is lacking or uncomfortable.

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "EMPATHY AND ACKNOWLEDGING PATIENT CUES": """
Evaluate the interviewer's ability to use supportive comments regarding the patient’s emotions and demonstrate empathy. Use the following criteria for scoring:

Score 5: The interviewer uses supportive comments regarding the patient’s emotions and employs techniques such as NURS (name, understand, respect, support) to demonstrate empathy effectively.
Score 3: The interviewer is neutral, neither particularly empathetic nor unsupportive, maintaining a balanced but not deeply empathetic stance.
Score 1: No empathy is demonstrated; the interviewer may use a negative emphasis or openly criticize the patient, showing a lack of sensitivity to the patient’s emotional state.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "PATIENT’S PERSPECTIVE (BELIEFS; Case specific)": """
Evaluate how well the interviewer elicits and addresses the patient’s beliefs and perspective on their illness. Use the following criteria for scoring:

Score 5: The interviewer thoroughly elicits the patient’s perspectives, including their beliefs about the beginning of the illness, their feelings, ideas of cause, function, and expectations (FIFE), and actively addresses these beliefs.
Score 3: The interviewer elicits some of the patient’s perspectives on the illness but may not address all beliefs or fails to follow through in addressing these beliefs.
Score 1: The interviewer fails to elicit the patient’s perspective or beliefs about the illness.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "IMPACT OF ILLNESS ON PATIENT AND PATIENT’S SELF-IMAGE": """
Assess how the interviewer explores the effects of the illness on the patient's life and self-image. Use the following criteria for scoring:

Score 5: The interviewer inquires deeply about how the illness affects the patient's feelings and lifestyle changes. The interviewer explores these issues thoroughly and offers counseling or resources to support the patient.
Score 3: The interviewer addresses the impact of the illness on the patient's life or self-image only partially. The interviewer might not offer any additional support such as counseling or resources.
Score 1: The interviewer fails to acknowledge or explore the impact of the illness on the patient's life and self-image.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "IMPACT OF ILLNESS ON FAMILY": """
Evaluate how the interviewer addresses the impact of the patient’s illness on their family. Use the following criteria for scoring:

Score 5: The interviewer inquires about the patient’s family structure and thoroughly addresses the impact of the patient’s illness and/or treatment on the family. The interviewer explores these issues in detail.
Score 3: The interviewer recognizes the impact of the illness or treatment on family members and lifestyle but does not explore these issues adequately.
Score 1: The interviewer fails to address the impact of the illness or treatment on the family members and their lifestyle.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "SUPPORT SYSTEMS": """
Evaluate how the interviewer explores the patient’s support systems, including emotional, financial support, and access to healthcare. Use the following criteria for scoring:

Score 5: The interviewer thoroughly determines:
- What emotional support the patient has.
- What financial support the patient has and learns about their access to healthcare.
- About other resources available to the patient and family and suggests appropriate community resources.
(In focused histories, addressing one pertinent support aspect in depth is sufficient.)
Score 3: The interviewer determines some aspects of the available support but does not fully explore or suggest resources.

Score 1: The interviewer fails to determine or discuss any support currently available to the patient.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "PATIENT’S EDUCATION & UNDERSTANDING": """
Evaluate the interviewer's efforts to educate the patient about their condition and to assess the patient's understanding. Use the following criteria for scoring:

Score 5: The interviewer determines the patient’s level of interest in learning about their condition, provides appropriate education, and uses the teach-back method to check the patient's understanding. Techniques may include asking the patient to repeat information, inquiring if the patient has additional questions, posing hypothetical situations, or asking the patient to demonstrate techniques.
Score 3: The interviewer asks if the patient understands the information but does not use teach-back techniques. There is some attempt to determine interest in patient education, but it could be more thorough.
Score 2: The interviewer provides information but does not check the patient’s understanding.
Score 1: The interviewer fails to assess the patient's level of understanding and does not effectively address misunderstandings when evident. The issue of patient education is also neglected.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ASSESS MOTIVATION FOR CHANGES": """
Evaluate the interviewer's approach to assessing the patient's motivation for making lifestyle or behavioral changes. Use the following criteria for scoring:

Score 5: The interviewer inquires about how the patient feels regarding the lifestyle/behavioral change and tailors information and suggestions based on the patient's level of readiness.
Score 3: The interviewer asks about the patient's feelings toward changes but fails to follow up appropriately based on the patient's responses or readiness.
Score 1: The interviewer does not assess the patient's motivation to make changes, does not offer any options or plans, or incorrectly assumes the patient’s readiness for change.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ADMITTING LACK OF KNOWLEDGE": """
Evaluate the interviewer's willingness to admit a lack of knowledge and their approach to seeking accurate information. Use the following criteria for scoring:

Score 5: When asked for information or advice they are not equipped to provide, the interviewer admits their lack of knowledge but immediately offers to seek resources or consult colleagues to answer the question(s).
Score 3: The interviewer admits lack of knowledge when asked for information they cannot provide, but only rarely seeks other resources or help to find the answers.
Score 1: When asked for information they are not equipped to provide, the interviewer makes up answers in an attempt to satisfy the patient’s questions and does not refer to any other resources.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "INFORMED CONSENT FOR INVESTIGATIONS & PROCEDURES": """
Evaluate how the interviewer discusses investigations and procedures with the patient, focusing on the extent to which they cover the necessary aspects of informed consent. Use the following criteria for scoring:

Score 5: The interviewer thoroughly discusses the purpose and nature of all investigations and procedures, reviews foreseeable risks and benefits, discloses alternatives including their risks and benefits, and mentions that taking no action is always an alternative.
Score 3: The interviewer covers some aspects of the investigations and procedures but omits certain elements of informed consent, such as full disclosure of alternatives or specific risks and benefits.
Score 1: The interviewer fails to discuss the purpose, nature, risks, benefits, or alternatives of investigations or procedures adequately.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ACHIEVE A SHARED PLAN": """
Evaluate the interviewer's effectiveness in discussing the diagnosis or prognosis with the patient and negotiating a treatment plan. Use the following criteria for scoring:

Score 5: The interviewer discusses the diagnosis and/or prognosis comprehensively and negotiates a treatment plan, inviting the patient to contribute their own thoughts, ideas, suggestions, and preferences.
Score 3: The interviewer discusses the diagnosis and/or prognosis and outlines a plan, but does not fully engage the patient in the planning process or allow for patient input, resulting in a lack of full quality in the shared decision-making process.
Score 1: The interviewer fails to discuss the diagnosis and/or prognosis with the patient, missing an opportunity to negotiate or even formulate a treatment plan.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ENCOURAGEMENT OF QUESTIONS": """
Evaluate how well the interviewer encourages the patient to ask questions throughout the interview. Use the following criteria for scoring:

Score 5: The interviewer encourages the patient to ask questions at the end of major subsections and provides at least two opportunities for the patient to bring up additional topics or points, including one at the end of the interview.
Score 4: The interviewer provides only one opportunity for the patient to ask questions, typically at the end of the interview.
Score 3: The interviewer provides one opportunity for the patient to ask questions but not near the end of the encounter.
Score 2: The interviewer does not specifically ask if there are questions, but the climate and pace of the interview allow for them.
Score 1: The interviewer fails to provide the patient with the opportunity to ask questions or discuss additional points, and may even discourage the patient’s questions.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "CLOSURE": """
Evaluate the effectiveness of the interview's closure by assessing the clarity and completeness of future plans. Use the following criteria for scoring:

Score 5: At the end of the interview, the interviewer clearly specifies the future plans, including actions to be taken by both the interviewer (such as making referrals or consultations) and the patient (such as dietary changes or appointments for therapy), along with clear timelines for the next communication or appointment.
Score 3: At the end of the interview, the interviewer partially details the future plans but leaves some aspects unclear or vague.
Score 1: At the end of the interview, the interviewer fails to specify any plans for the future, leaving the patient without a clear understanding of what to expect next. There is no closure whatsoever.

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
"""
}



