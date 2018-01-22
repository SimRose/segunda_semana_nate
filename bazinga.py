lista_numeros = [1, 3, 5, 12, 20, 30, 2, 14, 15, 72]


for indice in range(len(lista_numeros)):
    if lista_numeros[indice] % 3 == 0 or lista_numeros[indice] % 5 == 0:
        if lista_numeros[indice] % 3 == 0 and lista_numeros[indice] % 5 == 0:
            valor_nuevo = "Bazinga"
        elif lista_numeros[indice] % 3 == 0:
            valor_nuevo = "Fizz"
        elif lista_numeros[indice] % 5 == 0:
            valor_nuevo = "Buzz"
        lista_numeros[indice] = valor_nuevo

print(lista_numeros)

