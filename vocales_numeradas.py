input_usuario = input("escribe algo: ")
lista_vocales = ["a", "e", "i", "o", "u"]
orden = 1
intento = 1
contador = 0
input_modificada = input_usuario

while intento < len(input_usuario):
    if input_modificada[contador] in lista_vocales:
        input_modificada = input_modificada.replace(input_modificada[contador], str(orden), 1)
        orden += 1
    intento += 1
    contador += 1


print(input_modificada)