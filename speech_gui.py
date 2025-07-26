import tkinter as tk
import speech_recognition as sr
import pyttsx3
import os
from datetime import datetime

# Project: Voice Assistant with GUI
# Created by Srilekha for internal internship project
# Date: July 2025

# setup for text to speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# try to pick female voice if available
for v in voices:
    if "female" in v.name.lower() or "zira" in v.name.lower():
        engine.setProperty('voice', v.id)
        break

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# main logic to check commands
def process_commands(text):
    text = text.lower()

    if "open calculator" in text:
        os.system("calc")
        engine.say("opening calculator")

    elif "open notepad" in text:
        os.system("notepad")
        engine.say("opening notepad")

    elif "open word" in text:
        try:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            engine.say("opening word")
        except:
            engine.say("word not found")

    elif "open powerpoint" in text:
        try:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            engine.say("opening powerpoint")
        except:
            engine.say("powerpoint is not available")

    elif "open notepad plus plus" in text or "open notepad++" in text:
        try:
            os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
            engine.say("opening notepad plus plus")
        except:
            engine.say("notepad plus plus is not installed")

    elif "what time" in text or "what's the time" in text:
        now = datetime.now().strftime("%I:%M %p")
        engine.say("the time is " + now)

    else:
        engine.say(text)

    engine.runAndWait()

# function to listen from mic
def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        status_label.config(text="🎙️ Listening...", fg="#D31C8D")
        root.update()

        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5, phrase_time_limit=20)

        try:
            text = r.recognize_google(audio)
            result_label.config(text="🗣️ You said:\n" + text, fg="#67D3C1")
            status_label.config(text="✅ Processed", fg="#53D38A")
            process_commands(text)

        except sr.UnknownValueError:
            result_label.config(text="❌ Could not understand.", fg="red")
            status_label.config(text="❌ Try again", fg="red")

        except sr.RequestError:
            result_label.config(text="⚠️ Check internet connection", fg="orange")
            status_label.config(text="⚠️ Network error", fg="orange")

# clears screen
def clear_text():
    result_label.config(text="")
    status_label.config(text="")

# GUI part
root = tk.Tk()
root.title("🎤 Srilekha Voice Assistant")
root.geometry("620x540")
root.configure(bg="#45A7B4")

frame = tk.Frame(
    root,
    bg="#E0FFFF",
    bd=10,
    relief="ridge",
    highlightbackground="black",
    highlightcolor="black",
    highlightthickness=3
)
frame.place(relx=0.5, rely=0.5, anchor="center", width=540, height=460)


tk.Label(frame, text="Speak. Recognize. Respond.", font=("Arial", 30, "italic"),
         bg="#E0FFFF", fg="#555").pack(pady=(0, 10))

# heading
tk.Label(frame, text="Speech Recognition", font=("Helvetica", 20, "bold"),
         bg="#E0FFFF", fg="#1F7264").pack(pady=5)

# start button
start_btn = tk.Button(
    frame, text="🎧 Start Listening", font=("Helvetica", 14, "bold"),
    bg="#00ADB5", fg="white", activebackground="#00FFF5", activeforeground="black",
    padx=20, pady=8, command=recognize_speech
)
start_btn.pack(pady=10)

# clear button
clear_btn = tk.Button(
    frame, text="🧹 Clear", font=("Helvetica", 12, "bold"),
    bg="#8A0C75", fg="white", activebackground="#F53F27", activeforeground="black",
    padx=15, pady=5, command=clear_text
)
clear_btn.pack(pady=5)

# status + result
status_label = tk.Label(frame, text="", font=("Helvetica", 12), bg="#E0FFFF", fg="black")
status_label.pack(pady=5)

result_label = tk.Label(frame, text="", font=("Helvetica", 14),
                        wraplength=480, justify="center", bg="#E0FFFF", fg="black")
result_label.pack(pady=15)

# run app
root.mainloop()
