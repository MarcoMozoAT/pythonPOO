class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad= edad
        self.grado = grado

    def estudiar(self):
        print ("Llamaste al metodo Estudiar")

nombre= input ("Digame su nombre: ")
edad = input ("digame su edad: ")
grado = input ("digame su grado: ")


estudiante = Estudiante(nombre, edad, grado)

print("El estudiante se llama: " + estudiante.nombre)

estudiar = input()
if (estudiar.lower() == "estudiar"):
    estudiante.estudiar()
