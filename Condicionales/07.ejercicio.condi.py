#Conversión de temperaturas. Crear un menú de opciones. 

menu = int(input("""
                         
        Eliga una opcion
        
        (1) Fahrenheit a Celsius
        (2) Fahrenheit a Kelvin
        (3) Fahrenheit a Rankine
        (4) Fahrenheit a Réaumur
        (5) Celsius a Fahrenheit
        (6) Celsius a Kelvin
        (7) Celsius a Rankine
        (8) Celsius a Réaumur
        (9) Kelvin a Celsius
        (10) Kelvin a Fahrenheit
        (11) Kelvin a Rankine
        (12) Kelvin a Réaumur
        (13) Rankine a Celsius
        (14) Rankine a Fahrenheit
        (15) Rankine a Kelvin
        (16) Rankine a Réaumur
        (17) Réaumur a Celsius
        (18) Réaumur a Fahrenheit
        (19) Réaumur a Kelvin
        (20) Réaumur a Rankine
                   
                     """))

if menu == 1:
    valorf = float(input("Ingrese el valor de los grados fahrenheit: "))
    
    celsius = (valorf - 32) / 1.8
    
    print(f"El valor en grados Celsius es: {celsius}")
    
elif menu == 2:
    valorf = float(input("Ingrese el valor de los grados fahrenheit: "))
    
    kelvin = (valorf + 459.67) / 1.8
    
    print(f"El valor en grados Kelvin es: {kelvin}")
    
elif menu == 3:
    valorf = float(input("Ingrese el valor de los grados fahrenheit: "))

    rankine = valorf + 459.67
    
    print(f"El valor en grados Rankine es: {rankine}")
    
elif menu == 4:
    valorf = float(input("Ingrese el valor de los grados fahrenheit: "))
    
    reaumur = (valorf - 32) / 2.25
    
    print(f"El valor en grados reaumur es: {reaumur}")
    
elif menu == 5:
    valorc = float(input("Ingrese el valor de los grados Celsius: "))
    
    fahrenheit = valorc * 1.8 + 32
    
    print(f"El valor en grados fahrenheit es: {fahrenheit}")
    
elif menu == 6:
    valorc = float(input("Ingrese el valor de los grados Celsius: "))
    
    kelvin = valorc + 273.15
    
    print(f"El valor en grados Kelvin es: {kelvin}")
    
elif menu == 7:
    valorc = float(input("Ingrese el valor de los grados Celsius: "))
    
    rankine = valorc * 1.8 + 32 + 459.67
    
    print(f"El valor en grados rankine es: {rankine}")

elif menu == 8:
    valorc = float(input("Ingrese el valor de los grados Celsius: "))
    
    reaumur = valorc * 0.8 
    
    print(f"El valor en grados reaumur es: {reaumur}")

elif menu == 9:
    valork = float(input("Ingrese el valor de los grados Kelvin: "))
    
    celsius = valork - 273.15
    
    print(f"El valor en grados Celsius es: {celsius}")
    
elif menu == 10:
    valork = float(input("Ingrese el valor de los grados Kelvin: "))
    
    fahrenheit = valork * 1.8 - 459.67
    
    print(f"El valor en grados Fahrenheit es: {fahrenheit}")
    
elif menu == 11:
    valork = float(input("Ingrese el valor de los grados Kelvin: "))
    
    rankine = valork * 1.8
    
    print(f"El valor en grados Rankine es: {rankine}")
    
elif menu == 12:
    valork = float(input("Ingrese el valor de los grados Kelvin: "))
    
    reaumur = (valork - 273.15) * 0.8  
    
    print(f"El valor en grados Reaumur es: {reaumur}")

elif menu == 13:
    valorra = float(input("Ingrese el valor de los grados Rankine : "))
    
    celsius = (valorra - 32 - 459.67) / 1.8
    
    print(f"El valor en grados Celsius es: {celsius}")
    
elif menu == 14:
    valorra = float(input("Ingrese el valor de los grados Rankine : "))
    
    fahrenheit = valorra - 459.67
    
    print(f"El valor en grados Fahrenheit es: {fahrenheit}")
    
elif menu == 15:
    valorra = float(input("Ingrese el valor de los grados Rankine : "))
    
    kelvin = valorra / 1.8
    
    print(f"El valor en grados Kelvin es: {kelvin}")
    
elif menu == 16:
    valorra = float(input("Ingrese el valor de los grados Rankine : "))
    
    reaumur = (valorra - 32 - 459.67) / 2.25
    
    print(f"El valor en grados Reaumur es: {reaumur}")

elif menu == 17:
    valorre = float(input("Ingrese el valor de los grados Reaumur : "))
    
    celsius = valorre * 1.25
    
    print(f"El valor en grados Celsius es: {celsius}")
    
elif menu == 18:
    valorre = float(input("Ingrese el valor de los grados Reaumur : "))
    
    fahrenheit = valorre * 2.25 + 32
    
    print(f"El valor en grados fahreinheit es: {fahrenheit}")
    
elif menu == 19:
    valorre = float(input("Ingrese el valor de los grados Reaumur : "))
    
    kelvin = valorre * 1.25 + 273.15
    
    print(f"El valor en grados Kelvin es: {kelvin}")
    
elif menu == 20:
    valorre = float(input("Ingrese el valor de los grados Reaumur : "))
    
    rankine = valorre * 2.25 + 32 + 459.67
    
    print(f"El valor en grados Rankine es: {rankine}")
    
print("Fin del programa")