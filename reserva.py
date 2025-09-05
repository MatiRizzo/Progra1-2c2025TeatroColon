import random
from nombres_teatroV2 import *

# Función para generar IDs de reserva
def id_alt_r():
    def n_alt():
        return random.randint(1,1000)
    n = n_alt()
    while n in ids_reserva:
        n = n_alt()
    ids_reserva.append(n)
    return n

# Crear reservas aleatorias
while len(datos_globales_reserva) != len(nombres):
    id_reserva = id_alt_r()
    id_usuario = random.choice(ids_usuario)
    ubicacion_u = random.choice(ubicacion)
    show = random.choice(solo_ids_show)
    datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_u, show])

# Función para mostrar reservas
def ver_m2(matriz):
    columnas_t = ["ids","id us","ubicacion","id_show"]
    print("-"*50)
    print("\t".join(columnas_t))
    print("-"*50)
    for fila in matriz:
        print("\t".join(str(c) for c in fila))