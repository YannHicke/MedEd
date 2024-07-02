# extract_excerpts.py

instructions_start = """
You will be given a transcript of a conversation between a physician and patient, where you will extract relevant direct quotes depending on your task. 
In your response, directly copy the relevant parts of the conversation. Do not output any other additional text other than the direct quotes. Do not remove "Physician:" or "Patient:". If not applicable, just output "Not applicable."

Your task:
"""

instructions_end = """

Here is the conversation transcript for which you will extract direct quotes:

"""

mirs_items = {
    "OPENING": """
    Identify the opening of the conversation where the physician greets the patient, which may include performing a self-introduction, role clarification, and/or polite patient address inquiry.

**Example**: Physician: "Hello, I am Dr. Carter, your cardiologist for today. How should I address you?"
**Example**: Physician: "I am Dr. Carter, your cardiologist. What brings you in today?"
**Example**: Physician: "Hello, I'm the nurse on duty."
**Example**: Physician: "Hello, what brings you in today?"
**Example**: Physician: "What brings you in today??"
""",

    "ELICITS SPECTRUM OF CONCERNS": """
    If applicable, identify part(s) of the conversation where the physician elicits the patient's concerns at the onset of the conversation or lack thereof. 

**Example**:
Physician: "What brings you in today? Is there anything else bothering you?"
Patient: "I’ve been having severe headaches."
Physician: "Okay, and what else?"
Patient: "Sometimes I feel dizzy too."
Physician: "Got it. Is there anything else that we should discuss today?"
Patient: "No, that’s all."

**Example**:
Physician: "What brings you in today?"
Patient: "I’ve been having severe headaches."
Physician: "I see, we'll look into that."
""",

    "NEGOTIATES PRIORITIES & SETS AGENDA": """
    If applicable, identify part(s) of the conversation where the physician negotiates priorities of patient concerns, lists all of the concerns, sets the agenda at the onset of the interview with the patient’s agreement, or lack therof. 
    If the physician does not negotiate priorities or set an agenda, simply state "Physician does not negotiate priorities or set an agenda."

**Example**:
Physician: "Okay. All right. Well, it sounds like the fatigue has been quite troubling for you recently. Let’s prioritize that for today’s discussion. I also notice you mentioned concerns about your diet changes. We'll definitely touch on that as well. How does it sound if we start with the fatigue and then move on to discuss your dietary concerns? We might also consider setting another appointment to cover anything else in depth. Does that approach work for you?"
Patient: "Yeah, that sounds good."

**Example**:
Physician: "I see you're here for headaches. I'll start with that. What medication have you been taking?"
Patient: "I also have some concerns about my sleep and stress levels."
Physician: "Okay, we might cover those later if there's time. Let’s keep the focus on the headaches for now."
""",

    "ELICITING THE NARRATIVE THREAD or the ‘PATIENT’S STORY’": """
    If applicable, identify part(s) of the conversation where the physician encourages and lets the patient talk about their problem, or lack thereof.

**Example**:
Physician: "Tell me about what's been happening with your health recently."
Patient: "It started a few months ago with some mild discomfort, and then..."
Physician: [Listens attentively, nodding, making notes without interrupting]
Patient: "...and that's why I'm really concerned about these symptoms now."
Physician: "Thank you for sharing that. It helps me understand your situation better. Let’s discuss what might be causing these symptoms."

**Example**:
Physician: "So, what brings you in today?"
Patient: "Well, I've been having some pain in my—"
Physician: "Where is the pain? When did it start? Have you taken anything for it?"
Patient: "It’s in my back, it started last week, and I—"
Physician: "Okay, let’s do some tests and I’ll prescribe something for the pain."
""",

    "TIMELINE": """
    Identify part(s) of the conversation where the physician establishes a timeline of the chief concern and history of the present illness or lack thereof. You may not state "Not applicable".

**Example**:
Physician: "Let's start from when you first noticed something was off. Can you walk me through what happened next and how things progressed?"
Patient: "Yes, it started with feeling unusually tired after my usual morning jog about two months ago. A few days later, I noticed my heart was racing even at rest. By the end of that week, I was also experiencing shortness of breath."
Physician: "And how did these symptoms change or develop over the next few weeks?"
Patient: "The shortness of breath got worse, and two weeks ago, I began having mild chest pains occasionally, especially in the evenings."
Physician: "Has there been anything else accompanying these symptoms or any variation in their intensity?"
Patient: "Yes, last week, the chest pains became more frequent, and I noticed swelling in my legs."

**Example**:
Physician: "So you're having chest pains, how long has that been happening?"
Patient: "It's been a few weeks."
Physician: "Okay, and how severe are these pains?"
Patient: "They're quite bad sometimes."
Physician: "Alright, we’ll look into that."
""",

    "ORGANIZATION": """
    Identify part(s) of the conversation regarding the organization of the interview, which may follow a logical order or may be disjointed or unorganized. You may not state "Not applicable".

**Example**:
Physician: "How have you been feeling overall these past few weeks?"
Patient: "Not great, I've been really tired."
Physician: "Can you tell me more about when the tiredness usually occurs?"
Patient: "It's mostly in the mornings, but sometimes after lunch as well."
Physician: "Have there been any recent changes in your diet or daily routines that might correlate with this tiredness?"
Patient: "Now that you mention it, yes, I've been skipping breakfast often because of my early meetings."
Physician: "Let's explore that further. Have you noticed any other symptoms like headaches or dizziness?"
Patient: "Actually, yes, there have been a few headaches in the past week."

**Example**:
Physician: "Have you noticed any changes in your appetite?"
Patient: "Yes, I've been eating less."
Physician: "Okay. Have you had any recent travels?"
Patient: "No, not recently."
Physician: "What about your exercise routine? Has it changed?"
Patient: "It's the same as usual."
Physician: "Do you have any joint pain or stiffness?"
Patient: "No, nothing like that."

""",

    "PACING OF INTERVIEW": """
    Identify excerpt(s) of the conversation, focusing on the physician's attentiveness, the smooth progression of the interview, and the deliberate use of silence. For this task, you are encouraged to extract excerpts liberally.

## Below are two exemplars.
**Example**:
Physician: "I noticed you mentioned earlier that you've been having trouble sleeping. Can you tell me more about when that started?"
Patient: "Yes, it's been about three weeks now. I just lie there, unable to sleep."
Physician: [Silently nods, giving the patient a moment to continue] "That sounds difficult. How has this affected your day-to-day activities?"
Patient: "I'm always tired now, and it's hard to concentrate at work."

**Example**:
Physician: "So, you've been feeling unwell. Tell me about that."
Patient: "Well, it started with some fatigue, and then I—"
Physician: "Fatigue, got it. And are you taking any medications?"
Patient: "Yes, I've been on—"
Physician: "Okay, and any family history we should know about?"

""",

    "QUESTIONING SKILLS – TYPES OF QUESTIONS": """
    Identify question(s) used by the physician, including open-ended questions, why questions, multiple questions, or leading questions.

**Example**:
Physician: "Can you describe what a typical day looks like for you now, considering your current health?"
Patient: "Well, I usually start feeling tired by mid-morning, and I have to take breaks more often than before."
Physician: "What specific times do you find yourself needing to take these breaks?"
Patient: "It's usually around 10 AM and then again at about 2 PM."

**Example**:
Physician: "Do you get tired after you exercise?"
Patient: "Yes, more than usual."
Physician: "Why do you think you're getting tired? Is it because you're not sleeping well or maybe you're not eating properly?"
Patient: "I'm not sure, maybe it's a bit of both. I've also been stressed."
""",

    "QUESTIONING SKILLS - SUMMARIZING": """
    If applicable, identify part(s) of the conversation where the physician summarized data obtained during the interview.

**Example**:
Physician: "So today you've described experiencing a range of symptoms starting with headaches, moving to occasional dizziness, and you've also mentioned some recent issues with your vision. Let me make sure I've got everything: Your headaches began around three weeks ago, initially mild but have increased in frequency and intensity. The dizziness is sporadic, mostly in the mornings, and your vision issues started last week, primarily blurring when reading. Is all of this correct?"
Patient: "Yes, that's right."

**Example**:
Physician: "Okay, we've covered quite a bit today about your headaches and some of your lifestyle factors."
Patient: "Yes, we did."
""",

    "QUESTIONING SKILLS - DUPLICATION": """
    If applicable, identify part(s) of the conversation where the physician unnecessarily repeated questions seeking information that has already been provided or the physician consistently seeked information previously provided, showing a failure to track or remember patient information.
    If no questions were duplicated, simply respond "No questions were duplicated."

**Example**:
Physician: "Can you tell me when you first noticed your symptoms?"
Patient: "It started with a mild fever last Tuesday."
Physician: "Okay, and just to clarify, did any other symptoms accompany the fever at that time?"
Patient: "Yes, I also had some chills and a sore throat."
Physician: [Later in the conversation] "You mentioned earlier that the fever began last Tuesday. To summarize, along with the fever, you had chills and a sore throat, correct?"

**Example**:
Physician: "Have you experienced any nausea associated with your headaches?"
Patient: "Yes, I've had some nausea, mostly in the mornings."
Physician: [Five minutes later] "And you mentioned nausea, right? When does that usually occur?"
Patient: "As I said, it's mostly in the mornings."
""",

    "QUESTIONING SKILLS - LACK OF JARGON": """
    If applicable, identify part(s) of the conversation where the physician avoided medical jargon and instead used language easily understood the patient, or lack thereof.

**Example**:
Physician: "You mentioned feeling an unusual tightness in your chest. Can you describe that feeling? Is it like a pressure or a squeezing sensation?"
Patient: "It's more like a squeezing feeling."
Physician: "That's helpful to know. Sometimes what you're describing is called 'angina,' which is just a medical term for chest pain caused by reduced blood flow to the heart muscle."

**Example**:
Physician: "Based on your symptoms, we're looking at a probable case of gastroesophageal reflux disease, which might be contributing to your dyspepsia."
Patient: "Sorry, I'm not sure what those terms mean."
Physician: "Ah, yes, those are quite technical. Gastroesophageal reflux disease is what you might know as acid reflux, and dyspepsia is just another word for indigestion."
""",

    "QUESTIONING SKILLS - VERIFICATION OF PATIENT INFORMATION (in vignette)": """
    If applicable, identify part(s) of the conversation where the physician seeked clarification, verification, and specificity of the patient’s responses, or lack thereof.

**Example**:
Physician: "You mentioned feeling dizzy occasionally. Can you tell me more about what you're doing when these episodes occur?"
Patient: "Usually, it happens when I stand up too quickly."
Physician: "So it's mainly upon standing. Does this happen every time you stand up quickly, or are there certain times of the day when it's more likely to occur?"
Patient: "It's more in the mornings."

**Example**:
Physician: "So, you've been feeling unwell, correct?"
Patient: "Yes, mostly tired and sometimes dizzy."
Physician: "Okay, let's talk about your diet then."
""",

    "VERBAL FACILITATION SKILLS": """
    If applicable, identify part(s) of the conversation where the physician used verbal encouragement and facilitated skills to engage the patient, or lack thereof.

**Example**:
Physician: "It sounds like you've been quite diligent with your exercise routine. Can you tell me more about what you do?"
Patient: "I try to walk every morning."
Physician: "Every morning, that’s impressive! How has it been affecting your energy levels?"
Patient: "I've noticed I feel less tired during the day."
Physician: "That’s great to hear. It shows how your efforts are paying off."

**Example**:
Physician: "You mentioned you started exercising. What type?"
Patient: "I’ve been trying to walk more."
Physician: "Okay, and your medication?"
Patient: "I take it in the morning."
Physician: "Make sure it’s every morning."
""",

    "EMPATHY AND ACKNOWLEDGING PATIENT CUES": """
    If applicable, identify part(s) of the conversation where the physician used supportive comments regarding the patient’s emotions, demonstrated empathy, or lack thereof. 

**Example**:
Physician: "It sounds like you've been under a lot of stress from these symptoms. It must be quite challenging for you."
Patient: "Yes, it's been very hard."
Physician: "I can only imagine how tough that is. We're here to support you through this and find ways to make you feel better."

**Example**:
Physician: "You need to manage your stress better. Continuing like this will only make your condition worse."
Patient: "I've been trying, but it's not easy."
Physician: "Well, it's important for your health to make an effort."
""",

    "PATIENT’S PERSPECTIVE (BELIEFS; Case specific)": """
    If applicable, identify part(s) of the conversation where the physician elicits and addresses the patient's beliefs and perspective on the illness, or lack thereof. 

**Example**:
Physician: "Can you share what you believe might be causing your symptoms?"
Patient: "I think it might be stress-related because it started when I changed jobs."
Physician: "That’s an important observation. Let’s explore how your job change has coincided with your symptoms and discuss how we can address the stress component as part of your treatment."

**Example**:
Physician: "Your tests show you have high blood pressure. We need to start treatment immediately."
Patient: "Could my job stress be affecting my blood pressure?"
Physician: "It’s all about your diet and exercise. We’ll start you on medication."
""",

    "IMPACT OF ILLNESS ON PATIENT AND PATIENT’S SELF-IMAGE": """
    If applicable, identify part(s) of the conversation where the physician explores how the illness affects the patient's life and self-image, or lack thereof.

**Example**:
Physician: "How has this diagnosis impacted how you see yourself and your day-to-day activities?"
Patient: "It's been hard. I feel like I'm not the same person anymore."
Physician: "It's completely normal to feel that way. Let's discuss how we can help you cope with these changes. We have support groups and counseling services that might help you."

**Example**:
Physician: "You need to start treatment immediately. It's important to manage your symptoms effectively."
Patient: "I'm worried about how this will change my life. I feel very different now."
Physician: "The most important thing is to keep your symptoms under control."
""",

    "SUPPORT SYSTEMS": """
    Identify part(s) of the conversation where the physician explores the patient’s support systems, including emotional, financial support, and access to healthcare.
    If support systems were not discussed, simply state "Physician did not discuss support currently available to the patient."

**Example**:
Physician: "Who do you have at home to support you emotionally during this time?"
Patient: "My sister has been very helpful."
Physician: "That’s good to hear. How are you managing financially with the treatment costs? And do you have reliable access to the healthcare services you need?"
Patient: "It's been difficult financially."
Physician: "Let me give you information about some community resources that can help with healthcare costs and additional support groups that might be beneficial for you and your sister."

**Example**:
Physician: "It’s important to stay positive and manage your treatment effectively."
Patient: "I’m struggling with this on my own, and it’s getting overwhelming."
Physician: "Just try to follow the treatment plan as best you can."
""",

    "PATIENT’S EDUCATION & UNDERSTANDING": """
    If applicable, identify part(s) of the conversation where the physician educates the patient about their condition and assesses the patient’s understanding, or lack thereof. 

**Example**:
Physician: "It's important that you understand how to manage your diabetes at home. Can you explain to me how you'll take your medication and what you should do if your blood sugar goes too high?"
Patient: "I take my medication in the morning and check my blood sugar. If it's too high, I'll..."
Physician: "That’s right, and remember to also..."

**Example**:
Physician: "You need to start taking these new medications for your hypertension. Take one pill in the morning and one in the evening."
Patient: "What should I do if I experience any side effects?"
Physician: "Just continue with the medication and we can discuss it during your next appointment."
""",

    "ASSESS MOTIVATION FOR CHANGES": """
    If applicable, identify part(s) of the conversation where the physician assessed the patient's motivation for lifestyle or behavioral changes, or lack thereof. 

**Example**: 
Physician: "How do you feel about making some changes to your diet to help manage your diabetes?"
Patient: "I know it's important, but I find it hard to stick to diets."
Physician: "That's completely understandable. Let's start with small, manageable changes. How about we try integrating one healthy meal a day and see how that goes?"

**Example**: 
Physician: "You need to start exercising more regularly to improve your heart health."
Patient: "I've tried before, but I struggle with staying motivated."
Physician: "It's very important for your health. Try to make an effort."
""",

    "ACHIEVE A SHARED PLAN": """
    If applicable, identify part(s) of the conversation where the physician discussed the diagnosis or prognosis and/or negotatiated a plan with the patient, or lack thereof.
    
**Example**: 
Physician: "Based on your test results, it looks like you have Type 2 diabetes. Let’s discuss what this means for you and explore how we can manage it. What are your thoughts on treatment, and what approach would you prefer?"
Patient: "I've read about lifestyle changes and medications, but I'm not sure what would be best for me."
Physician: "Both are good options. We can start with some moderate lifestyle adjustments and see how much they help, and consider medications if your sugar levels aren't controlled. How does that sound?"

**Example**: 
Physician: "You have high blood pressure. We need to start you on medication right away."
Patient: "Are there other things I can do besides medication?"
Physician: "Medication is the best option. We'll start with that."
""",

    "ENCOURAGEMENT OF QUESTIONS": """
    If applicable, identify part(s) of the conversation where the physician encouraged the patient to ask questions or lack thereof. 
    If the physician fails to provide the patient with the opportunity to ask questions or discuss additional points, simply state "Physician does not provide patient with opportunities for questions."
    
**Example**:
Physician: "We've discussed your treatment options for managing diabetes. Do you have any questions about what we’ve covered so far?"
Patient: "I'm curious about the side effects of these medications."
Physician: "That’s a great question. Let's go through them..."
[Later in the interview]
Physician: "Before we finish, do you have any other questions or is there anything else you'd like to discuss?"

**Example**:
Physician: "So we will start with this new medication. I'll see you in six weeks for a follow-up."
Patient: "Could I ask about—"
Physician: "We're really pressed for time today, but we can get into more details next time."
""",

    "CLOSURE": """
    Identify the conversation's closure, considering the clarity and completeness of future plans if applicable.

**Example**:
Physician: "We've covered a lot today. I will consult with a specialist about your case and make a referral for you to see them. You should start adjusting your diet as we discussed and begin the physical therapy sessions twice a week. Our office will call you by Tuesday to confirm the details of your referral and next appointment. Do you have any questions or concerns about what we’ve planned?"
Patient: "No, that sounds clear. Thank you."
Physician: "Great, we'll ensure everything is set up for you, and I look forward to seeing how you progress."

**Example**:
Physician: "Alright, so that's it for today. Make sure you follow the instructions we talked about."
Patient: "So, what exactly should I do next? Do I need to come back?"
Physician: "Just go ahead with the changes we discussed. We'll sort out the details later."
"""
}

