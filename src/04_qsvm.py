import pandas as pd
import numpy as np
import pennylane as qml
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/processed.csv").sample(40)

X = df.drop("label", axis=1).values
y = df["label"].values

X = (X - X.min()) / (X.max() - X.min())

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def kernel(x1, x2):
    qml.AngleEmbedding(x1[:2], wires=[0,1])
    qml.adjoint(qml.AngleEmbedding)(x2[:2], wires=[0,1])
    return qml.probs(wires=[0,1])

def kernel_matrix(A, B):
    return np.array([[kernel(a,b)[0] for b in B] for a in A])

X_train, X_test, y_train, y_test = train_test_split(X, y)

K_train = kernel_matrix(X_train, X_train)
K_test = kernel_matrix(X_test, X_train)

model = SVC(kernel="precomputed")
model.fit(K_train, y_train)

print("QSVM Accuracy:", model.score(K_test, y_test))
