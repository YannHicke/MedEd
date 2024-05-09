import sys
import openai
import os
import datetime

# Define the custom CSS
CSS ="""
footer {display: none !important;}
#end_chat_button {
    background-color: red !important;
    color: white !important;
    border: none !important;
}
"""

js = "(x) => alert('Chat finished!')"

# Error checking for command line arguments
# if len(sys.argv) < 3:
#     print("Error: Please provide the API key and the file name (without .txt.) as arguments.")
#     sys.exit(1)

# Read in API key and context
# openai.api_key = sys.argv[1]
base_file_name = sys.argv[1]
patient_info = os.path.join("./context", base_file_name + ".txt")
# ehr_file = os.path.join("../patient_profile_picture", base_file_name + ".png")
# ehr_file = os.path.join("../patient_profile_picture", "James_Turner" + ".png")
ehr_file = os.path.join("./patient_profile_picture", base_file_name + ".png")
session_filename = datetime.datetime.now().strftime("./conversation_history/" + base_file_name + '_%Y-%m-%d_%H-%M-%S.txt')

# Error checking for patient context file existence
if not os.path.exists(patient_info):
    print(f"Error: File '{patient_info}' not found within the 'context' directory.")
    sys.exit(1)

# Error checking for ehr file existence
if not os.path.exists(ehr_file):
    print(f"Error: File '{ehr_file}' not found within the 'patient_profile_picture' directory.")
    sys.exit(1)

if not os.path.exists('./conversation_history'):
    os.makedirs('./conversation_history')
    sys.exit(1)

