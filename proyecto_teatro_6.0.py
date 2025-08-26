from nombres_teatro import *
from funciones_de_teatro import *


inicio=True
admin=False

#region ingreso
#es para empezar el ingreso
while inicio==True:
    #es la funcion que dicta que puede poner el usuario para cada opcion
    ingreso=int(input("Si posee un usuario presione 0 para ingresar.\nSi no posee presione 1 para crear un usuario nuevo:"))
    #validacion de que toque 0 o 1 exclusivamente
    while ingreso !=0 and ingreso !=1:
        print("Ingreso no valido seleccione 1 o 0: ")
        ingreso=int(input("Si posee un usuario presione 0 para ingresar.\nSi no posee presione 1 para crear un usuario nuevo:"))

    #inicio de el ingreso de un usuario creado anteriormente
    if ingreso==0:
        #ingreso del dni con validacion de que exista en los datos globales de dnis (cambiar lista por una lista paralela)
        dni=int(input("Ingrese su dni: "))
        if dni not in datos_globales_dni:
            print("El dni ingresado no existe.")
            dni=int(input("Ingrese su dni: "))
        #ingreso de la contraseña con validacion de que exista en los datos globales de dnis (cambiar lista por una lista paralela)
        contraseña=input("Ingrese su contraseña: ")
        while contraseña not in datos_globales_contraseñas:
            print("Contraseña incorrecta.")
            contraseña=input("Ingrese su contraseña: ")
        #esto es para que alguien sea admin necesitamos que en lugar de 
        # cambiar uno por uno hacer un lista con dnis y contraseñas que sean para admin    
        if (dni==47346945 or dni==46624535) and (contraseña=="superadmin"):
            #esto hace que puedas desbloquear opciones de admin
            admin=True
            #esto es para avanzar al siguiente  paso que es el de opciones
            menu=True
        #esto es una validacion extra que no es  exactamente necesaria porque las 
        # hacen antes pero es para validar que el dni y la contraseaña sean correctas 
        # (deberia validar que sea el dni y la contraseña de la misma contraseña)
        elif dni in datos_globales_dni and contraseña in datos_globales_contraseñas:
            menu=True

        inicio=False

    elif ingreso==1:
    #CREAR USUARIO
        #llama a una funcion para asignar un id a cada usuario
        id_usuario = id_user()
        #es para ingresar un nombre que tenga un maximo de 8 caracteres mas de eso se rompe la matriz
        #hace una validacion basica de que no puede exceder los 8 caracteres o modifica de 8 a mas caracteres con ese 8 de abajo
        nombre = input("Ingrese nombre: ")
        nombre=nombre.ljust(8, " ")
        #esto es para ingresar un dni con la validacion de que no puede estar anteriormente en la lista de datos globales
        dni = int(input("Ingrese documento: "))
        while dni not in datos_globales_dni:
            datos_globales_dni.append(dni)     
        #se ingresa el telefono con la validacion de que sea mayor a 1100000000 o menor a 1199999999
        telefono = int(input("Ingrese numero de telefono: "))
        while telefono<1100000000 or telefono>1199999999:
            print("El numero colocado no es valido.")
            telefono = int(input("Ingrese numero de telefono: "))
        # se ingresa el correo y si no tiene gmail yahoo hotmail te rebota y te manda a hacerlo de vuelta
        correo = input("Ingrese correo: ")
        while "@gmail.com" not in correo and "@yahoo.com" not in correo and "@hotmail.com" not in correo:
            print("Correo invalido. Su correo debe tener @gmail, @yahoo o @hotmail")
            correo = input("Ingrese correo:")
        #se ingresa una contraseña que tenga mas de 5 caracteres y si es menos rebota rebota
        contraseña= input("Ingrese una contraseña de mas de 5 caracteres: ")
        while len (contraseña) <5:  
            print("Contraseña invalida. Debe tener mas de 5 caracteres.")
            contraseña= input("Ingrese una contraseña de mas de 5 caracteres: ")
        if len(contraseña) >5:
            print("Usuario creado con exito.")
            datos_globales_contraseñas.append(contraseña)
        #si todas las validaciones funcionan agrega todos estos datos y le agrega un dato que es True que siempre tiene que estar
        #porque es para ver si esta activo o inactivo
        datos_globales_usuarios.append([id_usuario,nombre,dni,telefono,correo,True])  
        menu=True
#region program princ
#PROGRAMA PRINCIPAL
while menu==True:
    if admin==True:
        print("\n1-MOSTRAR SHOWS\n2-GENERAR RESERVAS\n3-BUSCAR SHOWS\n4-CERRAR SESION\n5-BORRAR SHOW\n6-RESERVAS\n7-GENERAR SHOW\n8-VER USUARIOS\n9-BORRAR USUARIO\n10-BORRAR RESERVAS\n11-SALIR")
        usuario = int(input("Elige una opcion: "))
        salida = 11
    if admin==False:
        print("\n1-MOSTRAR SHOWS\n2-GENERAR RESERVA\n3-BUSCAR SHOW\n4-CERRAR SESION\n5-SALIR")
        usuario = int(input("Elige una opcion: "))
        salida = 5
    #region opciones
    if usuario == 1: #MOSTRAR SHOWS
       matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
       ver_m(matriz_ordenada) 
    elif usuario == 2: #GENERAR RESERVA
        id_reserva = id_alt_r()  # Llamar a la función

        id_usuario = int(input("Ingresar el numero de id: "))
        while id_usuario not in solo_ids_usuario:
            print("Id inexistente")

            id_usuario = int(input("Ingresar el numero de id: "))
        print("-----------------")
        print("Para platea elija 1")
        print("Para campo elija 2")
        print("Para vip elija 3")
        print("-----------------")

        ubicacion_u = int(input("Elegi tipo de ubiacion: "))
        while ubicacion_u >3 or ubicacion_u <=0:
            print("Numero invalido, por favor ingrese un numero valido.")
            ubicacion_u = int(input("Elegi tipo de ubiacion: "))
        if ubicacion_u == 1:
            ubicacion_e = "Platea   "
        elif ubicacion_u == 2:
            ubicacion_e = "Campo    "
        elif ubicacion_u == 3:
            ubicacion_e = "Vip       "

        ver_m(matriz) 
        show = int(input("Ingrese el numero de id del show que desea asistir: "))
        while show not in solo_ids_show:
            print("El id ingresado no existe, por favor ingrese un id valido.")
            show = int(input("Ingrese el numero de id del show que desea asistir: "))
        for i in datos_globales:
            if i[0] == show:
                i[4] = i[4] - 1
        datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_e, show])
        print("AGREGADO CORRECTAMENTE!")
    elif usuario == 3: #BUSCAR SHOWS

        print("\n1-BUSCAR POR ID\n2-BUSCAR POR FECHA")

        elec = int(input(" "))

        if elec == 1:

            elec = int(input("Ingrese id: "))

            lista_temp = []

            for i in datos_globales:
                if i[0] == elec:
                    lista_temp.append(i)

            if len(lista_temp) > 0:
                ver_m(lista_temp) 
            else:
                print("No coincide con ningún id.")

        elif elec == 2:
        
            año = int(input("Ingrese año: "))
            mes = int(input("Ingrese mes: "))
            dia = int(input("Ingrese dia: "))
            fecha_buscada = datetime(año, mes, dia).date()

            lista_temp = []

            for i in datos_globales:
                if i[5] == fecha_buscada:
                    lista_temp.append(i)


            if len(lista_temp) > 0:
                ver_m(lista_temp) 
            else:
                print("No hay fechas disponibles.")
    elif usuario == 4: #SALIR DE LA SESION
        game=True
        admin=False

    elif usuario == 5 and admin==True: #BORRAR SHOW
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

    elif usuario == 6 and admin==True: #MOSTRAR RESERVAS
       ver_m2(matriz2)

    elif usuario == 7 and admin==True: #GENERAR SHOWS
        id_show = id_alt()

        tipo_Evento = input("Ingrese el tipo de evento: ")
        tipo_Evento=tipo_Evento.ljust(20, " ")

        duracion = int(input("Ingrese la duracion del evento: "))

        espectadores = int(input("Ingrese la capacidad maxima de espectadores: "))

        espacios_disponibles = random.randint(0,20)


        año = int(input("Ingrese año: "))
        mes = int(input("Ingrese mes: "))
        dia = int(input("Ingrese dia: "))
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
            print("No hay espacio en el dia para el show ingresado.")


    elif usuario == 8 and admin==True: #VER USUARIOS
        
        ver_m3(matriz3)

   
    elif usuario == 9 and admin==True: #BORRAR USUARIO

        eleccion = int(input("Seleccione id a eliminar: "))

        for i in datos_globales_usuarios:
            if i[0] == eleccion:
                i[5] = False

        for i in datos_globales_reserva[:]:
            if i[1] == eleccion:
                datos_globales_reserva.remove(i)
    elif usuario == 10 and admin==True: #BORRAR RESERVA

        eleccion = int(input("Seleccione id de reserva a eliminar: "))


        for i in datos_globales_reserva[:]:
            if i[0] == eleccion:
                datos_globales_reserva.remove(i)

    elif usuario == salida:
        break
