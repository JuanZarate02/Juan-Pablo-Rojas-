#Escriba una función para comprobar si un número cae en un rango determinado. 
# Defina como parámetros rango de inicio, número y rango final.  

def num(n):
    if 0 <=  n <= 10:
        return True
    else:
        return False
    
n = int(input("Ingrese un numero"))
resu = num(n)
print(resu)
