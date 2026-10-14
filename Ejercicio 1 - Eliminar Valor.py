"""Ejercicio 1"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.menor = None
        self.mayor = None


class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        self.raiz = self._insertar_desde(self.raiz, dato)

    def _insertar_desde(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.dato:
            nodo.menor = self._insertar_desde(nodo.menor, dato)
        elif dato > nodo.dato:
            nodo.mayor = self._insertar_desde(nodo.mayor, dato)
        # Los números repetidos no se almacenan dos veces.
        return nodo

    def eliminar(self, dato):
        self.raiz = self._quitar_desde(self.raiz, dato)

    def _quitar_desde(self, nodo, dato):
        if nodo is None:
            return None

        if dato < nodo.dato:
            nodo.menor = self._quitar_desde(nodo.menor, dato)
        elif dato > nodo.dato:
            nodo.mayor = self._quitar_desde(nodo.mayor, dato)
        else:
            # Si no hay hijo izquierdo, se conserva el derecho (si existe).
            if nodo.menor is None:
                return nodo.mayor
            # Si no hay hijo derecho, se conserva el izquierdo.
            if nodo.mayor is None:
                return nodo.menor

            # Con dos hijos, se usa el menor valor del subárbol derecho.
            reemplazo = nodo.mayor
            while reemplazo.menor is not None:
                reemplazo = reemplazo.menor
            nodo.dato = reemplazo.dato
            nodo.mayor = self._quitar_desde(nodo.mayor, reemplazo.dato)

        return nodo

    def valores_ordenados(self):
        datos = []

        def visitar(nodo):
            if nodo is None:
                return
            visitar(nodo.menor)
            datos.append(nodo.dato)
            visitar(nodo.mayor)

        visitar(self.raiz)
        return datos


def crear_arbol(valores):
    arbol = ArbolBusqueda()
    for valor in valores:
        arbol.insertar(valor)
    return arbol


def demostrar_eliminacion(titulo, valores, objetivo):
    arbol = crear_arbol(valores)
    print(f"\n{titulo}")
    print("Antes:", arbol.valores_ordenados())
    arbol.eliminar(objetivo)
    print(f"Después de eliminar {objetivo}:", arbol.valores_ordenados())


def main():
    # Cada prueba usa un árbol nuevo para que una eliminación no afecte a otra.
    demostrar_eliminacion(
        "Caso 1: eliminar una hoja", [50, 30, 70, 20, 40, 60, 80], 80
    )
    demostrar_eliminacion(
        "Caso 2: eliminar un nodo con un hijo", [50, 30, 70, 20, 40, 60], 70
    )
    demostrar_eliminacion(
        "Caso 3: eliminar un nodo con dos hijos", [50, 30, 70, 20, 40, 60, 80], 50
    )


if __name__ == "__main__":
    main()
