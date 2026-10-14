"""Ejercicio 4"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class Arbol:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def es_completo(self):
        return self._revisar(self.raiz)

    def _revisar(self, nodo):
        if nodo is None:
            return True

        tiene_izquierdo = nodo.izquierdo is not None
        tiene_derecho = nodo.derecho is not None

        # Un nodo tiene que contar con los dos hijos o con ninguno.
        if tiene_izquierdo and not tiene_derecho:
            return False
        if tiene_derecho and not tiene_izquierdo:
            return False

        return self._revisar(nodo.izquierdo) and self._revisar(nodo.derecho)


def main():
    raiz_valida = Nodo(50)
    raiz_valida.izquierdo = Nodo(30)
    raiz_valida.derecho = Nodo(70)
    ejemplo_valido = Arbol(raiz_valida)
    print("Árbol con dos hijos en la raíz:", ejemplo_valido.es_completo())

    raiz_invalida = Nodo(50)
    raiz_invalida.izquierdo = Nodo(30)
    ejemplo_invalido = Arbol(raiz_invalida)
    print("Árbol con un solo hijo en la raíz:", ejemplo_invalido.es_completo())


if __name__ == "__main__":
    main()
