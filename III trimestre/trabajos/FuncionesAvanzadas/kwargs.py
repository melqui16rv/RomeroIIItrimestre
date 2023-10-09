#Definimos una funcion llamada 'function' que recibe argumentos como pares clave-valor y muestra informacion sobre ellos

def function(**kwargs):
    #print(type(kwargs))
    #Iteramos a traves de las claves (keys) y mostramos las claves (keys) una por una
    for key in kwargs.keys():
        print("Clave:", key)

    #Iteramos a traves de los valores (values) y mostramos los valores uno por uno
    for value in kwargs.values():
        print("Valor:", value)

    #Iteramos a traves de los pares clave-valor y mostramos ambos juntos
    for key, value in kwargs.items():
        print(f'Clave: {key}, Valor: {value}')


#Llamamos a la funcion y le pasamos algunos pares clave-valor
function(programa="adso", ficha=2693629, aprendices=16)



#dict={
#    'programa':'adso',
#    'ficha':2693629,
#    'aprendices':16
#}
