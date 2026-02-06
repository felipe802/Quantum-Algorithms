# %%
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

# 1. Definição do circuito
# Criamos um registro com 2 qubits e 2 bits clássicos (para armazenar a medição)
# No espaço de Hilbert, isso representa um sistema de dimensão 4
qc = QuantumCircuit(2, 2)

# 2. Criação de Superposição (porta Hadamard)
# Aplicamos a porta H no qubit 0 (controle)
# Isso transforma |0> em |+> = (|0> + |1>) / sqrt(2)
qc.h(0)

# 3. Emaranhamento (porta CNOT)
# qubit 0 é o controle e qubit 1 é o alvo
# Se qubit 0 for |1>, o qubit 1 inverte. Isso cria a correlação dita anteriormente
qc.cx(0, 1)

# 4. Medição (colapso da função de onda)
# Realiza-se a medição de ambos os qubits para os respectivos bits clássicos.
# Este passo "força" o sistema a escolher um estado base (regra de Born)
qc.measure([0, 1], [0, 1])

# 5. Execução e simulação
# Utiliza-se o AerSimulator para rodar o experimento 1024 vezes
sim = AerSimulator()
job = sim.run(qc, shots=1024)
result = job.result()

# Obtém-se a contagem de quantas vezes cada estado foi medido
counts = result.get_counts()
print(f"Resultados das medições (Estado: Frequência): {counts}")

fig_circ = qc.draw(output='mpl')
fig_circ.suptitle("Circuito de Emaranhamento (Estado de Bell)", fontsize=14) # Adiciona o título
fig_circ.tight_layout() # Ajusta o layout para o titulo nao cortar
fig_circ.savefig("circuito1_bell.png")

# Gerar o histograma de resultados
fig_hist = plot_histogram(counts, title="Resultados das medições - Estado de Bell")
fig_hist.savefig("histograma_shots")



