lista_numeros = []
dato_usuario = ""
multiplo_dos = []
multiplo_tres = []
multiplo_cinco = []
multiplo_siete = []

while dato_usuario != "FIN":
    dato_usuario = input("que numero desea agregar a la lista?(escriba fin cuando haya terminado)").upper()
    if dato_usuario.isdigit():
        lista_numeros.append(dato_usuario)
        print("Numero agregado")
        dato_usuario = ""

for indice in lista_numeros:
    dato = int(indice)
    if dato % 2 == 0:
        multiplo_dos.append(dato)
    if dato % 3 == 0:
        multiplo_tres.append(dato)
    if dato % 5 == 0:
        multiplo_cinco.append(dato)
    if dato % 7 == 0:
        multiplo_siete.append(dato)

print("multiplo_dos= {}".format(multiplo_dos))
print("multiplo_tres= {}".format(multiplo_tres))
print("multiplo_cinco= {}".format(multiplo_cinco))
print("multiplo_siete= {}".format(multiplo_siete))
