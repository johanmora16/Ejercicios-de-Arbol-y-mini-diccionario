"""Mini-proyecto: diccionario con búsqueda exacta y autocompletado en un BST."""

import unicodedata


def clave_texto(texto):
    """Prepara una clave uniforme: ignora mayúsculas, tildes y espacios externos."""
    limpio = unicodedata.normalize("NFD", texto.strip().casefold())
    return "".join(letra for letra in limpio
                   if unicodedata.category(letra) != "Mn")


class EntradaDiccionario:
    def __init__(self, palabra, definicion):
        self.palabra = palabra
        self.definicion = definicion


class NodoPalabra:
    def __init__(self, entrada):
        self.entrada = entrada
        self.izquierda = None
        self.derecha = None


class DiccionarioBST:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def insertar(self, palabra, definicion):
        nueva = EntradaDiccionario(palabra.strip(), definicion.strip())
        if not nueva.palabra or not nueva.definicion:
            return False

        if self.raiz is None:
            self.raiz = NodoPalabra(nueva)
            self.cantidad = 1
            return True

        actual = self.raiz
        clave_nueva = clave_texto(nueva.palabra)
        while True:
            clave_actual = clave_texto(actual.entrada.palabra)
            if clave_nueva == clave_actual:
                return False
            if clave_nueva < clave_actual:
                if actual.izquierda is None:
                    actual.izquierda = NodoPalabra(nueva)
                    self.cantidad += 1
                    return True
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = NodoPalabra(nueva)
                    self.cantidad += 1
                    return True
                actual = actual.derecha

    def buscar(self, texto):
        clave = clave_texto(texto)
        actual = self.raiz
        while actual is not None:
            actual_clave = clave_texto(actual.entrada.palabra)
            if clave == actual_clave:
                return actual.entrada
            if clave < actual_clave:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return None

    def listar(self):
        resultado = []

        def recoger(nodo):
            if nodo is None:
                return
            recoger(nodo.izquierda)
            resultado.append(nodo.entrada)
            recoger(nodo.derecha)

        recoger(self.raiz)
        return resultado

    def buscar_por_prefijo(self, prefijo):
        prefijo = clave_texto(prefijo)
        if not prefijo:
            return []

        coincidencias = []

        def explorar(nodo):
            if nodo is None:
                return
            explorar(nodo.izquierda)
            if clave_texto(nodo.entrada.palabra).startswith(prefijo):
                coincidencias.append(nodo.entrada)
            explorar(nodo.derecha)

        explorar(self.raiz)
        return coincidencias


PALABRAS_INICIALES = [
    ("abeja", "Insecto que produce miel."),
    ("abogado", "Persona que ejerce la abogacía."),
    ("abrigo", "Prenda que protege del frío."),
    ("abuelo", "Padre de uno de los padres."),
    ("aceite", "Líquido graso usado para cocinar."),
    ("agua", "Líquido esencial para la vida."),
    ("aire", "Mezcla de gases que respiramos."),
    ("alegria", "Sentimiento de felicidad."),
    ("algoritmo", "Conjunto de pasos para resolver un problema."),
    ("almacen", "Lugar donde se guardan productos."),
    ("amigo", "Persona con quien se tiene amistad."),
    ("amor", "Sentimiento de afecto hacia alguien."),
    ("animal", "Ser vivo que puede sentir y moverse."),
    ("anillo", "Aro que se usa como adorno en un dedo."),
    ("arbol", "Planta con tronco y ramas."),
    ("archivo", "Documento o conjunto de datos guardados."),
    ("arena", "Conjunto de granos pequeños de roca."),
    ("arte", "Actividad que expresa ideas y emociones."),
    ("astronomia", "Ciencia que estudia los astros."),
    ("aula", "Sala destinada a la enseñanza."),
    ("audio", "Sonido que puede grabarse o reproducirse."),
    ("auto", "Vehículo que se desplaza por carretera."),
    ("autonomia", "Capacidad de actuar por cuenta propia."),
    ("autor", "Persona que crea una obra."),
    ("autoridad", "Poder o facultad para dirigir."),
    ("aurora", "Luz que aparece antes de salir el sol."),
    ("auxiliar", "Ayudar o prestar apoyo."),
    ("avion", "Aeronave que vuela por el aire."),
    ("azucar", "Sustancia dulce usada en alimentos."),
    ("bailar", "Mover el cuerpo siguiendo un ritmo."),
    ("biblioteca", "Lugar donde se consultan libros."),
    ("bicicleta", "Vehículo de dos ruedas impulsado con pedales."),
    ("bosque", "Lugar con muchos árboles."),
    ("computadora", "Máquina electrónica que procesa datos."),
    ("cuaderno", "Conjunto de hojas para escribir."),
    ("dato", "Información que puede registrarse."),
    ("diccionario", "Obra que contiene palabras y definiciones."),
    ("escuela", "Institución dedicada a la enseñanza."),
    ("estudiante", "Persona que estudia."),
    ("familia", "Grupo de personas unidas por parentesco."),
    ("flor", "Parte de una planta que puede producir semillas."),
    ("guitarra", "Instrumento musical de cuerdas."),
    ("internet", "Red mundial de dispositivos conectados."),
    ("libro", "Conjunto de páginas con contenido."),
    ("lluvia", "Agua que cae de las nubes."),
    ("musica", "Arte de combinar sonidos."),
    ("palabra", "Unidad del lenguaje con significado."),
    ("programa", "Conjunto de instrucciones para una tarea."),
    ("teclado", "Dispositivo que permite introducir texto."),
    ("ventana", "Abertura que permite entrar luz y aire."),
]


def crear_diccionario():
    diccionario = DiccionarioBST()
    for palabra, definicion in PALABRAS_INICIALES:
        diccionario.insertar(palabra, definicion)
    return diccionario


def imprimir_entrada(entrada):
    print(f"{entrada.palabra}: {entrada.definicion}")


def mostrar_menu():
    print("\n=== DICCIONARIO INTELIGENTE ===")
    print("1. Buscar una palabra")
    print("2. Autocompletar con un prefijo")
    print("3. Mostrar todas las palabras")
    print("0. Terminar")


def ejecutar():
    diccionario = crear_diccionario()
    print(f"Diccionario preparado: {diccionario.cantidad} palabras.")

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            consulta = input("Palabra que querés buscar: ")
            entrada = diccionario.buscar(consulta)
            if entrada is None:
                print("No se encontró esa palabra.")
            else:
                imprimir_entrada(entrada)

        elif opcion == "2":
            prefijo = input("Escribí las primeras letras: ").strip()
            sugeridas = diccionario.buscar_por_prefijo(prefijo)
            if sugeridas:
                print("Coincidencias:")
                for entrada in sugeridas:
                    imprimir_entrada(entrada)
            else:
                print("No hay palabras que comiencen con ese prefijo.")

        elif opcion == "3":
            print("\n--- LISTADO ALFABÉTICO ---")
            for entrada in diccionario.listar():
                imprimir_entrada(entrada)

        elif opcion == "0":
            print("Diccionario cerrado. ¡Hasta luego!")
            return

        else:
            print("Opción incorrecta; seleccioná 1, 2, 3 o 0.")


if __name__ == "__main__":
    ejecutar()