#Escriba una función que acepte una cadena y calcule el número de letras mayúsculas y minúsculas

def mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 1
    for letra in cadena:
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1
    return mayusculas, minusculas
cadena = input("Ingrese una palabra")
resu = mayusculas_minusculas(cadena)
print(f"Mayúsculas: {resu [0]}")
print(f"Minúsculas: {resu [1]}")



    

