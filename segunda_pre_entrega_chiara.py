# -Crear un programa que permita el modelamiento de clientes en una pagina de compras
# -Crear un paquete redistribuible con el programa creado
# -La clase cliente debe tener minimo 4 atributos y 2 metodos
# -Se debe utilizar el metodo __str__() para darle nombre a los objetos

# Clase

class Client:
    def __init__(self, user, mail, password, age):
        self.user = user
        self.mail = mail
        self.__password = password
        self.age = age

    def __str__(self):
        return f"Nombre: {self.user}, E-mail: {self.mail}, Edad: {self.age}"
    
    def delete_client(self, user):
        self.user = ''
        print(f"El usuario: '{user}' fue eliminado con éxito")

    def modify_client(self, user, newUser):
        self.user = newUser
        print(f"El usuario: '{user}' fue modificado con éxito")



# Interaccion

def user_managment(): 

    new_client = ''
    clients = []

    while True:
        opcion = int(input('Menu de seleccion\nPara agregar usuario seleccione 1\nPara mostrar usuario seleccione 2\nPara eliminación seleccione 3\nPara modificacion seleccione 4\nPara salir seleccione 5:'))
            
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
        elif opcion == 5:
            print("Hasta luego!")
            break
        elif opcion == 1234: #opcion oculta solo para administradores
            if(clients.len == 0):
                print('no hay clientes')
            else:
                print(clients)
        else:
            print('Opcion invalida')
        # elif opcion == 2:
        #     sign_up()
        # elif opcion == 3:
        #     print('Hasta luego!')
     
       

user_managment()