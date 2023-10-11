# -Crear un programa que permita el modelamiento de clientes en una pagina de compras
# -Crear un paquete redistribuible con el programa creado
# -La clase cliente debe tener minimo 4 atributos y 2 metodos
# -Se debe utilizar el metodo __str__() para darle nombre a los objetos

from paquete_clientes.clientes import Client

def user_managment(): 

    new_client = ''
    clients = []

    while True:
        opcion = int(input('Menu de seleccion\nPara agregar usuario seleccione 1\nPara mostrar usuario seleccione 2\nPara modificacion seleccione 3\nPara salir seleccione 4:'))
            
        if opcion == 1:
            user = input('Agregue su nombre de usuario: ')
            mail = input('Agregue su e-mail: ')
            password = input('Agregue su contraseña: ')
            age = input('Agregue su edad: ')
            new_client = Client(user, mail, password, age)
            clients.append(new_client)
            print(f"Su usuario: '{new_client.user}' fue creado con éxito")
        elif opcion == 2:
            if(new_client == ''):
                print('No existe el cliente')
            else:
                print(str(new_client))
        elif opcion == 3:
            newUser = input('Agregue su nuevo nombre de usuario')
            Client.modify_client(user(new_client), newUser(new_client))
        elif opcion == 4:
            print("Hasta luego!")
            break
        elif opcion == 1234: #opcion oculta solo para administradores
            if(clients.len == 0):
                print('no hay clientes')
            else:
                print(clients)
        else:
            print('Opcion invalida')
     
       

user_managment()