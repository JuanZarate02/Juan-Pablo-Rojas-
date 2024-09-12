#Escriba una función para sumar todos los números de una lista. Lista de muestras: (8, 2, 3, 0, 7)Resultado esperado: 20.

def num ():
    
    num =  [8, 2, 3, 0, 7]
    suma = 0
    for i in num:
        suma += i
    print(suma, end="")
num()