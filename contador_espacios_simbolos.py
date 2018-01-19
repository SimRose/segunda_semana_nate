frase_usuario = input("¿Que frase deseas analizar?")

espacio = " "
punto = "."
coma = ","

numero_espacios = 0
numero_puntos = 0
numero_comas = 0

for caracter in frase_usuario:
    if caracter == espacio:
        numero_espacios += 1
    elif caracter == punto:
        numero_puntos += 1
    elif caracter == coma:
        numero_comas += 1

print("Espacios: {}".format(numero_espacios))
print("Puntos: {}".format(numero_puntos))
print("Comas: {}".format(numero_comas))

