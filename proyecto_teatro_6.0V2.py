from nombres_teatroV2 import *
from funciones_de_teatroV2 import *

inicio=True
menu=True
admin=True

#region ingreso
while True:
    while inicio==False:

        ingreso=int(input("Si posee un usuario presione 0 para ingresar.\nSi no posee presione 1 para crear un usuario nuevo:"))
        while ingreso !=0 and ingreso !=1:
            print("Ingreso no valido seleccione 1 o 0: ")
            ingreso=int(input("Si posee un usuario presione 0 para ingresar.\nSi no posee presione 1 para crear un usuario nuevo:"))


        if ingreso==0:
            dni_ingres=int(input("escriba su dni para verificacion "))
            while dni_ingres not in datos_de_ingreso_dni and dni_ingres not in dni_admins:
                print("id no encontrado revise que este bien su dni")
                dni_ingres=int(input("escriba su dni para verificacion "))

            if dni_ingres in datos_de_ingreso_dni or dni_ingres in dni_admins:
                contraseña=input("escriba su contraseña de usuario ")
                
                while (contraseña not in datos_globales_contraseñas and dni_ingres not in datos_de_ingreso_dni) \
                        and (contraseña not in contraseñas_admin and dni_ingres not in dni_admins):

                    print("su contraseña o dni no son correctos")
                    print("si desea cambiar el dni seleccione 1 si quiere cambiar la contraseña elija 2 y " \
                    "si quiere volver al elegir para crear un usuario nuevo")

                    vuelta=int(input(""))
                
                    while vuelta not in (0,1,2):
                        print("ese numero no esta dentro del rango")
                        print("si desea cambiar el dni seleccione 1 si quiere cambiar la contraseña elija 2 y" \
                        " si quiere volver al elegir para crear un usuario nuevo ")

                        vuelta=int(input(""))
                
                    if vuelta==1:
                        dni_ingres=int(input("escriba su dni para verificacion"))
                
                    elif vuelta==2:
                        contraseña=(input("escriba su contraseña para verificacion"))
            
                    elif vuelta==0:
                        ingreso=int(input("Si posee un usuario presione 0 para ingresar.\n" \
                        "Si no posee presione 1 para crear un usuario nuevo:"))
                print("llegaste aca")
                if contraseña in contraseñas_admin and dni_ingres  in dni_admins:
                    menu=True
                    admin=True
                    print("ingreso consegido")
                    inicio=False
                elif contraseña not in contraseñas_admin and dni_ingres not in dni_admins:
                    verificacion=busqueda(dni_ingres,contraseña)
                    if verificacion==True:
                        print("ingresando a su cuenta")
                        menu=True
                        inicio=False

        if ingreso==1:
            num_usuario=id_user()
            nombre=input("escriba el nombre que desee usar ")
            dni_cread=int(input("escriba el numero de su dni "))
            while dni_cread<0:
                print("su dni es menor a  porfavor revise nuevamente su dni ")
                dni_cread=int(input("escriba el numero de su dni "))
            datos_de_ingreso_dni.append(dni_cread)
            telefono_cread=int(input("escriba su numero de telefono sin codigo de area "))
            while telefono_cread<1100000000 or telefono_cread>1199999999:
                print("numero no valido por favor presione un numero dentro del rango de 1100000000 y 1199999999")
                telefono_cread=int(input("escriba su numero de telefono sin codigo de area "))
            email=input("escriba su email ")
            while "@gmail.com" not in email and "@hotmail.com" not in email and "@yahoo.com" not in email: 
                print("algo esta mal con su email porfavor revise si ha puesto el @gmail,hotmail o yahoo")
                email=input("escriba su email ")
            activo=True
            contraseña=input("escriba la contraseña que desea ")
            datos_globales_contraseñas.append(contraseña)
            datos_globales_usuarios.append([num_usuario, nombre, dni_cread, telefono_cread, email, activo])

        
    #region program princ
    #PROGRAMA PRINCIPAL
    while menu==True:
        if admin==True:
            print("\n1-Shows\n2-Reserva\n3-Usuario\n4-Cerrar sesion\n5-SALIR")
            usuario = int(input("Elige una opcion: "))
        if admin==False:
            print("\n1-Shows\n2-Reserva\n3-Usuario\n4-Cerrar sesion\n5-SALIR")
            usuario = int(input("Elige una opcion: "))
        #region opciones
        #region Shows
        if usuario == 1: #SUB MENU SHOWS
            if admin==False:
                print("\n1-Ver show\n2-Buscar show")
            if admin==True:
                print("\n1-Ver show\n2-Buscar show\n3-Borrar show\n4-Editar show \n5-Generar show")
            usuario_i = int(input("Elige una opcion: "))

            if usuario_i == 1:   #VER SHOW
                matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
                ver_m(matriz_ordenada)
            
            elif usuario_i == 2: #BUSCAR SHOW

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


            elif usuario_i == 3 and admin==True: #BORRAR SHOW
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
                print("show eliminado")

            elif usuario_i == 4 and admin==True: #EDITAR SHOW
                print("gat")

                eleccion = int(input("Seleccione el id del show: "))

                for i in datos_globales:

                    if i[0] == eleccion:
                        i[1] = input("seleccione porque tipo de evento quiere cambiarlo: ")

                        fecha = i[5]

                        lista_temp2 = []
                        suma = 0

                        for u in datos_globales:
                            if u[5] == fecha:
                                lista_temp2.append(u)

                        if suma <= 750:
                            suma_aux = int(input("ingresa la cantidad de minutos: "))
                            while (suma + suma_aux) >= 750:
                                suma_aux = int(input("ingresa la cantidad de minutos: "))
                            i[2] = suma_aux
                            
                        else:
                            print("no es posible agregar un show")
                        
                        i[3] = input("seleccion la cant espectadores: ")

                        i[4] = input("seleccion la cant esp disponibles: ")
            elif usuario_i == 5 and admin==True: #GENERAR SHOW
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
#region reservas
        elif usuario == 2: #SUB MENU RESERVAS , CERRAR SESION
            if admin==False:
                print("\n1-Ver reserva\n2-Generar reserva")
            if admin==True:
                print("\n1-Ver reserva\n2-Generar reserva\n3-Borrar reserva\n4-Gererar reserva (pregunta)\n5-Editar reserva")
            usuario_i = int(input("Elige una opcion: "))

            if usuario_i == 1:  #ver reserva     
                ver_m2(matriz2)

            elif usuario_i == 2: #GENERAR RESERVA
            
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

            elif usuario_i == 3 and admin==True: #BORRAR RESERVA
                eleccion = int(input("Seleccione id de reserva a eliminar: "))


                for i in datos_globales_reserva[:]:
                    if i[0] == eleccion:
                        datos_globales_reserva.remove(i)
                print("reserva eliminada")

            elif usuario_i == 4 and admin==True: #GENERAR RESERVA

                id_reserva = id_alt_r()  # Llamar a la función

                dni_usuario = int(input("Ingresar el numero de id: "))
                while id_usuario not in datos_de_ingreso_dni:
                    print("Id inexistente")
                    dni_usuario = int(input("Ingresar el numero de id: "))
                id_usuario=id_user()
                
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

            elif usuario_i == 5 and admin==True: #EDITAR RESERVA
                print("gat")

                eleccion = int(input("Seleccione el id de reserva a editar: "))

                for i in datos_globales_reserva:
                    if i[0] == eleccion:
                        i[2] = int(input("ingrese ubicacion: "))
                        i[3] = input("ingresar show: ")     
#region usuarios
        elif usuario == 3: #SUBMENU USUARIOS
            if admin==False:
                print("\n1-Ver usuario\n2-¿¿¿¿Editar usuario????")
            if admin==True:
                print("\n1-Ver usuario\n2-Editar usuario\n3-Borrar usuario")
            usuario_i = int(input("Elige una opcion: "))
            if usuario_i == 1: #VER USUARIOS
                ver_m3(matriz3) 
            elif usuario_i == 2: #EDITAR USUARIO
                print("gat")

                eleccion = int(input("Seleccione el id de usuario a editar: "))

                for i in datos_globales_usuarios:
                    if i[0] == eleccion:
                        i[1] = input("ingrese nombre: ")
                        i[2] = int(input("Ingrese dni: "))
                        i[3] = int(input("ingrese telefono: "))
                        i[4] = input("Ingrese el correo: ")

            elif usuario == 3 and admin==True: #BORRAR USUARIO
                eleccion = int(input("Seleccione id a eliminar: "))

                for i in datos_globales_usuarios:
                    if i[0] == eleccion:
                        i[5] = False

                for i in datos_globales_reserva[:]:
                    if i[1] == eleccion:
                        datos_globales_reserva.remove(i)

        

        elif usuario == 4: #CERRAR SESION
            admin=False
            menu=False
            inicio=True

        elif usuario == 5: #SALIR
            break

