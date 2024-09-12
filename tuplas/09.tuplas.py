# Comprobar si todos los elementos de la tupla son iguales

tuple1 = (45, 45, 45, 45)
primer_valor = tuple1[0]
resultado = True

for i in tuple1:
    if i != primer_valor:
        resultado = False
        break    
print(resultado)
  