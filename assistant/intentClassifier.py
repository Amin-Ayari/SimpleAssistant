import json
import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("models/all-MiniLM-L6-v2")
def load_intents(path="data/intents.json"):
    with open(path, "r") as file:
        return json.load(file) #returns the intents as a dictionary


def embed_intents(intents: dict):#takes the intent and returns embbed version
    embedded = {}
    for level, intent_group in intents.items():
        embedded[level] = {}
        for key, descriptions in intent_group.items():
            if isinstance(descriptions, dict):
                embedded[level][key] = {
                    k: model.encode(v) for k, v in descriptions.items()
                }
            else:
                embedded[level][key] = model.encode(descriptions)
    return embedded #dictionary of embedded intents
def cosine(vector1, vector2): #calculates the simialrity between two vectors using cosine 
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))  #scalar product / product of norms

def classify(user_input: str, intent_group: dict):
    input_vector = model.encode(user_input)
    
    best_match = None
    best_score = -1

    for intent_name, intent_vector in intent_group.items():
        score = cosine(input_vector, intent_vector)
        if score > best_score:
            best_score = score
            best_match = intent_name

    return best_match

