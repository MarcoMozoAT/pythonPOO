#decoradores @property
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property #decorador para decir que es un geter
    def nombre(self):
        return self._nombre
    
    @nombre.setter #decorador para decir que es un setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

    @nombre.deleter #decorador que elimina valores 
    def nombre(self):
        del self._nombre
    
    

marco= Persona ("Lucas", 23)
nombre = marco.nombre
print (nombre)

marco.nombre= "marcoyyyy"
nombre = marco.nombre
print (nombre)


del marco.nombre
nombre = marco.nombre
print(nombre)
    