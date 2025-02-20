from exercicio2_3 import quickselect


def encontrar_mediana(arr):
    return quickselect(arr, len(arr) // 2)


def k_menores(arr, k):
    if k >= len(arr):
        return arr
    k_esimo = quickselect(arr, k)
    return [x for x in arr if x <= k_esimo][:k]


lista = [5, 2, 9, 1, 5, 6]
print("Mediana:", encontrar_mediana(lista))
print("3 menores:", k_menores(lista, 3))
