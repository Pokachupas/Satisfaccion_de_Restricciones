def es_seguro(grafo, v, c, asignacion):
    for nodo in grafo[v]:
        if nodo in asignacion and asignacion[nodo] == c:
            return False
    return True

def asignacion_colores(grafo, colores, asignacion, v):
    if v not in grafo:
        return True

    for color in colores:
        if es_seguro(grafo, v, color, asignacion):
            asignacion[v] = color
            if asignacion_colores(grafo, colores, asignacion, v + 1):
                return True
            del asignacion[v]

    return False

def resolver_coloracion(grafo, colores):
    asignacion = {}
    if asignacion_colores(grafo, colores, asignacion, 0):
        print("Asignación satisfactoria:")
        for nodo, color in asignacion.items():
            print(f"Nodo {nodo}: {color}")
    else:
        print("No se encontró una asignación satisfactoria.")

# Ejemplo de grafo
grafo = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2],
}

colores_disponibles = ['Rojo', 'Verde', 'Azul']

resolver_coloracion(grafo, colores_disponibles)
