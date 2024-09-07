#Escriba un programa Python para eliminar duplicados de una lista

dupli = ["1", "1", "2", "3", "4", "1", "5"]
while "1" in dupli:
    dupli.remove ("1")
print(dupli)