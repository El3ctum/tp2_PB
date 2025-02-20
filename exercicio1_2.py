import numpy as np
import timeit
from soma_paralela import soma_paralela

vetor = np.random.randint(1, 100001, size=10000)
print("Soma sequencial:", timeit.timeit(lambda: np.sum(vetor), number=100))
print("Soma paralela:", timeit.timeit(lambda: soma_paralela(vetor), number=100))