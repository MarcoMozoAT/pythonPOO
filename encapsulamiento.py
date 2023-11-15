#encapsulamiento
    #protejer elementos de una clase  
class Miclase:
    def __init__(self) :
        #"_" privado
        #"__" muy muy privado
        self._atributoPrivado = "valor"

objecto = Miclase()
print(objecto._atributoPrivado)

