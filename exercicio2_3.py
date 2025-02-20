import numpy as np


def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quickselect(right, k - len(left) - len(middle))


if __name__ == "__main__":
    for _ in range(10):
        lista = np.random.randint(1, 1001, size=10000).tolist()
        for k in [1, 2500, 5000, 7500, 9999]:
            result = quickselect(lista.copy(), k)
            print(f"Lista {_+1}, k={k}: {result}")
