numero_usuario = ""
lista_numeros = []

while not numero_usuario == "FIN":
    numero_usuario = input("Introduce el numero que deseas agregar:(escribe FIN para terminar)").upper()
    if numero_usuario.isdigit():
        lista_numeros.append(numero_usuario)
        numero_usuario = ""

cantidad_numeros = 0

for numero in lista_numeros:
    cantidad_numeros += 1

print("largo_lista = {}".format(cantidad_numeros))