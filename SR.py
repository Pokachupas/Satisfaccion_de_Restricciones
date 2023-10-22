def restricciones_satisfechas(asignacion, regiones, colores):
    for region1, color1 in asignacion.items():
        for region2, color2 in asignacion.items():
            if region1 != region2 and regiones[region1][region2] == 1 and color1 == color2:
                return False
    return True

def asignacion_satisfactoria(asignacion, regiones, colores):
    if len(asignacion) == len(regiones):
        return restricciones_satisfechas(asignacion, regiones, colores)
    
    region_no_asignada = [region for region in regiones if region not in asignacion]
    region_actual = region_no_asignada[0]
    
    for color in colores:
        nueva_asignacion = asignacion.copy()
        nueva_asignacion[region_actual] = color
        if asignacion_satisfactoria(nueva_asignacion, regiones, colores):
            asignacion.update(nueva_asignacion)
            return True
    return False

regiones = {
    'A': {'B': 1, 'C': 1},
    'B': {'A': 1, 'C': 1},
    'C': {'A': 1, 'B': 1}
}

colores = ['Rojo', 'Verde', 'Azul']

asignacion = {}
if asignacion_satisfactoria(asignacion, regiones, colores):
    print("Asignación satisfactoria:")
    for region, color in asignacion.items():
        print(f"Región {region}: {color}")
else:
    print("No se encontró una asignación satisfactoria.")