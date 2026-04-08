value = 1.0

for i in range(10):
    print(f"Iteration {i}")

    # Quantum simulation (mock)
    quantum_output = value * 0.8

    # Classical optimization
    value = quantum_output - 0.05

    print("Updated Value:", value)

    # Stop condition
    if abs(value) < 0.01:
        print("✅ Converged")
        break
