from intentClassifier import classify
import webbrowser
import urllib.parse

from winotify import Notification

def alert(message: str):
    toast = Notification(
        app_id="Assistant",
        title="Language Barrier",
        msg=message
    )
    toast.show()
def google_search(query: str):
    formatted = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={formatted}"
    webbrowser.open(url)


def handle(user_input, intent_group):
    intent_name = classify(user_input, intent_group)
    name =""
    input_clean = user_input.lower()
    keywords = ["search for", "google", "look up", "find"]
    for keyword in keywords:
        if input_clean.find(keyword) != -1:
            name = input_clean.split(keyword)[-1].strip()
    try:
        google_search(name)

    except:
        alert("Sorry, I didn't understand the command.")