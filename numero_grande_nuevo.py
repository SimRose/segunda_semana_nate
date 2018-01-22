lista_numeros = [12, 231, 543, 34, 46, 1, 5]
numero_grande = lista_numeros[0]

for indice in range(len(lista_numeros)):
    if lista_numeros[indice] > numero_grande:
        numero_grande = lista_numeros[indice]

print(numero_grande)
