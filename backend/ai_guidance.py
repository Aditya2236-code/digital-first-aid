import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")


def generate_ai_first_aid(data, risk):

    prompt = f"""
    A person has the following condition:

    Heart Rate: {data.heart_rate}
    Oxygen Level: {data.oxygen_level}
    Chest Pain: {data.chest_pain}
    Breathing Difficulty: {data.breathing_difficulty}

    Risk Level: {risk}

    Provide 4 short first aid steps.
    Only return steps, each on a new line.
    """

    try:
        response = model.generate_content(prompt)

        steps = response.text.split("\n")

        clean_steps = [s.strip("- ").strip() for s in steps if s.strip()]

        return clean_steps[:4]

    except Exception as e:

        # fallback if AI fails
        return [
            "Call emergency services immediately",
            "Help the person sit upright",
            "Loosen tight clothing",
            "Monitor breathing and pulse"
        ]