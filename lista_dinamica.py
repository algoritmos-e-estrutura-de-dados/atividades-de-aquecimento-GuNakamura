from node import Node


class Lista:
    inicio = None

    def __init__(self):
        self.inicio = None

        # adicionar no final da lista

    def adicionar(self, valor, inicio=False):
        if inicio:
            self.adicionar_no_inicio(valor)
        else:
            self.adicionar_no_fim(valor)

    def adicionar_no_inicio(self, valor):
        novo = Node(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    def adicionar_no_fim(self, valor):
        if self.inicio is None:
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio
            while aux.proximo is not None:
                aux = aux.proximo

            aux.proximo = Node(valor, None)
            aux.proximo.anterior = aux

    def remover(self, valor):
        aux = self.inicio
        if aux.valor == valor:
            # aux.valor = None
            self.inicio = aux.proximo
        else:
            while aux.proximo is not None:
                aux = aux.proximo
                if aux.valor == valor:
                    aux.anterior.proximo = aux.proximo

    # lista dinamica
    def show(self):
        aux = self.inicio
        print("[", end='')
        while aux.proximo is not None:
            print(f"{aux.valor}", end=', ')
            aux = aux.proximo
        print(f"{aux.valor}]")

        from lista import Lista

lista = Lista()

lista.adicionar(1)
lista.adicionar(2, inicio=True)
lista.adicionar(3)
lista.adicionar(4, inicio=True)
lista.adicionar(5)
lista.adicionar(6)
lista.adicionar(7, inicio=True)
lista.adicionar(8)
lista.adicionar(9, inicio=True)

lista.show()

lista.remover(3)
lista.remover(8)
lista.remover(6)

lista.show()

class Node:
    valor = 0
    proximo = None
    anterior = None

    def __init__(self, valor=0, proximo=None, anterior=None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior