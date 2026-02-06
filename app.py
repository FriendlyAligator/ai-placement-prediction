from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained pipeline model
model = pickle.load(open("model/placement_model.pkl", "rb"))
accuracy = pickle.load(open("model/accuracy.pkl", "rb"))

@app.route("/")
def home():
    return render_template(
        "index.html",
        accuracy_text = f"Cross-Validation Accuracy (Synthetic Data): {accuracy*100:.2f}%"

    )

@app.route("/predict", methods=["POST"])
def predict():
    cgpa = float(request.form["cgpa"])
    internships = int(request.form["internships"])
    projects = int(request.form["projects"])
    aptitude = float(request.form["aptitude"])
    communication = float(request.form["communication"])

    features = [[cgpa, internships, projects, aptitude, communication]]

    # Pipeline handles scaling
    prob = model.predict_proba(features)[0][1] * 100

    # Clamp probability (avoid 0% / 100%)
    prob = max(5, min(prob, 95))

    if prob >= 50:
        result = f"🎉 Placement Probability: {prob:.2f}% (High Chance)"
    else:
        result = f"⚠️ Placement Probability: {prob:.2f}% (Low Chance)"

    return render_template(
        "index.html",
        prediction_text=result,
        accuracy_text=f"Cross-Validation Accuracy: {accuracy*100:.2f}%",
        probability=round(prob,2)
    )

# 🚨 THIS PART IS REQUIRED 🚨
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
