
import gradio as gr
from datetime import datetime

def process_command(text):
    if not text or not text.strip():
        return "Please speak or enter a command.", ""

    command = text.lower().strip()

    if "what time" in command or "what's the time" in command:
        response = f"The time is {datetime.now().strftime('%I:%M %p')}."
    elif "hello" in command or "hi" in command:
        response = "Hello! I am Srilekha's Voice Assistant. How can I help you?"
    elif "your name" in command:
        response = "I am Srilekha's Voice Assistant."
    elif "open calculator" in command:
        response = "Opening Calculator is available only in the desktop version."
    elif "open notepad" in command:
        response = "Opening Notepad is available only in the desktop version."
    elif "open word" in command:
        response = "Opening Microsoft Word is available only in the desktop version."
    elif "open powerpoint" in command:
        response = "Opening PowerPoint is available only in the desktop version."
    else:
        response = f"You said: {text}. I am still learning this command."

    return response, response


with gr.Blocks(title="Srilekha Voice Assistant") as demo:
    gr.Markdown("# 🎤 Srilekha Voice Assistant")
    gr.Markdown("### Speak. Recognize. Respond.")
    gr.Markdown(
        "Use the microphone if your browser supports voice input, "
        "or type a command below."
    )

    command_input = gr.Textbox(
        label="Your command",
        placeholder="Try: Hello, or What time is it?",
    )

    with gr.Row():
        run_button = gr.Button("✨ Process Command", variant="primary")
        clear_button = gr.ClearButton()

    response_box = gr.Textbox(label="Assistant Response", interactive=False)
    speech_output = gr.Textbox(label="Voice Output Text", visible=False)

    run_button.click(
        fn=process_command,
        inputs=command_input,
        outputs=[response_box, speech_output],
    )

    command_input.submit(
        fn=process_command,
        inputs=command_input,
        outputs=[response_box, speech_output],
    )

demo.launch()
