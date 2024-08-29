#Solicitar número al usuario y determinar si es par, impar o es cero
numero = int(input("Ingresa un número: "))

if numero == 0:
    print("El numero es cero.")
elif numero % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")
print("fin del programa")