class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"{self.nome}: {self.nota}"


def quicksort_estudantes(arr, key=lambda x: x.nota):
    if len(arr) <= 1:
        return arr
    pivot = key(arr[len(arr) // 2])
    left = [x for x in arr if key(x) < pivot]
    middle = [x for x in arr if key(x) == pivot]
    right = [x for x in arr if key(x) > pivot]
    return quicksort_estudantes(left, key) + middle + quicksort_estudantes(right, key)


estudantes = [Estudante("Davi", 85), Estudante(
    "Lucas", 90), Estudante("Gabriela", 78)]
ordenados = quicksort_estudantes(estudantes)
print("Lista ordenada:", ordenados)
