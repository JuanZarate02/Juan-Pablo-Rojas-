#Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente. 
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if (numero1 <= numero2) and (numero1 <= numero3):
    menor = numero1
    if numero2 <= numero3:
        medio = numero2
        mayor = numero3
    else:
        medio = numero3
        mayor = numero2
elif (numero2 <= numero1) and (numero2 <= numero3):
    menor = numero2
    if numero1 <= numero3:
        medio = numero1
        mayor = numero3
    else:
        medio = numero3
        mayor = numero1
else:
    menor = numero3
    if numero1 <= numero2:
        medio = numero1
        mayor = numero2
    else:
        medio = numero2
        mayor = numero1

print(f"Números en orden ascendente: {menor}, {medio}, {mayor}")

print(f"Números en orden descendente: {mayor}, {medio}, {menor}")
print("fin del programa")
