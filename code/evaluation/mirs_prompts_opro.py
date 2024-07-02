# mirs_prompts.py

instructions_start = """
Evaluate the conversation using the provided rubric below.
If no excerpts are provided, the score and explanation should both be "N/A" unless otherwise stated.
"""

instructions_end = """
Provide your response in the following json format without including the code block delimiters. 

### Response Format:
{
  "explanation": "Detail each step of your analysis, citing direct quotes from the conversation to support your score.",
  "score": "Provide the numeric score based on your comprehensive analysis"
}

Here is the conversation excerpt:
"""

mirs_prompts_opro = {
    "OPENING": """
Evaluate whether the excerpt contains a complete self-introduction, role clarification, and a polite inquiry about how to address the patient by name. 

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- Score of 5: Complete introduction with self-introduction, role clarification, and polite patient address inquiry using the patient’s name.
- Score of 4: One element missing from the introduction.
- Score of 3: Two elements missing from the introduction.
- Score of 2: Only a basic greeting, such as 'hello', with most elements missing.
- Score of 1: No introduction provided.

## Below are some exemplars for each score.
**Conversation Excerpt**: 
Physician: "Hello, I am Dr. Carter, your cardiologist for today. How should I address you?"
Score: 5

**Conversation Excerpt**: 
Physician: "Hello, I am Dr. Carter, your cardiologist. What brings you in today?"
Score: 4

**Conversation Excerpt**: 
Physician: "Hello, I'm the nurse on duty."
Score: 3

**Conversation Excerpt**: 
Physician: "Hello, what brings you in today?"
Score: 2

**Conversation Excerpt**: 
Physician: "What brings you in today??"
Score: 1

""",

    "ELICITS SPECTRUM OF CONCERNS": """
Evaluate how well the interviewer elicits the patient’s full spectrum of concerns within the first 3-5 minutes of the interview.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer elicits the patient’s full spectrum of concerns within the first 3-5 minutes of the interview. The interviewer asks 'what else' until no additional concerns are raised.
- Score a 4 if only one final 'what else' is missing but secondary concerns are addressed.
- (Average) Score a 3 if the interviewer only elicits the patient’s main concern without probing for additional concerns.
- Score a 2 if the interviewer merely states the concern without any elicitation.
- (Low) Score a 1 if the interviewer fails to elicit any of the patient’s concerns.

## Below are two exemplars. 
**Conversation Excerpt**: 
Physician: "What brings you in today? Is there anything else bothering you?"
Patient: "I’ve been having severe headaches."
Physician: "Okay, and what else?"
Patient: "Sometimes I feel dizzy too."
Physician: "Got it. Is there anything else that we should discuss today?"
Patient: "No, that’s all."
Score: 5

**Conversation Excerpt**: 
Physician: "What brings you in today?"
Patient: "I’ve been having severe headaches."
Physician: "I see, we'll look into that."
Score: 2

""",

    "NEGOTIATES PRIORITIES & SETS AGENDA": """
Evaluate the physician's approach to setting and negotiating the agenda with the patient, including how well the physician elicits patient concerns, sets a comprehensive agenda, and negotiates priorities at the onset of the interview.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- Score a 5 if the interviewer negotiates priorities of patient concerns as gathered, listing all of the concerns, and sets the agenda at the onset of the interview and gets the patient’s agreement to the agenda.
- Score a 4 if the full agenda is set before concerns are completely elicited.
- Score a 3 if the interviewer sets an agenda but does not negotiate priorities with the patient.
- Score a 2 if the interviewer lists some concerns but does not set an agenda or negotiate priorities.
- Score a 1 if the interviewer does not negotiate priorities or set an agenda. The interviewer focuses only on the chief concern and takes only the physician’s needs into account.
If the excerpt simply says "Physician does not negotiate priorities or set an agenda.", assign a score of 1. The explanation should just state "Physician does not negotiate priorities or set an agenda." and do not provide direct quotes.

## Below are some exemplars.
**Conversation Excerpt**: 
Physician: "Okay. All right. Well, it sounds like the fatigue has been quite troubling for you recently. Let’s prioritize that for today’s discussion. I also notice you mentioned concerns about your diet changes. We'll definitely touch on that as well. How does it sound if we start with the fatigue and then move on to discuss your dietary concerns? We might also consider setting another appointment to cover anything else in depth. Does that approach work for you?"
Patient: "Yeah, that sounds good."
Score: 5

**Conversation Excerpt**: 
Physician: "I see you're here for headaches. I'll start with that. What medication have you been taking?"
Patient: "I also have some concerns about my sleep and stress levels."
Physician: "Okay, we might cover those later if there's time. Let’s keep the focus on the headaches for now."
Score: 2

""",

    "ELICITING THE NARRATIVE THREAD or the ‘PATIENT’S STORY’": """
Evaluate the physician's effectiveness in encouraging and letting the patient talk about their problem. 

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer encourages the patient to share their story without interrupting, allowing for a complete narrative thread.
- Score a 4 if the interviewer asks the patient to tell them about a specific problem but does not allow for a complete narrative thread.
- (Average) Score a 3 if the interviewer generally allows the patient to talk but occasionally interrupts with focused questions or introduces unrelated topics.
- Score a 2 if the interviewer often interrupts the narrative with questions, setting a Q&A style rather than a conversational flow.
- (Low) Score a 1 if the interviewer fails to let the patient talk about their problem, dominating the conversation.

## Below are some exemplars.
**Conversation Excerpt**: 
Physician: "Tell me about what's been happening with your health recently."
Patient: "It started a few months ago with some mild discomfort, and then..."
Physician: [Listens attentively, nodding, making notes without interrupting]
Patient: "...and that's why I'm really concerned about these symptoms now."
Physician: "Thank you for sharing that. It helps me understand your situation better. Let’s discuss what might be causing these symptoms."
Score: 5

**Conversation Excerpt**: 
Physician: "So, what brings you in today?"
Patient: "Well, I've been having some pain in my—"
Physician: "Where is the pain? When did it start? Have you taken anything for it?"
Patient: "It’s in my back, it started last week, and I—"
Physician: "Okay, let’s do some tests and I’ll prescribe something for the pain."
Score: 1

""",

    "TIMELINE": """
Evaluate how well the physician establishes a timeline of the chief concern and history of the present illness.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- Score a 5 if the interviewer obtains sufficient information to establish a clear chronology of the chief concern and history of the present illness, including the sequence of associated symptoms and/or events.
- Score a 3 if the interviewer obtains some of the necessary information but fails to establish a complete chronology for all associated symptoms and events.
- Score a 1 if the interviewer fails to obtain any information necessary to establish a timeline or chronology of the patient’s concerns.

## Below are some exemplars.
**Conversation Excerpt**: 
Physician: "Let's start from when you first noticed something was off. Can you walk me through what happened next and how things progressed?"
Patient: "Yes, it started with feeling unusually tired after my usual morning jog about two months ago. A few days later, I noticed my heart was racing even at rest. By the end of that week, I was also experiencing shortness of breath."
Physician: "And how did these symptoms change or develop over the next few weeks?"
Patient: "The shortness of breath got worse, and two weeks ago, I began having mild chest pains occasionally, especially in the evenings."
Physician: "Has there been anything else accompanying these symptoms or any variation in their intensity?"
Patient: "Yes, last week, the chest pains became more frequent, and I noticed swelling in my legs."
Score: 5

**Conversation Excerpt**: 
Physician: "So you're having chest pains, how long has that been happening?"
Patient: "It's been a few weeks."
Physician: "Okay, and how severe are these pains?"
Patient: "They're quite bad sometimes."
Physician: "Alright, we’ll look into that."
Score: 1

""",

    "ORGANIZATION": """
Evaluate the physician's organization of the interview, considering if the questions follow a logical order and if the effective use of time ensures that tasks are completed within the allotted time.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if questions in the body of the interview follow a logical order to the patient, with effective use of time so tasks are completed within the time allowed.
- (Average) Score a 3 if the interviewer seems to follow a series of topics or agenda items, but there are a few minor disjointed questions.
- (Low) Score a 1 if the interviewer asks questions that seem disjointed and unorganized, affecting the interview's flow.

## Below are some exemplars.
**Conversation Excerpt**: 
Physician: "How have you been feeling overall these past few weeks?"
Patient: "Not great, I've been really tired."
Physician: "Can you tell me more about when the tiredness usually occurs?"
Patient: "It's mostly in the mornings, but sometimes after lunch as well."
Physician: "Have there been any recent changes in your diet or daily routines that might correlate with this tiredness?"
Patient: "Now that you mention it, yes, I've been skipping breakfast often because of my early meetings."
Physician: "Let's explore that further. Have you noticed any other symptoms like headaches or dizziness?"
Patient: "Actually, yes, there have been a few headaches in the past week."
Score: 5

**Conversation Excerpt**: 
Physician: "Have you noticed any changes in your appetite?"
Patient: "Yes, I've been eating less."
Physician: "Okay. Have you had any recent travels?"
Patient: "No, not recently."
Physician: "What about your exercise routine? Has it changed?"
Patient: "It's the same as usual."
Physician: "Do you have any joint pain or stiffness?"
Patient: "No, nothing like that."
Score: 1

""",

    "PACING OF INTERVIEW": """
Evaluate the pacing of the interview, focusing on the interviewer's attentiveness, the smooth progression of the interview, and the deliberate use of silence.

Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer is fully attentive to the patient’s responses, listens without interruption, and the interview progresses smoothly without awkward pauses. Silence is used deliberately.
- (Average) Score a 3 if the pace of the interview is generally comfortable, but there are occasional interruptions or awkward pauses.
- (Low) Score a 1 if the interviewer frequently interrupts the patient, with several awkward pauses breaking the flow of the interview.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "I noticed you mentioned earlier that you've been having trouble sleeping. Can you tell me more about when that started?"
Patient: "Yes, it's been about three weeks now. I just lie there, unable to sleep."
Physician: [Silently nods, giving the patient a moment to continue] "That sounds difficult. How has this affected your day-to-day activities?"
Patient: "I'm always tired now, and it's hard to concentrate at work."
Score: 5

**Conversation Excerpt**: 
Physician: "So, you've been feeling unwell. Tell me about that."
Patient: "Well, it started with some fatigue, and then I—"
Physician: "Fatigue, got it. And are you taking any medications?"
Patient: "Yes, I've been on—"
Physician: "Okay, and any family history we should know about?"
Score: 1

""",

    "QUESTIONING SKILLS – TYPES OF QUESTIONS": """
Evaluate the types of questions used by the physician, considering the sequence and appropriateness of open-ended versus specific questions, and score as follows:

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer begins information gathering with an open-ended question, follows up with more specific or direct questions, and each major line of questioning is begun with an open-ended question. No poor question types are used.
- (Average) Score a 3 if the interviewer often fails to start a line of inquiry with open-ended questions, relying instead on specific or direct questions, or occasionally uses leading, why, or multiple questions.
- (Low) Score a 1 if the interviewer frequently uses why questions, multiple questions, or leading questions, detracting from the quality of information gathered.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "Can you describe what a typical day looks like for you now, considering your current health?"
Patient: "Well, I usually start feeling tired by mid-morning, and I have to take breaks more often than before."
Physician: "What specific times do you find yourself needing to take these breaks?"
Patient: "It's usually around 10 AM and then again at about 2 PM."
Score: 5

**Conversation Excerpt**: 
Physician: "Do you get tired after you exercise?"
Patient: "Yes, more than usual."
Physician: "Why do you think you're getting tired? Is it because you're not sleeping well or maybe you're not eating properly?"
Patient: "I'm not sure, maybe it's a bit of both. I've also been stressed."
Score: 1

""",

   "QUESTIONING SKILLS - SUMMARIZING": """
Evaluate how the physician summarizes the data obtained during the interview.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer summarizes the data obtained at the end of each major line of inquiry or subsection to verify and/or clarify the information. For a focused history, one summary at the end is sufficient.
- (Average) Score a 3 if the interviewer summarizes data at the end of some lines of inquiry but not consistently, or the summary attempts are incomplete.
- (Poor) Score a 1 if the interviewer interviewer fails to summarize any of the data obtained.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "So today you've described experiencing a range of symptoms starting with headaches, moving to occasional dizziness, and you've also mentioned some recent issues with your vision. Let me make sure I've got everything: Your headaches began around three weeks ago, initially mild but have increased in frequency and intensity. The dizziness is sporadic, mostly in the mornings, and your vision issues started last week, primarily blurring when reading. Is all of this correct?"
Patient: "Yes, that's right."
Score: 5

**Conversation Excerpt**: 
Physician: "Okay, we've covered quite a bit today about your headaches and some of your lifestyle factors."
Patient: "Yes, we did."
Score: 1
""",

    "QUESTIONING SKILLS - DUPLICATION": """
Evaluate the interviewer's tendency to repeat questions seeking information that has already been provided, unless clarification or summarization is necessary.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer does not repeat questions unnecessarily and only seeks repetition for clarification or summarization.
- (Average) Score a 3 if the interviewer rarely repeats questions, and when questions are repeated, it is not for summarization or clarification but due to a lapse in memory.
- (Poor) Score a 1 if the interviewer consistently seeks information previously provided, showing a clear failure to track or remember patient information.
If the excerpt simply says "No questions were duplicated.", assign a score of 5. The explanation should state "No questions were duplicated." and do not provide direct quotes.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "Can you tell me when you first noticed your symptoms?"
Patient: "It started with a mild fever last Tuesday."
Physician: "Okay, and just to clarify, did any other symptoms accompany the fever at that time?"
Patient: "Yes, I also had some chills and a sore throat."
Physician: [Later in the conversation] "You mentioned earlier that the fever began last Tuesday. To summarize, along with the fever, you had chills and a sore throat, correct?"
Score: 5

**Conversation Excerpt**: 
Physician: "Have you experienced any nausea associated with your headaches?"
Patient: "Yes, I've had some nausea, mostly in the mornings."
Physician: [Five minutes later] "And you mentioned nausea, right? When does that usually occur?"
Patient: "As I said, it's mostly in the mornings."
Score: 1

""",

    "QUESTIONING SKILLS - LACK OF JARGON": """
Evaluate the physician's use of language, focusing on the avoidance of medical jargon and the clarity of communication.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer uses language easily understood by the patient, avoiding medical jargon or explaining terms immediately.
- (Average) Score a 3 if the interviewer occasionally uses medical terms without definition, requiring clarification upon patient request.
- (Low) Score a 1 if the conversation is dominated by medical jargon, making it inaccessible to the patient without definitions provided.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "You mentioned feeling an unusual tightness in your chest. Can you describe that feeling? Is it like a pressure or a squeezing sensation?"
Patient: "It's more like a squeezing feeling."
Physician: "That's helpful to know. Sometimes what you're describing is called 'angina,' which is just a medical term for chest pain caused by reduced blood flow to the heart muscle."
Score: 5

**Conversation Excerpt**: 
Physician: "Based on your symptoms, we're looking at a probable case of gastroesophageal reflux disease, which might be contributing to your dyspepsia."
Patient: "Sorry, I'm not sure what those terms mean."
Physician: "Ah, yes, those are quite technical. Gastroesophageal reflux disease is what you might know as acid reflux, and dyspepsia is just another word for indigestion."
Score: 1

""",

    "QUESTIONING SKILLS - VERIFICATION OF PATIENT INFORMATION (in vignette)": """
Evaluate how the physician seeks clarification, verification, and specificity of the patient’s responses.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer consistently seeks to clarify, verify, and specify patient responses, ensuring accurate understanding.
- (Average) Score a 3 if clarification, verification, and specificity are sought but not consistently, leading to some gaps in understanding.
- (Low) Score a 1 if the interviewer fails to clarify or verify patient responses consistently, largely ignoring the need for accuracy.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "You mentioned feeling dizzy occasionally. Can you tell me more about what you're doing when these episodes occur?"
Patient: "Usually, it happens when I stand up too quickly."
Physician: "So it's mainly upon standing. Does this happen every time you stand up quickly, or are there certain times of the day when it's more likely to occur?"
Patient: "It's more in the mornings."
Score: 5

**Conversation Excerpt**: 
Physician: "So, you've been feeling unwell, correct?"
Patient: "Yes, mostly tired and sometimes dizzy."
Physician: "Okay, let's talk about your diet then."
Score: 1

""",

    "VERBAL FACILITATION SKILLS": """
Evaluate the interviewer's use of verbal encouragement and facilitation skills to engage the patient.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer encourages the patient throughout the interview. Draws out information. Verbal encouragement, use of short statements, and echoing are used regularly when appropriate. The interviewer provides the patient with intermittent verbal encouragement, such as verbally praising the patient for proper health care technique.
- (Average) Score a 3 if the interviewer uses some facilitative skills but not consistently or at inappropriate times. Verbal encouragement could be used more effectively.
- (Low) Score a 1 if the interviewer fails to use facilitative skills to encourage the patient to tell the story.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "It sounds like you've been quite diligent with your exercise routine. Can you tell me more about what you do?"
Patient: "I try to walk every morning."
Physician: "Every morning, that’s impressive! How has it been affecting your energy levels?"
Patient: "I've noticed I feel less tired during the day."
Physician: "That’s great to hear. It shows how your efforts are paying off."
Score: 5

**Conversation Excerpt**: 
Physician: "You mentioned you started exercising. What type?"
Patient: "I’ve been trying to walk more."
Physician: "Okay, and your medication?"
Patient: "I take it in the morning."
Physician: "Make sure it’s every morning."
Score: 1

""",

    "EMPATHY AND ACKNOWLEDGING PATIENT CUES": """
Evaluate the interviewer's ability to use supportive comments regarding the patient’s emotions and demonstrate empathy, considering:

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer uses supportive comments regarding the patient’s emotions. The interviewer uses NURS (name, understand, respect, support) or specific techniques for demonstrating empathy.
- (Average) Score a 3 if the interviewer is neutral, neither overly positive nor negative in demonstrating empathy.
- (Low) Score a 1 if no empathy is demonstrated, with the interviewer using a negative emphasis or openly criticizing the patient.

## Below are two exemplars:
**Conversation Excerpt**: 
Physician: "It sounds like you've been under a lot of stress from these symptoms. It must be quite challenging for you."
Patient: "Yes, it's been very hard."
Physician: "I can only imagine how tough that is. We're here to support you through this and find ways to make you feel better."
Score: 5

**Conversation Excerpt**: 
Physician: "You need to manage your stress better. Continuing like this will only make your condition worse."
Patient: "I've been trying, but it's not easy."
Physician: "Well, it's important for your health to make an effort."
Score: 1

""",

    "PATIENT’S PERSPECTIVE (BELIEFS; Case specific)": """
    Evaluate the interview based on how well the physician provides the patient with opportunities to ask questions or bring up additional topics.
    
## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer elicits the patient’s healing practices and perspectives on the illness, including beliefs about its beginning, Feelings, Ideas of cause, Function and Expectations (FIFE).
- (Average) Score a 3 if the interviewer elicits some of the patient’s perspective on the illness AND/OR The interviewer does not follow through with addressing beliefs.
- (Low) Score a 1 if the interviewer fails to elicit the patient’s perspective.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "Can you share what you believe might be causing your symptoms?"
Patient: "I think it might be stress-related because it started when I changed jobs."
Physician: "That’s an important observation. Let’s explore how your job change has coincided with your symptoms and discuss how we can address the stress component as part of your treatment."
Score: 5

**Conversation Excerpt**: 
Physician: "Your tests show you have high blood pressure. We need to start treatment immediately."
Patient: "Could my job stress be affecting my blood pressure?"
Physician: "It’s all about your diet and exercise. We’ll start you on medication."
Score: 1

""",

    "IMPACT OF ILLNESS ON PATIENT AND PATIENT’S SELF-IMAGE": """
    If applicable, evaluate the physician's exploration of how the illness affects the patient's life and self-image.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer inquires about the patient’s feelings about the illness and how it has changed patient’s life. The interviewer explores these issues. (The interviewer offers counseling or resources to help. This is used in communication cases.)
- (Average) Score a 3 if the interviewer partially addresses the impact of the illness on the patient’s life or self-image. AND/OR The interviewer offers no counseling or resources to help.
- (Poor) Score a 1 if the interviewer fails to acknowledge any impact of the illness on the patient’s life or self-image.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "How has this diagnosis impacted how you see yourself and your day-to-day activities?"
Patient: "It's been hard. I feel like I'm not the same person anymore."
Physician: "It's completely normal to feel that way. Let's discuss how we can help you cope with these changes. We have support groups and counseling services that might help you."
Score: 5

**Conversation Excerpt**: 
Physician: "You need to start treatment immediately. It's important to manage your symptoms effectively."
Patient: "I'm worried about how this will change my life. I feel very different now."
Physician: "The most important thing is to keep your symptoms under control."
Score: 1

""",

    "ACHIEVE A SHARED PLAN": """
    If applicable, identify part(s) of the conversation where the physician discussed the diagnosis or prognosis and/or negotatiated a plan with the patient, or lack thereof.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the the interviewer discusses the diagnosis and/or prognosis and negotiates a plan with the patient. The interviewer invites the patient to contribute own thoughts, ideas, suggestions and preferences.
- (Average) Score a 3 if the interviewer discusses the diagnosis and/or prognosis and plan but does not allow the patient to contribute. Lacks full quality.
- (Poor) Score a 1 if the interviewer fails to discuss diagnosis and/or prognosis.

## Below are two exemplars: 
**Conversation Excerpt**: 
Physician: "Based on your test results, it looks like you have Type 2 diabetes. Let’s discuss what this means for you and explore how we can manage it. What are your thoughts on treatment, and what approach would you prefer?"
Patient: "I've read about lifestyle changes and medications, but I'm not sure what would be best for me."
Physician: "Both are good options. We can start with some moderate lifestyle adjustments and see how much they help, and consider medications if your sugar levels aren't controlled. How does that sound?"
Score: 5

**Conversation Excerpt**: 
Physician: "You have high blood pressure. We need to start you on medication right away."
Patient: "Are there other things I can do besides medication?"
Physician: "Medication is the best option. We'll start with that."
Score: 1

""",

    "ENCOURAGEMENT OF QUESTIONS": """
Evaluate the interview based on how well the interviewer provides the patient with opportunities to ask questions or bring up additional topics. Use the rubric below to assign a score.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer encourages the patient to ask questions at the end of a major subsection. The interviewer gives the patient the opportunity to bring up additional topics or points not covered in the interview. Two opportunities including one at the end of the interview.
- Score a 4 only one opportunity, at the end.
- (Average) Score a 3 one opportunity for questions but not near the end of the encounter.
- Score a 2 if the interviewer does not specifically ask if there are questions, but the climate and the pace of the interview allow them.
- (Low) Score a 1 if the interviewer fails to provide the patient with the opportunity to ask questions or discuss additional points. The interviewer may discourage the patient’s questions.
If the excerpts simply says "Physician does not provide patient with opportunities for questions.", assign a score of 1. The explanation should just state "Physician does not provide patient with opportunities for questions" and do not provide direct quotes.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "We've discussed your treatment options for managing diabetes. Do you have any questions about what we’ve covered so far?"
Patient: "I'm curious about the side effects of these medications."
Physician: "That’s a great question. Let's go through them..."
[Later in the interview]
Physician: "Before we finish, do you have any other questions or is there anything else you'd like to discuss?"
Score: 5

**Conversation Excerpt**: 
Physician: "So we will start with this new medication. I'll see you in six weeks for a follow-up."
Patient: "Could I ask about—"
Physician: "We're really pressed for time today, but we can get into more details next time."
Score: 1

""",

    "SUPPORT SYSTEMS": """
Assess the interviewer's exploration of the patient’s support systems, including emotional, financial support, and access to healthcare, with the following scoring:

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer thoroughly determines: what emotional support the patient has; what financial support the patient has and learns about their access to healthcare; about other resources available to the patient and family and suggests appropriate community resources. (In focused histories, addressing one pertinent support aspect in depth is sufficient.)
- (Average) Score a 3 if the interviewer determines some aspects of the available support but does not fully explore or suggest resources.
- (Poor) Score a 1 if the interviewer fails to determine or discuss any support currently available to the patient.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "Who do you have at home to support you emotionally during this time?"
Patient: "My sister has been very helpful."
Physician: "That’s good to hear. How are you managing financially with the treatment costs? And do you have reliable access to the healthcare services you need?"
Patient: "It's been difficult financially."
Physician: "Let me give you information about some community resources that can help with healthcare costs and additional support groups that might be beneficial for you and your sister."
Score: 5

**Conversation Excerpt**: 
Physician: "It’s important to stay positive and manage your treatment effectively."
Patient: "I’m struggling with this on my own, and it’s getting overwhelming."
Physician: "Just try to follow the treatment plan as best you can."
Score: 1

""",

    "PATIENT’S EDUCATION & UNDERSTANDING": """
Evaluate the physician's effectiveness in educating the patient by determining the patient's level of interest, providing appropriate education, and using the teach back technique to ensure understanding.

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- Score a 5 if when patient education is a goal, the interviewer determines the patient’s level of interest and provides education appropriately. The interviewer uses a teach back to check the patient’s understanding of information given during the interview. Techniques may include asking the patient to repeat information, asking if the patient has additional questions, posing hypothetical situations or asking the patient to demonstrate techniques.
- Score a 3 if the interviewer asks if the patient understands the information but does not use the teach back technique. Some attempt to determine the interest in patient education but could be more thorough.
- Score a 2 if the interviewer gives info but does not check on understanding.
- Score a 1 if the interviewer fails to assess patient’s level of understanding and does not effectively correct misunderstandings when they are evident. AND/OR The interviewer fails to address the issue of patient education.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "It's important that you understand how to manage your diabetes at home. Can you explain to me how you'll take your medication and what you should do if your blood sugar goes too high?"
Patient: "I take my medication in the morning and check my blood sugar. If it's too high, I'll..."
Physician: "That’s right, and remember to also..."
Score: 5

**Conversation Excerpt**: 
Physician: "You need to start taking these new medications for your hypertension. Take one pill in the morning and one in the evening."
Patient: "What should I do if I experience any side effects?"
Physician: "Just continue with the medication and we can discuss it during your next appointment."
Score: 1

""",

    "ASSESS MOTIVATION FOR CHANGES": """
Evaluate the physician's performance based on their ability to assess the patient's motivation for change and provide appropriate support and options. 

## Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 if the interviewer inquires how the patient feels about the lifestyle/behavioral change and gives information appropriate to patient’s level of readiness.
- (Average) Score a 3 if the interviewer inquires how the patient feels about changes but does not follow-up appropriately.
- (Poor) Score a 1 if the interviewer fails to assess patient’s level of motivation to change and does not offer any options or plans or assumes patient’s readiness for change.

## Below are some exemplars.
**Conversation Excerpt**: 
Physician: "How do you feel about making some changes to your diet to help manage your diabetes?"
Patient: "I know it's important, but I find it hard to stick to diets."
Physician: "That's completely understandable. Let's start with small, manageable changes. How about we try integrating one healthy meal a day and see how that goes?"
Score: 5

**Conversation Excerpt**: 
Physician: "You need to start exercising more regularly to improve your heart health."
Patient: "I've tried before, but I struggle with staying motivated."
Physician: "It's very important for your health. Try to make an effort."
Score: 1

""",

    "CLOSURE": """
Evaluate how well the physician specifies future plans for both the interviewer and the patient at the end of the interview.

Evaluation Rubric:
Assign a score of 1, 2, 3, 4, or 5.
- (High) Score a 5 at the end of the interview the interviewer clearly specifies the future plans: What the interviewer will do (leave and consult, make referrals) What the patient will do (wait, make diet changes, go to Physical Therapy); When (the time of the next communication or appointment.)
- (Average) Score a 3 if at the end of the interview, the interviewer partially details the plans for the future.
- (Low) Score a 1 if at the end of the interview, the interviewer fails to specify the plans for the future and the patient leaves the interview without a sense of what to expect. There is no closure whatsoever.

## Below are two exemplars.
**Conversation Excerpt**: 
Physician: "We've covered a lot today. I will consult with a specialist about your case and make a referral for you to see them. You should start adjusting your diet as we discussed and begin the physical therapy sessions twice a week. Our office will call you by Tuesday to confirm the details of your referral and next appointment. Do you have any questions or concerns about what we’ve planned?"
Patient: "No, that sounds clear. Thank you."
Physician: "Great, we'll ensure everything is set up for you, and I look forward to seeing how you progress."
Score: 5

**Conversation Excerpt**: 
Physician: "Alright, so that's it for today. Make sure you follow the instructions we talked about."
Patient: "So, what exactly should I do next? Do I need to come back?"
Physician: "Just go ahead with the changes we discussed. We'll sort out the details later."
Score: 1

"""
}
