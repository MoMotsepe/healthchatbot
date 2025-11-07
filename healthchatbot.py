#MO MOTSEPE 41822579
knowledge_base = {
    "flu": {"fever", "cough", "sore_throat"},
    "common_cold": {"sneezing", "runny_nose", "mild_fever"},
    "malaria": {"fever", "chills", "sweating", "headache"},
    "covid19": {"fever", "cough", "shortness_of_breath", "loss_of_taste"},
    "strep_throat": {"sore_throat", "swollen_lymph_nodes", "fever"}
}


advice_base = {
    "flu": [
        "Drink plenty of fluids",
        "Get lots of rest",
        "Use over-the-counter medications to reduce symptoms"
    ],
    "common_cold": [
        "Stay hydrated",
        "Rest as much as possible",
        "Use a humidifier"
    ],
    "malaria": [
        "Seek immediate medical attention",
        "Take antimalarial medications as prescribed",
        "Avoid mosquito bites"
    ],
    "covid19": [
        "Isolate yourself from others",
        "Get tested and follow health guidelines",
        "Monitor oxygen levels and seek care if needed"
    ],
    "strep_throat": [
        "Take prescribed antibiotics",
        "Avoid sharing utensils or drinks",
        "Gargle with warm salt water"
    ]
}
def diagnose(symptoms):
    for disease, disease_symptoms in knowledge_base.items():
        if disease_symptoms.issubset(symptoms):
            return disease
    return None

# Main chatbot interface
def chatbot():
    print("Welcome to the MO MEDISoft Diagnostic Chatbot")
    print("Enter your symptoms :")
    user_input = input("Your symptoms: ").lower()
    user_symptoms = set(sym.strip() for sym in user_input.split(","))

    disease = diagnose(user_symptoms)
    if disease:
        print(f"\nBased on your symptoms, you may have: **{disease.upper()}**")
        print("Recommended advice:")
        for advice in advice_base[disease]:
            print(f"- {advice}")
    else:
        print("\nUnable to determine the disease with the given symptoms.")
        print("Please consult a healthcare professional for further evaluation.")

if __name__ == "__main__":
    chatbot()

