#Escriba una función que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista. 

def elemento_unico (lista):
    elementos_unicos = []

    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
    return elementos_unicos
lista = [1, 1, 2, 3, 4, 5, 5, 6]
elementos_unicos = elemento_unico(lista)
print(elementos_unicos)
