lista_mixta = ["asda", 2, 4, "dfs", 43]
lista_numero = []
lista_str = []

for dato in lista_mixta:
    if type(dato) == int:
        lista_numero.append(dato)
    else:
        lista_str.append(dato)

print(lista_numero)
print(lista_str)