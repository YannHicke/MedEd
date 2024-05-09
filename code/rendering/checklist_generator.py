import json
from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import sys
import pandas as pd

"""
1) Opening
__ 2) Elicits Spectrum of Concerns
__ 3) Negotiates Priorities and Sets Agenda
__ 4) Eliciting Narrative Thread or “Patient’s Story”
__ 5) Timeline
__ 6) Organization
__ 7) Transitional Statements
__ 8) Pacing of Interview
__ 9) Types of Questions
__ 10) Summarizing
__ 11) Duplication
__ 12) Lack of Jargon
__ 13) Verification of Patient Information
__ 14) Interactive Technique


__ 15) Verbal Facilitation Skills
__ 16) Non-Verbal Facilitation Skills
__ 17) Empathy and Acknowledging Patient Cues
__ 18) Patient’s Perspective (Beliefs)
__ 19) Impact of Illness on Patient and Self-Image
__ 20) Impact of Illness on Family
__ 21) Support Systems
__ 22) Patient’s Education and Understanding
__ 23) Assess Motivation for Changes
__ 24) Admitting Lack of Knowledge
__ 25) Investigation/Procedure Informed Consent
__ 26) Achieve a Shared Plan
__ 27) Encouragement of Questions
__ 28) Closure
"""


case = sys.argv[1]

def add_checkmark(canvas, x, y):
    canvas.setFont("Helvetica", 12)
    canvas.setFillColor(colors.green)
    canvas.drawString(x, y, "✓")

def add_cross(canvas, x, y):
    canvas.setFont("Helvetica", 12)
    canvas.setFillColor(colors.red)
    canvas.drawString(x, y, "✗")

def add_score(canvas, x, y, score):
    canvas.setFont("Helvetica", 10)
    canvas.setFillColor(colors.blue)
    if score == 0:
        canvas.setFont("Helvetica", 7)
        canvas.drawString(x, y, "N/A")
    elif score == 1:
        canvas.setFillColor(colors.orange)
        canvas.drawString(x, y, "1")
    else:
        canvas.drawString(x, y, str(score))

def get_coordinates(item):
    coordinates = {
        "past illnesses (childhood adult)": (60, 594),
        "operations/injuries/accidents": (60, 582),
        "hospitalizations": (60, 570),
        "immunizations": (60, 560),
        "age-appropriate screening tests": (60, 548),
        "OB history": (60, 536),
        "psychiatric history": (60, 524),
        "taking medications": (60, 502),
        "allergies": (60, 470),
        "education": (326, 594),
        "social background (family household)": (326, 582),
        "occupational history": (326, 570),
        "habits (recreational drugs alcohol tobacco)": (326, 560),
        "support systems": (326, 548),
        "sexual history": (326, 536),
        "diet history": (326, 524),
        "exercise": (326, 512),
        "religious or spiritual beliefs": (326, 501),
        "safety (car gun fire)": (326, 488),
        "financial concerns": (326, 478),
        "age/health status of siblings": (60, 434),
        "age/health status of parents": (60, 422),
        "check for other FH of DM HTN CA stroke or heart disease": (60, 410),
        "age/health status of grandparents": (326, 434),
        "age/health status of children": (326, 422),
        "General Health": (60, 378),
        "Head, Eyes, Ears, Nose, Throat": (100, 378),
        "Pulmonary": (154, 378),
        "Cardiovascular": (194, 378),
        "Gastrointestinal": (226, 378),
        "Neuromuscular": (256, 378),
        "Hematologic": (289, 378),
        "Genitourinary": (335, 378),
        "Endocrine": (373, 378),
        "Psychiatric": (418, 378),
        



        # Add coordinates for each item in your form
    }
    return coordinates.get(item, (0, 0))

def get_coordinates_score(item):
    coordinates = {
        "Opening": (54, 298),
        "Elicits Spectrum of Concerns": (54, 286),
        "Negotiates Priorities and Sets Agenda": (54, 274),
        "Eliciting Narrative Thread or Patients Story": (54, 262),
        "Timeline": (54, 250),
        "Organization": (54, 238),
        "Transitional Statements": (54, 227),
        "Pacing of Interview": (54, 216),
        "Types of Questions": (54, 206),
        "Summarizing": (54, 194),
        "Duplication": (54, 182),
        "Lack of Jargon": (54, 170),
        "Verification of Patient Information": (54, 158),
        "Interactive Technique": (54, 146),
        "Verbal Facilitation Skills": (326, 298),
        "Non-Verbal Facilitation Skills": (326, 286),
        "Empathy and Acknowledging Patient Cues": (326, 274),
        "Patients Perspective (Beliefs)": (326, 262),
        "Impact of Illness on Patient and Self-Image": (326, 250),
        "Impact of Illness on Family": (326, 238),
        "Support Systems": (326, 227),
        "Patients Education and Understanding": (326, 216),
        "Assess Motivation for Changes": (326, 206),
        "Admitting Lack of Knowledge": (326, 194),
        "Investigation/Procedure Informed Consent": (326, 182),
        "Achieve a Shared Plan": (326, 170),
        "Encouragement of Questions": (326, 158),
        "Closure": (326, 146),
    }
    return coordinates.get(item, (0, 0))

# Load the JSON data
with open(f'../results/{case}_results.json') as f:
    data = json.load(f)

# Load the CSV data
df = pd.read_csv(f'../results/{case}.csv', encoding='latin1')
# df['Unnamed: 0'] = df['Unnamed: 0'].str.capitalize()
df.rename(columns={'Unnamed: 0': 'item'}, inplace=True)



# Open the PDF form
pdf_reader = PdfReader(open('../results/form.pdf', 'rb'))
pdf_writer = PdfWriter()

# Get the first page of the PDF
page = pdf_reader.pages[0]

# Create a canvas object to draw on the page
c = canvas.Canvas('temp.pdf', pagesize=letter)

# Iterate through the JSON data and add checkmarks or crosses
for section, items in data.items():
    for item, values in items.items():
        discussed = values['discussed']
        x, y = get_coordinates(item)
        if discussed == 'discussed':
            add_checkmark(c, x, y)
        else:
            add_cross(c, x, y)

# Iterate through the CSV data and add the scores
for index, row in df.iterrows():
    item = row['item']
    score = row['score']
    x, y = get_coordinates_score(item)
    add_score(c, x, y, score)

# Save the canvas modifications
c.showPage()
c.save()

# Merge the modifications with the original page
overlay_page = PdfReader('temp.pdf').pages[0]
page.merge_page(overlay_page)

# Add the modified page to the PDF writer
pdf_writer.add_page(page)

# Save the modified PDF
with open(f'../results/{case}_form.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)