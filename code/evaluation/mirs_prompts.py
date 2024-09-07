"""
mirs_prompts.py 
---------------
This file contains the MIRS rubric prompts for scoring and evaluating conversations.
"""

from prompts.opening import OPENING
from prompts.spectrum_of_concerns import SPECTRUM_OF_CONCERNS
from prompts.negotiates_priorities import NEGOTIATES_PRIORITIES_SETS_AGENDA
from prompts.eliciting_narrative_thread import ELICITING_NARRATIVE_THREAD
from prompts.timeline import TIMELINE
from prompts.organisation import ORGANIZATION
from prompts.transitional_statements import TRANSITIONAL_STATEMENTS
from prompts.questioning_types_of_questions import QUESTIONING_SKILLS_TYPES_OF_QUESTIONS
from prompts.questioning_summarizing import QUESTIONING_SKILLS_SUMMARIZING
from prompts.questioning_duplication import QUESTIONING_SKILLS_DUPLICATION
from prompts.questioning_lack_of_jargon import QUESTIONING_SKILLS_LACK_OF_JARGON
from prompts.questioning_verification import QUESTIONING_SKILLS_VERIFICATION_OF_PATIENT_INFORMATION
from prompts.verbal_facilitation import VERBAL_FACILITATION_SKILLS
from prompts.empathy_acknowledging_patient_cues import EMPATHY_AND_ACKNOWLEDGING_PATIENT_CUES
from prompts.patient_perspective import PATIENTS_PERSPECTIVE_BELIEFS
from prompts.patient_self_image import IMPACT_OF_ILLNESS_ON_PATIENT_AND_PATIENT_SELF_IMAGE
from prompts.support_systems import SUPPORT_SYSTEMS
from prompts.patient_education import PATIENTS_EDUCATION_AND_UNDERSTANDING
from prompts.assess_motivation import ASSESS_MOTIVATION_FOR_CHANGES
from prompts.achieved_shared_plan import ACHIEVE_A_SHARED_PLAN
from prompts.encouragement_questions import ENCOURAGEMENT_OF_QUESTIONS
from prompts.closure import CLOSURE


mirs_prompts = {
    "OPENING": OPENING,
    "ELICITS SPECTRUM OF CONCERNS": SPECTRUM_OF_CONCERNS,
    "NEGOTIATES PRIORITIES & SETS AGENDA": NEGOTIATES_PRIORITIES_SETS_AGENDA,
    "ELICITING THE NARRATIVE THREAD or the PATIENT_S STORY": ELICITING_NARRATIVE_THREAD,
    "TIMELINE": TIMELINE,
    "ORGANIZATION": ORGANIZATION,
    "TRANSITIONAL STATEMENTS": TRANSITIONAL_STATEMENTS,
    "QUESTIONING SKILLS TYPES OF QUESTIONS": QUESTIONING_SKILLS_TYPES_OF_QUESTIONS,
    "QUESTIONING SKILLS SUMMARIZING": QUESTIONING_SKILLS_SUMMARIZING,
    "QUESTIONING SKILLS DUPLICATION": QUESTIONING_SKILLS_DUPLICATION,
    "QUESTIONING SKILLS LACK OF JARGON": QUESTIONING_SKILLS_LACK_OF_JARGON,
    "QUESTIONING SKILLS VERIFICATION OF PATIENT INFORMATION": QUESTIONING_SKILLS_VERIFICATION_OF_PATIENT_INFORMATION,
    "VERBAL FACILITATION SKILLS": VERBAL_FACILITATION_SKILLS,
    "EMPATHY AND ACKNOWLEDGING PATIENT CUES": EMPATHY_AND_ACKNOWLEDGING_PATIENT_CUES,
    "PATIENTS PERSPECTIVE & BELIEFS": PATIENTS_PERSPECTIVE_BELIEFS,
    "IMPACT OF ILLNESS ON PATIENT AND PATIENT_S SELF-IMAGE": IMPACT_OF_ILLNESS_ON_PATIENT_AND_PATIENT_SELF_IMAGE,
    "SUPPORT SYSTEMS": SUPPORT_SYSTEMS,
    "PATIENTS EDUCATION AND UNDERSTANDING": PATIENTS_EDUCATION_AND_UNDERSTANDING,
    "ASSESS MOTIVATION FOR CHANGES": ASSESS_MOTIVATION_FOR_CHANGES,
    "ACHIEVE A SHARED PLAN": ACHIEVE_A_SHARED_PLAN,
    "ENCOURAGEMENT OF QUESTIONS": ENCOURAGEMENT_OF_QUESTIONS,
    "CLOSURE": CLOSURE
}

