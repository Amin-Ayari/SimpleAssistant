import os
import subprocess
from intentClassifier import classify




def open_app(name):
    try:
        subprocess.Popen(name)
    except FileNotFoundError:
        print(f"Could not find application: {name}")



def close_app(name):
    try:
        if os.name == "nt": 
            subprocess.run(["taskkill", "/IM", f"{name}.exe", "/F"], check=True)

    except subprocess.CalledProcessError:
        print(f"Could not close application: {name}")

def handle(user_input, intent_group):
    intent_name = classify(user_input, intent_group)
    name =""
    input_clean = user_input.lower()
    name = input_clean.strip("please").strip("open").strip("close").strip().strip("launch").strip("start").strip()
    if intent_name == "open":
        open_app(name)
    elif intent_name == "close":
        close_app(name)
    else:
        print("Sorry, I didn't understand the command.")