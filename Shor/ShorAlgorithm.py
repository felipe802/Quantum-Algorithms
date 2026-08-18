# Shor's Algorithm for Integer Factorization
# Hybrid Quantum-Classical implementation for factoring N = 15 with coprime a = 7

import math
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT, UnitaryGate
from qiskit.visualization import plot_histogram


def create_modular_unitary(a: int, N: int, num_qubits: int) -> np.ndarray:
    """
    Constructs the unitary permutation matrix corresponding to the
    modular multiplication operator: U|y> = |(a * y) mod N>.
    """
    dim = 2**num_qubits
    U = np.zeros((dim, dim))
    for i in range(dim):
        if i < N:
            U[(a * i) % N, i] = 1.0
        else:
            U[i, i] = 1.0
    return U


def main():
    # 1. Classical Setup
    N = 15
    a = 7
    print(f"=== Shor's Algorithm Factorization Demo ===")
    print(f"Target Composite Number: N = {N}")
    print(f"Chosen Coprime Base: a = {a}")
    print(f"Greatest Common Divisor gcd(a, N) = {math.gcd(a, N)}")
    assert math.gcd(a, N) == 1, "a and N must be coprime!"

    # 2. Quantum Circuit Dimensions
    t = 4        # Precision counting qubits (2^t = 16)
    n_target = 4 # Target register qubits to hold states up to N-1 (2^4 = 16 > 15)

    qc = QuantumCircuit(t + n_target, t)

    # Step A: Initialize counting register in uniform superposition
    for q in range(t):
        qc.h(q)

    # Step B: Initialize target register to |1> (since f(0) = a^0 mod N = 1)
    qc.x(t)
    qc.barrier()

    # Step C: Phase Kickback via Controlled Modular Exponentiation U^(2^j)
    unitary_base = create_modular_unitary(a, N, n_target)
    target_qubits = list(range(t, t + n_target))

    for counting_qubit in range(t):
        power = 2**counting_qubit
        u_power_matrix = np.linalg.matrix_power(unitary_base, power)
        c_u_gate = UnitaryGate(u_power_matrix, label=f"U^{power}").control(1)
        qc.append(c_u_gate, [counting_qubit] + target_qubits)

    qc.barrier()

    # Step D: Phase Decoding via Inverse Quantum Fourier Transform (QFT dagger)
    qft_inv = QFT(num_qubits=t, inverse=True, do_swaps=True).to_gate()
    qft_inv.name = "QFT†"
    qc.append(qft_inv, range(t))
    qc.barrier()

    # Step E: Measurement of the counting register
    for i in range(t):
        qc.measure(i, i)

    # 3. Simulation on AerSimulator
    simulator = AerSimulator()
    transpiled_qc = transpile(qc, simulator)
    result = simulator.run(transpiled_qc, shots=2048).result()
    counts = result.get_counts()

    print(f"\nMeasurement Histogram (Binary States): {counts}")

    # 4. Classical Post-Processing (Continued Fractions & Period Recovery)
    sorted_measurements = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    
    # Filter out the trivial '0000' measurement (phase = 0) to find the non-zero phase
    candidate_states = [state for state, _ in sorted_measurements if state != "0" * t]
    best_measurement = candidate_states[0] if candidate_states else sorted_measurements[0][0]

    measured_int = int(best_measurement, 2)
    phase = measured_int / (2**t)
    frac = Fraction(phase).limit_denominator(N)
    period_r = frac.denominator

    print(f"\nDominant Non-Trivial Measured State: |{best_measurement}> (decimal {measured_int})")
    print(f"Measured Phase: theta = {measured_int} / {2**t} = {phase}")
    print(f"Approximated Fraction (limit_denominator {N}): {frac.numerator} / {period_r}")
    print(f"Extracted Order/Period: r = {period_r}")

    # 5. Extracting Prime Factors
    if period_r % 2 == 0:
        base_term = int(a ** (period_r / 2))
        factor_1 = math.gcd(base_term - 1, N)
        factor_2 = math.gcd(base_term + 1, N)

        print(f"\n===> Factoring Results:")
        print(f"First Factor:  gcd({a}^({period_r}/2) - 1, {N}) = gcd({base_term - 1}, {N}) = {factor_1}")
        print(f"Second Factor: gcd({a}^({period_r}/2) + 1, {N}) = gcd({base_term + 1}, {N}) = {factor_2}")

        if factor_1 * factor_2 == N and factor_1 not in (1, N):
            print(f"SUCCESS: N = {N} factored into non-trivial primes {factor_1} and {factor_2}!")
        else:
            print("Factors are trivial, repeat with another measurement or base.")
    else:
        print("Extracted period is odd. Need to rerun.")


if __name__ == "__main__":
    main()
