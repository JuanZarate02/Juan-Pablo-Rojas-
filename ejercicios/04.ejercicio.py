#Programa que permita calcular la edad de una persona conociendo el año actual y el usuario digita su año de nacimiento.

año_actual = int(input("Ingrese el año actual: "))
año_nacimiento = int(input("Ingrese el año de nacimiento: "))

edad = año_actual - año_nacimiento

print(f"la edad es: {edad}")