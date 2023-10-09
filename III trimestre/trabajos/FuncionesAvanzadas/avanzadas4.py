#Definimos una funcion llamada 'base' que toma otra funcion llamada 'funcion' como argumento
def base(funcion):
    
    #Dentro de 'base', definimos una funcion interna llamada 'interna' que toma dos numeros 'n1' y 'n2'
    def interna(n1, n2):
        #Mostramos un mensaje al iniciar la funcion 'base'
        print('Inicia la funcion base')
        #print(funcion(n1,n2))#*        
        #return funcion(n1,n2)
        #Luego, ejecutamos la funcion 'funcion' que se paso como argumento con los numeros 'n1' y 'n2'
        funcion(n1, n2)
        #Mostramos un mensaje al finalizar la funcion 'base'
        print('Finaliza la funcion base')
    
    #Devolvemos la funcion interna 'interna'
    return interna

#Definimos dos funciones: 'suma' y 'resta' que toman dos numeros 'num1' y 'num2' y realizan las operaciones respectivas
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

#Llamamos a 'base' con la funcion 'suma' y guardamos el resultado en 'var1'
var1 = base(suma)
#Luego, llamamos a 'base' con la funcion 'resta' y guardamos el resultado en 'var2'
var2 = base(resta)

#var1(10,15)#*
#var2(15,10)#*

#Ahora, llamamos a 'var1', que es una funcion que encapsula 'suma', con los numeros 10 y 15
#Esto imprimirá un mensaje de inicio, ejecutará 'suma(10, 15)' y luego imprimirá un mensaje de finalizacion
print(var1(10, 15))

#Luego, llamamos a 'var2', que es una funcion que encapsula 'resta', con los numeros 15 y 10
#Esto imprimirá un mensaje de inicio, ejecutará 'resta(15, 10)' y luego imprimirá un mensaje de finalizacion
print(var2(15, 10))
