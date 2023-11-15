#herencia
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("estoy hablando un poco")




class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

def saludar():
    pass #sirve para declarar el metodo vacio


roberto = Empleado("Marco", 34, "argentino", "programador", 1500)
roberto.hablar()

