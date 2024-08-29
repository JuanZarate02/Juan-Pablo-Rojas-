#Crear un programa con un menú de opciones, que permita calcular las áreas de figuras geométricas que se muestran a continuación.

menu = int(input("""
        Eliga una opcion
        
        (1) Rectangulo
        (2) Cuadrado
        (3) Paralelogramo
        (4) Rombo
        (5) Trapecio
        (6) Triangulo
        (7) Triangulo Equilatero
        (8) Triangulo Rectangulo
        (9) Poligono Regular
                     
                     """))

if menu == 1:
        lado1 = float(input("Ingrese el valor del primer lado: "))
        lado2 = float(input("Ingrese el valor del segundo lado: "))
        
        area_rectangulo = lado1 * lado2
        
        print(f"El area del Rectangulo es: {area_rectangulo}")
        
elif menu == 2:
    lado_cuadrado = float(input("Ingrese el valor del lado: "))
        
    area_cuadarado = lado_cuadrado**2
        
    print(f"El area del Cuadrado es: {area_cuadarado}")

elif menu == 3:
        base = float(input("Ingrese el valor de la base: "))
        altura = float(input("Ingrese el valor de la altura: "))
        
        area_paralelogramo = base * altura
        
        print(f"El area del paralelogramo es: {area_paralelogramo}") 

elif menu == 4:
        diagonal1 = float(input("Ingrese el valor de la primera diagonal: "))
        diagonal2 = float(input("Ingrese el valor de la segunda diagonal: "))
        
        area_rombo = (diagonal1 * diagonal2) / 2
        
        print(f"El area del Rombo es: {area_rombo}")

elif menu == 5:
        base_mayor = float(input("Ingrese el valor de la base mayor: "))
        base_menor = float(input("Ingrese el valor de la base menor: "))
        altura = float(input("Ingrese el valor de la altura: "))
        
        area_trapecio = ((base_mayor + base_menor) * altura) / 2
        
        print(f"El area del Trapecio es: {area_trapecio}")
        
elif menu == 6:
        base = float(input("Ingrese el valor de la base: "))
        altura = float(input("Ingrese el valor de la altura: "))
        
        area_triangulo = (base * altura) / 2
        
        print(f"El area del Triangulo es: {area_triangulo}")

elif menu == 7:
        lado = float(input("Ingrese el valor del lado: "))
        
        area_triangulo_equilatero = ((3**0.5) / 4) * (lado **2)
        
        print(f"El area del Triangulo Equilatero es: {area_triangulo_equilatero}")  

elif menu == 8:
        cateto1 = float(input("Ingrese el valor del primer cateto: "))
        cateto2 = float(input("Ingrese el valor del segundo cateto: "))
        
        area_triangulo_rectangulo = (cateto1 * cateto2) / 2
        
        print(f"El area del Triangulo Rectangulo es: {area_triangulo_rectangulo}")      

elif menu == 9:
        perimetro = float(input("Ingrese el valor del perimetro: "))
        apotema = float(input("Ingrese el valor de la apotema: "))
        

        area_poligono = (perimetro * apotema) / 2
        
        print(f"El area del Poligono Regular es: {area_poligono}")      

print("Fin del programa")
