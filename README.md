# ⚛️ Quantum Algorithms: Practical Quantum Computing with Qiskit

This repository brings together clean, modular, and richly documented implementations of fundamental concepts in **Quantum Mechanics** and **Quantum Algorithms**. Developed originally as expository and practical material for **Undergraduate Research (IC)**, the project utilizes the open-source **Qiskit** (v1.x) framework to simulate quantum circuits and explore qubit behavior.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kZGYeHcZ014jM8A2tuBPwZPFd99C_N-d?usp=sharing)

---

## 🗺️ Map of Algorithms and Concepts

The table below presents a summary of everything implemented in the repository. Each module has its own detailed documentation with mathematical explanations and results analysis.

| Module | Quantum Algorithms / Concepts | Main Files | Status and Visual Results |
| :--- | :--- | :--- | :--- |
| 🔔 **[EstadoBell](./EstadoBell)** | Maximal Entanglement, Bell States ($|\Phi^{\pm}\rangle$, $|\Psi^{\pm}\rangle$), GHZ State, Controlled Bell, and CHSH Inequality. | `FirstBellState.py` <br> `GHZState.py` <br> `CHSH_Inequality.py` | ✅ Circuits, Histograms, and Numerical Proof of Non-Locality ($S \approx 2.82$). |
| 🔍 **[Grover](./Grover)** | Quantum unstructured search with quadratic speedup ($\mathcal{O}(\sqrt{N})$), phase Oracle, and Diffuser. | `GroverAlgorithm.py` | ✅ Amplitude amplification of $|\omega\rangle = |0101\rangle$ with success > 95%. |
| 🔄 **[QFT](./QFT)** | Quantum Fourier Transform, phase mapping, controlled fractional rotations, and bit-reversal correction. | `QFT_Algorithm.py` | ✅ Phase encoding and geometric correction via `SWAP` gates analyzed on state $|3\rangle$. |
| 🎚️ **[QPE](./QPE)** | Quantum Phase Estimation, *Phase Kickback*, cascaded controlled operators, and decoding via $QFT^\dagger$. | `QPE_Algorithm.py` | ✅ Exact eigenvalue extraction for secret phase $\theta = 0.125$ with 3 qubits. |
| 🔑 **[Shor](./Shor)** | Shor's Algorithm for integer factorization in polynomial time ($\mathcal{O}(n^3)$), Order/Period Finding, and Continued Fractions. | `ShorAlgorithm.py` | ✅ Factoring composite number $N = 15$ with $a = 7$ to yield prime factors $3$ and $5$. |
| 🛡️ **[BHT Collision](./BHT)** | Brassard-Høyer-Tapp algorithm solving the 2-to-1 collision problem via Birthday Paradox + Grover search. | `BHTAlgorithm.py` | ✅ Unitary Oracle $V = F^\dagger U F$, Grover Search, and Collision Pair Recovery ($\mathcal{O}(N^{1/3})$). |

---

## 🚀 Getting Started and Environment Setup

The scripts were developed and tested using the modern version of **Qiskit** and the high-performance local simulator **Qiskit Aer**.

### 1. Prerequisites
Make sure you have Python 3.9 or higher installed on your machine.

### 2. Creating a Virtual Environment (Recommended)
To avoid global dependency conflicts, create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate on Linux/macOS
source .venv/bin/activate

# Activate on Windows (Command Prompt)
.venv\Scripts\activate.bat
```

### 3. Installing Dependencies
Install all necessary packages via `pip`:

```bash
pip install qiskit qiskit-aer matplotlib pylatexenc
```

> [!TIP]  
> The `pylatexenc` library is installed to allow Qiskit to draw circuits in a rich graphic format using Matplotlib (mpl style with rendering of mathematical text).

---

## 💻 How to Run the Simulations

All scripts are self-executable and generate visual reports (circuits and probability distribution histograms) using Matplotlib's graphical interface.

To run any of the algorithms, navigate to the module's folder and execute the corresponding Python file:

```bash
# Example 1: Running Grover's Search Algorithm
python Grover/GroverAlgorithm.py

# Example 2: Running Quantum Phase Estimation
python QPE/QPE_Algorithm.py

# Example 3: Running Shor's Factorization Algorithm
python Shor/ShorAlgorithm.py
```

If you are in a Jupyter Notebook or Google Colab environment, the circuits and histograms will be rendered directly in the output cells using interactive display functions.

---

## 🛠️ Technologies Used

* **Language:** Python 3
* **Quantum Framework:** Qiskit (version 1.x)
* **Quantum Simulation:** Qiskit Aer (`AerSimulator`)
* **Data Visualization:** Matplotlib & Qiskit Visualization
* **Cloud Environment:** Google Colab (interactive badges at the top of each README)

---

## 📝 Contribution and Purpose

This project was built expositorily for educational and academic purposes. Feel free to clone, suggest improvements, or use the circuits in your own undergraduate research or independent quantum computing studies!

If you found this material helpful, feel free to give a 🌟 to the repository!