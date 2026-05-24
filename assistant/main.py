from intentClassifier import *
import intents.NotesIntent as NotesIntent
import intents.MusicIntent as MusicIntent
import intents.AppsIntent as AppIntent
import intents.SearchIntent as SearchIntent

intents = load_intents()
embedded_intents = embed_intents(intents)
def main():
    while True: 
        user_input = input("How can I assist you? ")
        intent_group = embedded_intents["general"]
        intent_name = classify(user_input, intent_group)
        if intent_name == "quit":
            break
        if intent_name == "notes":
            NotesIntent.handle(user_input, embedded_intents["specific"]["notes"])
        elif intent_name == "music":
            MusicIntent.handle(user_input, embedded_intents["specific"]["music"])
        elif intent_name == "app":
            AppIntent.handle(user_input, embedded_intents["specific"]["app"])
        elif intent_name == "search":
            SearchIntent.handle(user_input, embedded_intents["specific"]["search"])
        else:
            print("Sorry, I didn't understand that.")
main()