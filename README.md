# 🚑 Digital First Aid

An **AI-powered emergency first aid guidance system** that analyzes basic health indicators and provides immediate first-aid recommendations during potential medical emergencies.

This project helps users quickly evaluate risk levels based on symptoms and vital signs, offering guidance before professional medical help arrives.

---

# 🌐 Live Demo

Frontend deployed on Netlify:

https://digital-first-aid.netlify.app

⚠️ Note:
The deployed frontend UI works online, but the backend API must be run locally for full functionality.

---

# 🧠 Project Idea

In emergency situations, people often panic and do not know what steps to take immediately.

Digital First Aid provides:

• Instant risk assessment
• AI-generated first aid instructions
• Symptom-based analysis
• Quick decision support before medical help arrives

The goal is to **assist users in taking the right first aid actions quickly.**

---

# 🏗 System Architecture

Frontend (HTML + JavaScript)
⬇
FastAPI Backend (Python)
⬇
Risk Evaluation Logic
⬇
AI First Aid Guidance Generator

The frontend collects health data and sends it to the backend API, which evaluates the risk and generates first aid instructions.

---

# ⚙ Tech Stack

**Backend**

* Python
* FastAPI
* Uvicorn
* Pydantic

**Frontend**

* HTML
* CSS
* JavaScript

**Deployment**

* Netlify (Frontend)

---

# 📡 API Endpoints

### Health Check

GET /

Returns a message confirming the API is running.

---

### Analyze Health Data

POST /analyze

Accepts the following input:

```
{
  "heart_rate": int,
  "oxygen_level": int,
  "chest_pain": bool,
  "breathing_difficulty": bool
}
```

Returns:

* Risk score
* Risk level
* Recommendation
* First aid steps

---

# 🚀 Running the Project Locally

## 1️⃣ Clone Repository

```
git clone https://github.com/Aditya2236-code/digital-first-aid.git
cd digital-first-aid
```

---

## 2️⃣ Install Backend Dependencies

```
cd backend
pip install -r requirements.txt
```

---

## 3️⃣ Start FastAPI Server

```
python -m uvicorn app:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 4️⃣ Run Frontend

Open:

```
frontend/index.html
```

in your browser.

---

# 🧪 Example Usage

Input:

* Heart Rate: 130
* Oxygen Level: 88
* Chest Pain: True
* Breathing Difficulty: True

Output:

* Risk Level: High / Critical
* Recommendation: Seek urgent medical attention
* First Aid Steps: Immediate emergency instructions

---

# 🔮 Future Improvements

• Cloud deployment of backend API
• Database integration for medical history
• More advanced AI prediction models
• Mobile app version
• Integration with wearable devices
• Real-time emergency alerts

---

# ⚠ Disclaimer

This project is intended **for educational and hackathon purposes only**.

It does **not replace professional medical advice**.
Always seek medical professionals in real emergencies.

---

# 👨‍💻 Author

Aditya

GitHub:
https://github.com/Aditya2236-code
