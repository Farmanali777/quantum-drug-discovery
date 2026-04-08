from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_algorithms.minimum_eigensolvers import NumPyMinimumEigensolver

driver = PySCFDriver(atom="H 0 0 0; H 0 0 0.735")

problem = driver.run()

hamiltonian = problem.hamiltonian.second_q_op()

mapper = JordanWignerMapper()
qubit_op = mapper.map(hamiltonian)

solver = NumPyMinimumEigensolver()

result = solver.compute_minimum_eigenvalue(qubit_op)

print("Ground State Energy:", result.eigenvalue.real)
