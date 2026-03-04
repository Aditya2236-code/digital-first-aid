
from ai_guidance import generate_ai_first_aid


def calculate_risk(data):

    score = 0

    # Oxygen evaluation
    if data.oxygen_level < 90:
        score += 3
    elif 90 <= data.oxygen_level <= 94:
        score += 2

    # Heart rate evaluation
    if data.heart_rate > 120:
        score += 2
    elif 100 <= data.heart_rate <= 120:
        score += 1

    # Symptoms
    if data.chest_pain:
        score += 2

    if data.breathing_difficulty:
        score += 2

    # Risk classification
    if score >= 9:
        risk = "Critical"
        recommendation = "Immediate emergency medical attention required."
    elif score >= 6:
        risk = "High"
        recommendation = "Seek urgent medical consultation."
    elif score >= 3:
        risk = "Moderate"
        recommendation = "Monitor symptoms and consult a doctor if condition worsens."
    else:
        risk = "Low"
        recommendation = "Condition appears stable. Continue monitoring."

    # AI-generated first aid steps
    steps = generate_ai_first_aid(data, risk)

    return {
        "risk_score": score,
        "risk_level": risk,
        "recommendation": recommendation,
        "first_aid_steps": steps
    }
