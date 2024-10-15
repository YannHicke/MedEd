# extract_excerpts.py

instructions_start = """
You will be given a transcript of a conversation between a physician and patient, where you will extract relevant direct quotes depending on your task. You will observe notes and examples in each of the items that will help guide you in identifying the correct excerpts.
In your response, directly copy the relevant parts of the conversation. Do not output any other additional text other than the direct quotes. Do not remove any words. If not applicable, just output "Not applicable."

Your task:
"""

instructions_end = """

Here is the conversation transcript for which you will extract direct quotes:

"""

mirs_items = {
    "OPENING": """
    Identify part(s) of the conversation where the student conducts the opening of this medical interview, or the lack thereof.

    **Note:** Learner begins with the introduction of self, clarification of roles, and inquiry of how to address patient. The opening question identifies the problems or issues that the patient wishes to address. 
    **Example:** “Hello, I’m Carol Redding, (shaking patient’s hand) a student working with the team. Would you prefer I call you, Ms. Black or Phyllis? Are you comfortable right now? What brings you in today?”
""",

    "ELICITS SPECTRUM OF CONCERNS": """
    Identify part(s) of the conversation where the student elicits the patient's spectrum of concerns within the first 3-5 minutes of the interview, or the lack thereof.

    **Note:** Learner elicits the patient's full spectrum of concerns other than those expressed in the chief complaint within the first few minutes of the encounter. To ensure that the full spectrum of concerns has been obtained, asks if there is anything else the patient wishes to discuss until the patient says, “No.” Making sure in the beginning of the encounter that all issues the patient wishes to address have been elicited helps learners to prioritize and aids in making a time-efficient, patient-centered encounter.
""",

    "NEGOTIATES PRIORITIES & SETS AGENDA": """
    Identify part(s) of the conversation where the student negotiates the patient’s priorities and sets the agenda for their visit.

    **Note:** Learner ascertains the patient’s concerns. In negotiating priorities, a balance is struck between patient concerns and provider’s medical understanding of which problems might be more immediately important. An agenda is negotiated between learner and patient. In agenda setting and negotiating, the patient should not be told what is going to occur, but instead share in making an agreed plan. 
""",

    "ELICITING THE NARRATIVE THREAD or the PATIENT_S STORY": """
    Identify part(s) of the conversation where the student elicits the narrative thread, or the patient’s story, from the patient, or the lack thereof.

    **Note:** After the agenda is set, the learner encourages the patient to talk about the problem(s), in their own words and listens attentively without interrupting (except for encouragement to continue) until the patient has finished talking about the problem(s). This technique is an effective tool for data gathering, time-efficiency, and rapport building. It allows the patient to tell their story and can help learners gain a large amount of needed data in a short amount of time. 
    **Example:** “Tell me what’s been going on from when your symptoms first started up to today.”
""",

    "TIMELINE": """
    Identify part(s) of the conversation where the student establishes a timeline of the chief concern and history of the present illness, or the lack thereof.

    **Note:** The timeline pertains to the information contained in the chief complaint and history of the patient's current illness. To obtain a timeline, Learner should inquire when the patient was last free of this problem, and then follow the progression of the first signs and symptoms to the present. By carefully following the chronological progression of the complaint, the Learner will avoid missing important information. If several symptoms are reported, it is important that their chronological relationship to each other be determined. Learners need not gather the information in a chronological order or all at once if the information needed is obtained during the encounter. 
    **Example:** A 56-year-old male presents with left side chest pain for two hours. The patient's chest pain first occurred two years ago but only upon exertion and disappeared after a few minutes. One year ago, the pain increased in intensity and was diagnosed as angina pectoris. Nifedipine (l0 mg) qid was taken and the pain stopped occurring one month later. The patient continued to take Nifedipine (l0) bid and is still currently. Two hours ago, he experienced chest pain on the left and one hour ago he experienced sweating, faintness, palpitations, and the pain radiated to the left shoulder. 
""",

    "ORGANIZATION": """
    Identify part(s) of the conversation regarding the organization of the interview, which may follow a logical order or may be disjointed or unorganized, or the lack thereof.

    **Note:** Organization refers to the structure and organization of the entire conversation/encounter, encompassing the flow of the information gathered in the Introduction (when the Learner introduces self and explains their role), the body of the encounter, (Chief complaint and History of present illness, Past medical history, Family history, Social history, Review of systems), and the closure (the end of the encounter, but not the quality of the Closure because this is measured in another MIRS ITEM.) Questions in the body of the encounter follow a logical order to the patient. Learner imposes structure by systematically following a series of topics.  
""",

#     "PACING OF INTERVIEW": """
#     Identify excerpt(s) of the conversation, focusing on the physician's attentiveness, the smooth progression of the interview, and the deliberate use of silence. For this task, you are encouraged to extract excerpts liberally.

# ## Below are two exemplars.
# **Example**:
# Physician: "I noticed you mentioned earlier that you've been having trouble sleeping. Can you tell me more about when that started?"
# Patient: "Yes, it's been about three weeks now. I just lie there, unable to sleep."
# Physician: [Silently nods, giving the patient a moment to continue] "That sounds difficult. How has this affected your day-to-day activities?"
# Patient: "I'm always tired now, and it's hard to concentrate at work."

# **Example**:
# Physician: "So, you've been feeling unwell. Tell me about that."
# Patient: "Well, it started with some fatigue, and then I—"
# Physician: "Fatigue, got it. And are you taking any medications?"
# Patient: "Yes, I've been on—"
# Physician: "Okay, and any family history we should know about?"

# """,

    "QUESTIONING SKILLS TYPES OF QUESTIONS": """
    Identify part(s) of the conversation where the student demonstrates questioning skills, specifically looking at the types of questions they ask, or the lack thereof.

    **Note:** Learners should follow a line of inquiry that progresses from open-ended to specific followed with specific questions. 
    - Open-ended questions: Allow the learner to obtain a large amount of information about a particular area. It allows the patient to tell their story. This should be used to begin a line of inquiry then follow up with more focused and direct questions. Example: "What brings you here today?" or "Tell me about your general health.”
    - Direct or specific questions: Gather specific pertinent information. Example: “How old were you when you had your tonsils removed?" or "When did your pain begin?" or "How long have you had the pain?"
    Other types of direct questions elicit a "yes" or "no" answer from the patient, or a response to a choice that the learner has provided.   
    Example various types of questions: Learner (L): "Tell me about your problem." (Open-ended) Patient (P): "For two weeks, I've had a constant pain in my stomach, right here (points), above my navel." L: "Tell me about the pain." (Open-ended) P: "It's a burning sensation." L: "Is it a deep pain?" (Direct) P: "Yes, a deep one." L: "Does the pain move around?" (Direct) P: "No."  L: "What makes the pain feel worse?" (Open-ended)
    Learners should avoid using direct or (particularly) forced choice questions in beginning a line of inquiry because it restricts the possible flow of information and makes obtaining the necessary information a tedious task. Example: if NOT beginning with an open-ended question such as: "Tell me about the pain.” they must ask several direct questions: L: "Is the pain an ache?" P: "No."  L: "Is it a stabbing pain?" P: "No."  L: "Is it a dull pain?" P: "No."
    Learners should avoid these poor question types: 
    - Leading Questions supply a particular answer for the patient, desired answer is implied by how the question is phrased. This should also be avoided because some patients may agree with the leading questions rather than contradicting the learner. Example: "No headaches? Right?"
    - "Why" Questions: put the patient on the defensive and should be avoided. Example: "Why didn’t you come in sooner, you've had the problem for six weeks?"
    - Multiple Questions: a series of short questions asked in succession without allowing the patient to answer each individually. The patient may be confused about which question to answer. Example: “Does the pain feel like it’s as sharp after dinner or is it different than before dinner? Multiple questions may also be one question listing many options. Example: "Has anyone in your family ever had cancer, diabetes, heart disease, or high blood pressure?"  
""",

    "QUESTIONING SKILLS SUMMARIZING": """
    Identify part(s) of the conversation where the student demonstrates questioning skills, specifically looking at their ability to summarize, or the lack thereof.

    **Note:** Summarization is a review of the main details elicited during the visit and is typically used at the end of each sub-section but may be used at any time. In summarizing the Chief Complaint and History of Present Illness it is important to provide a detailed summarization to the patient. In summarizing the Family History, a brief general statement may be sufficient, especially for a negative or non-complex positive family history. In Review of Systems, it is appropriate to summarize only the positives discovered. 
    **Example:** "Other than a few headaches you are fairly healthy. Our main task is to clear up the problem you're having with your back. Is this how you see the problem?"
    Summarization of a body of information should be verified with the patient to make sure that all facts are correct. Verifying is done after summarization but may be utilized if a patient seems reluctant to interrupt, or to involve the patient in active listening.
    Summarizing data at the end of each subsection serves several communication purposes: 
    - To "jog" the memory in case the learner has forgotten to ask a question.
    - Allow the patient to hear how the learner understands the information. 
    - It proves to the patient that the learner has been listening, thus strengthening the relationship.
    - Provides an opportunity to verify information: 
    - Example: “To recap, your headache started yesterday, is on the left side, and is a pain level six. Is this correct?” 
    - Provides an opportunity to clarify information: 
    **Example:** "You said it is interfering with your attendance at school, how many days were missed?"
""",

    "QUESTIONING SKILLS DUPLICATION": """
    Identify part(s) of the conversation where the student demonstrates questioning skills, specifically looking at their duplication of information, or the lack thereof.

    **Note:** The learner must avoid repeating questions that seek information already provided by the patient, unless it’s for clarification or summarization purposes. Unnecessary repetition due to failure to remember information can disrupt the flow of the interview and potentially frustrate the patient.
    **Example:** If a patient has already stated their age, the learner should not ask “How old are you?” later in the interview. However, it would be appropriate to say something like, “Just to confirm, you mentioned earlier that you’re 45, is that correct?” for clarification purposes.
""",

    "QUESTIONING SKILLS LACK OF JARGON": """
    Identify part(s) of the conversation where the student demonstrates questioning skills, specifically looking at their lack of jargon.

    **Note:** One of the skills needed is the ability to communicate with the patient with terms known to lay persons – to substitute jargon or difficult medical terms. Learners may make erroneous assumptions about the patient's level of sophistication based on one or two medical terms used by the patient. 
    Jargon may also be misleading to a patient who does not want to admit they don’t understand the question/term. Therefore, learners should define questionable terms. Additionally, learners should be aware of educational levels. By keeping these things in mind when communicating with a patient, information will be clearer and long-term compliance easier to obtain.
    **Example:** “Was it a productive cough?" followed by “Productive means does anything come up when you cough?”
""",

    "QUESTIONING SKILLS VERIFICATION OF PATIENT INFORMATION": """
    Identify part(s) of the conversation where the student demonstrates questioning skills, specifically looking at their verification of patient information, or the lack thereof.

    **Note:** In the interest of gaining as accurate information as possible, the learner must verify and clarify the information given by the patient. 
    - Clarification: “Can you explain what you mean by ‘weak.’?” 
    - Verification: “I’m confused, you said you’d never been short of breath before but sounds like you had a similar feeling last year. Can you clear that up for me?” 
    If responses from the patient include specific diagnoses or medications, it is the task of the Learner to ascertain if the patient knows how the diagnosis was made or determine the quantity of medication. 
    **Example:** “You said you were allergic to penicillin. How do you know that?”
""",

    "VERBAL FACILITATION SKILLS": """
    Identify part(s) of the conversation where the student uses verbal facilitation skills, or the lack thereof.

    **Note:** It is important to actively encourage patients to continue their storytelling. Any behavior that has the effect of inviting patients to say more about the area being discussing is a facilitative response. Learner follows up patient’s initial story with focused facilitation skills to broaden and complete the story. The use of short statements and echoing (using a few words of the patient's last sentence) encourage the patient to say more about a topic and indicate that a learner is interested in what the patient is saying and wants them to continue. Learners use verbal encouragement to motivate the patient toward a cooperative relationship and continued health care throughout the encounter e.g., responding to the patient in a way that they feel encouraged in starting/continuing proper health care techniques. 
    Verbal Encouragement and use of occasional social praises.  
    **Example:** L: “Quitting smoking is excellent, that takes willpower!" 
    Short statements encourage them to continue talking about the problem. 
    **Example:** “Go on… tell me more” 
    Echoing to encourage patients to elaborate on a topic.  
    **Example:** P: “I couldn’t take in a good breath.”  L: “Did you feel as if you couldn’t get your breath?”
""",

    "EMPATHY AND ACKNOWLEDGING PATIENT CUES": """
    Identify part(s) of the conversation where the student demonstrates empathy and acknowledges patient cues, or the lack thereof.

    **Note:** Empathy is not only being sensitive, but also demonstrating that sensitivity to patients so they appreciate the understanding and support. To display empathy, actively acknowledge and follow-up on verbal patient cues, showing that they have been heard and understood. The patient is actively encouraged to express emotion. Empathic statements are supportive comments that specifically link the “I” of the provider and the “you” of the patient. They both name and appreciate the patient’s affect or predicament and express appreciation for the problem. 
    “NURS” is an active technique to demonstrate empathy and acknowledge patient cues: 
    - Naming emotion: “It must be very frustrating to not be able to work.” 
    - Express Understanding [Goal is to normalize or validate feelings/experience]: "That must have been difficult for you. I’d feel that way too.” 
    - Showing Respect: “I can appreciate how difficult it is for you to talk about this.” 
    - Offering Support [Partnering/assistance, showing concern/sensitivity]: “I’ll be working with you each step of the way.”
""",

    "PATIENTS PERSPECTIVE & BELIEFS": """
    Identify part(s) of the conversation where the student elicits the patient’s perspectives and beliefs, or the lack thereof. 

    **Note:** Learner should elicit the patient's perspective on symptoms in order for it to be effectively diagnosed and treated. The patient's beliefs about the beginning of their illness may affect their ability to talk about their symptoms or to understand the diagnosis. Gaining the patient perspective uncovers hidden concerns. 
    One method of eliciting beliefs is to encourage the patient to discuss FIFE:
    - Feelings: addresses the patient’s feelings about each of the problems.
    - Ideas: determines and acknowledges patient’s ideas (belief of cause) for each of the problems.
    - Function: determines how each problem affects the patient’s life.
    - Expectations: determines patient’s goals, what help the patient had expected for each problem.
    Does NOT have to be scripted, asked at one time or in order. It can occur at any point in the conversation. Ideas asked first may elicit feelings. Expectations may be incorporated into the shared agenda at the encounter onset. Function may help elicit information in the HPI.
    **Example:** L: "What do you think is going on?  P: I’m worried [Feelings] I may have something serious [Idea].  L: Why do you think it is serious?  P: My uncle died of stomach cancer one year ago [Hidden concern]. 
    L: I’m sorry to hear about your uncle. I understand your concern. How has this problem been affecting you at work and home? [Function]. P: Aside from the pain, I’m preoccupied with wondering what is making me sick. 
    L: Besides wanting to find out the cause of this problem, what can I do to help? [Expectations].”
""",

    "ADMITTING LACK OF KNOWLEDGE": """
    Identify part(s) of the conversation where the physician admits a lack of knowledge when necessary.
     
      **Note:** Learners must be aware of their own level of experience as related to the information they are able to give to the patient. If asked for information/advice they are not equipped to provide, they admit lack of experience in that area, offer to seek resource(s) to answer the question and a timeframe is established for getting back to the patient with the answers. 
      **Example:** a provider referring a patient to a cardiologist may lack knowledge about specialized cardiovascular testing but should still help answer the patient concern/question.
""",

    "IMPACT OF ILLNESS ON PATIENT AND PATIENT_S SELF-IMAGE": """
    Identify part(s) of the conversation where the student explores and addresses the impact of the illness on the patient and their self-image, or the lack thereof.

    **Note:** Learner must address the impact on self-image that certain illnesses/symptoms/situations may have on the patient. They should explore these issues in depth to the satisfaction of the patient. Learner also offers counseling or recommends resources, if appropriate. 
    **Example:** Immediately after a heart attack, a patient needs to change their sexual and physical activity, this may impact the way they view themselves. L: “Some patients stop exercising after having a heart attack for fear of triggering another. How is it affecting you?” Tell me about your exercise routine now? ... I can suggest a specialist to help.”
""",

    "IMPACT OF ILLNESS ON FAMILY": """
    Identify part(s) of the conversation where the student explores and addresses the impact of the illness on the patient’s family, or the lack thereof.

    **Note:** Depending on the diagnosis, as well as the information obtained during the personal history, there could be a tremendous impact of the patient's illness on the family and the family's lifestyle. 
    **Example:** For a patient with cancer this would certainly affect family members and family lifestyle because of the need for frequent treatment, side effects of drugs, potentially decreased family income, etc. 
    The Learner must address this issue and explore it in depth to the patient’s satisfaction. 
    **Example:** L: “You told me your child cries all through all night. Who else at home is affected by this?” P: “My husband. He cannot sleep and has missed work.”  L: “OK, let’s discuss ways to relieve this stress ...”
""",

    "SUPPORT SYSTEMS": """
    Identify part(s) of the conversation where the student explores the patient’s support systems, or the lack thereof.

    **Note:** Learner should explore the patient’s means of financial, social, and emotional support. Support systems might include other family members, friends, and the patient’s workplace. These are current resources which could be employed immediately. Learners may suggest other community resources including charitable organizations, self-help groups, etc., not yet thought of or known to the patient. 
    **Examples:** “These tests can be expensive; are you concerned about this?” “It sounds like you’ve been through a difficult time. Do you have someone you can talk to?” “Is there anyone that can help with the children until you’re feeling better?” “You told me that you are involved in your church, could they be a source of help?”
""",

    "PATIENTS EDUCATION AND UNDERSTANDING": """
    Identify part(s) of the conversation where the student explores the patient’s education and understanding, or the lack thereof.

    **Note:** Many times, patients who are labeled non-compliant may in fact not understand the information that is given to them. There are several ways to check the patient's understanding. Learners can ask the patient to repeat the information directly back, demonstrate techniques, or pose hypothetical situations to see if the patient will react appropriately. It is vital that when a patient must carry out therapy on their own without direct supervision, that they understand how to carry it out. 
    **Examples:** Learner “I’ve shown you how to test levels of sugar in your blood with the monitor, now will you show me so I can be sure that I explained it clearly?” or “Will you repeat back to me how to take your medicine, so I know I have given you the correct information?”
""",

    "ASSESS MOTIVATION FOR CHANGES": """
    Identify part(s) of the conversation where the physician assesses the patient’s motivation for changes, or the lack thereof. 

    **Note:** The learner assesses how the patient feels about lifestyle and/or behavioral changes like taking medicine, changing diet and exercise, smoking cessation, etc. Many interviewers assume patients will change their behavior without discussing it with them. This lack of communication may lead to return visits or non-compliance issues. Asking the patient about previous experiences, the patient’s view of the importance to change, and the patient’s confidence in ability to change will help to establish guidelines. Then Learner can provide information, as appropriate, based on the patient’s needs. Offer a menu of options, emphasize the patient’s ability to choose, and anticipate and plan for obstacles.
    **Example:** L: "You mentioned earlier that you've been struggling to quit smoking. On a scale of 1 to 10, how important is it for you to quit smoking right now?" P: "I'd say about a 7." L: "That's great that you recognize its importance. Using the same scale, how confident are you in your ability to quit?" P: "Maybe a 4 or 5." L: "I see. What do you think are the main obstacles to quitting?" P: "Well, I've tried before and it's just really hard. Especially when I'm stressed." L: "I understand. There are several ways we can approach this. We could try nicotine replacement therapy, medication, or counseling. Some people find a combination works best. What do you think might work for you?" P: "I'm not sure about medication..." L: "That's okay. How about we start with counseling and discuss some stress management techniques? We can always revisit other options later if needed."
""",

    "ACHIEVE A SHARED PLAN": """
    Identify part(s) of the conversation where the student achieves a shared plan with the patient, or the lack thereof.
    
    **Note:** A shared understanding is achieved with the patient, including nature and significance of the problem. The patient's understanding about the prognosis also plays a role in treatment 
    **Example:** someone who has had a family member die from a perforated ulcer may see a diagnosis of peptic ulcer as far more life threatening than the learner. 
    Learner involves the patient by making suggestions and encourages the patient to contribute thoughts, ideas, suggestions, and preferences. A mutually acceptable plan is negotiated, and learner checks in with patient on if the plan is acceptable and addresses concerns. Discussions between Learner and Patient include the: nature of the problem, significance of the problem and patient understanding about the problem/prognosis. 
    **Examples:** Learner - “It sounds like you would be interested in trying some medication to stop smoking. Of the options I told you about, which would you like to try first?” or “Since it is so hard for you to make physical therapy appointments, would it help if I suggest some ways to exercise your knee at work?”
""",

    "ENCOURAGEMENT OF QUESTIONS": """
    Identify part(s) of the conversation where the student encourages questions from the patient, or the lack thereof. 
    
    **Note:** Learners should encourage the patient to discuss additional points and ask questions by clearly providing an opportunity to do so. This can be done at the end of a major subsection and repeated at the end of the encounter.
    **Example:** [near beginning]: “If you have questions at any time, feel free to ask.” [Then, as encounter progresses]: “Before we move on, any questions?” 
""",

    "INFORMED CONSENT": """
    Identify part(s) of the conversation where the student obtains informed consent for investigations and procedures, or the lack thereof.

    **Note:** If discussing investigations and procedures, learner provides clear information on procedures (What is going to be done), including what patient might experience (Will it hurt or harm? How much? How long?), and how patient will be informed of results (When and how will the patient be informed of results and the meaning of the results). 
    Learner relates procedures to treatment plan, value, and purpose; encourages discussions of potential anxieties or negative outcomes. Exploration of the patient questions, concerns, and clear explanations of procedures facilitate the likelihood of compliance. 
    Components of discussions include:
    - Why the investigations & procedures must be done
    - How the investigation/procedure is going to be done to include what the Patient might experience
    - When and how the Patient will be informed of results and their meaning
    - What potential anxieties or negative outcomes there may be.
""",

    "INTERACTIVE TECHNIQUES": """
    Identify part(s) of the conversation where the student uses interactive techniques to engage with the patient, or the lack thereof.

    **Note:** Use patient-centered interviewing techniques during the entire encounter. Patient-centered approach promotes a collaborative partnership between patient and Learner. However, patient-centered does not mean patient-controlled. A collaborative partnership promotes a more equal relationship, which enhances long-term compliance. Learner progresses from patient-centered to provider-centered technique to elicit required information but returns the lead to the patient whenever appropriate.
""",

    "TRANSITIONAL STATEMENTS": """
    Identify part(s) of the conversation where the student uses transitional statements, or the lack thereof.

    **Note:** Transitional statements are two-part statements used between subsections to inform the patient that a new topic is going to be discussed (what) and (why). 
    **Example:** “(What) I'd like to get some information about your past medical history, (Why) to see if it has any bearing on your present problem.” 
    With transitions, the patient understands why the learner is changing the subject and why they are seeking the information. Poor quality or no transitional statements can hinder the development of rapport and could result in a hostile or uncooperative patient. A transitional statement can be helpful when asking intimate or difficult questions such as sexual history. 
    **Example:** Learner - “I am now going to ask you some questions about your social history. Some of my questions may be sensitive in nature or embarrassing, but I am asking them to better care for you.”
""",

    "CLOSURE": """
    Identify part(s) of the conversation where the physician closes the conversation, or the lack thereof.

    **Note:** It is important that the patient feel that there is some closure at the end of the encounter. The patient must be left with a definite feeling about what will happen next, what Learner will do, what the patient should do, and when the next communication will occur. Closure will vary in detail according to the level of the Learner. 
    Effective closure to the healthcare visit contains three components:
    - What the Learner will do
    - What the Patient will do
    - When the next steps will occur
    **Example:** “I will give you a prescription for antibiotics (what) and I would like you to get blood tests (what). I would like to see you again in one week (when).” Or “I will go speak to the team (what). If you would please change into your clothes (what). We will be back in a few minutes (when) to discuss your concerns together.”
"""
}
