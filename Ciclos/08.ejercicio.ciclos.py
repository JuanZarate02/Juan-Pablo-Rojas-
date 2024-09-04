#Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1.


x = 4
z = 1
for i in range(x):
    print(' ' * (x - i - 1), end='')
    for j in range(i + 1):
        print(z, end=' ')
        z += 1
    print()