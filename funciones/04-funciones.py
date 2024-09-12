#Escriba una función para multiplicar todos los números de una lista. Lista de muestra: (8, 2, 3, -1, 7)Resultado esperado: -336


def num ():
    
    num =  [8, 2, 3, -1, 7]
    multi = 1
    for i in num:
        multi *= i
    print(multi, end="")
num()