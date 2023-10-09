#Definimos una funcion llamada 'validar' que verifica si los valores proporcionados son del tipo correcto
def validar(**kwargs):
    # Usamos **kwargs para permitir que se pasen argumentos clave-valor de manera flexible

    for key, value in kwargs.items():
        # Iteramos a traves de todos los argumentos clave y sus valores

        if key == "edad":
            # Comprobamos si el argumento clave es 'edad'

            print(f"Es {value} una edad valida? {isinstance(value, int)}")
            # Imprimimos si el valor es un entero o no

        if key == "peso":
            # Comprobamos si el argumento clave es 'peso'

            print(f"Es {value} un peso valido? {isinstance(value, float)}")
            # Imprimimos si el valor es un numero decimal o no

        if key == "estatura":
            # Comprobamos si el argumento clave es 'estatura'

            print(f"Es {value} una estatura valida? {isinstance(value, float)}")
            # Imprimimos si el valor es un numero decimal o no

# Aqui estamos llamando a la funcion 'validar' con algunos ejemplos de valores
#validar(edad=15,peso=60.0, estatura=1.60)
#validar(edad='siete',peso='39', estatura='1.39')
validar(edad=34, peso=60, estatura=1.90)


#print(isinstance(60.0,float))