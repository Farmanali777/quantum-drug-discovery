import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/final_results.csv")

plt.figure()
plt.bar(df["Model"], df["Value"])
plt.title("Quantum vs Classical Performance")
plt.xlabel("Models")
plt.ylabel("Results")

plt.savefig("results/performance.png")

print("📊 Chart saved: results/performance.png")
