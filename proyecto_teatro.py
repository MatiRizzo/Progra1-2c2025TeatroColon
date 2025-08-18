
import random
from datetime import datetime, timedelta

#DATOS PARA SHOW

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


ids_shows = []

def id_alt():

    def n_alt():
        return random.randint(1000,9999)

    n = n_alt()

    while n in ids_shows:
        n = n_alt()
    ids_shows.append(n)
    
    return n

tipos_show = [
    "Concierto musical",
    "Espectáculo      ",
    "Show de stand    ",
    "Show de magia    ",
    "Show de danza    "
]


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

nombres = [
    "Juan     ", 
    "María    ", 
    "Pedro     ", 
    "Lucía     ", 
    "Sofía     ",
    "Carlos    ", 
    "Ana       ", 
    "Martín    ", 
    "Camila    ", 
    "Javier    ",
    "Laura     ",
    "Andrés    ",
    "Valentina ", 
    "Diego     ",
    "Florencia ",
    "Mateo     ",
    "Julieta   ", 
    "Nicolás   ", 
    "Paula     ", 
    "Agustín   ",
    "Victoria  ", 
    "Tomás     ", 
    "Martina   ", 
    "Sebastián ", 
    "Carolina   ",
    "Federico", 
    "Gabriela   ", 
    "Ignacio     "
]

ubicacion = ["platea    "
             ,"campo    "
             ,"vip      "]






#MATRICES
datos_globales = []

datos_globales_reserva = []


#whiles


#SHOW

while len(datos_globales) != 10:

    id_show = id_alt()

    tipo_Evento = random.choice(tipos_show)

    lista_m = [60,120,180]

    duracion = random.choice(lista_m)

    espectadores = random.randint(300,999)

    espacios_disponibles = random.randint(0,20)

    fecha = fecha_alt()


    datos_globales.append([id_show,tipo_Evento,duracion,espectadores,espacios_disponibles,fecha])



matriz = datos_globales

matriz_ordenada= sorted(matriz, key=lambda x: x[5])

def ver_m(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["ids","tipo evento","   duracion","cant_e","esp_d","fecha"]

    print("------------------------------------------------------------")
    for col in columnas_t:
        print(col, end="\t")
    print()

    print("-------------------------------------------------------------")

    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end="\t")
        print()

#Solo ids del show
solo_ids_show = []

for i in datos_globales:

    solo_ids_show.append(i[0])





#RESERVA


while len(datos_globales_reserva) != len(nombres):

    id_reserva = id_alt_r()

    nombre = random.choice(nombres)

    dni = random.randint(56000000,90000000)

    ubicacion_u = random.choice(ubicacion)

    show = random.choice(solo_ids_show)

    telefono = random.randint(1100000000, 1199999999)

    tipos_c = ["@gmail.com","@hotmail.com","@yahoo.com"]

    correo = nombre + random.choice(tipos_c)

    correo_ok = correo.replace(" ","")


    datos_globales_reserva.append([id_reserva,nombre,dni,ubicacion_u,show,telefono,correo_ok])


matriz2 = datos_globales_reserva


def ver_m2(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["ids","nombre     ","dni    ","        ubicacion","id_show","        telefono","mail"]

    print("-------------------------------------------------------------------------------------------------")
    for col in columnas_t:
        print(col, end="\t")
    print()

    print("--------------------------------------------------------------------------------------------------")

    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end="\t")
        print()







    



while True:

  

    #PROGRAMA PRINCIPAL

    print("\n1-MOSTRAR SHOWS\n2-RESERVAS\n3-GENERAR RESERVA\n4-GENERAR SHOW\n5-BUSCAR SHOW")

    usuario = int(input("Elige una opcion: "))

    if usuario == 1: #MOSTRAR SHOWS
       matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
       ver_m(matriz_ordenada) 
    elif usuario == 2: #MOSTRAR RESERVAS
       ver_m2(matriz2)
    elif usuario == 3: #GENERAR RESERVA
        id_reserva = id_alt_r()  # Llamar a la función
        nombre = input("Ingrese nombre: ")
        while len(nombre) < 9:
            nombre += " "
        dni = int(input("Ingrese numero de documento: "))
        print("\n1-Platea\n2-Campo\n3-Vip")
        ubicacion_u = int(input("Elegi tipo de ubiacion: "))
        if ubicacion_u == 1:
            ubicacion_e = "platea   "
        elif ubicacion_u == 2:
            ubicacion_e = "campo    "
        elif ubicacion_u == 3:
            ubicacion_e = "vip       "
        ver_m(matriz) 
        show = int(input("ingrese el numero de id del show que desea asistir: "))
        while show not in solo_ids_show:
            print("El id ingresado no existe")
            show = int(input("porfavor,ingrese el numero de id del show que desea asistir: "))
        for i in datos_globales:
            if i[0] == show:
                i[4] = i[4] - 1
        telefono = int(input("Ingrese numero de telefono: "))
        correo = input("Ingrese correo electronico: ")
        datos_globales_reserva.append([id_reserva, nombre, dni, ubicacion_e, show, telefono, correo])
        print("AGREGADO CORRECTAMENTE!")
    elif usuario == 4: #GENERAR SHOWS
        id_show = id_alt()

        tipo_Evento = input("Ingrese el tipo de evento")

        duracion = int(input("ingrese la duracion del evento"))

        espectadores = int(input("ingrese la capacidad maxima de espectadores"))

        espacios_disponibles = random.randint(0,20)


        año = int(input("ingrese año"))
        mes = int(input("ingrese mes"))
        dia = int(input("ingrese dia: "))
        fecha = datetime(año, mes, dia).date()

        #comprobar si se pasan los minuts

        lista_temp = []

        for i in datos_globales:
            if i[5] == fecha:
                lista_temp.append(i)


        suma = 0
        columna = 2
        for f in lista_temp:
            suma += f[columna]
        
        if (suma + duracion) < 720:

            datos_globales.append([id_show,tipo_Evento,duracion,espectadores,espacios_disponibles,fecha])
        else:
            print("No hay espacio en el dia para el show ingresado")
    elif usuario == 5: #BUSCAR SHOWS

        print("\n1-BUSCAR POR ID\n2-BUSCAR POR FECHA")

        elec = int(input(" "))

        if elec == 1:

            elec = int(input("inrese id"))

            lista_temp = []

            for i in datos_globales:
                if i[0] == elec:
                    lista_temp.append(i)

            if len(lista_temp) > 0:
                ver_m(lista_temp) 
            else:
                print("no coincide con ningun id")

        elif elec == 2:
        
            año = int(input("ingrese año"))
            mes = int(input("ingrese mes"))
            dia = int(input("ingrese dia: "))
            fecha_buscada = datetime(año, mes, dia).date()

            lista_temp = []

            for i in datos_globales:
                if i[5] == fecha_buscada:
                    lista_temp.append(i)


            if len(lista_temp) > 0:
                ver_m(lista_temp) 
            else:
                print("no hay fechas disponibles")
                

    elif usuario == 6: #SALIR
        break


