import time

def quicksort(arr, pivot_strategy='middle'):
    if len(arr) <= 1:
        return arr
    if pivot_strategy == 'first':
        pivot = arr[0]
    elif pivot_strategy == 'last':
        pivot = arr[-1]
    elif pivot_strategy == 'middle':
        pivot = arr[len(arr) // 2]
    else:
        raise ValueError("Estratégia inválida")
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left, pivot_strategy) + middle + quicksort(right, pivot_strategy)

lista = [5, 2, 9, 1, 5, 6]
for strategy in ['first', 'last', 'middle']:
    start = time.time()
    result = quicksort(lista.copy(), strategy)
    print(f"{strategy}: {result}, Tempo: {time.time() - start:.4f}s")