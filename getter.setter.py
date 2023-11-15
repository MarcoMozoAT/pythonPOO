class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
    
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

#getter : Acceder a un valor del atributo privado
marco= Persona ("Lucas", 23)
nombre = marco.get_nombre()

#setter : Modificar el valor del atributo privado
marco.set_nombre("marco") 
nombre = marco.get_nombre()
print (nombre)
    