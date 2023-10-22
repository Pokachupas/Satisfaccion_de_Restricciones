import random

def min_conflicts(grafo, max_iter):
    asignacion = {}  # Inicializar una asignación aleatoria
    for nodo in grafo.nodos:
        asignacion[nodo] = random.choice(grafo.colores)

    for _ in range(max_iter):
        conflictos = contar_conflictos(grafo, asignacion)
        if conflictos == 0:
            return asignacion  # La asignación es satisfactoria

        nodo_en_conflicto = obtener_nodo_en_conflicto(grafo, asignacion)
        mejor_color = encontrar_mejor_color(grafo, asignacion, nodo_en_conflicto)
        asignacion[nodo_en_conflicto] = mejor_color

    return None  # No se encontró una asignación satisfactoria

def contar_conflictos(grafo, asignacion):
    conflictos = 0
    for nodo in grafo.nodos:
        for vecino in grafo.adyacencias[nodo]:
            if asignacion[nodo] == asignacion[vecino]:
                conflictos += 1
    return conflictos

def obtener_nodo_en_conflicto(grafo, asignacion):
    nodos_en_conflicto = [nodo for nodo in grafo.nodos if hay_conflicto(grafo, nodo, asignacion)]
    return random.choice(nodos_en_conflicto)

def hay_conflicto(grafo, nodo, asignacion):
    for vecino in grafo.adyacencias[nodo]:
        if asignacion[nodo] == asignacion[vecino]:
            return True
    return False

def encontrar_mejor_color(grafo, asignacion, nodo):
    colores_disponibles = grafo.colores[:]
    colores_vecinos = set()
    for vecino in grafo.adyacencias[nodo]:
        colores_vecinos.add(asignacion[vecino])
    
    colores_disponibles = [color for color in colores_disponibles if color not in colores_vecinos]
    if colores_disponibles:
        return random.choice(colores_disponibles)
    else:
        return asignacion[nodo]  # Si no hay colores disponibles, mantener el color actual

# Definición de la clase Grafo
class Grafo:
    def __init__(self, nodos, adyacencias, colores):
        self.nodos = nodos
        self.adyacencias = adyacencias
        self.colores = colores

# Ejemplo de grafo
nodos = ["A", "B", "C", "D"]
adyacencias = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}
colores = ["Rojo", "Verde", "Azul"]

grafo = Grafo(nodos, adyacencias, colores)

# Resolver el problema de asignación de colores usando Mínimos Conflictos
asignacion = min_conflicts(grafo, max_iter=1000)

if asignacion:
    print("Asignación satisfactoria:")
    for nodo, color in asignacion.items():
        print(f"Nodo {nodo}: {color}")
else:
    print("No se encontró una asignación satisfactoria.")