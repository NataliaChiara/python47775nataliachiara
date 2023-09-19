# db = {}

# def gestion_de_usuarios(opcion_sistema=None):
#     if opcion_sistema is not None:
#         opcion = opcion_sistema
#     else:
#         opcion = int(input('Menú de selección\nPara login seleccione 1\nPara sign up seleccione 2\nPara salir seleccione 3: '))
        
#     if opcion == 1:
#         usuario = input('Ingrese su usuario: ')
#         contraseña = input('Ingrese su contraseña: ')
#         if 'usuario' not in db:
#             print('Su usuario no se encuentra creado en el sistema, lo redirigiremos a la pantalla de creación de usuarios')
#             gestion_de_usuarios(2)
#         else:
#             if contraseña == db['contraseña']:
#                 print(f"Usted fue logueado correctamente como {usuario}")
#             else:
#                 print('Su contraseña fue incorrecta.')
#                 gestion_de_usuarios(1)
#     elif opcion == 2:
#         usuario = input('Ingrese su usuario: ')
#         contraseña = input('Ingrese su contraseña: ')
#         db['usuario'] = usuario
#         db['contraseña'] = contraseña
#         print(f"Su usuario es: {usuario} y su contraseña es: {contraseña}")
#         print(db)
#         gestion_de_usuarios()
#     elif opcion == 3:
#         print('Hasta luego!')
#     else:
#         print('Opción no válida. Por favor, seleccione una opción válida.')
#         gestion_de_usuarios()

# gestion_de_usuarios()

# -----

import json

usuarios = {}

def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    usuarios[nombre_usuario] = contrasena
    guardar_datos()

def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario, _ in usuarios.items():
        print(usuario)

def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def guardar_datos():
    with open('/content/drive/MyDrive/usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo)

def cargar_datos():
    try:
        with open('/content/drive/MyDrive/usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

usuarios = cargar_datos()

while True:
    print("\nMenu de opciones:")
    print("1. Registrar usuario")
    print("2. Mostrar usuarios registrados")
    print("3. Iniciar sesión")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        mostrar_usuarios()
    elif opcion == '3':
        iniciar_sesion()
    elif opcion == '4':
        guardar_datos()
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
