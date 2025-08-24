
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


#DATOS USUARIOS

datos_globales_usuarios = []

id_usuarios = []

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


def ver_m3(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["id","nombre     ","dni    ","        telefono","mail","                               activo"]

    print("-----------------------------------------------------------------------------------------------------")
    for col in columnas_t:
        print(col, end="\t")
    print()

    print("-----------------------------------------------------------------------------------------------------")

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == True:
                matriz[f][c] = "\tACTIVO"
            elif matriz[f][c] == False:
                matriz[f][c] = "\tINACTIVO"
            print(matriz[f][c], end="\t")
        print()


#Solo ids del show
solo_ids_usuario = []

for i in datos_globales_usuarios:

    if i[5] == True:
        solo_ids_usuario.append(i[0])



#RESERVA


while len(datos_globales_reserva) != len(nombres):

    id_reserva = id_alt_r()

    id_usuario = random.choice(solo_ids_usuario)

    ubicacion_u = random.choice(ubicacion)

    show = random.choice(solo_ids_show)

    datos_globales_reserva.append([id_reserva,id_usuario,ubicacion_u,show])


matriz2 = datos_globales_reserva

datos_globales_contraseñas=["superadmin"]
datos_globales_dni=[47346945,46624535]

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

game=True
admin=False
"""---------------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------------------------------------------"""

while True:
    while game==True:
        ingreso=int(input("Si posse un usuario presione 0 para ingresar:\nSi no posee presione 1 para crear un usuario nuevo:"))
        if ingreso==0:
            dni=int(input("ingrese su dni:"))
            if dni not in datos_globales_dni:
                print("el dni ingresado no existe")
                dni=int(input("ingrese su dni:"))
            contraseña=input("ingrese su contraseña: ")
            if contraseña not in datos_globales_contraseñas:
                print("contraseña incorrecta")
                contraseña=input("ingrese su contraseña:")
            if (dni==47346945 or dni==46624535) and (contraseña=="superadmin"):
                admin=True
                
                #Mas adelante poner que volves con el -1 de forma linda
            elif dni==-1 or contraseña == -1:
                ingreso=int(input("Si posse un usuario presione 0 para ingresar:\nSi no posee presione 1 para crear un usuario nuevo:"))
   
        elif ingreso==1:
        #CREAR USUARIO
            id_usuario = id_user()

            nombre = input("ingrese nombre:")
            nombre=nombre.ljust(8, " ")

            dni = int(input("ingrese documento: "))
            datos_globales_dni.append(dni)
            while nombre==-1 or dni==-1:
                ingreso=int(input("Si posse un usuario presione 0 para ingresar:\nSi no posee presione 1 para crear un usuario nuevo:"))
            

            telefono = int(input("ingrese numero de telefono: "))
            while telefono<1100000000 or telefono>1199999999:
                print("el numero colocado no es valido")
                telefono = int(input("ingrese numero de telefono: "))

            correo = input("ingrese correo ")
            while "@gmail.com" not in correo and "@yahoo.com" not in correo and "@hotmail.com" not in correo:
                print("su correo debe tener @gmail, @yahoo o @hotmail")
                correo = input("ingrese correo")

            contraseña= input("ingrese una contraseña")
            while len (contraseña) <5:  
                print("contraseña invalida tiene que tener mas de 5 caracteres")
                contraseña= input("ingrese una contraseña ")
            if len(contraseña) >5:
                print("contraseña creada con exito")
                datos_globales_contraseñas.append(contraseña)

            #Mas adelante poner que volves con el .


            datos_globales_usuarios.append([id_usuario,nombre,dni,telefono,correo,True])  
        elif ingreso !=0 or ingreso !=1:
            print("ingreso no valido seleccione 1 o 0 ")
            ingreso=int(input("Si posse un usuario presione 0 para ingresar:\nSi no posee presione 1 para crear un usuario nuevo:"))
        game=False
    #PROGRAMA PRINCIPAL
    if admin==True:
        print("\n1-MOSTRAR SHOWS\n2-GENERAR RESERVAS\n3-BUSCAR SHOWS\n4-CERRAR SESION\n5-SALIR\n6-RESERVAS\n7-GENERAR SHOW\n8-VER USUARIOS\n9-BORRAR USUARIO\n10-BORRAR RESERVAS\n11-BORRAR SHOW")
        usuario = int(input("Elige una opcion: "))
    if admin==False:
        print("\n1-MOSTRAR SHOWS\n2-GENERAR RESERVA\n3-BUSCAR SHOW\n4-CERRAR SESION\n5-SALIR")
        usuario = int(input("Elige una opcion: "))
    
    if usuario == 1: #MOSTRAR SHOWS
       matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
       ver_m(matriz_ordenada) 
    elif usuario == 2: #GENERAR RESERVA
        id_reserva = id_alt_r()  # Llamar a la función
        id_usuario = int(input("ingresar el numero de id"))
        while id_usuario not in solo_ids_usuario:
            print("Id inexistente")
            id_usuario = int(input("ingresar el numero de id"))
        print("-----------------")
        print("para platea elija 1")
        print("para campo elija 2")
        print("para vip elija 3")
        print("-----------------")
        ubicacion_u = int(input("Elegi tipo de ubiacion: "))
        while ubicacion_u >3 or ubicacion_u <=0:
            print("no es valido el numero")
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
        datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_e, show])
        print("AGREGADO CORRECTAMENTE!")
    elif usuario == 3: #BUSCAR SHOWS

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
    elif usuario == 4: #SALIR DE LA SESION
        game=True
        admin=False
    elif usuario==5:
        break

    elif usuario == 6 and admin==True: #MOSTRAR RESERVAS
       ver_m2(matriz2)

    elif usuario == 7 and admin==True: #GENERAR SHOWS
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


    elif usuario == 8 and admin==True: #VER USUARIOS
        
        ver_m3(matriz3)


   
    elif usuario == 9 and admin==True: #BORRAR USUARIO

        eleccion = int(input("Seleccione id a eliminar "))

        for i in datos_globales_usuarios:
            if i[0] == eleccion:
                i[5] = False

        for i in datos_globales_reserva[:]:
            if i[1] == eleccion:
                datos_globales_reserva.remove(i)
    elif usuario == 10 and admin==True: #BORRAR RESERVA

        eleccion = int(input("Seleccione id de reserva a eliminar "))


        for i in datos_globales_reserva[:]:
            if i[0] == eleccion:
                datos_globales_reserva.remove(i)

    elif usuario == 11 and admin==True: #BORRAR SHOW
        eleccion = int(input("Ingrese id del show: "))

        # Borrar el show
        for s in datos_globales[:]:
            if s[0] == eleccion:
                datos_globales.remove(s)

        # Borrar todas las reservas asociadas
        for r in datos_globales_reserva[:]:
            if r[3] == eleccion:
                datos_globales_reserva.remove(r)

        # Actualizar lista de ids de shows
        solo_ids_show.clear()
        for s in datos_globales:
            solo_ids_show.append(s[0])
