# def suma(num1,num2):
#     return num1+num2
#     #print(num1+num2)

#Definimos una funcion llamada "suma" que toma varios argumentos
def suma(*args):
    #Imprimimos el tipo de argumentos que se pasan a la funcion
    print("El tipo de argumentos es:", type(args))

#Definimos una funcion llamada "mayor" que toma varios argumentos
def mayor(*args):
    #Inicializamos una variable "m" para encontrar el numero mayor
    m = 0
    #Iteramos a través de los argumentos pasados a la funcion
    for i in args:
        #Comparamos cada argumento con el numero actual más grande
        if i > m:
            m = i
    #Devolvemos el numero mayor encontrado
    return m

#Llamamos a la funcion "mayor" con varios numeros como argumentos
#y mostramos el numero mayor encontrado
print("El numero mayor es:", mayor(10, 23, 21, 100, 1000, 1, 2, 3))

#suma(10,23,21)
#suma('hola',122,[],{})

