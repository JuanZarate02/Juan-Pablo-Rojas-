#Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área. 


def regtangulo():
    if menu==1:
        a=float(input("ingrese el valor del lado a"))
        b=float(input("ingrese el valor del lado b"))
        area_regtangulo=a*b
        print(f"el area del regtangulo es:{area_regtangulo}")
def cuadrado():
    if menu==2:
        a=float(input("ingrese el valor del lado a"))
        area_cuadrado=a*a
        print(f"el area del regtangulo es:{area_cuadrado}")
def paralelogramo():
    if menu==3:
        print("paralelogramo")
        b=float(input("ingrese la base"))
        h=float(input("ingrese la altura"))
        area_paralelogramo=b*h
        print(f"el area es:{area_paralelogramo}")
def rombo():
    if menu==4:
        print("rombo")
        b=float(input("ingrese la diagonal mayor"))
        h=float(input("ingrese la diagonal menor"))
        area_rombo=(b*h)/2
        print(f"el area es:{area_rombo}")
def trapecio():
    if menu==5:
        print("trapecio")
        a=float(input("ingrese la base superor"))
        b=float(input("ingrese la base inferior"))
        h=float(input("ingrese la altura"))
        area_trapecio=((b*a)/2)*h
        print(f"el area es:{area_trapecio}")
def triangulo():
    if menu==6:
        print("triangulo")
        b=float(input("ingrese la base"))
        h=float(input("ingrese la altura"))
        area_triangulo=(b*h)/2
        print(f"el area es:{area_triangulo}")
def triangulo_equilatero():
    if menu == 7:
        print("triangulo equilatero")
        b=float(input("ingrese el valor del lado"))
        area_triangulo_equilatero=((3**0.5)/4)*(b**2)
        print(f"el area es:{area_triangulo_equilatero}")
def triangulo_regtangulo():
    if menu ==8:
        print("triangulo regtangulo")
        cateto1=float(input("ingrese cateto adyacente"))
        cateto2=float(input("ingrese cateto opuesto"))
        area_triangulo_regtangulo=(cateto1*cateto2)/2
        print(f"el area es:{area_triangulo_regtangulo}")
def poligono_regular ():
    if menu ==9:
        print("poligono regular")
        perimetro=float(input("ingrese el valor del perimetro"))
        apotema=float(input("ingrese el valor de la operacion"))
        area_poligono_regular=(perimetro*apotema)/2
        print(f"el area es:{area_poligono_regular}")
menu= int(input("""
    eliga una opcion
    (1) regtangulo
    (2) cuadrado
    (3) paralelogramo
    (4) rombo
    (5) trapecio
    (6) triangulo
    (7) triangulo equilatero
    (8) triangulo regtangulo
    (9) poligono regular
                    """))
regtangulo()
cuadrado()
paralelogramo()
rombo()
trapecio()
triangulo()
triangulo_equilatero()
triangulo_regtangulo()
poligono_regular()