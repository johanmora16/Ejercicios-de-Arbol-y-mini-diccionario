"""Ejercicio 3"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._ubicar(self.raiz, valor)

    def _ubicar(self, actual, valor):
        if valor < actual.valor:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(valor)
            else:
                self._ubicar(actual.izquierdo, valor)
        elif valor > actual.valor:
            if actual.derecho is None:
                actual.derecho = Nodo(valor)
            else:
                self._ubicar(actual.derecho, valor)

    def sumar_valores(self):
        return self._sumar_desde(self.raiz)

    def _sumar_desde(self, nodo):
        if nodo is None:
            return 0
        izquierda = self._sumar_desde(nodo.izquierdo)
        derecha = self._sumar_desde(nodo.derecho)
        return izquierda + nodo.valor + derecha

    def listar_inorden(self):
        lista = []

        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierdo)
                lista.append(nodo.valor)
                recorrer(nodo.derecho)

        recorrer(self.raiz)
        return lista


def main():
    arbol = Arbol()
    valores = [50, 30, 70, 80, 90]
    for valor in valores:
        arbol.insertar(valor)

    antes = arbol.listar_inorden()
    print("Arbol Original:", valores)
    print("Suma:", arbol.sumar_valores())
    print("El árbol no fue modificado:", antes == arbol.listar_inorden())


if __name__ == "__main__":
    main()