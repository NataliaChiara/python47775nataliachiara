class Client:
    def __init__(self, user, mail, password, age):
        self.user = user
        self.mail = mail
        self.__password = password
        self.age = age

    def __str__(self):
        return f"Nombre: {self.user}, E-mail: {self.mail}, Edad: {self.age}"

    def modify_client(self, user, newUser):
        self.user = newUser
        print(f"El usuario: '{user}' fue modificado con éxito y ahora es {newUser}")
