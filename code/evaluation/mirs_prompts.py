# mirs_prompts.py

mirs_prompts = {
    "Opening": """
Consider the following criteria for evaluating the opening of a medical interview. Assign a score from 1 to 5 based on the criteria provided:

- Score a 5 if the interviewer introduces themselves, clarifies their role, and inquires how to address the patient, using the patient’s name.
- Score a 4 if one element of the full introduction criteria is missing.
- Score a 3 if the interviewer’s introduction is missing two elements.
- Score a 2 if the introduction consists only of a basic 'hello', lacking most elements of a full introduction.
- Score a 1 if there is no introduction at all.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the above criteria, analyze the opening of the following conversation excerpt and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "ELICITS SPECTRUM OF CONCERNS": """
Evaluate if the interviewer elicits the patient's full spectrum of concerns within the first 3-5 minutes of the interview. Consider the following scoring criteria:

- Score a 5 if the interviewer elicits the patient’s full spectrum of concerns within the first 3-5 minutes of the interview. The interviewer asks 'what else' until no additional concerns are raised.
- Score a 4 if only one final 'what else' is missing but secondary concerns are addressed.
- Score a 3 if the interviewer only elicits the patient’s main concern without probing for additional concerns.
- Score a 2 if the interviewer merely states the concern without any elicitation.
- Score a 1 if the interviewer fails to elicit any of the patient’s concerns.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Analyze the provided conversation for how effectively the interviewer elicits the spectrum of concerns and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
    """,

    "NEGOTIATES PRIORITIES & SETS AGENDA": """
Consider the following criteria for evaluating how the interviewer negotiates priorities of patient concerns, lists all of the concerns, and sets the agenda at the onset of the interview with the patient’s agreement:

- Score a 5 if the interviewer negotiates priorities of patient concerns as gathered, listing all of the concerns, and sets the agenda at the onset of the interview and gets the patient’s agreement to the agenda.
- Score a 4 if the full agenda is set before concerns are completely elicited.
- Score a 3 if the interviewer sets an agenda but does not negotiate priorities with the patient.
- Score a 2 if the interviewer lists some concerns but does not set an agenda or negotiate priorities.
- Score a 1 if the interviewer does not negotiate priorities or set an agenda. The interviewer focuses only on the chief concern and takes only the physician’s needs into account.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the above criteria, analyze the conversation for how effectively the interviewer negotiates priorities and sets an agenda, and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "ELICITING THE NARRATIVE THREAD or the ‘PATIENT’S STORY’": """
Evaluate the interviewer's effectiveness in encouraging and letting the patient talk about their problem, based on the following criteria:

- Score a 5 if the interviewer encourages the patient to share their story without interrupting, allowing for a complete narrative thread.
- Score a 4 if the interviewer asks the patient to tell them about a specific problem but does not allow for a complete narrative thread.
- Score a 3 if the interviewer generally allows the patient to talk but occasionally interrupts with focused questions or introduces unrelated topics.
- Score a 2 if the interviewer often interrupts the narrative with questions, setting a Q&A style rather than a conversational flow.
- Score a 1 if the interviewer fails to let the patient talk about their problem, dominating the conversation.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the above criteria, analyze how well the interviewer facilitates the patient in telling their story and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "TIMELINE": """
Consider how well the interviewer establishes a timeline of the chief concern and history of the present illness, including the following scoring criteria:

- Score a 5 if the interviewer obtains sufficient information to establish a clear chronology of the chief concern and history of the present illness, including the sequence of associated symptoms and/or events.
- Score a 3 if the interviewer obtains some of the necessary information but fails to establish a complete chronology for all associated symptoms and events.
- Score a 1 if the interviewer fails to obtain any information necessary to establish a timeline or chronology of the patient’s concerns.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Assess the interviewer's ability to establish a timeline of events related to the patient’s chief concern and history of the present illness, and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "ORGANIZATION": """
Assess the organization of the interview, considering if the questions follow a logical order and if the effective use of time ensures that tasks are completed within the allotted time. Use the following criteria for scoring:

- Score a 5 if questions in the body of the interview follow a logical order to the patient, with effective use of time so tasks are completed within the time allowed.
- Score a 3 if the interviewer seems to follow a series of topics or agenda items, but there are a few minor disjointed questions.
- Score a 1 if the interviewer asks questions that seem disjointed and unorganized, affecting the interview's flow.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}


Based on the above criteria, analyze the conversation for the organization of the interview and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "TRANSITIONAL STATEMENTS (only for complete histories)": """
Evaluate the use of transitional statements by the interviewer, which explain the reasons for progressing from one section to another, with the following scoring guidelines:

- Score a 5 if the interviewer utilizes transitional statements effectively throughout the interview, clarifying the interview's structure for the patient.
- Score a 3 if the interviewer sometimes uses effective transitional statements but fails to do so consistently or some statements lack clarity.
- Score a 1 if interviewer progresses from one subsection to another in such a manner that the patient is left with a feeling of uncertainty as to the purpose of the questions. No transitional statements are made.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}


Analyze the effectiveness of transitional statements in the interview, considering only complete histories, and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "PACING OF INTERVIEW (not based on finishing on time)": """
Consider the pacing of the interview, focusing on the interviewer's attentiveness, the smooth progression of the interview, and the deliberate use of silence, scoring as follows:

- Score a 5 if the interviewer is fully attentive to the patient’s responses, listens without interruption, and the interview progresses smoothly without awkward pauses. Silence is used deliberately.
- Score a 3 if the pace of the interview is generally comfortable, but there are occasional interruptions or awkward pauses.
- Score a 1 if the interviewer frequently interrupts the patient, with several awkward pauses breaking the flow of the interview.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the above criteria, evaluate the pacing of the interview and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "QUESTIONING SKILLS – TYPES OF QUESTIONS": """
Analyze the types of questions used by the interviewer, considering the sequence and appropriateness of open-ended versus specific questions, and score as follows:

- Score a 5 if the interviewer begins information gathering with an open-ended question, follows up with more specific or direct questions, and each major line of questioning is begun with an open-ended question. No poor question types are used.
- Score a 3 if the interviewer often fails to start a line of inquiry with open-ended questions, relying instead on specific or direct questions, or occasionally uses leading, why, or multiple questions.
- Score a 1 if the interviewer frequently uses why questions, multiple questions, or leading questions, detracting from the quality of information gathered.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}


Evaluate the interviewer's use of questioning skills in terms of the types of questions asked and assign a score from 1 to 5 based on the criteria. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "QUESTIONING SKILLS - SUMMARIZING": """
Evaluate how the interviewer summarizes the data obtained during the interview, using the following criteria for scoring:

- Score a 5 if the interviewer summarizes the data obtained at the end of each major line of inquiry or subsection to verify and/or clarify the information. For a focused history, one summary at the end is sufficient.
- Score a 3 if the interviewer summarizes data at the end of some lines of inquiry but not consistently, or the summary attempts are incomplete.
- Score a 1 if the interviewer interviewer fails to summarize any of the data obtained.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Analyze the conversation for instances of summarizing data obtained during the interview and assign a score from 1 to 5 based on the criteria. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",    


    "QUESTIONING SKILLS - DUPLICATION": """
Assess the interviewer's tendency to repeat questions seeking information that has already been provided, unless clarification or summarization is necessary, with scoring as follows:

- Score a 5 if the interviewer does not repeat questions unnecessarily and only seeks repetition for clarification or summarization.
- Score a 3 if the interviewer rarely repeats questions, and when questions are repeated, it is not for summarization or clarification but due to a lapse in memory.
- Score a 1 if the interviewer consistently seeks information previously provided, showing a clear failure to track or remember patient information.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the criteria, analyze the conversation for instances of question duplication and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "QUESTIONING SKILLS - LACK OF JARGON": """
Evaluate the interviewer's use of language, focusing on the avoidance of medical jargon and the clarity of communication, scoring as follows:

- Score a 5 if the interviewer uses language easily understood by the patient, avoiding medical jargon or explaining terms immediately.
- Score a 3 if the interviewer occasionally uses medical terms without definition, requiring clarification upon patient request.
- Score a 1 if the conversation is dominated by medical jargon, making it inaccessible to the patient without definitions provided.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Analyze the conversation for the use of medical jargon and assign a score based on the clarity of communication, ranging from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "QUESTIONING SKILLS - VERIFICATION OF PATIENT INFORMATION (in vignette)": """
Consider how the interviewer seeks clarification, verification, and specificity of the patient’s responses, using the following criteria for scoring:

- Score a 5 if the interviewer consistently seeks to clarify, verify, and specify patient responses, ensuring accurate understanding.
- Score a 3 if clarification, verification, and specificity are sought but not consistently, leading to some gaps in understanding.
- Score a 1 if the interviewer fails to clarify or verify patient responses consistently, largely ignoring the need for accuracy.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Evaluate the interviewer's efforts to verify patient information as presented in the vignette and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "INTERACTIVE TECHNIQUES": """
Assess the balance between patient-centered and physician-centered interviewing styles used by the interviewer, with scoring as follows:

- Score a 5 if the interviewer consistently uses the patient-centered technique. The interviewer mixes patient-centered and physician-centered styles that promote a collaborative partnership between patient and doctor.
- Score a 3 if the interviewer initially uses a patient-centered style but reverts to physician-centered interview at the end (rarely returning the lead to the patient). OR The interviewer uses all patient-centered interviewing and fails to use physician-centered style and therefore does not accomplish the negotiated agenda.
- Score a 1 if the interview does not follow the patient’s lead. Uses only physician-centered technique halting the collaborative partnership.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Analyze the conversation for the use of interactive techniques and assign a score from 1 to 5 based on the balance between patient-centered and physician-centered interviewing styles. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "VERBAL FACILITATION SKILLS": """
Consider the interviewer's use of verbal encouragement and facilitation skills to engage the patient, using the following scoring guidelines:

- Score a 5 if the interviewer encourages the patient throughout the interview. Draws out information. Verbal encouragement, use of short statements, and echoing are used regularly when appropriate. The interviewer provides the patient with intermittent verbal encouragement, such as verbally praising the patient for proper health care technique.
- Score a 3 if the interviewer uses some facilitative skills but not consistently or at inappropriate times. Verbal encouragement could be used more effectively.
- Score a 1 if the interviewer fails to use facilitative skills to encourage the patient to tell the story.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Evaluate the interviewer's verbal facilitation skills and assign a score from 1 to 5 based on the criteria provided. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "NON-VERBAL FACILITATION SKILLS": """
Assess the interviewer's use of non-verbal communication skills to put the patient at ease and facilitate engagement, with scoring as follows:

- Score a 5 if the interviewer puts the patient at ease and facilitates communication by using: Good eye contact; Relaxed, open body language; Appropriate facial expression; Eliminating physical barriers; and Making appropriate physical contact with the patient.
- Score a 3 if the interviewer makes some use of facilitative techniques but could be more consistent. One or two techniques are not used effectively. OR Some physical barrier may be present.
- Score a 1 if the interviewer makes no attempt to put the patient at ease. Body language is negative or closed. OR Any annoying mannerism (foot or pencil tapping) intrudes on the interview. Eye contact is not attempted or is uncomfortable.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the criteria, analyze the conversation for the use of non-verbal facilitation skills and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "EMPATHY AND ACKNOWLEDGING PATIENT CUES": """
Evaluate the interviewer's ability to use supportive comments regarding the patient’s emotions and demonstrate empathy, considering:

- Score a 5 if the interviewer uses supportive comments regarding the patient’s emotions. The interviewer uses NURS (name, understand, respect, support) or specific techniques for demonstrating empathy.
- Score a 3 if the interviewer is neutral, neither overly positive nor negative in demonstrating empathy.
- Score a 1 if no empathy is demonstrated, with the interviewer using a negative emphasis or openly criticizing the patient.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the criteria, analyze the conversation for instances of empathy and acknowledging patient cues, assigning a score from 1 to 5.
""",

    "PATIENT’S PERSPECTIVE (BELIEFS; Case specific)": """
Assess how well the interviewer elicits and addresses the patient's beliefs and perspective on the illness, including:

- Score a 5 if the interviewer elicits the patient’s healing practices and perspectives on the illness, including beliefs about its beginning, Feelings, Ideas of cause, Function and Expectations (FIFE).
- Score a 3 if the interviewer elicits some of the patient’s perspective on the illness AND/OR The interviewer does not follow through with addressing beliefs.
- Score a 1 if the interviewer fails to elicit the patient’s perspective.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Evaluate the interviewer's effort to understand and incorporate the patient's perspective and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "IMPACT OF ILLNESS ON PATIENT AND PATIENT’S SELF-IMAGE": """
Consider the interviewer's exploration of how the illness affects the patient's life and self-image, using the following guidelines for scoring:

- Score a 5 if the interviewer inquires about the patient’s feelings about the illness and how it has changed patient’s life. The interviewer explores these issues. (The interviewer offers counseling or resources to help. This is used in communication cases.)
- Score a 3 if the interviewer partially addresses the impact of the illness on the patient’s life or self-image. AND/OR The interviewer offers no counseling or resources to help.
- Score a 1 if the interviewer fails to acknowledge any impact of the illness on the patient’s life or self-image.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Analyze the conversation for how the illness's impact on the patient is addressed and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "IMPACT OF ILLNESS ON FAMILY": """
Evaluate how the interviewer addresses the impact of the patient’s illness on their family, considering:

- Score a 5 if the interviewer inquires about the structure of the patient’s family. The interviewer addresses the impact of the patient’s illness and/or treatment on family. The interviewer explores these issues.
- Score a 3 if the interviewer recognizes the impact of the illness or treatment on the family members and on family lifestyle but fails to explore these issues adequately.
- Score a 1 if the interviewer fails to address the impact of the illness or treatment on the family members and on family lifestyle.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the criteria, evaluate the interviewer's consideration of the illness's impact on the patient's family and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "SUPPORT SYSTEMS": """
Assess the interviewer's exploration of the patient’s support systems, including emotional, financial support, and access to healthcare, with the following scoring:

- Score a 5 if the interviewer determines 1. what emotional support the patient has. 2. what financial support the patient has and learns about health care access 3. about other resources available to the patient and family and suggests appropriate community resources. (in focused histories limited to what patient needs to manage impact; one thing is sufficient).
- Score a 3 if the interviewer determines some of the available support.
- Score a 1 if the interviewer fails to determine what support is currently available to the patient.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Evaluate the conversation for how well the interviewer identifies and addresses the patient's support systems and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "PATIENT’S EDUCATION & UNDERSTANDING": """
Consider the interviewer's effort to educate the patient about their condition and to assess the patient’s understanding, scoring as follows:

- Score a 5 if when patient education is a goal, the interviewer determines the patient’s level of interest and provides education appropriately. The interviewer uses a teach back to check the patient’s understanding of information given during the interview. Techniques may include asking the patient to repeat information, asking if the patient has additional questions, posing hypothetical situations or asking the patient to demonstrate techniques.
- Score a 3 if the interviewer asks if the patient understands the information but does not use the teach back technique. Some attempt to determine the interest in patient education but could be more thorough.
- Score a 2 if the interviewer gives info but does not check on understanding.
- Score a 1 if the interviewer fails to assess patient’s level of understanding and does not effectively correct misunderstandings when they are evident. AND/OR The interviewer fails to address the issue of patient education.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Analyze the interviewer's approach to patient education and understanding, and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "ASSESS MOTIVATION FOR CHANGES": """
Evaluate the interviewer's approach to assessing the patient's motivation for lifestyle or behavioral changes, with the following criteria:

- Score a 5 if the interviewer inquires how the patient feels about the lifestyle/behavioral change and gives information appropriate to patient’s level of readiness.
- Score a 3 if the interviewer inquires how the patient feels about changes but does not follow-up appropriately.
- Score a 1 if the interviewer fails to assess patient’s level of motivation to change and does not offer any options or plans or assumes patient’s readiness for change.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}


Based on the criteria, assess how well the interviewer evaluates and supports the patient's motivation for changes and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "ADMITTING LACK OF KNOWLEDGE": """
Evaluate the interviewer's willingness to admit lack of knowledge and their approach to seeking accurate information, considering:

- Score a 5 if the interviewer, when asked for information or advice that interviewer is not equipped to provide, admits to lack of knowledge in that area but immediately offers to seek resources to answer the question(s).
- Score a 3 if the interviewer, when asked for information or advice that interviewer is not equipped to provide, admits lack of knowledge, but rarely seeks other resources for answers.
- Score a 1 if the interviewer, when asked for information, which interviewer is not equipped to provide, makes up answers in an attempt to satisfy the patient’s questions, but never refers to other resources.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Analyze the conversation for instances where the interviewer admits a lack of knowledge and how they address it, assigning a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "INFORMED CONSENT FOR INVESTIGATIONS & PROCEDURES": """
Assess how the interviewer discusses investigations and procedures, including risks, benefits, and alternatives, using the following criteria:

- Score a 5 if the interviewer discusses the purpose and nature of all investigations and procedures. The interviewer reviews foreseeable risks and benefits of the proposed investigation or procedure. The interviewer discloses alternative investigations or procedures and their relative risks and benefits. Taking no action is considered always considered an alternative.
- Score a 3 if the interviewer discusses some aspects of the investigations and procedures but omits some elements of informed consent.
- Score a 1 if the interviewer fails to discuss investigations or procedures.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Evaluate the interviewer's approach to informed consent for investigations and procedures, and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "ACHIEVE A SHARED PLAN": """
Consider the interviewer's effectiveness in discussing the diagnosis or prognosis and negotiating a plan with the patient, including:

- Score a 5 if the the interviewer discusses the diagnosis and/or prognosis and negotiates a plan with the patient. The interviewer invites the patient to contribute own thoughts, ideas, suggestions and preferences.
- Score a 3 if the interviewer discusses the diagnosis and/or prognosis and plan but does not allow the patient to contribute. Lacks full quality.
- Score a 1 if the interviewer fails to discuss diagnosis and/or prognosis.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Assess the conversation for how well a shared plan is achieved, encouraging patient involvement, and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "ENCOURAGEMENT OF QUESTIONS": """
Evaluate the interviewer's encouragement for the patient to ask questions throughout the interview, with the following scoring:

- Score a 5 if the interviewer encourages the patient to ask questions at the end of a major subsection. The interviewer gives the patient the opportunity to bring up additional topics or points not covered in the interview. Two opportunities including one at the end of the interview.
- Score a 4 only one opportunity, at the end.
- Score a 3 one opportunity for questions but not near the end of the encounter.
- Score a 2 if the interviewer does not specifically ask if there are questions, but the climate and the pace of the interview allow them.
- Score a 1 if the interviewer fails to provide the patient with the opportunity to ask questions or discuss additional points. The interviewer may discourage the patient’s questions.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Based on the criteria, analyze the interviewer's encouragement of patient questions and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
""",

    "CLOSURE": """
Assess the effectiveness of the interview's closure, considering the clarity and completeness of future plans, using the following guidelines:

- Score a 5 at the end of the interview the interviewer clearly specifies the future plans: What the interviewer will do (leave and consult, make referrals) What the patient will do (wait, make diet changes, go to Physical Therapy); When (the time of the next communication or appointment.)
- Score a 3 if at the end of the interview, the interviewer partially details the plans for the future.
- Score a 1 if at the end of the interview, the interviewer fails to specify the plans for the future and the patient leaves the interview without a sense of what to expect. There is no closure whatsoever.

Provide your response in a json format with your explanation and the assigned score. Always quote the Physician questions or responses from the conversation to support your explanation.
{"explanation":explanation, "score": score}

Evaluate the conversation for how effectively the interview is concluded, focusing on the clarity and completeness of closure, and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation.
"""
}



