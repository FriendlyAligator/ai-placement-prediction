# 🎓 AI Placement Prediction System

A full-stack Machine Learning web application that predicts a student’s placement probability based on academic and skill-based inputs.
The system is built using Python, Flask, and Logistic Regression, and is deployed live on Render.


🚀 Live Demo

🔗 Live Application:
👉 https://ai-placement-prediction.onrender.com

🔗 GitHub Repository:
👉 https://github.com/FriendlyAligator/ai-placement-prediction


📌 Project Overview

This project aims to simulate a real-world placement prediction system where a student can enter their academic details and receive a placement probability along with a visual progress bar.

The application focuses not only on model accuracy but also on:

User experience

Clear probability interpretation

Real deployment of an ML model


✨ Features

. 📊 Predicts placement probability (%)

. 🧠 Machine Learning model trained using Logistic Regression

. 📈 Probability shown using a dynamic progress bar

. 🎨 Premium glassmorphism UI with dark & light mode

. 🌐 Deployed live using Render

. 📦 Clean project structure (industry-style)


🛠️ Tech Stack
🔹 Frontend
    . HTML5
    . CSS3 (Glassmorphism UI)
    . JavaScript

🔹 Backend
   . Python
   . Flask
   . Gunicorn

🔹 Machine Learning
   . Scikit-learn
   . Pandas
   . NumPy
   . Logistic Regression
   . Cross-Validation

🔹 Deployment
   . GitHub
   . Render (Cloud Deployment)

🧠 Machine Learning Model Details
. Model Used: Logistic Regression
. Input Features:
. CGPA
. Number of Internships
. Number of Projects
. Aptitude Score
. Communication Skills (1–10)
. Output: Placement Probability (%)
. Evaluation Method: Cross-Validation
. Accuracy: Displayed dynamically in the UI
. Logistic Regression was chosen for its interpretability and effectiveness in binary classification problems like placement prediction.


▶️ How to Run Locally

Follow these steps to run the project on your local machine:

1️⃣ Clone the repository
git clone https://github.com/FriendlyAligator/ai-placement-prediction.git
cd ai-placement-prediction

2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Flask app
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000

📂 Project Structure
ai-placement-prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── placement_model.pkl
│   └── accuracy.pkl
│
├── dataset/
│   └── placement_data.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css


🎯 Future Improvements
. Add user authentication
. Store prediction history
. Improve dataset size
. Add explainability (feature importance)
. Convert backend to FastAPI

👨‍💻 Author
Sanskar Shaw
🎓 Student | Aspiring Data Scientist / ML Engineer

🔗 GitHub: https://github.com/FriendlyAligator
🔗 LinkedIn: https://www.linkedin.com/in/sanskar-shaw-0845b62a0/

⭐ If you like this project

Give it a ⭐ on GitHub — it motivates me to build more!




