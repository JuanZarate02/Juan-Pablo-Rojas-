#Eliminar cadenas vacías de la lista de cadenas. Ejemplo dado: list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Resultado esperado: ["Mike", "Emma", "Kelly", "Brad"]

list_nom = ["Mike", "", "Emma", "Kelly", "", "Brad"]

while "" in list_nom:
    list_nom.remove("")
print(list_nom)