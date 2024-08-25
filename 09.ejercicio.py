# Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. 
# Debe tener como entradas el valor unitario, 
# la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.

valor_producto = int(input("Ingrese el valor del producto: "))
cantidad_producto = int(input("Ingrese cuantos producto comprara: "))

valor_venta_total = valor_producto * cantidad_producto
iva = valor_venta_total * 0.16

valor_final = valor_venta_total + iva

print(f"El valor total de los productos es: {valor_venta_total} ")
print(f"El valor del IVA es: {iva} ")
print(f"El valor final es: {valor_final} ")