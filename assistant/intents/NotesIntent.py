import os

from intentClassifier import classify

NOTES_DIR = "data/notes"

def setup():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def read_note(name):
    note_path = os.path.join(NOTES_DIR, f"{name}.txt")
    if os.path.exists(note_path):
        with open(note_path, "r") as f:
            print(f.read())
    else:
        print("Note not found.")

def create_note(name):
    note_path = os.path.join(NOTES_DIR, f"{name}.txt")
    with open(note_path, "w") as f:
        f.write("")

def delete_note(name):
    note_path = os.path.join(NOTES_DIR, f"{name}.txt")
    if os.path.exists(note_path):
        os.remove(note_path)
    else:
        print("Note not found.")

def handle(user_input, intent_group):
    intent_name = classify(user_input, intent_group)
    name =""
    name = user_input.lower().split("note")[-1].strip()
    keywords = ["named", "called", "titled"]
    for keyword in keywords:
        if name.find(keyword) != -1:
            name = name.split(keyword)[-1].strip()
    if intent_name == "read":
        read_note(name)
    elif intent_name == "create":
        create_note(name)
    elif intent_name == "delete":
        delete_note(name)
    else:
        print("Sorry, I didn't understand the command.")