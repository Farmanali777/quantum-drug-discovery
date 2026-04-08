import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

df = pd.read_csv("data/raw.csv")

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

df["features"] = df["canonical_smiles"].apply(featurize)
df = df.dropna()

df["label"] = df["standard_value"].astype(float) < 1000

X = list(df["features"])
y = df["label"].astype(int)

processed = pd.DataFrame(X, columns=["MolWt", "LogP", "HDonors", "HAcceptors"])
processed["label"] = y

processed.to_csv("data/processed.csv", index=False)
print("Preprocessing done.")
