from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request model
class HealthInput(BaseModel):
    heart_rate: int
    oxygen_level: int
    chest_pain: bool
    breathing_difficulty: bool


@app.get("/")
def home():
    return {"message": "Digital First Aid API is running"}


@app.post("/analyze")
def analyze_health(data: HealthInput):

    risk = "LOW"
    emergency = False
    advice = "You seem stable. Monitor your condition."

    # Simple risk logic for demo
    if data.heart_rate > 120 or data.oxygen_level < 90:
        risk = "CRITICAL"
        emergency = True
        advice = "Call emergency services immediately."

    elif data.chest_pain or data.breathing_difficulty:
        risk = "HIGH"
        advice = "Seek medical attention as soon as possible."

    return {
        "risk_level": risk,
        "advice": advice,
        "emergency": emergency
    }