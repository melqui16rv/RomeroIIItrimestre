#Esta funcion toma dos numeros, los suma y devuelve el resultado
def suma(n1, n2):
    return n1 + n2

#Esta funcion toma dos numeros, los resta y devuelve el resultado
def resta(n1, n2):
    return n1 - n2

#Esta funcion toma dos numeros, los multiplica y devuelve el resultado
def producto(n1, n2):
    return n1 * n2

#Esta funcion toma dos numeros, los divide y devuelve el resultado
def division(n1, n2):
    return n1 / n2

#Se definir una funcion llamada 'operacion'
#Esta funcion toma otra funcion (como 'suma', 'resta', etc),
#y dos numeros Luego, ejecuta esa funcion con los numeros dados
def operacion(funcion, numero1, numero2):
    #Imprimimos el resultado de la funcion con los numeros dados
    print(funcion(numero1, numero2))

#Aquí estamos usando nuestra funcion 'operacion' para sumar 10 y 5
operacion(suma, 10, 5)

