#polimorfismo
# permite que diferentes objetos de diferentes clases respondan a un mismo mensaje de diferentes maneras
#Llamar al mimso metodo y q te responda diferente 
class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "wooow"

def HacerSonido(animal): 
    print(animal.sonido())

gato = Gato()
perro = Perro()

HacerSonido(gato)