#Escriba una función para encontrar el máximo de tres números. 

def max_num():
    if num1 > num2 and num1 > num3:
        return print(f"El numero mayor es: {num1}")
    
    elif num2 > num1 and num2 > num3:
        return print(f"El numero mayor es: {num2}")
    
    elif num3 > num1 and num3 > num2:
        return print(f"El nuemro mayor es:{num3}")
    
num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese un numero"))
num3 = int(input("Ingrese un numero"))
    
max_num()