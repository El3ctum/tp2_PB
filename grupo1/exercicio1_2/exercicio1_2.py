import numpy as np
import time
from openMp import setup_vector, vector_sum_sequential, vector_sum_parallel

# Configuração do vetor
vector_size = 10000
vector = setup_vector(vector_size, 1, 100000)

# Cálculo sequencial
start_time = time.time()
sequential_sum = vector_sum_sequential(vector)
tempo_sequencial = time.time() - start_time
print(f"Soma Sequencial: {sequential_sum:.2f}, Tempo: {
      tempo_sequencial:.6f} segundos")

# Cálculo paralelo
start_time = time.time()
parallel_sum = vector_sum_parallel(vector)
tempo_paralelo = time.time() - start_time
print(f"Soma Paralela: {parallel_sum:.2f}, Tempo: {
      tempo_paralelo:.6f} segundos")

# Comparação de desempenho
if tempo_paralelo < tempo_sequencial:
    print(f"Versão paralela foi {
          tempo_sequencial / tempo_paralelo:.2f}x mais rápida!")
else:
    print("Versão sequencial foi mais rápida.")
