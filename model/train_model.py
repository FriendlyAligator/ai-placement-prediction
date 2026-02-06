import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("../dataset/placement_data.csv")

X = data.drop("PlacementStatus", axis=1)
y = data["PlacementStatus"]

# Proper split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=7,
    stratify=y
)

# Pipeline (VERY IMPORTANT)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(
        max_iter=1000,
        C=0.5,          # regularization → avoids overconfidence
        solver="lbfgs"
    ))
])

pipeline.fit(X_train, y_train)

# Cross-validation accuracy (REALISTIC)
cv_scores = cross_val_score(pipeline, X, y, cv=5)
accuracy = cv_scores.mean()

print("Cross-Validation Accuracy:", accuracy)

# Save
pickle.dump(pipeline, open("placement_model.pkl", "wb"))
pickle.dump(accuracy, open("accuracy.pkl", "wb"))
