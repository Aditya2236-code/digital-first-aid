# Digital First Aid API

A FastAPI-based backend system that analyzes basic health indicators 
and provides first-level medical risk assessment.

## 🚀 Tech Stack
- Python
- FastAPI
- Uvicorn
- Pydantic

## 📁 Project Structure
digital-first-aid/
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
└── .gitignore

## ⚙️ How to Run Locally

1. Clone repository
2. Navigate to backend folder
3. Install dependencies

pip install -r requirements.txt

4. Run server

python -m uvicorn app:app --reload

Server runs on:
http://127.0.0.1:8000

## 📌 API Endpoints

GET /
→ Health check message

POST /analyze
→ Accepts:
{
  "heart_rate": int,
  "oxygen_level": int,
  "chest_pain": bool,
  "breathing_difficulty": bool
}

## 📈 Future Improvements
- Add database integration
- Add frontend dashboard
- Deploy on cloud
- Add AI-based prediction logic
