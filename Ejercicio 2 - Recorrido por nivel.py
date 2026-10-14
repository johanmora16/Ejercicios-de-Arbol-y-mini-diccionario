"""Ejercicio 2"""


class Nodo:
    def __init__(self, numero):
        self.numero = numero
        self.izq = None
        self.der = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, numero):
        nuevo = Nodo(numero)
        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if numero < actual.numero:
                if actual.izq is None:
                    actual.izq = nuevo
                    return
                actual = actual.izq
            elif numero > actual.numero:
                if actual.der is None:
                    actual.der = nuevo
                    return
                actual = actual.der
            else:
                return  # No se insertan valores duplicados.

    def recorrido_por_niveles(self):
        if self.raiz is None:
            return []

        # La lista funciona como cola: se procesa usando un índice creciente.
        cola = [self.raiz]
        salida = []
        posicion = 0

        while posicion < len(cola):
            actual = cola[posicion]
            posicion += 1
            salida.append(actual.numero)

            if actual.izq is not None:
                cola.append(actual.izq)
            if actual.der is not None:
                cola.append(actual.der)

        return salida


def main():
    arbol = Arbol()
    for numero in [50, 30, 70, 20, 40]:
        arbol.agregar(numero)

    print("Recorrido:", arbol.recorrido_por_niveles())


if __name__ == "__main__":
    main()