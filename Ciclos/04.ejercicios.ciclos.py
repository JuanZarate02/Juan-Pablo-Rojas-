#Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio


suma = 0
contador = 0

for i in range(10):
    numero = float(input("Ingrese el número"))
    suma += numero
    contador += 1

prom = suma / contador

print(f"La suma de los números es: {suma}")
print(f"El promedio de los números es: {prom}")
