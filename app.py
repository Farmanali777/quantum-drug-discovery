# Disable RDKit warnings
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')

# Flask & libraries
from flask import Flask, render_template, request
import pandas as pd
import joblib

# RDKit
from rdkit import Chem
from rdkit.Chem import Descriptors

# PennyLane
from src.pennylane_qml import run_pennylane

# Initialize Flask
app = Flask(__name__, template_folder="templates")

# Load trained ML model
model = joblib.load("model.pkl")

# -----------------------------
# Feature Extraction (RDKit)
# -----------------------------
def featurize(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        return [
            Descriptors.MolWt(mol),
            Descriptors.MolLogP(mol),
            Descriptors.NumHDonors(mol),
            Descriptors.NumHAcceptors(mol)
        ]
    return None

# -----------------------------
# FINAL HYBRID PREDICTION
# -----------------------------
def predict_molecule(features):
    if features is None:
        return "Invalid SMILES ❌"

    mw = features[0]

    # 🔥 HYBRID LOGIC
    # Small molecules → heuristic
    if mw < 200:
        return "Active ✅ (Low molecular weight heuristic)"

    try:
        prediction = model.predict([features])[0]

        if prediction == 1:
            return "Active ✅"
        else:
            return "Inactive ❌"

    except Exception:
        return "Prediction Error ⚠️"

# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results")
def results():
    df = pd.read_csv("results/final_results.csv")

    labels = df["Model"].tolist()
    values = df["Value"].tolist()

    # Add PennyLane result
    try:
        pennylane_result = run_pennylane()
        labels.append("PennyLane")
        values.append(round(pennylane_result, 4))
    except Exception:
        labels.append("PennyLane")
        values.append(0)

    return render_template(
        "results.html",
        data=df.to_dict(orient="records"),
        labels=labels,
        values=values
    )

@app.route("/predict", methods=["GET", "POST"])
def predict():
    result = None

    if request.method == "POST":
        smiles = request.form["smiles"]
        features = featurize(smiles)
        result = predict_molecule(features)

    return render_template("predict.html", result=result)

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
