from pydantic import BaseModel
from typing import List

class HealthInput(BaseModel):
    heart_rate: int
    oxygen_level: int
    chest_pain: bool
    breathing_difficulty: bool


class HealthResponse(BaseModel):
    risk_score: int
    risk_level: str
    recommendation: str
    first_aid_steps: List[str]