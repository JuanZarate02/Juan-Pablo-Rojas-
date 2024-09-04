#Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como


z = 5
x = 1

while z > 0:
    print('*' * x + ' ' * z)
    x += 1
    z -= 1
    
z = 4
x = 1

while z > 0:
    print('*' * z + ' ' * x)
    x += 1
    z -= 1

