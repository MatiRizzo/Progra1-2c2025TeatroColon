import random
from nombres_teatroV2 import *
from datetime import datetime, timedelta

# Función para generar IDs de shows
def id_alt():
    n=random.randint(1000, 9999)
    while n in ids_shows:
        n=random.randint(1000, 9999)
    ids_shows.append(n)
    return n

# Función para generar fechas aleatorias de shows
def fecha_alt():
    fecha_inicio = datetime(2025, 1, 1)
    fecha_fin = datetime(2025, 12, 31)
    rango_dias = (fecha_fin - fecha_inicio).days
    dias_random = random.randint(0, rango_dias)
    fecha_aleatoria = fecha_inicio + timedelta(days=dias_random)
    return fecha_aleatoria.date()

# Crear 10 shows aleatorios
while len(datos_globales) != 10:
    id_show = id_alt()
    tipo_Evento = random.choice(tipos_show)
    duracion = random.choice([60,120,180])
    espectadores = random.randint(300, 999)
    espacios_disponibles = 999-espectadores
    fecha = fecha_alt()
    datos_globales.append([id_show, tipo_Evento, duracion, espectadores, espacios_disponibles, fecha])

# Guardar solo los IDs de los shows
for i in datos_globales:
    solo_ids_show.append(i[0])

# Función para mostrar matriz de shows
def ver_m(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    columnas_t = ["ids", "tipo evento", "duracion", "cant_e", "esp_d", "fecha"]
    print("-"*66)
    print("\t".join(columnas_t))
    print("-"*66)
    for f in range(filas):
        print("\t".join(str(matriz[f][c]) for c in range(columnas)))