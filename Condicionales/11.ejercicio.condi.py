#El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado
pizza = int(input("ingrese el tamaño deseado de la pizza"))
adicional = int(input("ingrese el numero de ingredientes adicionales"))

if pizza == 1:
    precio = 15000
elif pizza == 2:
    precio = 24000
elif pizza == 3:
    precio = 36000
else:
    print("ingrese un tamalo de pizza valido")

precio_adicional = adicional * 4000
precio_total = precio + precio_adicional

print(f"el precio a pagar es: {precio_total}")
