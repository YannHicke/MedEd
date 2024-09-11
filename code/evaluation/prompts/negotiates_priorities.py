NEGOTIATES_PRIORITIES_SETS_AGENDA = """
You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the student negotiates the patient’s priorities and sets the agenda for their visit. You will then provide your evaluation in a given JSON format.

To ensure a thorough evaluation, follow these steps:

  **Step 1. Scoring:**
    - As you read the transcript, evaluate the medical student’s performance based on the criteria for each score level:
      - **Score 5:** The student fully negotiates the priorities of patient concerns. The student lists all of the concerns, sets the agenda at the onset of the interview, and gets the patient’s agreement to the agenda.
      - **Score 4:** The student mostly negotiates the priorities of patient concerns, but not as thoroughly as in a score of 5. They set the agenda at the onset of the interview before they discuss the patient's spectrum of concerns and get the patient’s agreement to the agenda.
      - **Score 3:** The student sets the agenda but the student elicits only partial concerns and therefore does not accomplish the complete patient agenda for their visit.
      - **Score 2:** The student minimally negotiates priorities and fails to accomplish the complete patient agenda. Limited efforts are made to set an agenda.
      - **Score 1:** The student does not negotiate priorities or set an agenda. The student focuses only on the chief complaint and takes only the physician’s needs into account. 

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





# NEGOTIATES_PRIORITIES_SETS_AGENDA_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient.
# You will be evaluating how well the medical student negotiates priorities of patient concerns, lists all of the concerns, and sets the agenda at the onset of the interview with the patient's agreement. 
# To ensure a thorough evaluation, follow these steps:

# **1. Identify Key Elements:**
#    -  As you read the excerpt, create a list noting whether each element is present or absent:
#       - Elicitation of all patient concerns
#       - Listing of all concerns
#       - Negotiation of priorities with patient
#       - Setting an agenda for the visit
#       - Getting patient's agreement on the agenda

# **2.  Self-Consistency Check:** Ensure your list from Step 1 aligns with the criteria for each score level:
#     - **Score 5:** All concerns listed, priorities negotiated, agenda set with patient agreement
#     - **Score 4:** Agenda set before all concerns fully elicited
#     - **Score 3:** Agenda set without negotiating priorities
#     - **Score 2:** Some concerns listed, no agenda set or priorities negotiated
#     - **Score 1:** Only chief concern addressed, no agenda setting or priority negotiation

# **3.  Provide Justification:** Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

#   "examples": [
#     {
#       "score": 5,
#       "excerpt": "Physician: \"So, Mrs. Johnson, you've mentioned three issues today: the abdominal pain, your recent weight loss, and the persistent cough. Are there any other concerns you'd like to discuss?\"
# Patient: \"No, that covers everything.\"
# Physician: \"Alright. Given our time today, we might not be able to address all of these in depth. Which of these issues is most important to you right now?\"
# Patient: \"I'm really worried about the abdominal pain.\"
# Physician: \"I understand. Let's prioritize the abdominal pain for today's discussion. We'll also touch on your weight loss as that might be related. For the cough, would you be comfortable if we schedule a follow-up appointment to discuss that in more detail?\"
# Patient: \"Yes, that sounds good.\"
# Physician: \"Great. So our plan for today is to focus on your abdominal pain, discuss your weight loss, and then briefly touch on your cough to see if there's anything urgent we need to address. Does this plan work for you?\"
# Patient: \"Yes, that works for me.\"
# Physician: \"Excellent. Let's begin by discussing your abdominal pain in more detail.\"",
#       "response": {
#         "elements_present": [
#           "Elicitation of all patient concerns",
#           "Listing of all concerns",
#           "Negotiation of priorities with patient",
#           "Setting an agenda for the visit",
#           "Getting patient's agreement on the agenda"
#         ],
#         "elements_absent": [],
#         "score": 5,
#         "justification": "The physician excels in negotiating priorities and setting an agenda. They summarize all the patient's concerns: \"you've mentioned three issues today: the abdominal pain, your recent weight loss, and the persistent cough.\" They then ask for the patient's priority: \"Which of these issues is most important to you right now?\" The physician sets a clear agenda based on the patient's priority and the time constraints, suggesting a plan for addressing the lower-priority concern: \"For the cough, would you be comfortable if we schedule a follow-up appointment to discuss that in more detail?\" Finally, they clearly state the plan and get the patient's agreement: \"Does this plan work for you?\" This approach demonstrates excellent patient-centered care and effective agenda-setting."
#       }
#     },
#     {
#       "score": 4,
#       "excerpt": "Physician: \"Hello, Mrs. Smith. I understand you're here about headaches and fatigue. Let's plan to discuss both of these today, starting with the headaches. We'll then move on to the fatigue if we have time. How does that sound?\"
# Patient: \"That's fine, but I also wanted to ask about some recent weight gain.\"
# Physician: \"I see. We'll try to address that as well if time permits. Let's begin with discussing your headaches.\"",
#       "response": {
#         "elements_present": [
#           "Listing of some concerns",
#           "Setting an agenda for the visit",
#           "Getting patient's partial agreement on the agenda"
#         ],
#         "elements_absent": [
#           "Elicitation of all patient concerns",
#           "Negotiation of priorities with patient"
#         ],
#         "score": 4,
#         "justification": "The physician sets an agenda at the beginning of the interview: \"Let's plan to discuss both of these today, starting with the headaches.\" They seek the patient's agreement: \"How does that sound?\" However, this agenda is set before all concerns are fully elicited, as evidenced by the patient bringing up an additional concern about weight gain. The physician acknowledges this new concern but doesn't fully incorporate it into the agenda: \"We'll try to address that as well if time permits.\" While the physician does a good job of setting an initial agenda, they miss the opportunity to fully elicit all concerns before doing so, resulting in a score of 4."
#       }
#     },
#     {
#       "score": 3,
#       "excerpt": "Physician: \"Good morning, Mr. Brown. I understand you're here for a follow-up on your diabetes and to discuss some new symptoms. Let's start with reviewing your diabetes management, then we'll discuss your new symptoms, and finally, we'll talk about any necessary changes to your treatment plan. Does that work for you?\"
# Patient: \"Yes, but I'm really worried about these new symptoms.\"
# Physician: \"I understand, but it's important that we review your diabetes management first. We'll get to your new symptoms right after that.\"",
#       "response": {
#         "elements_present": [
#           "Listing of some concerns",
#           "Setting an agenda for the visit",
#           "Getting patient's agreement on the agenda"
#         ],
#         "elements_absent": [
#           "Elicitation of all patient concerns",
#           "Negotiation of priorities with patient"
#         ],
#         "score": 3,
#         "justification": "The physician sets a clear agenda for the visit: \"Let's start with reviewing your diabetes management, then we'll discuss your new symptoms, and finally, we'll talk about any necessary changes to your treatment plan.\" They also seek the patient's agreement: \"Does that work for you?\" However, when the patient expresses more concern about the new symptoms, the physician doesn't negotiate priorities, instead insisting on their original plan: \"I understand, but it's important that we review your diabetes management first.\" This shows a lack of flexibility and failure to negotiate priorities based on the patient's expressed concerns, resulting in a score of 3."
#       }
#     },
#     {
#       "score": 2,
#       "excerpt": "Physician: \"What brings you in today, Ms. Davis?\"
# Patient: \"I've been having trouble sleeping, and I'm also concerned about some chest pain I've been experiencing.\"
# Physician: \"I see. Those both sound concerning. Let's start by talking about your sleep issues. How long has this been going on?\"
# Patient: \"Well, the chest pain is really what's worrying me most.\"
# Physician: \"Okay, we can discuss that too. Now, about your sleep problems...\"",
#       "response": {
#         "elements_present": [
#           "Listing of some concerns"
#         ],
#         "elements_absent": [
#           "Elicitation of all patient concerns",
#           "Negotiation of priorities with patient",
#           "Setting an agenda for the visit",
#           "Getting patient's agreement on the agenda"
#         ],
#         "score": 2,
#         "justification": "The physician acknowledges the patient's concerns: \"I see. Those both sound concerning.\" However, they don't set a clear agenda for the visit or negotiate priorities with the patient. When the patient expresses that the chest pain is their primary concern, the physician briefly acknowledges it but continues with their own chosen topic: \"Okay, we can discuss that too. Now, about your sleep problems...\" This approach shows a lack of proper agenda-setting and priority negotiation, resulting in a score of 2."
#       }
#     },
#     {
#       "score": 1,
#       "excerpt": "Physician: \"Hello, Mr. Wilson. What's the main issue you're here for today?\"
# Patient: \"I've been having this rash on my arm, but I'm also having some other issues I'd like to discuss.\"
# Physician: \"Let's focus on the rash for now. How long have you had it?\"
# Patient: \"About a week, but—\"
# Physician: \"And have you tried any over-the-counter treatments?\"",
#       "response": {
#         "elements_present": [],
#         "elements_absent": [
#           "Elicitation of all patient concerns",
#           "Listing of all concerns",
#           "Negotiation of priorities with patient",
#           "Setting an agenda for the visit",
#           "Getting patient's agreement on the agenda"
#         ],
#         "score": 1,
#         "justification": "The physician focuses solely on the first complaint mentioned by the patient: \"Let's focus on the rash for now.\" When the patient attempts to bring up other issues, the physician dismisses them and continues to focus only on the rash. There is no attempt to elicit all of the patient's concerns, negotiate priorities, or set an agenda for the visit. The physician's approach is entirely physician-centered, ignoring the patient's attempts to discuss other health issues. This complete lack of agenda-setting and priority negotiation results in a score of 1."
#       }
#     }
#   ],
#   "response_format": [
#     {
#       "score": "json_object"
#     }
#   ]

# """

# NEGOTIATES_PRIORITIES_SETS_AGENDA2_OLD = """
# You will be given the transcript of a medical interview between a medical student (called physician) and a patient. Your task is to evaluate how well the medical student negotiates priorities of patient concerns, lists all of the concerns, and sets the agenda at the onset of the interview with the patient's agreement. Provide your assessment in a specific JSON format.

# Evaluation Process:
# 1. Identify Key Elements: As you read the excerpt, note whether each element is present or absent:
#    - Elicitation of all patient concerns
#    - Listing of all concerns
#    - Negotiation of priorities with patient
#    - Setting an agenda for the visit
#    - Getting patient's agreement on the agenda

# 2. Self-Consistency Check: Ensure your list from Step 1 aligns with the criteria for each score level:
#    - Score 5: All concerns listed, priorities negotiated, agenda set with patient agreement
#    - Score 4: Agenda set before all concerns fully elicited
#    - Score 3: Agenda set without negotiating priorities
#    - Score 2: Some concerns listed, no agenda set or priorities negotiated
#    - Score 1: Only chief concern addressed, no agenda setting or priority negotiation

# 3. Provide Justification: Based on your analysis in Steps 1 and 2, assign a score and clearly explain your reasoning. Directly quote phrases from the excerpt to support your evaluation.

# Please provide your evaluation in the following JSON format. Provide your entire response in the JSON format and nothing else:

# {
#   "evaluation": {
#     "elements_present": [
#       "List of elements present in the interview"
#     ],
#     "elements_absent": [
#       "List of elements missing from the interview"
#     ],
#     "score": 0,
#     "justification": "A clear explanation of your scoring, with direct quotes from the excerpt to support your evaluation"
#   }
# }

# Examples:
# The following examples illustrate how to apply the evaluation criteria and format the response:

# Example 1:
# Input: 
# Physician: "So, Mrs. Johnson, you've mentioned three issues today: the abdominal pain, your recent weight loss, and the persistent cough. Are there any other concerns you'd like to discuss?"
# Patient: "No, that covers everything."
# Physician: "Alright. Given our time today, we might not be able to address all of these in depth. Which of these issues is most important to you right now?"
# Patient: "I'm really worried about the abdominal pain."
# Physician: "I understand. Let's prioritize the abdominal pain for today's discussion. We'll also touch on your weight loss as that might be related. For the cough, would you be comfortable if we schedule a follow-up appointment to discuss that in more detail?"
# Patient: "Yes, that sounds good."
# Physician: "Great. So our plan for today is to focus on your abdominal pain, discuss your weight loss, and then briefly touch on your cough to see if there's anything urgent we need to address. Does this plan work for you?"
# Patient: "Yes, that works for me."
# Physician: "Excellent. Let's begin by discussing your abdominal pain in more detail."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Elicitation of all patient concerns",
#       "Listing of all concerns",
#       "Negotiation of priorities with patient",
#       "Setting an agenda for the visit",
#       "Getting patient's agreement on the agenda"
#     ],
#     "elements_absent": [],
#     "score": 5,
#     "justification": "The physician excels in negotiating priorities and setting an agenda. They summarize all the patient's concerns: \"you've mentioned three issues today: the abdominal pain, your recent weight loss, and the persistent cough.\" They then ask for the patient's priority: \"Which of these issues is most important to you right now?\" The physician sets a clear agenda based on the patient's priority and the time constraints, suggesting a plan for addressing the lower-priority concern: \"For the cough, would you be comfortable if we schedule a follow-up appointment to discuss that in more detail?\" Finally, they clearly state the plan and get the patient's agreement: \"Does this plan work for you?\" This approach demonstrates excellent patient-centered care and effective agenda-setting."
#   }
# }

# Example 2:
# Input: 
# Physician: "Hello, Mrs. Smith. I understand you're here about headaches and fatigue. Let's plan to discuss both of these today, starting with the headaches. We'll then move on to the fatigue if we have time. How does that sound?"
# Patient: "That's fine, but I also wanted to ask about some recent weight gain."
# Physician: "I see. We'll try to address that as well if time permits. Let's begin with discussing your headaches."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Listing of some concerns",
#       "Setting an agenda for the visit",
#       "Getting patient's partial agreement on the agenda"
#     ],
#     "elements_absent": [
#       "Elicitation of all patient concerns",
#       "Negotiation of priorities with patient"
#     ],
#     "score": 4,
#     "justification": "The physician sets an agenda at the beginning of the interview: \"Let's plan to discuss both of these today, starting with the headaches.\" They seek the patient's agreement: \"How does that sound?\" However, this agenda is set before all concerns are fully elicited, as evidenced by the patient bringing up an additional concern about weight gain. The physician acknowledges this new concern but doesn't fully incorporate it into the agenda: \"We'll try to address that as well if time permits.\" While the physician does a good job of setting an initial agenda, they miss the opportunity to fully elicit all concerns before doing so, resulting in a score of 4."
#   }
# }

# Example 3:
# Input: 
# Physician: "Good morning, Mr. Brown. I understand you're here for a follow-up on your diabetes and to discuss some new symptoms. Let's start with reviewing your diabetes management, then we'll discuss your new symptoms, and finally, we'll talk about any necessary changes to your treatment plan. Does that work for you?"
# Patient: "Yes, but I'm really worried about these new symptoms."
# Physician: "I understand, but it's important that we review your diabetes management first. We'll get to your new symptoms right after that."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Listing of some concerns",
#       "Setting an agenda for the visit",
#       "Getting patient's agreement on the agenda"
#     ],
#     "elements_absent": [
#       "Elicitation of all patient concerns",
#       "Negotiation of priorities with patient"
#     ],
#     "score": 3,
#     "justification": "The physician sets a clear agenda for the visit: \"Let's start with reviewing your diabetes management, then we'll discuss your new symptoms, and finally, we'll talk about any necessary changes to your treatment plan.\" They also seek the patient's agreement: \"Does that work for you?\" However, when the patient expresses more concern about the new symptoms, the physician doesn't negotiate priorities, instead insisting on their original plan: \"I understand, but it's important that we review your diabetes management first.\" This shows a lack of flexibility and failure to negotiate priorities based on the patient's expressed concerns, resulting in a score of 3."
#   }
# }

# Example 4:
# Input: 
# Physician: "What brings you in today, Ms. Davis?"
# Patient: "I've been having trouble sleeping, and I'm also concerned about some chest pain I've been experiencing."
# Physician: "I see. Those both sound concerning. Let's start by talking about your sleep issues. How long has this been going on?"
# Patient: "Well, the chest pain is really what's worrying me most."
# Physician: "Okay, we can discuss that too. Now, about your sleep problems..."

# Output:
# {
#   "evaluation": {
#     "elements_present": [
#       "Listing of some concerns"
#     ],
#     "elements_absent": [
#       "Elicitation of all patient concerns",
#       "Negotiation of priorities with patient",
#       "Setting an agenda for the visit",
#       "Getting patient's agreement on the agenda"
#     ],
#     "score": 2,
#     "justification": "The physician acknowledges the patient's concerns: \"I see. Those both sound concerning.\" However, they don't set a clear agenda for the visit or negotiate priorities with the patient. When the patient expresses that the chest pain is their primary concern, the physician briefly acknowledges it but continues with their own chosen topic: \"Okay, we can discuss that too. Now, about your sleep problems...\" This approach shows a lack of proper agenda-setting and priority negotiation, resulting in a score of 2."
#   }
# }

# Example 5:
# Input: 
# Physician: "Hello, Mr. Wilson. What's the main issue you're here for today?"
# Patient: "I've been having this rash on my arm, but I'm also having some other issues I'd like to discuss."
# Physician: "Let's focus on the rash for now. How long have you had it?"
# Patient: "About a week, but—"
# Physician: "And have you tried any over-the-counter treatments?"

# Output:
# {
#   "evaluation": {
#     "elements_present": [],
#     "elements_absent": [
#       "Elicitation of all patient concerns",
#       "Listing of all concerns",
#       "Negotiation of priorities with patient",
#       "Setting an agenda for the visit",
#       "Getting patient's agreement on the agenda"
#     ],
#     "score": 1,
#     "justification": "The physician focuses solely on the first complaint mentioned by the patient: \"Let's focus on the rash for now.\" When the patient attempts to bring up other issues, the physician dismisses them and continues to focus only on the rash. There is no attempt to elicit all of the patient's concerns, negotiate priorities, or set an agenda for the visit. The physician's approach is entirely physician-centered, ignoring the patient's attempts to discuss other health issues. This complete lack of agenda-setting and priority negotiation results in a score of 1."
#   }
# }

# Now, please evaluate the following medical interview transcript:
# """