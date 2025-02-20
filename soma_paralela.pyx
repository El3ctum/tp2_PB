# cython: language_level=3
cimport cython
from cython.parallel import prange
cimport numpy as np
from numpy cimport int64_t

def soma_paralela(np.ndarray[int64_t, ndim=1] vetor):
    cdef int i, n = vetor.shape[0]
    cdef long long soma = 0
    with nogil:
        for i in prange(n, schedule='static'):
            soma += vetor[i]
    return soma