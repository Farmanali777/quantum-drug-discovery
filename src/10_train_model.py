import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("data/processed.csv")

# Features & target
X = df.drop("label", axis=1)   # ✅ FIXED
y = df["label"]                # ✅ FIXED

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")
