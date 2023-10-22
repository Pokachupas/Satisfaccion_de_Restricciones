def ac3(tareas, trabajadores):
    cola = [(tarea, trabajador) for tarea in tareas for trabajador in trabajadores]
    restricciones = {tarea: [] for tarea in tareas}  # Inicializar restricciones para cada tarea

    for tarea in tareas:
        for trabajador in trabajadores:
            if es_asignacion_valida(tarea, trabajador, tareas, trabajadores):
                restricciones[tarea].append(trabajador)

    while cola:
        tarea, trabajador = cola.pop(0)

        if revise(tarea, trabajador, restricciones):
            if not tareas[tarea] or not trabajadores[trabajador]:
                return False

            for tarea_vecina in restricciones[tarea]:
                if tarea_vecina != tarea:
                    cola.append((tarea_vecina, trabajador))

    return True

def es_asignacion_valida(tarea, trabajador, tareas, trabajadores):
    # Verificar si el trabajador cumple con los requisitos de la tarea
    for habilidad_tarea in tareas[tarea]:
        if habilidad_tarea not in trabajadores[trabajador]:
            return False
    return True

def revise(tarea, trabajador, restricciones):
    revisado = False
    for tarea_vecina in restricciones[tarea]:
        if not tareas[tarea] or not trabajadores[trabajador]:
            continue
        consistente = False
        for habilidad_tarea in tareas[tarea]:
            for habilidad_trabajador in trabajadores[tarea_vecina]:
                if habilidad_tarea == habilidad_trabajador:
                    consistente = True
                    break
            if consistente:
                break
        if not consistente:
            tareas[tarea].remove(habilidad_tarea)
            revisado = True
    return revisado

# Ejemplo de tareas y trabajadores
tareas = {
    "Tarea A": ["Habilidad X", "Habilidad Y"],
    "Tarea B": ["Habilidad Y"],
    "Tarea C": ["Habilidad X", "Habilidad Y"],
}

trabajadores = {
    "Trabajador 1": ["Habilidad X", "Habilidad Y"],
    "Trabajador 2": ["Habilidad X"],
    "Trabajador 3": ["Habilidad Y"],
}

if ac3(tareas, trabajadores):
    print("Asignación satisfactoria:")
    for tarea, habilidades in tareas.items():
        print(f"{tarea} -> {', '.join(habilidades)}")
else:
    print("No se encontró una asignación satisfactoria.")