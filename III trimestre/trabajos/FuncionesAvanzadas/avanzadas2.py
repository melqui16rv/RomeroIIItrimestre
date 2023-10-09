#Definimos una funcion llamada 'base' que toma un numero 'x'
def base(x):
    #Dentro de 'base', definimos dos funciones internas: 'suma' y 'resta'
    #Estas funciones internas tienen acceso a 'x' porque están dentro de 'base'

    #'suma' toma un numero 'y' y devuelve la suma de 'x' e 'y'
    def suma(y):
        return x + y

    #'resta' toma un numero 'y' y devuelve la resta de 'x' y 'y'
    def resta(y):
        return x - y

    #Finalmente, 'base' devuelve una lista que contiene las funciones 'suma' y 'resta'
    return [suma, resta]

#Ahora, llamamos a 'base' con el numero 10 y guardamos las funciones 'suma' y 'resta' en 'usoFuncionRetornada'
usoFuncionRetornada = base(10)
#print(base(1))

#Luego, utilizamos la funcion 'resta' (que está en la posicion 1 de la lista) con el numero 20
#y mostramos el resultado Debería imprimir 10 (porque 10 - 20 = -10)
print(usoFuncionRetornada[1](20))






# def prueba():
#     pass

# print(prueba)

# class Prueba:
#     pass

# x=Prueba()
# print(x)