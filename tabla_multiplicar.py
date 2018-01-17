numero_usuario = ""

while not numero_usuario.isdigit():
    numero_usuario = (input("Que numero deseas multiplicar? "))

numero_usuario = int(numero_usuario)

for numero in range(1, 11):
    resultado = numero * numero_usuario
    print("{} x {} = {}".format(numero_usuario, numero, resultado))


