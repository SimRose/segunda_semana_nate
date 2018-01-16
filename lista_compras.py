mi_lista = []

elemento_lista = input("Que deseas agregar a la lista?(escriba FIN para cancelar)").upper()

while not elemento_lista == "FIN":
    mi_lista.append(elemento_lista)
    elemento_lista = input("Que deseas agregar a la lista?(escriba FIN para cancelar)").upper()

if len(mi_lista) > 0:
    print("Esta es la lista de las compras:")

    for item in mi_lista:
        print(str(item).capitalize())

    print("La lista ha terminado")
else:
    print("Tu lista de compras está vacía")

print("¡Hasta luego!")