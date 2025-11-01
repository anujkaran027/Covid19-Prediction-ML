import pickle
import numpy as np

# Load saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Feature order
FEATURES = [
    "Breathing Problem", "Fever", "Dry Cough", "Sore throat", "Running Nose",
    "Asthma", "Chronic Lung Disease", "Headache", "Heart Disease", "Diabetes",
    "Hyper Tension", "Fatigue", "Gastrointestinal", "Abroad travel",
    "Contact with COVID Patient", "Attended Large Gathering",
    "Visited Public Exposed Places", "Family working in Public Exposed Places"
]

def predict_covid(symptom_values):
    arr = np.array(symptom_values).reshape(1, -1)
    prediction = model.predict(arr)[0]
    return prediction