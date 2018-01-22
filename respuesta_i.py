input_usuario = input("decime algo:")
vocales = ["a", "e", "i", "o", "u"]
respuesta = input_usuario

for vocal in vocales:
    respuesta = respuesta.replace(vocal, "i")

print(respuesta)