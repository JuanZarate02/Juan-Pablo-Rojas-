#Programa que permita ingresar 5 números y calcular el promedio.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))
num5 = int(input("Ingrese el quinto número: "))

suma = num1 + num2 + num3 + num4 + num5
promedio = suma / 5

print(f"El promedio de los numeros ingresados es: {promedio}")