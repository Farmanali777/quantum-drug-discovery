from qiskit_aer import Aer
from qiskit.algorithms import QAOA
from qiskit.algorithms.optimizers import COBYLA
from qiskit.utils import QuantumInstance
from qiskit.opflow import PauliSumOp

# Backend
backend = Aer.get_backend("aer_simulator")

# Quantum instance
qi = QuantumInstance(backend)

# ✅ Correct operator
operator = PauliSumOp.from_list([("ZZ", 1.0)])

# Optimizer
optimizer = COBYLA()

# QAOA
qaoa = QAOA(optimizer=optimizer, quantum_instance=qi)

# Run
result = qaoa.compute_minimum_eigenvalue(operator)

print("QAOA Result:", result.eigenvalue.real)
