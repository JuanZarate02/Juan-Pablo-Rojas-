#Escriba un programa para imprimir los números pares de una lista determinada.


def pares(num):
    for numero in num:
        if numero % 2 == 0:
            print(numero, "El nuemro es par")
        else:
            print(numero, "El numero es impar")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares(num)

