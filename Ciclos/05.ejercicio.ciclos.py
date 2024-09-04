#Escriba un programa para mostrar la tabla de multiplicar de un entero dado.

n = int(input("Ingrese un numero entero"))

contador = 1

for i in range(1, 10):
    multipli = n * i
    print(multipli)