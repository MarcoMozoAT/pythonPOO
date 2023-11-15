#decoradores
#funcion que decora a otra 

def decorador (function):
    def funcion_modificada():
        print("antes de llamar a la funcion")
        function()
        print("despueds de llamar a la funcion")
    return funcion_modificada()

def saludo():
    print("Hola Marco")

saludoModificado = decorador(saludo)
saludoModificado()