class DNode:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class DoublyLinkedList:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_inicio(self, valor):
        novo_no = DNode(valor)
        if not self.cabeca:
            self.cabeca = self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no

    def inserir_final(self, valor):
        novo_no = DNode(valor)
        if not self.cauda:
            self.cabeca = self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.proximo
        print("None")

    def insertion_sort(self):
        if not self.cabeca or not self.cabeca.proximo:
            return
        sorted_list = DoublyLinkedList()
        atual = self.cabeca
        while atual:
            proximo = atual.proximo
            atual.proximo = atual.anterior = None  # Desconecta o nó
            sorted_list._inserir_ordenado(atual)
            atual = proximo
        self.cabeca = sorted_list.cabeca
        self.cauda = sorted_list.cauda

    def _inserir_ordenado(self, no):
        if not self.cabeca or no.valor < self.cabeca.valor:
            no.proximo = self.cabeca
            if self.cabeca:
                self.cabeca.anterior = no
            self.cabeca = no
            if not self.cauda:
                self.cauda = no
            return
        atual = self.cabeca
        while atual.proximo and atual.proximo.valor < no.valor:
            atual = atual.proximo
        no.proximo = atual.proximo
        no.anterior = atual
        if atual.proximo:
            atual.proximo.anterior = no
        else:
            self.cauda = no
        atual.proximo = no


lista = DoublyLinkedList()
lista.inserir_final(3)
lista.inserir_final(1)
lista.inserir_final(2)
lista.exibir()
lista.insertion_sort()
lista.exibir()
