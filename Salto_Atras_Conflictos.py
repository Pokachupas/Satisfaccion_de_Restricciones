# Definición de la clase Grafo
class Grafo:
    def __init__(self):
        self.nodos = set()         # Conjunto de nodos en el grafo
        self.adyacencias = {}      # Diccionario de adyacencias entre nodos

    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        self.adyacencias[nodo] = set()  # Inicializar las adyacencias de un nodo como un conjunto vacío

    def agregar_adyacencia(self, nodo1, nodo2):
        self.adyacencias[nodo1].add(nodo2)
        self.adyacencias[nodo2].add(nodo1)  # Agregar nodos adyacentes en ambas direcciones

# Función para verificar si un color es compatible con los vecinos del nodo actual
def es_compatible(grafo, nodo, color, asignacion):
    for vecino in grafo.adyacencias[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Función principal para asignar colores a los nodos del grafo
def asignar_colores(grafo, colores, asignacion, nodo_actual):
    if len(asignacion) == len(grafo.nodos):
        return True  # Todas las asignaciones han sido realizadas

    for color in colores:
        if es_compatible(grafo, nodo_actual, color, asignacion):
            asignacion[nodo_actual] = color
            siguiente_nodo = obtener_siguiente_nodo(grafo, asignacion)
            if asignar_colores(grafo, colores, asignacion, siguiente_nodo):
                return True
            del asignacion[nodo_actual]  # Retroceder si la asignación no es satisfactoria

    return False

# Función para obtener el siguiente nodo a asignar (selecciona el nodo con más adyacencias)
def obtener_siguiente_nodo(grafo, asignacion):
    nodos_sin_asignar = [nodo for nodo in grafo.nodos if nodo not in asignacion]
    if nodos_sin_asignar:
        return max(nodos_sin_asignar, key=lambda nodo: len(grafo.adyacencias[nodo]))
    return None  # Retorna None cuando todos los nodos han sido asignados

# Ejemplo de grafo
grafo = Grafo()
grafo.agregar_nodo("A")
grafo.agregar_nodo("B")
grafo.agregar_nodo("C")
grafo.agregar_adyacencia("A", "B")
grafo.agregar_adyacencia("B", "C")
colores = ["Rojo", "Verde", "Azul"]

asignacion = {}
if asignar_colores(grafo, colores, asignacion, "A"):
    print("Asignación satisfactoria:")
    for nodo, color in asignacion.items():
        print(f"Nodo {nodo}: {color}")
else:
    print("No se encontró una asignación satisfactoria.")