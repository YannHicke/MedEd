import gradio as gr
import signal
from config import *
from openai import OpenAI



context = """You are an AI designed to help medical professionals practice conversing empathetically by imitating patients. 
Imitate the following patient so that a medical professional can practice conducting a history taking exam.
Note you may ask the medical professional any questions.

Your affect is pleasant. You are nervous about your illness.

Do not provide information on smoking, alcohol use, or recreational drug use without prompting. You may discuss them when directly asked or when\
discussing social history or your lifestyle. 
Do not provide your sexual history unless directly asked.

Stay in character, do not admit you are an AI.

If you are asked about details about family members not provided within the family history context, you do not know the health status of this\
family member or if they are alive or dead.

Do not volunteer responses pertaining to the review of systems unless directly asked about it.

When you are asked an open-ended question about your symptoms, include a statement of emotion, progress, or challenge in your answer.
An example of a statement of emotion is as follows: My father had colon cancer and died because of it. I'm scared the same thing is happening to me.
An example of a statement of progress is as follows: I'm smoking less than when I last came to the doctor's.
An example of a statement of challenge is as follows: I've been having difficulty remembering to take my medications every day. 

If the medical professional acknowledges, praises, reassures, encourages, or shows support in their response, thank them in your next response.
If the medical professional gives inadequate acknowledgement, uses inappropriate humor, denies your concerns, or terminates the discussion of\
your emotions, do not thank them in your next response.

If the user respond unsympathetically, use a nonjudgemental tone in response.

Here is the patient's information for whom to imitate:
 
 """

# context_file = '../context/context_GI_Bleeding.txt'
context_file = '../context/context_palpitations.txt'
# Read the content from the provided file
with open(context_file, 'r') as f:
    context += f.read().strip()

messages = [
    {"role": "system", "content": context},
]

convo_history = []


def save_conversation(history):
    with open(session_filename, 'w') as f:  # 'w' mode to overwrite if the file exists
        for message in history:
            role = message["role"]
            content = message["content"]
            f.write(f"{role.capitalize()}: {content}\n")
        f.write("\n")

def end_chat():
    """End the chat, save the conversation, and quit the application."""
    save_conversation(convo_history)
    os.kill(os.getpid(), signal.SIGINT)

def add_text(history, text):
    messages.append({"role": "user", "content": text})
    convo_history.append({"role": "user", "content": text})
    history = history + [(text, None)]
    return history, ""

client = OpenAI(api_key="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")

def bot(history):
    response = client.chat.completions.create(
            model="gpt-4-0125-preview", 
            messages=messages
        )
    reply= response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    convo_history.append({"role": "assistant", "content": reply})
    history[-1][1] = reply
    return history


with gr.Blocks(title="OSCE_Patient",theme=gr.themes.Soft(),css=CSS) as demo:
    gr.Markdown("<h1><center>Patient</center></h1>")

    with gr.Row():
        with gr.Column():
            gr.Image(ehr_file, show_label=False)

        with gr.Column(scale=4):
            chatbot = gr.Chatbot([], elem_id="chatbot", show_label=False)

            with gr.Row():
                with gr.Column(scale=1):
                    txt = gr.Textbox(
                        show_label=False,
                        placeholder="Enter text and press enter"
                    )
                with gr.Column(scale=0, min_width=110):
                    end_button = gr.Button("End Chat", elem_id="end_chat_button").click(end_chat)

    txt.submit(add_text, [chatbot, txt], [chatbot, txt]).then(
        bot, chatbot, chatbot
    )

demo.launch(share=True)
