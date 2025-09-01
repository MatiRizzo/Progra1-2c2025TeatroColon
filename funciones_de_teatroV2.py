from nombres_teatroV2 import *
import random
from datetime import datetime, timedelta
 
#DATOS PARA SHOW
ids_shows = []

def id_alt():
    def n_alt():
        return random.randint(1000,9999)
    n = n_alt()
    while n in ids_shows:
        n = n_alt()
    ids_shows.append(n)
    
    return n


def fecha_alt():

    # Definimos el rango de fechas
    fecha_inicio = datetime(2025, 1, 1)
    fecha_fin = datetime(2025, 12, 31)

    # Calculamos el rango de días
    rango_dias = (fecha_fin - fecha_inicio).days

    # Generamos un número aleatorio de días para sumar
    dias_random = random.randint(0, rango_dias)

    # Obtenemos la fecha aleatoria
    fecha_aleatoria = fecha_inicio + timedelta(days=dias_random)

    return fecha_aleatoria.date()  # Solo la fecha

while len(datos_globales) != 10:

    id_show = id_alt()

    tipo_Evento = random.choice(tipos_show)

    lista_m = [60,120,180]

    duracion = random.choice(lista_m)

    espectadores = random.randint(300,999)

    espacios_disponibles = random.randint(0,20)

    fecha = fecha_alt()

    datos_globales.append([id_show,tipo_Evento,duracion,espectadores,espacios_disponibles,fecha])

#DATOS PARA RESERVA
ids_reserva = []

def id_alt_r():

    def n_alt():
        return random.randint(1,1000)
    n = n_alt()
    while n in ids_reserva:
        n = n_alt()
    ids_reserva.append(n)
    
    return n


def id_user():

    def n_alt():
        return random.randint(1000,9999)

    n = n_alt()

    while n in id_usuarios:
        n = n_alt()
    id_usuarios.append(n)

    return n


while len(datos_globales_usuarios) != len(nombres):

    id_usuario = id_user()

    nombre = random.choice(nombres)
    nombre=nombre.ljust(10, " ")

    dni = random.randint(56000000,90000000)

    telefono = random.randint(1100000000, 1199999999)

    tipos_c = ["@gmail.com","@hotmail.com","@yahoo.com"]

    correo = nombre + random.choice(tipos_c)
  
    correo_ok = correo.replace(" ","")
    
    while len(correo_ok) < 25:
        correo_ok += " "
    
    Activo = [True,False]

    Activo_conf = random.choice(Activo)

    datos_globales_usuarios.append([id_usuario,nombre,dni,telefono,correo_ok,Activo_conf])

matriz3 = datos_globales_usuarios

#visualizacion de matrices
#region imprimir matriz
def ver_m(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["ids","tipo evento","   duracion","cant_e","esp_d","fecha"]
    print("-"*66)
    for col in columnas_t:
        print(col, end="\t")
    print()
    print("-"*66)

    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end="\t")
        print()



#DATOS USUARIOS
def ver_m2(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["ids","id us","ubicacion","id_show"]

    print("-"*50)
    for col in columnas_t:
        print(col, end="\t")
    print()

    print("-"*50)

    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end="\t")
        print()



def ver_m3(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["id","nombre     ","dni    ","        TEELEFONO","MAIL","                                ESTADO"]

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


#Solo ids del show
for i in datos_globales:

    solo_ids_show.append(i[0])


#solo ids usuarios
for i in datos_globales_usuarios:

    if i[5] == True:
        ids_usuario.append(i[0])

for i in datos_globales_usuarios:
    dni_usuarios.append(i[3])


#reserva
while len(datos_globales_reserva) != len(nombres):

    id_reserva = id_alt_r()

    id_usuario = random.choice(ids_usuario)

    ubicacion_u = random.choice(ubicacion)

    show = random.choice(solo_ids_show)

    datos_globales_reserva.append([id_reserva,id_usuario,ubicacion_u,show])

matriz2 = datos_globales_reserva

def busqueda(dni, contraseña):
    for i in range(len(datos_de_ingreso_dni)):
        if datos_de_ingreso_dni[i] == dni and datos_globales_contraseñas[i] == contraseña:
            return True
    return False