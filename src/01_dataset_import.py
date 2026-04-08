from chembl_webresource_client.new_client import new_client
import pandas as pd

print("Downloading dataset...")

target = new_client.target
activity = new_client.activity

targets = target.search("kinase")
target_id = targets[0]["target_chembl_id"]

data = activity.filter(
    target_chembl_id=target_id,
    standard_type="IC50"
)

df = pd.DataFrame(data)
df = df[["canonical_smiles", "standard_value"]].dropna()

df.to_csv("data/raw.csv", index=False)
print("Dataset saved.")
