#Leer el número de llantas de una compra y mostrar el valor que debe pagarse. El almacén las vende con la siguiente política: Si se compran menos de 6 llantas, el precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000, y si se compran más de 7 llantas, el precio unitario es $180000.
llantas = int(input("ingrese el numero de llantas a comprar"))

if llantas < 6:
    precio = 240000
elif llantas >= 6 and llantas <= 7:
    precio = 221000
else:
    precio = 180000

precio_total = precio * llantas

print(f"el valor a pagar por {llantas} es de: {precio_total} ")