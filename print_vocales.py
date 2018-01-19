frase_usuario = input("¿De que frase desea mostrar las vocales?")

vocales = ["a", "e", "i", "o", "u"]
vocales_usuario = []

for letra in frase_usuario:
    if letra in vocales:
        vocales_usuario.append(letra)

print(vocales_usuario)

