#Escriba un programa para mostrar un patrón como Z con asteriscos

fil = 8

for i in range(fil):
    print('*', end='')
print()

for i in range(1, fil - 1):
    for j in range(fil - i - 1):
        print(' ', end='')
    print('*')

for i in range(fil):
    print('*', end='')
print() 