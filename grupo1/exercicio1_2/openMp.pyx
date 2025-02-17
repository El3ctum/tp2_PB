# cython: language_level=3, boundscheck=False, wraparound=False, nonecheck=False, initializedcheck=False
import numpy as np
cimport cython
from cython.parallel import prange

def vector_sum_sequential(double[:] vector):
    cdef double sum = 0
    cdef int i
    for i in range(vector.shape[0]):
        sum += vector[i]
    return sum

def vector_sum_parallel(double[:] vector):
    cdef double sum = 0
    cdef int i
    for i in prange(vector.shape[0], nogil=True, schedule='static'):
        sum += vector[i]
    return sum

def setup_vector(int size, int min_value, int max_value):
    # Gere números aleatórios de ponto flutuante no intervalo [min_value, max_value)
    cdef double[:] vector = np.random.uniform(min_value, max_value, size).astype(np.float64)
    return vector