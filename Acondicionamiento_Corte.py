def asignar_tareas(tareas, trabajadores, nodos_de_corte, asignacion_actual=None, indice_tarea=0):
    if asignacion_actual is None:
        asignacion_actual = {}

    if indice_tarea == len(tareas):
        # Se han asignado todas las tareas
        return asignacion_actual

    tarea_actual = tareas[indice_tarea]

    for trabajador in trabajadores:
        if trabajador in nodos_de_corte:
            continue  # Saltar nodos de corte condicionados

        if es_asignacion_valida(tarea_actual, trabajador, asignacion_actual):
            asignacion_actual[indice_tarea] = trabajador
            resultado = asignar_tareas(tareas, trabajadores, nodos_de_corte, asignacion_actual, indice_tarea + 1)
            if resultado:
                return resultado

    return None

def es_asignacion_valida(tarea, trabajador, asignacion_actual):
    # Verificar si el trabajador cumple con los requisitos de la tarea
    if tarea["requisitos"] not in trabajador["habilidades"]:
        return False

    # Verificar si el trabajador ya está asignado a otra tarea con los mismos requisitos
    for indice_tarea_asignada, trabajador_asignado in asignacion_actual.items():
        if trabajador_asignado == trabajador and tarea["requisitos"] == tareas[indice_tarea_asignada]["requisitos"]:
            return False

    return True

# Ejemplo de tareas y trabajadores
tareas = [
    {"nombre": "Tarea A", "requisitos": "Habilidad X"},
    {"nombre": "Tarea B", "requisitos": "Habilidad Y"},
    {"nombre": "Tarea C", "requisitos": "Habilidad X"},
]

trabajadores = [
    {"nombre": "Trabajador 1", "habilidades": ["Habilidad X"]},
    {"nombre": "Trabajador 2", "habilidades": ["Habilidad Y"]},
    {"nombre": "Trabajador 3", "habilidades": ["Habilidad X"]},
]

# Definir los nodos de corte (variables críticas)
nodos_de_corte = ["Trabajador 2"]

asignacion = asignar_tareas(tareas, trabajadores, nodos_de_corte)

if asignacion:
    print("Asignación satisfactoria:")
    for indice_tarea, trabajador in asignacion.items():
        tarea = tareas[indice_tarea]
        print(f"{tarea['nombre']} -> {trabajador['nombre']}")
else:
    print("No se encontró una asignación satisfactoria.")