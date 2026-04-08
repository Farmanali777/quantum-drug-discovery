
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')
from flask import Flask, render_template, request
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# Initialize Flask
app = Flask(__name__, template_folder="templates")

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
# Improved Prediction Logic
# -----------------------------
def predict_molecule(features):
    if features is None:
        return "Invalid SMILES ❌"

    mw, logp, h_donors, h_acceptors = features

    # More realistic rule-based logic
    if mw < 300 and logp < 3 and h_donors <= 2:
        return "Active ✅"
    else:
        return "Inactive ❌"

# -----------------------------
# Routes
# -----------------------------

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Results Dashboard
@app.route("/results")
def results():
    df = pd.read_csv("results/final_results.csv")

    labels = df["Model"].tolist()
    values = df["Value"].tolist()

    return render_template(
        "results.html",
        data=df.to_dict(orient="records"),
        labels=labels,
        values=values
    )

# Prediction Page
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
