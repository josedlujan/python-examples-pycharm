class Persona:
    nombre = ""
    edad = 0
    pais = ""

    def __init__(self,nombre,edad,pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def saludar(self):
        print("Hola mi nombre es",self.nombre)

    def despedir(self):
        print("Hasta pronto")

    def comprar(self):
        self.saludar()
        print("Puedo comprar X cosa")

class Empleado:
    trabajo = ""


class Estudiante(Persona,Empleado):
    escuela = ""
    #sin init y con init
    def __init__(self,nombre,empleo):
        self.nombre  = nombre
        self.trabajo = empleo





#diferncia de ()
pepito = Persona('jose',20,'cancun')
pepito.comprar()

#estudiante
#estudiante = Estudiante('juan',10,'lima')
estudiante = Estudiante('juan','vendedor')
estudiante.comprar()
print(estudiante.trabajo)