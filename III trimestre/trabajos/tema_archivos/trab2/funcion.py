from os import strerror

def prontt():
    counters={chr(ch):0 for ch in range(ord('a'), ord('z') +1)}
    total_characters=0
    try:
        line_counter=0
        with open(r'c:\\melqui\\datos.txt', "r", encoding="utf-8") as file:
            for line in file:
                line_counter +=1
                for char in line:
                    if char.isalpha():
                        counters[char.lower()] +=1
                    total_characters +=1

        for char in counters.keys():
            c=counters[char]
            if c>0:
                print(f"El caracter '{char}' aparece {c} veces")

        print(f"El archivo contiene {line_counter} lineas.")
        print(f"El archivo contiene {total_characters} caracteres en total.")

    except IOError as e:
        print("Oops, algo salió mal: ", strerror(e.errno))