from os import strerror
from funcion import*

try:
    with open('c:\\melqui\\datos.txt', 'wt') as file:
        nombre=str(input("Ingrese nombre: "))
        edad=str(input("Digite su edad: "))
        documento=str(input("Digite su documento: "))
        direccion=str(input("Digite su direccion: "))

        for i in range(1):
            file.write("Datos personales" +str("\n""nombre: " +nombre) +str("\n""edad: " +edad) +str("\n""documento: " +documento) +str("\n""direccion: " +direccion))
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


prontt()





# from os import strerror


# try:
#     file = open('c:\\melqui\\datos.txt', 'wt')
#     nombre=str(input("ingrese nombre: "))
#     edad=str(input("digite su edad: "))
#     documento=str(input("digite su documento: "))
#     direccion=str(input("digite su direccion: "))


#     for i in range(1):
#         file.write("Datos personales"+str("\n""nombre: "+nombre) +str("\n""edad: "+edad)+str("\n""documento: "+documento)+str("\n""direccion: " +direccion))
#     file.close()


# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# def prontt():
#     counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
#     total_characters = 0  # Agregamos un contador para el total de caracteres
#     try:
#         line_counter = 0
#         with open(r'c:\\melqui\\datos.txt', "r", encoding="utf-8") as file:
#             for line in file:
#                 line_counter += 1
#                 for char in line:
#                     if char.isalpha():
#                         counters[char.lower()] += 1
#                     total_characters += 1  # Incrementamos el contador de caracteres

#         file.close()
            
#         for char in counters.keys():
#             c = counters[char]
#             if c > 0:
#                 print(f"¡La letra '{char}' aparece {c} veces!")

#         print(f"El archivo contiene {line_counter} líneas en total.")
#         print(f"El archivo contiene {total_characters} caracteres en total.")  # Imprimimos el total de caracteres
            
#     except IOError as e:
#         print("Oops, algo salió mal: ", strerror(e.errno))
# prontt()