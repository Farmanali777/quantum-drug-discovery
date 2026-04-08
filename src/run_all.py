import os

print("🚀 Starting Quantum Drug Discovery Pipeline...\n")

steps = [
    "python src/01_dataset_import.py",
    "python src/02_preprocessing.py",
    "python src/03_classical_ml.py",
    "python src/04_qsvm.py",
    "python src/05_vqe.py",
    "python src/06_qaoa.py",
    "python src/07_hybrid_loop.py",
    "python src/08_mlflow_tracking.py"
]

for step in steps:
    print(f"\n▶ Running: {step}")
    os.system(step)

print("\n✅ FULL PIPELINE COMPLETED SUCCESSFULLY")
