#El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico se calcula con la fórmula:
genero = int(input("""
Elija el numero de su genero 
(1) Mujer 
(2) Hombre 
            """))
edad = int(input("ingrese su edad"))

if genero == 1:
    pulsaciones = (220 - edad) / 10
elif genero == 2:
    pulsaciones = (210 - edad) / 10
else:
    print("ingrese un numero valido")

print(f"su numero de pulsaciones es: {pulsaciones}")