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

    def excluir(self, posicao):
        if not self.cabeca:
            return
        if posicao == 0:
            self.cabeca = self.cabeca.proximo
            if self.cabeca:
                self.cabeca.anterior = None
            else:
                self.cauda = None
            return
        atual = self.cabeca
        for _ in range(posicao):
            if not atual.proximo:
                return
            atual = atual.proximo
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.cauda = atual.anterior

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.proximo
        print("None")

    def exibir_reverso(self):
        atual = self.cauda
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.anterior
        print("None")


lista = DoublyLinkedList()
lista.inserir_inicio(1)
lista.inserir_final(2)
lista.inserir_final(3)
lista.exibir()
lista.excluir(1)
lista.exibir()
lista.exibir_reverso()
