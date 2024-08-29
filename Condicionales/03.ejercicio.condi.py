#Solicitar número al usuario y determinar si es negativo, positivo o cero.
numero = float(input("Ingrese un número: "))
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número es cero.")
    
print("Fin del programa")