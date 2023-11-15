#decoradores
#funcion que decora a otra (agarra la funcion y le agrega funcionalidas a la funciuon antes o/y despues de ejectutarla)
#se usa para validar
def decorador (function):
    def funcion_modificada():
        print("antes de llamar a la funcion")
        function()
    return funcion_modificada()

@decorador #llama a la funcion que va agregar antes una funcion
def saludo2():
    print("Holamarco, como estas?")

saludo2()