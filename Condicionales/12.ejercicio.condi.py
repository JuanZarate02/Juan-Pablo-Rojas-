#Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos, no hay descuento
cantidad = int(input("ingrese la cantidad de productos"))
valor = float(input("ingrese el valor de los productos"))

if cantidad <= 5:
    print("no hay descuento")
elif cantidad > 5 and cantidad <= 10:
    descuento = valor * (5/100)
elif cantidad > 10:
    descuento = valor * (8/100)

valor_total = (valor - descuento) * cantidad
print(f"el valor total es {valor_total}")