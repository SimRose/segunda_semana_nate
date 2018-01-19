frase_usuario = input("¿Que frase desea analizar?")

import string
mayusculas = list(string.ascii_uppercase)

numero_mayusculas = 0

for letra in frase_usuario:
    if letra in mayusculas:
        numero_mayusculas += 1

print("Mayusculas: {}".format(numero_mayusculas))