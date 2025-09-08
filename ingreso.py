from nombres_teatroV2 import *
from funciones_de_teatroV2 import *
import re

def login():
    dni_ingres=int(input("escriba su dni para verificacion "))
    while dni_ingres not in datos_de_ingreso_dni and dni_ingres not in dni_admins:
        print("id no encontrado revise que este bien su dni")
        dni_ingres=int(input("escriba su dni para verificacion "))

    else:
        contraseña=input("escriba su contraseña de usuario ")
        
        while (contraseña not in datos_globales_contraseñas and dni_ingres not in datos_de_ingreso_dni) \
                and (contraseña not in contraseñas_admin and dni_ingres not in dni_admins):

            print("su contraseña o dni no son correctos")
            print("si desea cambiar el dni seleccione 1 si quiere cambiar la contraseña elija 2 y " \
            "si quiere volver al elegir para crear un usuario nuevo")

            vuelta=int(input(""))
            while vuelta !=0 and vuelta!=1 and vuelta!=2:
                print("ese numero no esta dentro del rango")
                print("si quiere volver al menu de seleccion seleccione 0\n si desea cambiar el dni seleccione 1"
                      "\n si quiere cambiar la contraseña elija 2")

                vuelta=int(input(""))

            if vuelta==1:
                dni_ingres=int(input("escriba su dni para verificacion"))
        
            elif vuelta==2:
                contraseña=(input("escriba su contraseña para verificacion"))
    
            elif vuelta==0:
                return "fallo"  #habria que ver

        if contraseña in contraseñas_admin and dni_ingres in dni_admins:
            print("Ingreso conseguido como ADMIN")
            return "admin"
        elif busqueda(dni_ingres, contraseña):
            print("Ingreso conseguido como USUARIO")
            return "usuario"
        else:
            return "fallo"


def registrar():
    num_usuario = id_user()
    nombre = input("Escriba el nombre que desee usar: ")
    dni_cread = int(input("Escriba el número de su DNI: "))
    while dni_cread < 0:
        print("El DNI no puede ser negativo, intente de nuevo")
        dni_cread = int(input("Escriba el número de su DNI: "))

    telefono_cread = int(input("Escriba su número de teléfono sin código de área: "))
    while telefono_cread < 1100000000 or telefono_cread > 1199999999:
        print("Número no válido (1100000000 a 1199999999)")

        telefono_cread = int(input("Escriba su número de teléfono sin código de área: "))
    telefono_organizado= f"{telefono_cread[1:]}-{telefono_cread[2:6]}-{telefono_cread[6:]}"

    email = input("Escriba su email: ")
    coincidencias = re.findall("@", email)       
    if coincidencias==None:
        print("Email inválido, debe ser @gmail.com, @hotmail.com o @yahoo.com")
        email = input("Escriba su email: ")

    activo = True
    contraseña = input("Escriba la contraseña que desea: ")

    numero_oculto="11-XXXX-XXXX"
    print(f"se a creado su usuario con la siguiente informacion \
          \n numero de usuario: {num_usuario}\n nombre: {nombre}\n dni: {dni_cread}\n numero: {numero_oculto}\n email:{email}")

    datos_de_ingreso_dni.append(dni_cread)
    datos_globales_contraseñas.append(contraseña)
    datos_globales_usuarios.append([num_usuario, nombre, dni_cread, telefono_organizado, email, activo])

    print("Usuario registrado con éxito")
"""testeo de las variables"""
#region testeo
"""

registrar()
login()

"""