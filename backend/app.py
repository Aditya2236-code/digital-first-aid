from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import HealthInput, HealthResponse
from services import calculate_risk
from guidance import generate_first_aid
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Digital First Aid API is running"}


@app.post("/analyze", response_model=HealthResponse)
def analyze_health(data: HealthInput):

    result = calculate_risk(data)

    return result