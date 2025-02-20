class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class LinkedList:
    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self, valor):
        novo_no = Node(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserir_final(self, valor):
        novo_no = Node(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def excluir(self, valor):
        if not self.cabeca:
            return
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            return
        atual = self.cabeca
        while atual.proximo and atual.proximo.valor != valor:
            atual = atual.proximo
        if atual.proximo:
            atual.proximo = atual.proximo.proximo

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")


lista = LinkedList()
lista.inserir_inicio(1)
lista.inserir_final(2)
lista.inserir_final(3)
lista.exibir()
lista.excluir(2)
lista.exibir()
