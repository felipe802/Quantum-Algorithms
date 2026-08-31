# Entanglement & Bell States: Complete Implementation

This folder contains the source code and visual results for fundamental and advanced quantum entanglement concepts, from the four **Bell States** to multipartite entanglement (GHZ) and empirical tests of local realism (CHSH inequality).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kZGYeHcZ014jM8A2tuBPwZPFd99C_N-d?usp=sharing)

---

## 1. Overview

The implementations explore how quantum Hadamard ($H$), Pauli-X ($X$), and CNOT ($CX$) gates can be orchestrated to create extremely strong quantum correlations. Below, you will find the circuits, histograms, and technical explanations for each implemented test case.

---

## 2. The Four Bell States

Bell states form a maximally entangled orthonormal basis for a two-qubit system.

### A. First Bell State $|\Phi^+\rangle$
**Equation:** $|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$  
**Code:** [`FirstBellState.py`](./FirstBellState.py)

| Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](FirstBellCirc.png) | ![Histogram](FirstBellHist.png) |

* **How it's created:** A Hadamard ($H$) gate is applied to the first qubit, followed by a $CNOT$ gate with the first qubit as control and the second as target.

---

### B. Second Bell State $|\Phi^-\rangle$
**Equation:** $|\Phi^-\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}$  
**Code:** [`SecondBellState.py`](./SecondBellState.py)

| Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](SecondBellCirc.png) | ![Histogram](SecondBellHist.png) |

* **How it's created:** Similar to the first state, but applying an $X$ (or $Z$) gate beforehand to introduce the negative quantum phase difference.

---

### C. Third Bell State $|\Psi^+\rangle$
**Equation:** $|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}$  
**Code:** [`ThirdBellState.py`](./ThirdBellState.py)

| Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](ThirdBellCirc.png) | ![Histogram](ThirdBellHist.png) |

* **How it's created:** Qubits are initialized to opposite states before creating the superposition, generating perfect anti-symmetry correlations.

---

### D. Fourth Bell State $|\Psi^-\rangle$
**Equation:** $|\Psi^-\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}$  
**Code:** [`FourthBellState.py`](./FourthBellState.py)

| Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](FourthBellCirc.png) | ![Histogram](FourthBellHist.png) |

* **How it's created:** Also known as the singlet state, it exhibits rotational symmetry and a negative phase between opposite state superpositions.

---

## 3. Multipartite Entanglement: GHZ State

**Equation:** $|GHZ\rangle = \frac{|000\rangle + |111\rangle}{\sqrt{2}}$  
**Code:** [`GHZState.py`](./GHZState.py)

Extending maximal entanglement to 3 qubits (the Greenberger-Horne-Zeilinger state). Measuring any single qubit instantly dictates the state of the other two, collapsing exclusively to $|000\rangle$ or $|111\rangle$.

| GHZ Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](ghz_circ.png) | ![Histogram](ghz_hist.png) |

---

## 4. Quantum Sub-routines: Controlled Bell State

**Code:** [`ControlledBell.py`](./ControlledBell.py)

Demonstrates how to abstract the preparation of a Bell State into a custom quantum gate block and apply it conditionally using a control qubit (acting as a quantum conditional or "quantum if-statement"). If the control is $|1\rangle$, the target qubits become entangled.

| Abstract Controlled Circuit | Resulting Measurement Histogram |
| :---: | :---: |
| ![Circuit](controled_bell.png) | ![Histogram](controled_bell_hist.png) |

---

## 5. Proving Non-Locality: CHSH Inequality

**Code:** [`CHSH_Inequality.py`](./CHSH_Inequality.py)

An algorithmic simulation of the experimental CHSH test (a generalization of Bell's Theorem).

By rotating Alice and Bob's measurement bases to specific non-orthogonal angles, the test calculates the correlation parameter $S$. Classical local realism enforces a strict boundary of $|S| \le 2$. However, the simulated quantum system consistently violates this limit, reaching Tsirelson's bound:

$$S \approx 2\sqrt{2} \approx 2.82$$

> [!IMPORTANT]  
> The numerical violation proven in this script is one of the most robust computational proofs that quantum mechanics is fundamentally non-local, and that local hidden variables cannot explain the experimental results.

---

## 6. Technical Details

* **Framework:** Qiskit (v1.x)
* **Simulator:** `AerSimulator` (Qiskit Aer) with 1024 shots.
* **Purpose:** Educational and expository material for Undergraduate Research (IC).

> [!TIP]  
> To interact directly with the quantum codes, test other angles, and visualize Bloch spheres in real time, we highly recommend using the **Google Colab** link located at the top of this page.
