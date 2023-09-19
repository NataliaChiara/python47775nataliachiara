# -Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. 
# -Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales
# -El proyecto debe compartirse utilizando Colab bajo el nombre "Primera pre-entrega + apellido"
# -El formato de registro es: nombre de usuario y contrasena
# -Utilizar una funcion para almacenar la informacion y otra funcion para mostrar la informacion
# -Utilizar un diccionario para almacenar dicha informacion, con el par usuario-contrasena (clave-valor)
# -Utilizar otra funcion para el login de usuarios, comprobando que la contrasena coincida con el usuario
# -Utilizando los conceptos de la clase 8, guarde la informacion en un archivo de texto dentro de su Drive

import json

def mostrar_info():
    try:
        with open('datos.json', 'r') as archivo:
            return json.load(archivo)
    except Exception as error:
        print(error)
        return {"usuario": '', "contrasena": ''}

bd = mostrar_info()

def gestion_de_usuarios(opcion_sistema=None): #aca tambien puede ser con un 'while true' pero esta opcion me parecio mejor asi no se repite todo desde cero
    if opcion_sistema is not None:
        opcion = opcion_sistema
    else:
        opcion = int(input('Menu de seleccion\nPara login seleccione 1\nPara sign up seleccione 2\nPara salir seleccione 3: '))
        
    if opcion == 1:
        login()
    elif opcion == 2:
        sign_up()
    elif opcion == 3:
        print('Hasta luego!')
    elif opcion == 1234: #opcion oculta solo para administradores
        print(mostrar_info())
    else:
        print('Opcion invalida')
        gestion_de_usuarios()

def login():
    usuario = input('Ingrese su usuario:')
    contrasena = input('Ingrese su contrasena:')
    if usuario != bd['usuario']:
        print('Su usuario no se encuentra creado en el sistema, lo redirigiremos a la pantalla de creacion de usuarios')
        gestion_de_usuarios(2)
    else:
        if contrasena == bd['contrasena']:
            print(f"Usted fue logueado correctamente como {usuario}")
        else:
            print('Su contrasena fue incorrecta. Intentelo nuevamente')
            gestion_de_usuarios(1)

def sign_up():
        usuario = input('Ingrese su usuario:')
        contrasena = input('Ingrese su contrasena:')
        almacenar_info(usuario, contrasena)
        
        print(f"Su usuario es: {usuario} y su contrasena es: {contrasena}")
        gestion_de_usuarios()

def almacenar_info(usuario, contrasena):
    bd['usuario'] = usuario
    bd['contrasena'] = contrasena
    with open('datos.json', 'w') as archivo:
        json.dump(bd, archivo)

gestion_de_usuarios()