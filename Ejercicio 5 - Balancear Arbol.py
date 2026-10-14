"""Ejercicio 5"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._agregar(self.raiz, dato)

    def _agregar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izq is None:
                nodo.izq = Nodo(dato)
            else:
                self._agregar(nodo.izq, dato)
        elif dato > nodo.dato:
            if nodo.der is None:
                nodo.der = Nodo(dato)
            else:
                self._agregar(nodo.der, dato)

    def obtener_valores(self):
        ordenados = []

        def guardar(nodo):
            if nodo is None:
                return
            guardar(nodo.izq)
            ordenados.append(nodo.dato)
            guardar(nodo.der)

        guardar(self.raiz)
        return ordenados

    def altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

    def balancear_arbol(self):
        valores = self.obtener_valores()
        otro = Arbol()

        def formar(primero, ultimo):
            if primero > ultimo:
                return None
            centro = (primero + ultimo) // 2
            raiz = Nodo(valores[centro])
            raiz.izq = formar(primero, centro - 1)
            raiz.der = formar(centro + 1, ultimo)
            return raiz

        otro.raiz = formar(0, len(valores) - 1)
        return otro


def main():
    arbol_original = Arbol()
    for numero in range(1, 11):
        arbol_original.agregar(numero)

    arbol_nuevo = arbol_original.balancear_arbol()
    print("Altura del árbol inicial:", arbol_original.altura(arbol_original.raiz))
    print("Altura del árbol nuevo:", arbol_nuevo.altura(arbol_nuevo.raiz))
    print("Números del árbol inicial:", arbol_original.obtener_valores())
    print("Números del árbol balanceado:", arbol_nuevo.obtener_valores())


if __name__ == "__main__":
    main()