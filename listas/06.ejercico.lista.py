#Dada una lista de números. Escribe un programa para convertir cada elemento de una lista en su cuadrado. 
# Ejemplo dado: numbers = [1, 2, 3, 4, 5, 6, 7]Resultado esperado: numbers = [1, 4, 9, 16, 25, 36, 49]

list_numb = [1, 2, 3, 4, 5, 6, 7]
cuadrados =[]
for i in list_numb:
    cuadrados.append (i **2)
print(cuadrados)
