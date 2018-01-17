
lista_numeros = []
numero_a_agregar = ""

while len(lista_numeros) < 10:
    while not numero_a_agregar.isdigit():
        numero_a_agregar = input("Que numero desea agregar a la lista?")
    lista_numeros.append(int(numero_a_agregar))
    print("Numero agregado")
    numero_a_agregar = ""

numero_grande = lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_grande:
        numero_grande = numero

print("El numero mas grande es el {}".format(numero_grande))



