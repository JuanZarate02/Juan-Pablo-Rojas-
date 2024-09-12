#Escriba una función que tome un número como parámetro y verifique que el número sea primo o no. Un número primo 
# (o primo) es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y sí mismo.

def num_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("El numero no es primo")
            return False
    print("El numero es primo")
    return True
num_primo(180)   

