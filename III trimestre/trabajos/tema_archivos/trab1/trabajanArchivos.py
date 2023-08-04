#punto 4 de la actividad propuesta el dia 26/julio/2023 *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_

#importamos la función 'strerror' del módulo 'os'. Que a necesitaremos mas adelante.
from os import strerror

#se crea un diccionario con 26 contadores, uno para cada letra del alfabeto de(a hasta z).
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

#Le pedimos al usuario que nos de el nombre del archivo que quiere analizar.
file_name = input("Dale, ingresa el nombre del archivo a analizar: ")

try:
    #abrimos el archivo en modo lectura de texto para esto ponemos (rt) y lo ponemos en la variable (file).
    file = open(file_name, "rt")

    #el programa va línea por línea en el archivo.
    for line in file:
        #luego carácter por carácter en cada línea.
        for char in line:
            #si el carácter es una letra, se va a ir contando
            if char.isalpha():
                # Pero primero se convierte a minúsculas para de esta manera poder contar mayúsculas y minúsculas juntas.
                counters[char.lower()] += 1

    #despues se cierra el archivo ya halla contar todo los caracteres.
    file.close()

    #ahora mostramos los resultados de cuanto se repitio cada caracter 
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(f"¡La letra '{char}' aparece {c} veces!")

except IOError as e:
    #si hay un error, lo manejamos con una excepción de tipo IOError monstrando un mensaje ("Oops, algo salió mal: ).
    print("Oops, algo salió mal: ", strerror(e.errno))




#punto 5 de la actividad propuesta el dia 26/julio/2023 *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_
from os import strerror


counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
counters['numeros'] = 0
counters['especiales'] = 0

file_name = input("Ingresa el nombre del archivo a analizar: ")

try:
    file = open(file_name, "rt")

    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
            elif char.isdigit():
                counters['numeros'] += 1
            else:
                counters['especiales'] += 1

    file.close()

    for char in counters.keys():
        c = counters[char]
        if c > 0:
            if char == 'numeros':
                print(f"Caracteres numéricos -> {c}")
            elif char == 'especiales':
                print(f"Caracteres especiales -> {c}")
            else:
                print(f"Letra '{char}' -> {c}")

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    
    




#PROCESO DE APRENDIZAJE*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_

# Se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto del tipo archivo:
stream = open("c:/melqui/prueba.txt", "rt", encoding="utf-8")

# Se imprime el contenido del archivo:
print(stream.read()) 


from os import strerror

try:
    counter = 0
    stream = open('c:/melqui/prueba.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
    
    
    
    
    


from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('c:/melqui/prueba2.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
    

# from os import strerror

# try:
# 	character_counter = line_counter = 0
# 	for line in open('c:/melqui/prueba2.txt', 'rt'):
# 		line_counter += 1
# 		for char in line:
# 			print(char, end='')
# 			character_counter += 1
# 	print("\n\nCaracteres en el archivo: ", character_counter)
# 	print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))


from os import strerror

try:
	file = open('c:/melqui/newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))



# from os import strerror

# try:
#     file = open('c:/melqui/newtext2.txt', 'wt')
#     for i in range(10):
#         file.write("línea #" + str(i+1) + "\n")
#     file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))







data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))












from os import strerror

source_file_name = input("Ingresa el nombre del archivo fuente: ")
try:
    source_file = open(source_file_name, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

destination_file_name = input("Ingresa el nombre del archivo destino: ")
try:
    destination_file = open(destination_file_name, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino:", strerror(e.errno))
    source_file.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = source_file.readinto(buffer)
    while readin > 0:
        written = destination_file.write(buffer[:readin])
        total += written
        readin = source_file.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
source_file.close()
destination_file.close()














from os import strerror

# Inicializa 26 contadores para cada letra latina.
# Nota: hemos usado una comprensión para esto.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # Si es una letra...
            if char.isalpha():
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1
    file.close()
    # Demos salida a los contadores.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    









from os import strerror

# Inicializa 26 contadores para cada letra latina.
# Nota: hemos usado una comprensión para esto.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # Si es una letra...
            if char.isalpha():
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1
    file.close()
    # Demos salida a los contadores.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    
    
    
    
    
















# from os import strerror


# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
# counters['numeros'] = 0
# counters['especiales'] = 0

# file_name = input("Ingresa el nombre del archivo a analizar: ")

# try:
#     file = open(file_name, "rt")

#     for line in file:
#         for char in line:
#             if char.isalpha():
#                 counters[char.lower()] += 1
#             elif char.isdigit():
#                 counters['numeros'] += 1
#             elif not char.isspace():
#                 counters['especiales'] += 1

#     file.close()

#     for char in counters.keys():
#         c = counters[char]
#         if c > 0:
#             if char == 'numeros':
#                 print(f"Caracteres numéricos -> {c}")
#             elif char == 'especiales':
#                 print(f"Caracteres especiales -> {c}")
#             else:
#                 print(f"Letra '{char}' -> {c}")

# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))
