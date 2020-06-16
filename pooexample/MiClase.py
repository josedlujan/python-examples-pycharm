class Usuario:
    nombre = "jose"
    correo = "jose@gmail.com"
    password = "xxxxxxx"


    def __init__(self):
        self.nombre = "juan"

    def cambiarContraseña(self,contraseña):
        self.password = contraseña



pepito = Usuario()
print(pepito.nombre)