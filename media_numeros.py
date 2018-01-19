numero_usuario = ""
lista_numeros = []

while not numero_usuario == "FIN":
    numero_usuario = input("Introduce el numero que deseas agregar:(escribe FIN para terminar)").upper()
    if numero_usuario.isdigit():
        lista_numeros.append(int(numero_usuario))
        numero_usuario = ""

suma_numeros = 0

for numero in lista_numeros:
    suma_numeros += numero

media_numeros = suma_numeros / len(lista_numeros)

print("media = {}".format(media_numeros))