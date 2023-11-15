#abstraccion
#ocultar los detalles inecesarios y mostrar lo necesario

class Auto():
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado ="encendido"
        print("el auto esta encendido")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
            print("conduciendo")
auto= Auto()
auto.conducir()

#En este eujemplo hay Abstraccion el usuario no sabe que hay un if y que se llama a una funcion el solo ve el resultado 
#Cuando llamemos a conducir() esperamos a q el auto condusca sin importar q hace ese ese metodo a eso se le llama abastraccion
