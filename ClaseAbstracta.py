#Clases abstractas
#clase q no se puede instanciar/crear clases apartir de esa plantilla

from abc import ABC, abstractclassmethod

class Persona (ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def HacerActividad (self):
        pass

    def presentar(self):
        print("hola me llamo" + self.nombre)


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def HacerActividad (self):
        print("Estoy estudiando: " + self.actividad)


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def HacerActividad (self):
        print("Estoytrabajando de: " + self.actividad)


marco = Estudiante ("Marco", 21, "Masculino", "Programador")
yoz = Trabajador ("Yoz", 21, "Masculino", "Programador")

marco.presentar()
marco.HacerActividad()

