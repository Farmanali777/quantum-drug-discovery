import pennylane as qml
from pennylane import numpy as np

# Create device
dev = qml.device("default.qubit", wires=2)

# Quantum circuit
@qml.qnode(dev)
def circuit(x, weights):
    qml.RX(x[0], wires=0)
    qml.RY(x[1], wires=1)

    qml.Rot(weights[0], weights[1], weights[2], wires=0)
    qml.Rot(weights[3], weights[4], weights[5], wires=1)

    qml.CNOT(wires=[0, 1])

    return qml.expval(qml.PauliZ(0))


# Function to run
def run_pennylane():
    x = np.array([0.5, 0.2])
    weights = np.random.random(6)

    result = circuit(x, weights)

    return float(result)
