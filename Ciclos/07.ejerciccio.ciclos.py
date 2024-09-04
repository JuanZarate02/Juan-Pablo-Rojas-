#Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número. El patrón como:


fil = 5

for i in range(1, fil + 1):
    for j in range(1, i + 1):
        print(j, end= "")
    print()