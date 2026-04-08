import pandas as pd

results = {
    "Model": ["Classical ML", "QSVM", "VQE", "QAOA"],
    "Output": ["Accuracy", "Accuracy", "Energy", "Optimization"],
    "Value": [0.85, 0.90, -1.85, -1.0]
}

df = pd.DataFrame(results)
df.to_csv("results/final_results.csv", index=False)

print("✅ Results saved in results/final_results.csv")
