import random
from nombres_teatroV2 import *


# Función para generar IDs de usuarios
def id_user():
    n=random.randint(1000,9999)
    while n in id_usuarios:
        n=random.randint(1000,9999)       
    id_usuarios.append(n)
    return n

# Crear usuarios aleatorios a partir de nombres
while len(datos_globales_usuarios) != len(nombres):
    id_usuario = id_user()
    nombre = random.choice(nombres).ljust(10, " ")
    dni = random.randint(56000000, 90000000)
    telefono = random.randint(1100000000, 1199999999)
    correo = (nombre + random.choice(["@gmail.com","@hotmail.com","@yahoo.com"])).replace(" ", "")
    while len(correo) < 25:
        correo += " "
    Activo_conf = random.choice([True, False])
    datos_globales_usuarios.append([id_usuario, nombre, dni, telefono, correo, Activo_conf])

matriz3 = datos_globales_usuarios

# Guardar solo IDs y DNIs de usuarios activos
for i in datos_globales_usuarios:
    if i[5] == True:
        ids_usuario.append(i[0])
for i in datos_globales_usuarios:
    dni_usuarios.append(i[2])

# Función para mostrar matriz de usuarios
def ver_m3(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["id","nombre     ","dni    ","        TELEFONO","MAIL","                                ESTADO"]

    print("-"*111)
    for col in columnas_t:
        print(col, end="\t")
    print()
    print("-"*111)

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == True:
                matriz[f][c] = "\tACTIVO"
            elif matriz[f][c] == False:
                matriz[f][c] = "\tINACTIVO"
            print(matriz[f][c], end="\t")
        print()


