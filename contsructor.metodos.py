class Celular:
    #constructor
    def __init__ (self, marca, modelo, camara):
        self.marca=marca
        self.modelo = modelo
        self.camara = camara

    #metodos
    def llamar (self):
        print("Estas haciendo un llamado" + self.modelo)

    def cortar (self):
        print("Estas cortando el llamado desde tu" + self.modelo)

#objeto: una instancia de una clase
celular1 = Celular("samsung", "s23", "30px")
celular1.llamar()


