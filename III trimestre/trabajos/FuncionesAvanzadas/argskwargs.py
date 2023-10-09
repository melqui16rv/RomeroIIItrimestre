#Definimos una funcion llamada "funcion" que toma argumentos arbitrarios "*args" y argumentos de palabras clave "**kwargs"
def funcion(*args, **kwargs):
    #Iteramos a traves de los argumentos posicionales "*args" y los imprimimos uno por uno
    for elemento in args:
        print("Elemento:", elemento)

    #Iteramos a traves de los argumentos de palabras clave "**kwargs" y los imprimimos en el formato "clave : valor"
    for key, val in kwargsitems():
        print(f'{key} : {val}')

#Llamamos a la funcion "funcion" con argumentos posicionales y de palabras clave
funcion(1, 2, 3, 4, fecha='6-10-2023', hora='7:30 am')

#Definimos una variable "x" con un valor de 100
x = 100

#Comprobamos si la variable "x" es una instancia de la clase "int" (entero) e imprimimos el resultado
print("¿La variable x es un entero?", isinstance(x, int))
