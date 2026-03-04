def generate_first_aid(risk_level, data):
    
    steps = []

    if risk_level == "Critical":
        steps = [
            "Call emergency services immediately (e.g., 108).",
            "Keep the person calm and seated upright.",
            "Loosen tight clothing around chest and neck.",
            "Monitor breathing continuously.",
            "If breathing stops and you are trained, begin CPR.",
            "Do NOT give food or water."
        ]

    elif risk_level == "High":
        steps = [
            "Keep the person seated and calm.",
            "Avoid physical activity.",
            "Monitor heart rate and breathing.",
            "Seek medical attention as soon as possible."
        ]

    elif risk_level == "Moderate":
        steps = [
            "Allow the person to rest.",
            "Monitor symptoms for changes.",
            "Consult a doctor if condition worsens."
        ]

    else:
        steps = [
            "Condition appears stable.",
            "Continue monitoring vital signs.",
            "Seek medical advice if symptoms develop."
        ]

    return steps