# Escriba un programa para mostrar n términos de número 
# natural y su suma (Fibonacci). Se le solicita al usuario 
# que ingrese el n término de la serie. Los primeros términos de
# la serie de Fibonacci son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, y así sucesivamente.


n = int(input("Ingrese un numero natural "))
suma = 0
numero1 = 0 
numero2 = 1
for i in range (n):
    print(suma)
    numero1 = numero2
    numero2 = suma
    suma = numero1 + numero2