#Definimos una función llamada 'base' que toma otra función llamada 'funcion' como argumento
def base(funcion):
    #Dentro de 'base', definimos una función interna llamada 'interna'
    def interna():
        #Mostramos un mensaje al iniciar la función 'base'
        print('Inicia la función base')
        #Luego, ejecutamos la función 'funcion' que se pasó como argumento
        funcion()
        #Mostramos un mensaje al finalizar la función 'base'
        print('Finaliza la función base')
    #Devolvemos la función interna 'interna'
    return interna

#Definimos dos funciones: 'integrada' y 'otraFuncion'
def integrada():
    print('Funcion Integrada')

def otraFuncion():
    print('Otra Funcion')

#Llamamos a 'base' con la función 'integrada' y guardamos el resultado en 'var1'
var1 = base(integrada)
#Luego, llamamos a 'base' con la función 'otraFuncion' y guardamos el resultado en 'var2'
var2 = base(otraFuncion)

#Ahora, llamamos a 'var1', que es una función que encapsula 'integrada'
#Esto imprimirá un mensaje de inicio, ejecutará 'integrada' y luego imprimirá un mensaje de finalización
var1()

#Luego, llamamos a 'var2', que es una función que encapsula 'otraFuncion'
#Esto imprimirá un mensaje de inicio, ejecutará 'otraFuncion' y luego imprimirá un mensaje de finalización
var2()



#def integrada(parametro):
#    print(f'{parametro} de la funcion Integrada')



