"""
BHT (Brassard-Høyer-Tapp) Collision Finding Algorithm
Quantum implementation using Qiskit for 2-to-1 collision problem.
Author: Felipe Junqueira Leite
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import UnitaryGate
from qiskit.visualization import plot_histogram

def main():
    # 1. Classical 2-to-1 function setup (4 qubits -> N = 16 elements)
    n_qubits = 4
    N = 2 ** n_qubits
    np.random.seed(42)
    f_perm = np.random.permutation(N)
    f_tilde = f_perm // 2  # 2-to-1 mapping

    print("=" * 60)
    print("🚀 BHT Quantum Collision Algorithm (Brassard-Høyer-Tapp, 1997)")
    print("=" * 60)

    # 2. Classical sampling of M = ceil(N^(1/3)) elements
    M = int(np.ceil(N ** (1 / 3)))  # M = 3
    amostras_x = list(np.random.choice(N, size=M, replace=False))
    tabela = {x: f_tilde[x] for x in amostras_x}
    alvos = set(tabela.values())

    print(f"📋 Classical Pre-sampling ({M} items): {tabela}")

    # 3. Construction of Quantum Oracle V = F^\dagger U F
    matriz_F = np.eye(N)[f_perm].T
    matriz_U = np.diag([-1.0 if (y // 2) in alvos else 1.0 for y in range(N)])
    matriz_V = matriz_F.T @ matriz_U @ matriz_F

    # Householder Diffuser: D = 2|s><s| - I
    matriz_D = 2 * (np.ones((N, N)) / N) - np.eye(N)

    # 4. Quantum Circuit Assembly
    circuito_bht = QuantumCircuit(n_qubits, n_qubits)
    circuito_bht.h(range(n_qubits))  # Uniform superposition
    circuito_bht.append(UnitaryGate(matriz_V, label="Oráculo V"), range(n_qubits))
    circuito_bht.append(UnitaryGate(matriz_D, label="Difusor D"), range(n_qubits))
    circuito_bht.measure(range(n_qubits), range(n_qubits))

    # 5. Simulation on AerSimulator
    simulador = AerSimulator()
    contagens = simulador.run(transpile(circuito_bht, simulador), shots=1024).result().get_counts()

    # Identify collision partner
    for bitstring in sorted(contagens, key=contagens.get, reverse=True):
        x_quantico = int(bitstring, 2)
        if f_tilde[x_quantico] in alvos and x_quantico not in amostras_x:
            x_classico = [k for k, v in tabela.items() if v == f_tilde[x_quantico]][0]
            print(f"\n🎉 Collision Pair Found: x₁ = {x_classico} and x₂ = {x_quantico}")
            print(f"✅ Proof: f({x_classico}) = f({x_quantico}) = {f_tilde[x_quantico]}")
            break

    print("\n📊 Raw Counts:", contagens)
    
    # Save output figures
    circ_fig = circuito_bht.draw('mpl', style="iqp")
    circ_fig.savefig("BHT/bht_circ.png", bbox_inches="tight")
    
    hist_fig = plot_histogram(contagens, title="Algoritmo BHT: Amplificação das Colisões")
    hist_fig.savefig("BHT/bht_hist.png", bbox_inches="tight")
    print("💾 Figures saved to BHT/ directory.")

if __name__ == "__main__":
    main()
