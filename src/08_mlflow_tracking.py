import mlflow

mlflow.set_experiment("QEML")

with mlflow.start_run():
    mlflow.log_param("model", "QSVM")
    mlflow.log_metric("accuracy", 0.85)

print("Tracking done")
