# nojson_mirs_prompts.py

nojson_mirs_prompts = {

    "OPENING": """
<instructions>
  <welcome>Welcome to the evaluator training module for assessing the opening of medical interviews. This session employs a chain-of-thought approach within an n-shot learning framework, providing detailed examples to guide your evaluations through structured and detailed reasoning.</welcome>
  <evaluation_rubric>
    <score_5>Complete introduction with self-introduction, role clarification, and polite patient address inquiry using the patient’s name.</score_5>
    <score_4>One element missing from the introduction.</score_4>
    <score_3>Two elements missing from the introduction.</score_3>
    <score_2>Only a basic greeting, such as 'hello', with most elements missing.</score_2>
    <score_1>No introduction provided.</score_1>
  </evaluation_rubric>
  <examples>
    <example>
      <score>5</score>
      <conversation_excerpt>"Hello, I am Dr. Carter, your cardiologist for today. How should I address you?"</conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Elements listed include self-introduction ("I am Dr. Carter"), role specification ("your cardiologist for today"), and patient address inquiry ("How should I address you?").</step>
        <step number="2">Consistency Check: All elements match the full introduction criteria.</step>
        <step number="3">Synthesize and Score: As no elements are missing, the score is 5.</step>
        <step number="4">Justify the Score: The score of 5 is fully justified as the introduction meets all the criteria, demonstrating a complete and respectful engagement.</step>
      </CoT_analysis>
    </example>
    <example>
      <score>4</score>
      <conversation_excerpt>"Hello, I am Dr. Carter, your cardiologist. What brings you in today?"</conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Elements listed include self-introduction ("I am Dr. Carter") and role specification ("your cardiologist").</step>
        <step number="2">Consistency Check: Missing the patient address inquiry.</step>
        <step number="3">Synthesize and Score: With one element missing, the score is 4.</step>
        <step number="4">Justify the Score: The lack of a patient address inquiry results in a deduction, justifying the score of 4.</step>
      </CoT_analysis>
    </example>
    <example>
      <score>3</score>
      <conversation_excerpt>"Hello, I'm the nurse on duty."</conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Elements noted include role specification ("nurse on duty").</step>
        <step number="2">Consistency Check: Missing self-introduction and patient address inquiry.</step>
        <step number="3">Synthesize and Score: Two key elements missing, thus the score is 3.</step>
        <step number="4">Justify the Score: The absence of self-introduction and a patient address inquiry justifies the score of 3.</step>
      </CoT_analysis>
    </example>
    <example>
      <score>2</score>
      <conversation_excerpt>"Hello, what brings you in today?"</conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Only a basic greeting is noted.</step>
        <step number="2">Consistency Check: Lacking self-introduction, role clarification, and patient address inquiry.</step>
        <step number="3">Synthesize and Score: As most key elements are missing, the score is 2.</step>
        <step number="4">Justify the Score: The minimal introduction provided, which lacks the necessary elements of a complete and polite interview opening, justifies the score of 2.</step>
      </CoT_analysis>
    </example>
    <example>
      <score>1</score>
      <conversation_excerpt>"What brings you in today?"</conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: No greeting or introduction elements.</step>
        <step number="2">Consistency Check: No elements present.</step>
        <step number="3">Synthesize and Score: No introduction; assigns score of 1.</step>
        <step number="4">Justify the Score: No introduction elements are present at all, justifying the lowest score.</step>
      </CoT_analysis>
    </example>
  </examples>
  <task>Apply the chain of thought process to analyze a provided conversation excerpt from a medical interview. Use the steps outlined to evaluate, score, and justify your evaluation comprehensively.</task>
  <response_format>
    <response>
      <explanation>Detail each step of your analysis, citing direct quotes from the conversation to support your score.</explanation>
      <score>Provide the score based on your comprehensive analysis</score>
    </response>
  </response_format>
</instructions>
""",




    "ELICITS SPECTRUM OF CONCERNS": """
<instructions>
  <welcome>Welcome to the evaluator training module focusing on 'ELICITS SPECTRUM OF CONCERNS' in medical interviews. This session will guide you through a structured evaluation process using the Chain of Thought approach to assess interactions based on their completeness and depth.</welcome>
  <evaluation_rubric>
    <score_5>The interviewer elicits the patient’s full spectrum of concerns at the beginning of the interview, asking broad questions like 'Is there anything else?' until the patient confirms there are no additional concerns.</score_5>
    <score_4>The interviewer elicits most concerns but may miss one follow-up opportunity to ask for additional issues.</score_4>
    <score_3>The interviewer elicits only the main concern or few concerns but does not adequately explore if there are other issues.</score_3>
    <score_2>The interviewer mentions concerns but does not engage the patient to explore them further or ask if there are additional issues.</score_2>
    <score_1>The interviewer fails to elicit any concerns from the patient, focusing solely on procedural or unrelated topics without addressing patient's issues.</score_1>
  </evaluation_rubric>
  <examples>
    <example>
      <score>5</score>
      <conversation_excerpt>
        Physician: "I'm Dr. Lee, and I'll be looking after you today. What brings you in, and is there anything else we should discuss right away?"
        Patient: "I've been having some chest pain since yesterday."
        Physician: "I see, and aside from the chest pain, is there anything else that's been troubling you?"
        Patient: "Now that you mention it, I've also been feeling very tired."
        Physician: "Got it, we'll definitely look into both. Anything else?"
        Patient: "No, that's all."
      </conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Physician systematically asks for primary concern and then follows up multiple times to ensure no other issues are missed.</step>
        <step number="2">Consistency Check: Each follow-up aligns with the highest rubric criteria, ensuring all concerns are surfaced.</step>
        <step number="3">Synthesize and Score: Since the physician confirmed there are no additional issues after repeated inquiries, the interaction earns a score of 5.</step>
        <step number="4">Justify the Score: Fully justified as the physician's questions covered all potential concerns the patient might have, adhering to the top standards of patient engagement.</step>
      </CoT_analysis>
    </example>
    <example>
      <score>4</score>
      <conversation_excerpt>
        Physician: "Good morning, I’m Dr. Smith. What issues brought you here today?"
        Patient: "I have been experiencing some back pain."
        Physician: "I understand. We'll definitely address that. Is there anything else you think we should look into?"
        Patient: "Well, I sometimes feel a bit dizzy too."
        Physician: "Alright, we'll explore both issues. Thank you for letting me know."
      </conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Physician identifies main and secondary concern but stops after one follow-up.</step>
        <step number="2">Consistency Check: Missing additional follow-ups that could reveal more concerns.</step>
        <step number="3">Synthesize and Score: A near-complete elicitation but lacks one final prompt to cover absolutely all concerns, fitting a score of 4.</step>
        <step number="4">Justify the Score: Justified as the physician nearly reaches full coverage of concerns but stops slightly short.</step>
      </CoT_analysis>
    </example>
    <example>
      <score>3</score>
      <conversation_excerpt>
        Physician: "Tell me what problems you're facing today."
        Patient: "I've been feeling really anxious lately."
        Physician: "I see, let's talk about what might be causing your anxiety."
      </conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Main concern is elicited without further probing for any additional issues.</step>
        <step number="2">Consistency Check: No attempt to ask if there are other concerns besides anxiety.</step>
        <step number="3">Synthesize and Score: Elicitation focuses only on one concern, justifying a score of 3.</step>
        <step number="4">Justify the Score: Justified by the lack of breadth in the elicitation process, focusing only on the initial concern.</step>
      </CoT_analysis>
    </example>
    <example>
      <score>2</score>
      <conversation_excerpt>
        Physician: "What seems to be the problem?"
        Patient: "I've had some headaches."
        Physician: "Headaches can be tough. We'll check into that."
      </conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Physician only acknowledges the concern stated by the patient without asking for more details or other concerns.</step>
        <step number="2">Consistency Check: No elicitation beyond acknowledging the stated problem.</step>
        <step number="3">Synthesize and Score: The physician’s engagement is minimal, meriting a score of 2.</step>
        <step number="4">Justify the Score: Justified as the physician does not explore the issue deeply nor inquire about additional concerns.</step>
      </CoT_analysis>
    </example>
    <example>
      <score>1</score>
      <conversation_excerpt>
        Physician: "Let's get started with your check-up. Any changes since last time?"
        Patient: "Actually, I've been experiencing some new pains."
        Physician: "We'll note that down. Let's proceed with the routine checks."
      </conversation_excerpt>
      <CoT_analysis>
        <step number="1">Sketchpad Listing: Physician ignores the new concerns mentioned by the patient, focusing only on procedural tasks.</step>
        <step number="2">Consistency Check: No attempt to explore or acknowledge the new pains described by the patient.</step>
        <step number="3">Synthesize and Score: The physician’s failure to elicit any information about the patient’s concerns results in a score of 1.</step>
        <step number="4">Justify the Score: Justified as the physician completely disregards the patient’s expressed concerns, focusing solely on routine procedures.</step>
      </CoT_analysis>
    </example>
  </examples>
  <task>Using the provided conversation excerpts, apply the chain of thought process to analyze and score the interviewer's effectiveness at eliciting the patient's full spectrum of concerns. Follow the steps outlined and ensure your evaluations are comprehensive and justified.</task>
  <response_format>
    <response>
      <explanation>Detail each step of your analysis, citing direct quotes from the conversation to support your score.</explanation>
      <score>Enter the score based on your comprehensive analysis.</score>
    </response>
  </response_format>
</instructions>""",



    "NEGOTIATES PRIORITIES & SETS AGENDA": """
Consider the following criteria for evaluating how the interviewer negotiates priorities of patient concerns, lists all of the concerns, and sets the agenda at the onset of the interview with the patient’s agreement:

Score 5: The interviewer negotiates priorities of patient concerns as gathered, listing all of the concerns, and sets the agenda at the onset of the interview, obtaining the patient’s agreement.
Score 4: The full agenda is set before all concerns are completely elicited.
Score 3: The interviewer sets an agenda but does not negotiate priorities with the patient.
Score 2: The interviewer lists some concerns but does not set an agenda or negotiate priorities.
Score 1: The interviewer does not negotiate priorities or set an agenda, focusing only on the chief concern and considering only the physician’s needs.

Examples:
Good Example:
Conversation Excerpt: Physician: "Okay. All right. Well, it sounds like the fatigue has been quite troubling for you recently. Let’s prioritize that for today’s discussion. I also notice you mentioned concerns about your diet changes. We'll definitely touch on that as well. How does it sound if we start with the fatigue and then move on to discuss your dietary concerns? We might also consider setting another appointment to cover anything else in depth. Does that approach work for you?"
Patient: "Yeah, that sounds good."
Explanation: The physician's approach, as quoted, "Let’s prioritize that for today’s discussion... How does it sound if we start with the fatigue and then move on to discuss your dietary concerns?" clearly shows effective negotiation of priorities and setting of the agenda. By asking for confirmation with "Does that approach work for you?" the physician ensures the patient’s agreement to the proposed plan, demonstrating excellent patient-centered communication and agenda setting. Therefore, this conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt: Physician: "I see you're here for headaches. We'll start with that. What medication have you been taking?"
Patient: "I also have some concerns about my sleep and stress levels."
Physician: "Okay, we might cover those later if there's time. Let’s keep the focus on the headaches for now."

Explanation: In this conversation, the physician acknowledges the patient's additional concerns about sleep and stress but decides to defer them, emphasizing the chief complaint of headaches instead. By saying, "We might cover those later if there's time," the physician does not effectively negotiate priorities or engage in setting a collaborative agenda with the patient. This shows a disregard for the patient's input on their own health priorities, resulting in a conversation that prioritizes the physician’s agenda over the patient's broader health concerns. Therefore, this conversation would score a 1.
Score: 1

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

Examples:
Good Example:
Conversation Excerpt:
Physician: "Tell me about what's been happening with your health recently."
Patient: "It started a few months ago with some mild discomfort, and then..."
Physician: [Listens attentively, nodding, making notes without interrupting]
Patient: "...and that's why I'm really concerned about these symptoms now."
Physician: "Thank you for sharing that. It helps me understand your situation better. Let’s discuss what might be causing these symptoms."

Explanation: The physician effectively facilitates a full narrative from the patient, allowing them to express their concerns without interruption, which helps in building a comprehensive understanding of the patient’s issues. This approach fosters a better diagnostic process and patient rapport. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "So, what brings you in today?"
Patient: "Well, I've been having some pain in my—"
Physician: "Where is the pain? When did it start? Have you taken anything for it?"
Patient: "It’s in my back, it started last week, and I—"
Physician: "Okay, let’s do some tests and I’ll prescribe something for the pain."

Explanation: The physician interrupts the patient's attempt to tell their story, turning the conversation into a series of quick questions and answers. This disrupts the narrative flow, making it difficult for the patient to fully express their concerns, potentially missing critical information. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "TIMELINE": """
Consider how well the interviewer establishes a timeline of the chief concern and history of the present illness, including the following scoring criteria:

Score 5: The interviewer obtains sufficient information to establish a clear chronology of the chief concern and history of the present illness, including the sequence of associated symptoms and/or events.
Score 3: The interviewer obtains some of the necessary information but fails to establish a complete chronology for all associated symptoms and events.
Score 1: The interviewer fails to obtain any information necessary to establish a timeline or chronology of the patient’s concerns.

Examples:
Good Example:
Conversation Excerpt:
Physician: "Let's start from when you first noticed something was off. Can you walk me through what happened next and how things progressed?"
Patient: "Yes, it started with feeling unusually tired after my usual morning jog about two months ago. A few days later, I noticed my heart was racing even at rest. By the end of that week, I was also experiencing shortness of breath."
Physician: "And how did these symptoms change or develop over the next few weeks?"
Patient: "The shortness of breath got worse, and two weeks ago, I began having mild chest pains occasionally, especially in the evenings."
Physician: "Has there been anything else accompanying these symptoms or any variation in their intensity?"
Patient: "Yes, last week, the chest pains became more frequent, and I noticed swelling in my legs."

Explanation: The physician effectively maps out a detailed and sequential timeline, starting from the initial symptom of unusual fatigue and progressing to more severe symptoms like chest pains and swelling. The physician's structured questions, such as "And how did these symptoms change or develop over the next few weeks?" and "Has there been anything else accompanying these symptoms or any variation in their intensity?" help to establish a comprehensive chronology of the events, crucial for diagnosis and treatment planning. Therefore, this conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "So you're having chest pains, how long has that been happening?"
Patient: "It's been a few weeks."
Physician: "Okay, and how severe are these pains?"
Patient: "They're quite bad sometimes."
Physician: "Alright, we’ll look into that."

Explanation: In this conversation, the physician fails to establish a detailed timeline of the chief concern and history of the present illness. The physician's questions are brief and lack depth, missing the opportunity to inquire about the sequence of symptoms or any associated events. The patient's responses are not probed further to clarify the onset, progression, or fluctuations in symptoms. This results in a lack of chronological understanding of the patient's condition, which is crucial for accurate diagnosis and effective treatment planning. Therefore, this conversation would score a 1.
Score: 1

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ORGANIZATION": """
Assess the organization of the interview, considering if the questions follow a logical order and if the effective use of time ensures that tasks are completed within the allotted time. Use the following criteria for scoring:

Score 5: Questions in the body of the interview follow a logical order to the patient, with effective use of time so tasks are completed within the time allowed.
Score 3: The interviewer seems to follow a series of topics or agenda items, but there are a few minor disjointed questions.
Score 1: The interviewer asks questions that seem disjointed and unorganized, affecting the interview's flow.

Examples:
Good Example:
Conversation Excerpt:
Physician: "How have you been feeling overall these past few weeks?"
Patient: "Not great, I've been really tired."
Physician: "Can you tell me more about when the tiredness usually occurs?"
Patient: "It's mostly in the mornings, but sometimes after lunch as well."
Physician: "Have there been any recent changes in your diet or daily routines that might correlate with this tiredness?"
Patient: "Now that you mention it, yes, I've been skipping breakfast often because of my early meetings."
Physician: "Let's explore that further. Have you noticed any other symptoms like headaches or dizziness?"
Patient: "Actually, yes, there have been a few headaches in the past week."

Explanation: The physician’s questions follow a logical order that builds on the information provided by the patient, each question naturally leading into the next. The discussion progresses smoothly from general health to specific symptoms, effectively using the interview time to gather comprehensive data about the patient’s condition. Therefore, this conversation would score a 5. 
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Have you noticed any changes in your appetite?"
Patient: "Yes, I've been eating less."
Physician: "Okay. Have you had any recent travels?"
Patient: "No, not recently."
Physician: "What about your exercise routine? Has it changed?"
Patient: "It's the same as usual."
Physician: "Do you have any joint pain or stiffness?"
Patient: "No, nothing like that."

Explanation: The physician's questions appear random and do not follow a logical or coherent order, jumping from dietary changes to travel history, then to exercise routines and joint health without any clear connection or follow-up on the initial concern of decreased appetite. This disjointed questioning disrupts the flow of the interview, making it challenging to build a comprehensive understanding of the patient's health status. The lack of organization affects the effectiveness of the interview and likely does not make the best use of the allotted time. Therefore, this conversation would score a 1.
Score: 1

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "TRANSITIONAL STATEMENTS (only for complete histories)": """
Evaluate the use of transitional statements by the interviewer, which explain the reasons for progressing from one section to another, with the following scoring guidelines:

Score 5: The interviewer utilizes transitional statements effectively throughout the interview, clarifying the interview's structure for the patient.
Score 3: The interviewer sometimes uses effective transitional statements but fails to do so consistently or some statements lack clarity.
Score 1: The interviewer progresses from one subsection to another in such a manner that the patient is left with a feeling of uncertainty as to the purpose of the questions. No transitional statements are made.

Examples:
Good Example:
Conversation Excerpt:
Physician: "Now that we've discussed your current symptoms, I'd like to go back to when you first noticed these issues to understand their onset better."
Patient: "Okay, that makes sense."
Physician: "You mentioned earlier feeling tired. Let’s explore how this has impacted your daily activities to get a clearer picture of your overall health status."
Patient: "Sure, I've definitely been less active."

Explanation: The physician uses effective transitional statements such as, "Now that we've discussed your current symptoms, I'd like to go back to when you first noticed these issues," which helps the patient understand the shift from discussing current symptoms to reviewing their onset. Another clear transition is indicated with, "Let’s explore how this has impacted your daily activities," seamlessly moving the discussion to the effects of the symptoms, thus maintaining clarity and context throughout the interview. Therefore, this conversation would score a 5.

Score: 5

Poor Example:
Conversation Excerpt:
Physician: "How often do you exercise?"
Patient: "About three times a week."
Physician: "Do you have any allergies?"
Patient: "Yes, I'm allergic to penicillin."
Physician: "What medications are you currently taking?"
Patient: "I take a blood pressure pill each morning."

Explanation: The physician moves from discussing exercise habits directly to inquiring about allergies and then to medication usage without using any transitional statements. This abrupt shift between topics can leave the patient feeling confused about the relevance and connection between questions. There is no explanation provided by the physician on why they are moving from one topic to another, resulting in a disjointed and potentially disorienting experience for the patient. Therefore, this conversation would score a 1.
Score: 1

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "PACING OF INTERVIEW (not based on finishing on time)": """
Consider the pacing of the interview, focusing on the interviewer's attentiveness, the smooth progression of the interview, and the deliberate use of silence, scoring as follows:

Score 5: The interviewer is fully attentive to the patient’s responses, listens without interruption, and the interview progresses smoothly without awkward pauses. Silence is used deliberately.
Score 3: The pace of the interview is generally comfortable, but there are occasional interruptions or awkward pauses.
Score 1: The interviewer frequently interrupts the patient, with several awkward pauses breaking the flow of the interview.

Examples:
Good Example:
Conversation Excerpt:
Physician: "I noticed you mentioned earlier that you've been having trouble sleeping. Can you tell me more about when that started?"
Patient: "Yes, it's been about three weeks now. I just lie there, unable to sleep."
Physician: [Silently nods, giving the patient a moment to continue] "That sounds difficult. How has this affected your day-to-day activities?"
Patient: "I'm always tired now, and it's hard to concentrate at work."

Explanation: The physician exhibits full attentiveness to the patient's concerns about trouble sleeping and allows space for the patient to express the impact of this issue. The interviewer's use of silence after the patient's initial response encourages further details, enhancing the flow of the interview without rushing or interrupting, which demonstrates a well-paced and patient-centered approach. Therefore, this conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "So, you've been feeling unwell. Tell me about that."
Patient: "Well, it started with some fatigue, and then I—"
Physician: "Fatigue, got it. And are you taking any medications?"
Patient: "Yes, I've been on—"
Physician: "Okay, and any family history we should know about?"

Explanation: The physician frequently interrupts the patient, cutting off their explanations about symptoms and medications. These interruptions disrupt the flow of the conversation and likely make the patient feel unheard. Additionally, the rapid progression from one question to another without allowing the patient sufficient time to answer fully creates a rushed and uncomfortable environment. This lack of smooth pacing and deliberate use of silence negatively affects the quality of the interview. Therefore, this conversation would score a 1.
Score: 1

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "QUESTIONING SKILLS – TYPES OF QUESTIONS": """
Analyze the types of questions used by the interviewer, considering the sequence and appropriateness of open-ended versus specific questions, and score as follows:

Score 5: The interviewer begins information gathering with an open-ended question, follows up with more specific or direct questions, and each major line of questioning is begun with an open-ended question. No poor question types are used.
Score 3: The interviewer often fails to start a line of inquiry with open-ended questions, relying instead on specific or direct questions, or occasionally uses leading, why, or multiple questions.
Score 1: The interviewer frequently uses why questions, multiple questions, or leading questions, detracting from the quality of information gathered.

Examples:
Good Example:
Conversation Excerpt:
Physician: "Can you describe what a typical day looks like for you now, considering your current health?"
Patient: "Well, I usually start feeling tired by mid-morning, and I have to take breaks more often than before."
Physician: "What specific times do you find yourself needing to take these breaks?"
Patient: "It's usually around 10 AM and then again at about 2 PM."

Explanation: The physician starts the inquiry with an open-ended question, "Can you describe what a typical day looks like for you now, considering your current health?" which allows the patient to provide information freely. This is followed by a more specific question, "What specific times do you find yourself needing to take these breaks?" effectively narrowing down the inquiry to gather detailed information without leading the patient. This sequence of questioning facilitates a comprehensive understanding while maintaining a patient-centered approach. Therefore, this conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Do you get tired after you exercise?"
Patient: "Yes, more than usual."
Physician: "Why do you think you're getting tired? Is it because you're not sleeping well or maybe you're not eating properly?"
Patient: "I'm not sure, maybe it's a bit of both. I've also been stressed."

Explanation: The physician starts with a specific question, "Do you get tired after you exercise?" which limits the patient's response. Furthermore, the follow-up is a combination of a 'why' question and multiple questions packed into one, "Why do you think you're getting tired? Is it because you're not sleeping well or maybe you're not eating properly?" This could confuse the patient and detract from the quality of information gathered by leading the patient's responses and not allowing them to freely express what they consider significant. This shows a poor use of questioning skills in the interview. Therefore, this conversation would score a 1.
Score: 1

Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

   "QUESTIONING SKILLS - SUMMARIZING": """
Evaluate how the interviewer summarizes the data obtained during the interview, using the following criteria for scoring:

Score 5: The interviewer summarizes the data obtained at the end of each major line of inquiry or subsection to verify and/or clarify the information. For a focused history, one summary at the end is sufficient.
Score 3: The interviewer summarizes data at the end of some lines of inquiry but not consistently, or the summary attempts are incomplete.
Score 1: The interviewer fails to summarize any of the data obtained.

Examples:
Good Example:
Conversation Excerpt:
Physician: "So today you've described experiencing a range of symptoms starting with headaches, moving to occasional dizziness, and you've also mentioned some recent issues with your vision. Let me make sure I've got everything: Your headaches began around three weeks ago, initially mild but have increased in frequency and intensity. The dizziness is sporadic, mostly in the mornings, and your vision issues started last week, primarily blurring when reading. Is all of this correct?"
Patient: "Yes, that's right."

Explanation: The physician effectively summarizes the patient’s symptoms, clearly restating the details provided to ensure there are no misunderstandings. This summary at the end of the major line of inquiry helps to verify the information with the patient, allowing any corrections or additional details to be added, which ensures a comprehensive understanding of the patient's health status. Therefore, this conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Okay, we've covered quite a bit today about your headaches and some of your lifestyle factors."
Patient: "Yes, we did."

Explanation: The physician’s statement, "Okay, we've covered quite a bit today about your headaches and some of your lifestyle factors," does not effectively summarize the data obtained during the interview. This statement is overly general and lacks any detailed recount of the specific information discussed, such as the onset, frequency, or triggers of the headaches, or detailed lifestyle factors that could influence these symptoms. There is no attempt to verify or clarify the information, nor does it provide the patient with an opportunity to correct or confirm the details. This omission could lead to misunderstandings and inaccuracies in diagnosing or planning further care. Therefore, this conversation would score a 1.
Score: 1


Task:
Based on the above criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",    


    "QUESTIONING SKILLS - DUPLICATION": """
Assess the interviewer's tendency to repeat questions seeking information that has already been provided, unless clarification or summarization is necessary, with scoring as follows:

Score 5: The interviewer does not repeat questions unnecessarily and only seeks repetition for clarification or summarization.
Score 3: The interviewer rarely repeats questions, and when questions are repeated, it is not for summarization or clarification but due to a lapse in memory.
Score 1: The interviewer consistently seeks information previously provided, showing a clear failure to track or remember patient information.

Examples:
Good Example:
Conversation Excerpt:
Physician: "Can you tell me when you first noticed your symptoms?"
Patient: "It started with a mild fever last Tuesday."
Physician: "Okay, and just to clarify, did any other symptoms accompany the fever at that time?"
Patient: "Yes, I also had some chills and a sore throat."
Physician: [Later in the conversation] "You mentioned earlier that the fever began last Tuesday. To summarize, along with the fever, you had chills and a sore throat, correct?"

Explanation: The physician revisits previously provided information not to ask redundant questions but to confirm and summarize the details for accuracy. This approach shows that the physician is tracking the patient's information attentively and using repetition strategically to ensure a clear and accurate understanding of the patient's symptoms. The use of duplication here is purposeful, aiding in clarifying and confirming the patient's health history, which enhances the quality of the medical interview. Therefore, this conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Have you experienced any nausea associated with your headaches?"
Patient: "Yes, I've had some nausea, mostly in the mornings."
Physician: [Five minutes later] "And you mentioned nausea, right? When does that usually occur?"
Patient: "As I said, it's mostly in the mornings."

Explanation: The physician unnecessarily repeats the question about nausea, asking for information that the patient had already provided earlier in the interview. This duplication indicates a failure to track or remember patient information effectively, which can disrupt the flow of the interview and potentially undermine the patient’s confidence in the physician’s attentiveness. Therefore, this conversation would score a 1.
Score: 1

Task:
Based on the criteria, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "QUESTIONING SKILLS - LACK OF JARGON": """
Evaluate the interviewer's use of language, focusing on how well they avoid medical jargon and ensure clarity of communication. Use the following criteria for scoring:

Score 5: The interviewer uses language that is easily understood by the patient, avoiding medical jargon entirely or explaining any technical terms immediately.
Score 3: The interviewer occasionally uses medical terms without definition, which may require clarification upon patient request.
Score 1: The conversation is dominated by medical jargon, making it inaccessible to the patient without definitions provided.

Examples:
Good Example:
Conversation Excerpt:
Physician: "You mentioned feeling an unusual tightness in your chest. Can you describe that feeling? Is it like a pressure or a squeezing sensation?"
Patient: "It's more like a squeezing feeling."
Physician: "That's helpful to know. Sometimes what you're describing is called 'angina,' which is just a medical term for chest pain caused by reduced blood flow to the heart muscle."

Explanation: The physician uses clear, patient-friendly language and immediately explains the medical term "angina" when it is used, ensuring the patient understands the discussion. This approach fosters effective communication and helps the patient feel more informed about their condition. Therefore, this conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Based on your symptoms, we're looking at a probable case of gastroesophageal reflux disease, which might be contributing to your dyspepsia."
Patient: "Sorry, I'm not sure what those terms mean."
Physician: "Ah, yes, those are quite technical. Gastroesophageal reflux disease is what you might know as acid reflux, and dyspepsia is just another word for indigestion."

Explanation: The physician initially uses complex medical terms "gastroesophageal reflux disease" and "dyspepsia" without providing definitions, making the conversation difficult for the patient to follow. Although the physician provides explanations later, the initial use of jargon without immediate clarification could confuse the patient and impede effective communication. Therefore, this conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "QUESTIONING SKILLS - VERIFICATION OF PATIENT INFORMATION (in vignette)": """
Evaluate how effectively the interviewer clarifies, verifies, and seeks specificity of the patient's responses during the interview. Use the following criteria for scoring:

Score 5: The interviewer consistently seeks to clarify, verify, and specify patient responses, ensuring an accurate understanding of the patient’s statements.
Score 3: Clarification, verification, and specificity are sought but not consistently, leading to some gaps in understanding.
Score 1: The interviewer fails to clarify or verify patient responses consistently, largely ignoring the need for accuracy.
Examples:

Good Example:
Conversation Excerpt:
Physician: "You mentioned feeling dizzy occasionally. Can you tell me more about what you're doing when these episodes occur?"
Patient: "Usually, it happens when I stand up too quickly."
Physician: "So it's mainly upon standing. Does this happen every time you stand up quickly, or are there certain times of the day when it's more likely to occur?"
Patient: "It's more in the mornings."

Explanation: The physician effectively clarifies and verifies the patient's initial vague statement about dizziness by asking specific follow-up questions. This helps the physician accurately understand the context and conditions under which the symptoms occur, ensuring comprehensive and accurate patient care. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "So, you've been feeling unwell, correct?"
Patient: "Yes, mostly tired and sometimes dizzy."
Physician: "Okay, let's talk about your diet then."

Explanation: The physician moves on without verifying the details about the patient's tiredness or the dizziness mentioned. There's a failure to seek specificity or further clarification about these symptoms, which could lead to misunderstandings or misdiagnosis, demonstrating a lack of thoroughness in patient care. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "INTERACTIVE TECHNIQUES": """
Evaluate the balance between patient-centered and physician-centered interviewing styles used by the interviewer. Use the following criteria for scoring:

Score 5: The interviewer consistently uses a patient-centered technique while effectively incorporating physician-centered elements that promote a collaborative partnership between patient and doctor.
Score 3: The interviewer initially uses a patient-centered style but reverts to a physician-centered approach at the end, rarely returning the lead to the patient. Alternatively, the interviewer uses only patient-centered interviewing without effectively incorporating physician-centered elements, failing to accomplish the negotiated agenda.
Score 1: The interview is dominated by a physician-centered approach, not following the patient’s lead, which halts the collaborative partnership.

Examples:
Good Example:
Conversation Excerpt:
Physician: "I'd like to hear more about how these symptoms are affecting your daily life."
Patient: "It's been tough, especially in the mornings."
Physician: "That sounds challenging. Let's see if we can adjust your medication to help with the mornings. What do you think about that plan?"
Patient: "That could really help, thank you."

Explanation: The physician uses a patient-centered approach by inviting the patient to share more about their experience and then incorporates a physician-centered element by suggesting a medication adjustment. This mix promotes a collaborative partnership, ensuring that the patient feels heard and involved in their care plan. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Based on your symptoms, we need to start treatment with a new medication regimen immediately."
Patient: "I've read some concerns about side effects of those medications. Could we discuss those a bit?"
Physician: "Right now, controlling your symptoms is our priority. We can discuss potential side effects during your next visit."

Explanation: In this conversation, the physician adopts a predominantly physician-centered approach, emphasizing treatment decisions without sufficient patient input. The patient's attempt to discuss their concerns about side effects is deferred to a future conversation, which can diminish the patient’s sense of involvement and trust in the care process. This lack of immediate engagement and responsiveness to the patient's concerns reflects a failure to maintain a collaborative partnership. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "VERBAL FACILITATION SKILLS": """
Evaluate the interviewer's verbal facilitation skills, focusing on how effectively they encourage the patient to share their story and participate in the conversation. Use the following criteria for scoring:

Score 5: The interviewer consistently encourages the patient throughout the interview by drawing out information using verbal encouragement, short statements, and echoing techniques. Praises are intermittently given for patient engagement or correct healthcare practices.
Score 3: The interviewer uses some verbal facilitation skills but not consistently or sometimes at inappropriate times. There is room for more effective use of verbal encouragement.
Score 1: The interviewer fails to use verbal facilitation skills to encourage the patient to tell their story or contribute to the conversation.

Examples:
Good Example:
Conversation Excerpt:
Physician: "It sounds like you've been quite diligent with your exercise routine. Can you tell me more about what you do?"
Patient: "I try to walk every morning."
Physician: "Every morning, that’s impressive! How has it been affecting your energy levels?"
Patient: "I've noticed I feel less tired during the day."
Physician: "That’s great to hear. It shows how your efforts are paying off."

Explanation: The physician effectively uses verbal facilitation skills by praising the patient’s efforts and encouraging them to share more about their experiences. The use of echoing and positive reinforcement helps to build rapport and draw out valuable information about the patient’s health behaviors. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "You mentioned you started exercising. What type?"
Patient: "I’ve been trying to walk more."
Physician: "Okay, and your medication?"
Patient: "I take it in the morning."
Physician: "Make sure it’s every morning."

Explanation: The physician briefly acknowledges the patient’s exercise but quickly moves on without using the opportunity to encourage further discussion or provide any verbal praise or encouragement. The conversation lacks facilitation skills that could help in building engagement or encouraging the patient to elaborate on their health practices. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "NON-VERBAL FACILITATION SKILLS": """
Evaluate the interviewer's use of non-verbal communication skills to put the patient at ease and facilitate engagement. Use the following criteria for scoring:

Score 5: The interviewer puts the patient at ease and facilitates effective communication using good eye contact, relaxed and open body language, appropriate facial expressions, eliminating physical barriers, and making appropriate physical contact.
Score 3: The interviewer utilizes some facilitative non-verbal techniques effectively, but could be more consistent. One or two techniques are not utilized effectively, or some physical barrier may still be present.
Score 1: The interviewer makes no attempt to put the patient at ease. The body language is negative or closed, annoying mannerisms such as foot or pencil tapping are present, or eye contact is lacking or uncomfortable.

Examples:
Good Example:
Conversation Excerpt:
Physician: "I understand this must be difficult for you. How are you feeling about everything?"
Patient: "It's been tough, honestly."
Physician: [Nods understandingly, maintains eye contact, leans forward slightly]

Explanation: The physician uses effective non-verbal cues to facilitate engagement and put the patient at ease. Good eye contact, open and inviting body posture, and an understanding nod all contribute to a comforting and communicative atmosphere. This approach helps the patient feel more comfortable and understood. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Tell me more about your symptoms."
Patient: "Well, I've been feeling..."
Physician: [Looks at computer screen, body turned away, makes no eye contact]

Explanation: The physician's non-verbal communication is poor, with the body turned away from the patient and attention focused on the computer screen instead of the patient. Lack of eye contact and closed body language do not facilitate an engaging or comforting environment. These non-verbal cues can make the patient feel neglected and uneasy. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "EMPATHY AND ACKNOWLEDGING PATIENT CUES": """
Evaluate the interviewer's ability to use supportive comments regarding the patient’s emotions and demonstrate empathy. Use the following criteria for scoring:

Score 5: The interviewer uses supportive comments regarding the patient’s emotions and employs techniques such as NURS (name, understand, respect, support) to demonstrate empathy effectively.
Score 3: The interviewer is neutral, neither particularly empathetic nor unsupportive, maintaining a balanced but not deeply empathetic stance.
Score 1: No empathy is demonstrated; the interviewer may use a negative emphasis or openly criticize the patient, showing a lack of sensitivity to the patient’s emotional state.

Examples:
Good Example:
Conversation Excerpt:
Physician: "It sounds like you've been under a lot of stress from these symptoms. It must be quite challenging for you."
Patient: "Yes, it's been very hard."
Physician: "I can only imagine how tough that is. We're here to support you through this and find ways to make you feel better."

Explanation: The physician effectively demonstrates empathy by acknowledging the patient’s stress and validating their feelings, using phrases that show understanding and support. The use of empathetic statements like "I can only imagine how tough that is" reflects a deep engagement with the patient's emotional state. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "You need to manage your stress better. Continuing like this will only make your condition worse."
Patient: "I've been trying, but it's not easy."
Physician: "Well, it's important for your health to make an effort."

Explanation: The physician's responses lack empathy and can be perceived as critical. By emphasizing what the patient should do without acknowledging the difficulty they are experiencing, the physician fails to demonstrate support or understanding of the patient’s emotional struggles. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "PATIENT’S PERSPECTIVE (BELIEFS; Case specific)": """
Evaluate how well the interviewer elicits and addresses the patient’s beliefs and perspective on their illness. Use the following criteria for scoring:

Score 5: The interviewer thoroughly elicits the patient’s perspectives, including their beliefs about the beginning of the illness, their feelings, ideas of cause, function, and expectations (FIFE), and actively addresses these beliefs.
Score 3: The interviewer elicits some of the patient’s perspectives on the illness but may not address all beliefs or fails to follow through in addressing these beliefs.
Score 1: The interviewer fails to elicit the patient’s perspective or beliefs about the illness.

Examples:
Good Example:
Conversation Excerpt:
Physician: "Can you share what you believe might be causing your symptoms?"
Patient: "I think it might be stress-related because it started when I changed jobs."
Physician: "That’s an important observation. Let’s explore how your job change has coincided with your symptoms and discuss how we can address the stress component as part of your treatment."

Explanation: This physician effectively elicits the patient's beliefs about the cause of their symptoms and acknowledges the patient's perspective, integrating it into the treatment discussion. This approach aligns with the FIFE model, ensuring a comprehensive understanding of the patient's views. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Your tests show you have high blood pressure. We need to start treatment immediately."
Patient: "Could my job stress be affecting my blood pressure?"
Physician: "It’s all about your diet and exercise. We’ll start you on medication."

Explanation: Although the patient attempts to discuss their belief that stress might be influencing their condition, the physician dismisses this perspective and focuses solely on a biomedical treatment approach. This neglects the patient's view and does not incorporate their beliefs into the care plan, missing an opportunity for a holistic approach. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "IMPACT OF ILLNESS ON PATIENT AND PATIENT’S SELF-IMAGE": """
Assess how the interviewer explores the effects of the illness on the patient's life and self-image. Use the following criteria for scoring:

Score 5: The interviewer inquires deeply about how the illness affects the patient's feelings and lifestyle changes. The interviewer explores these issues thoroughly and offers counseling or resources to support the patient.
Score 3: The interviewer addresses the impact of the illness on the patient's life or self-image only partially. The interviewer might not offer any additional support such as counseling or resources.
Score 1: The interviewer fails to acknowledge or explore the impact of the illness on the patient's life and self-image.

Examples:
Good Example:
Conversation Excerpt:
Physician: "How has this diagnosis impacted how you see yourself and your day-to-day activities?"
Patient: "It's been hard. I feel like I'm not the same person anymore."
Physician: "It's completely normal to feel that way. Let's discuss how we can help you cope with these changes. We have support groups and counseling services that might help you."

Explanation: The physician effectively inquires about the patient’s emotional response to the illness and its impact on their life, demonstrating an understanding and supportive approach. The offer of counseling and support groups shows a proactive effort to assist the patient in coping with these changes. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "You need to start treatment immediately. It's important to manage your symptoms effectively."
Patient: "I'm worried about how this will change my life. I feel very different now."
Physician: "The most important thing is to keep your symptoms under control."

Explanation: The physician ignores the patient's expressed concerns about the impact of the illness on their life and self-image, focusing solely on symptom management. This lack of acknowledgment of the patient's emotional and psychological needs would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "IMPACT OF ILLNESS ON FAMILY": """
Evaluate how the interviewer addresses the impact of the patient’s illness on their family. Use the following criteria for scoring:

Score 5: The interviewer inquires about the patient’s family structure and thoroughly addresses the impact of the patient’s illness and/or treatment on the family. The interviewer explores these issues in detail.
Score 3: The interviewer recognizes the impact of the illness or treatment on family members and lifestyle but does not explore these issues adequately.
Score 1: The interviewer fails to address the impact of the illness or treatment on the family members and their lifestyle.

Examples:
Good Example:
Conversation Excerpt:
Physician: "Can you tell me a bit about who lives at home with you and how they've been coping with your condition?"
Patient: "My spouse and two children. They are quite stressed, especially since I've been unable to work."
Physician: "It's important to consider how this affects them too. We have family counseling available, and I can also suggest some resources to help your family understand and cope with these changes."

Explanation: The physician effectively explores the structure of the patient’s family and directly addresses how the patient's illness affects them, showing a comprehensive understanding of the family dynamics. The offer of family counseling and resources indicates a thorough approach to the family's needs. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Make sure you follow the treatment plan so you can get back to your duties at home quickly."
Patient: "It's been tough on my family, especially my kids."
Physician: "Yes, let's focus on getting you better."

Explanation: The physician acknowledges the patient's statement about family challenges but does not explore or address the impact of the illness on the family further. This lack of engagement with the patient’s concerns about their family misses an opportunity to understand and support the patient’s familial context. This conversation would score a 1.
Score: 1

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

Examples:
Good Example:
Conversation Excerpt:
Physician: "Who do you have at home to support you emotionally during this time?"
Patient: "My sister has been very helpful."
Physician: "That’s good to hear. How are you managing financially with the treatment costs? And do you have reliable access to the healthcare services you need?"
Patient: "It's been difficult financially."
Physician: "Let me give you information about some community resources that can help with healthcare costs and additional support groups that might be beneficial for you and your sister."

Explanation: The physician effectively explores all critical aspects of the patient's support system, addressing emotional support, financial constraints, and healthcare access. Suggestions for community resources show a proactive approach to supporting the patient’s comprehensive needs. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "It’s important to stay positive and manage your treatment effectively."
Patient: "I’m struggling with this on my own, and it’s getting overwhelming."
Physician: "Just try to follow the treatment plan as best you can."

Explanation: The physician does not explore the patient’s lack of support or address their stated challenges, missing critical information about the patient’s emotional, financial, or healthcare support systems. This lack of engagement shows a failure to recognize and support the patient’s needs adequately. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "PATIENT’S EDUCATION & UNDERSTANDING": """
Evaluate the interviewer's efforts to educate the patient about their condition and to assess the patient's understanding. Use the following criteria for scoring:

Score 5: The interviewer determines the patient’s level of interest in learning about their condition, provides appropriate education, and uses the teach-back method to check the patient's understanding. Techniques may include asking the patient to repeat information, inquiring if the patient has additional questions, posing hypothetical situations, or asking the patient to demonstrate techniques.
Score 3: The interviewer asks if the patient understands the information but does not use teach-back techniques. There is some attempt to determine interest in patient education, but it could be more thorough.
Score 2: The interviewer provides information but does not check the patient’s understanding.
Score 1: The interviewer fails to assess the patient's level of understanding and does not effectively address misunderstandings when evident. The issue of patient education is also neglected.

Examples:
Good Example:
Conversation Excerpt:
Physician: "It's important that you understand how to manage your diabetes at home. Can you explain to me how you'll take your medication and what you should do if your blood sugar goes too high?"
Patient: "I take my medication in the morning and check my blood sugar. If it's too high, I'll..."
Physician: "That’s right, and remember to also..."

Explanation: The physician effectively educates the patient by first explaining the management of diabetes and then using the teach-back method to ensure the patient has understood the instructions clearly. This approach, combined with encouraging the patient to ask questions and providing additional clarification, exemplifies excellent patient education and engagement. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "You need to start taking these new medications for your hypertension. Take one pill in the morning and one in the evening."
Patient: "What should I do if I experience any side effects?"
Physician: "Just continue with the medication and we can discuss it during your next appointment."

Explanation: The physician gives basic instructions on how to take the medication but fails to adequately address the patient's concerns about potential side effects. There is no effort to check the patient's understanding of the treatment plan or to educate the patient about why they are taking these medications and how they work. The lack of responsiveness to the patient's question about side effects and the absence of a teach-back method to confirm understanding demonstrate poor patient education practices. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ASSESS MOTIVATION FOR CHANGES": """
Evaluate the interviewer's approach to assessing the patient's motivation for making lifestyle or behavioral changes. Use the following criteria for scoring:

Score 5: The interviewer inquires about how the patient feels regarding the lifestyle/behavioral change and tailors information and suggestions based on the patient's level of readiness.
Score 3: The interviewer asks about the patient's feelings toward changes but fails to follow up appropriately based on the patient's responses or readiness.
Score 1: The interviewer does not assess the patient's motivation to make changes, does not offer any options or plans, or incorrectly assumes the patient’s readiness for change.

Examples:
Good Example:
Conversation Excerpt:
Physician: "How do you feel about making some changes to your diet to help manage your diabetes?"
Patient: "I know it's important, but I find it hard to stick to diets."
Physician: "That's completely understandable. Let's start with small, manageable changes. How about we try integrating one healthy meal a day and see how that goes?"

Explanation: The physician effectively assesses the patient's motivation and readiness to change by first understanding their feelings and concerns about diet changes. By suggesting a gradual approach, the physician tailors the intervention to the patient's expressed level of readiness, enhancing the likelihood of successful behavioral change. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "You need to start exercising more regularly to improve your heart health."
Patient: "I've tried before, but I struggle with staying motivated."
Physician: "It's very important for your health. Try to make an effort."

Explanation: Although the physician identifies the need for change, they fail to assess or support the patient's motivation effectively. The physician's response lacks empathy and does not offer practical solutions or encouragement tailored to the patient's challenges with motivation. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ADMITTING LACK OF KNOWLEDGE": """
Evaluate the interviewer's willingness to admit a lack of knowledge and their approach to seeking accurate information. Use the following criteria for scoring:

Score 5: When asked for information or advice they are not equipped to provide, the interviewer admits their lack of knowledge but immediately offers to seek resources or consult colleagues to answer the question(s).
Score 3: The interviewer admits lack of knowledge when asked for information they cannot provide, but only rarely seeks other resources or help to find the answers.
Score 1: When asked for information they are not equipped to provide, the interviewer makes up answers in an attempt to satisfy the patient’s questions and does not refer to any other resources.

Examples:
Good Example:
Conversation Excerpt:
Patient: "Can this medication interact with my herbal supplements?"
Physician: "I'm not sure about the specific interaction with those supplements, but it's important to know. Let me consult with our pharmacist and get back to you with accurate information."

Explanation: The physician admits to not having immediate knowledge about the interaction between prescribed medication and herbal supplements but takes responsibility to find accurate information by consulting a pharmacist. This proactive approach shows a commitment to providing reliable and safe patient care. This conversation would score a 5.
Score: 5

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "INFORMED CONSENT FOR INVESTIGATIONS & PROCEDURES": """
Evaluate how the interviewer discusses investigations and procedures with the patient, focusing on the extent to which they cover the necessary aspects of informed consent. Use the following criteria for scoring:

Score 5: The interviewer thoroughly discusses the purpose and nature of all investigations and procedures, reviews foreseeable risks and benefits, discloses alternatives including their risks and benefits, and mentions that taking no action is always an alternative.
Score 3: The interviewer covers some aspects of the investigations and procedures but omits certain elements of informed consent, such as full disclosure of alternatives or specific risks and benefits.
Score 1: The interviewer fails to discuss the purpose, nature, risks, benefits, or alternatives of investigations or procedures adequately.

Examples:
Good Example:
Conversation Excerpt:
Physician: "We need to consider a biopsy to better understand the nature of this mass. The procedure will help us determine if it's benign or malignant. The risks include minor bleeding and infection, but these are generally rare. As alternatives, we could continue to monitor with imaging, though it won’t give us as definitive an answer as a biopsy. Choosing no action is also an option, but it carries its own risks of non-detection if the mass changes."
Patient: "What happens if I choose to wait and keep monitoring?"
Physician: "We can schedule regular scans to observe any changes, which allows us to act quickly if there's any development."

Explanation: This physician clearly outlines the purpose of the biopsy, its risks and benefits, and discusses alternative options including their respective risks and benefits. The inclusion of monitoring and taking no action as viable alternatives helps ensure the patient is fully informed. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "We should schedule you for a biopsy to check this area further."
Patient: "What does the biopsy involve?"
Physician: "It’s a simple procedure to get a better look at the issue. We can talk more on the day of the procedure."

Explanation: The physician mentions the biopsy but fails to discuss its nature, risks, or benefits in detail and does not mention any alternatives or the option of no action. The patient is left without crucial information necessary to make an informed decision, and the physician's suggestion to discuss details on the day of the procedure does not meet the standards of informed consent. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "ACHIEVE A SHARED PLAN": """
Evaluate the interviewer's effectiveness in discussing the diagnosis or prognosis with the patient and negotiating a treatment plan. Use the following criteria for scoring:

Score 5: The interviewer discusses the diagnosis and/or prognosis comprehensively and negotiates a treatment plan, inviting the patient to contribute their own thoughts, ideas, suggestions, and preferences.
Score 3: The interviewer discusses the diagnosis and/or prognosis and outlines a plan, but does not fully engage the patient in the planning process or allow for patient input, resulting in a lack of full quality in the shared decision-making process.
Score 1: The interviewer fails to discuss the diagnosis and/or prognosis with the patient, missing an opportunity to negotiate or even formulate a treatment plan.

Examples:
Good Example:
Conversation Excerpt:
Physician: "Based on your test results, it looks like you have Type 2 diabetes. Let’s discuss what this means for you and explore how we can manage it. What are your thoughts on treatment, and what approach would you prefer?"
Patient: "I've read about lifestyle changes and medications, but I'm not sure what would be best for me."
Physician: "Both are good options. We can start with some moderate lifestyle adjustments and see how much they help, and consider medications if your sugar levels aren't controlled. How does that sound?"

Explanation: The physician clearly explains the diagnosis and encourages the patient to participate in deciding the treatment approach, incorporating the patient’s initial thoughts and concerns into the planning. This ensures the plan aligns with the patient's preferences and lifestyle, making it a collaborative and supportive process. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "You have high blood pressure. We need to start you on medication right away."
Patient: "Are there other things I can do besides medication?"
Physician: "Medication is the best option. We'll start with that."

Explanation: While the physician provides a diagnosis, they fail to discuss the prognosis or engage the patient in the decision-making process, dismissing the patient's inquiry about alternatives. This lack of patient involvement does not foster a shared understanding or agreement on the treatment plan. This conversation would score a 1.
Score: 1

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

Examples:
Good Example:
Conversation Excerpt:
Physician: "We've discussed your treatment options for managing diabetes. Do you have any questions about what we’ve covered so far?"
Patient: "I'm curious about the side effects of these medications."
Physician: "That’s a great question. Let's go through them..."
[Later in the interview]
Physician: "Before we finish, do you have any other questions or is there anything else you'd like to discuss?"

Explanation: The physician provides multiple opportunities for the patient to ask questions and bring up additional concerns, first after discussing treatment options and again at the end of the interview. This fosters an open dialogue and ensures that the patient feels heard and involved in their care. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "So we will start with this new medication. I'll see you in six weeks for a follow-up."
Patient: "Could I ask about—"
Physician: "We're really pressed for time today, but we can get into more details next time."

Explanation: The physician not only fails to encourage questions but actively discourages them by citing time constraints. This prevents the patient from discussing their concerns or clarifying their understanding, which could lead to confusion or noncompliance with the treatment plan. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
""",

    "CLOSURE": """
Evaluate the effectiveness of the interview's closure by assessing the clarity and completeness of future plans. Use the following criteria for scoring:

Score 5: At the end of the interview, the interviewer clearly specifies the future plans, including actions to be taken by both the interviewer (such as making referrals or consultations) and the patient (such as dietary changes or appointments for therapy), along with clear timelines for the next communication or appointment.
Score 3: At the end of the interview, the interviewer partially details the future plans but leaves some aspects unclear or vague.
Score 1: At the end of the interview, the interviewer fails to specify any plans for the future, leaving the patient without a clear understanding of what to expect next. There is no closure whatsoever.

Examples:
Good Example:
Conversation Excerpt:
Physician: "We've covered a lot today. I will consult with a specialist about your case and make a referral for you to see them. You should start adjusting your diet as we discussed and begin the physical therapy sessions twice a week. Our office will call you by Tuesday to confirm the details of your referral and next appointment. Do you have any questions or concerns about what we’ve planned?"
Patient: "No, that sounds clear. Thank you."
Physician: "Great, we'll ensure everything is set up for you, and I look forward to seeing how you progress."

Explanation: This closure effectively summarizes the future plans with clear responsibilities assigned to both the physician and the patient, including specific follow-up actions and timelines. The physician also checks for any final questions, ensuring the patient leaves well-informed. This conversation would score a 5.
Score: 5

Poor Example:
Conversation Excerpt:
Physician: "Alright, so that's it for today. Make sure you follow the instructions we talked about."
Patient: "So, what exactly should I do next? Do I need to come back?"
Physician: "Just go ahead with the changes we discussed. We'll sort out the details later."

Explanation: The physician ends the interview without clear instructions or definite plans for follow-up, leaving the patient unsure about the next steps. There is no mention of specific actions, timelines, or follow-up appointments, resulting in a lack of closure. This conversation would score a 1.
Score: 1

Task:
Based on the above criteria and examples, analyze the provided conversation and assign a score from 1 to 5. Remember to quote the Physician questions or responses from the conversation to support your explanation. Use the format: Explanation: [Your Explanation], Score: [Your Score].
"""
}



