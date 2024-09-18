#Escriba una clase llamada Circle construida por un radio y dos métodos que calcularán el área y el 
# perímetro de un círculo.


import math

class circle:
    def __init__(self, radio):
        self.radio = radio 

    def area(self):
        return math.pi * self.radio**2

    def perimetro(self):
        return 2 * math.pi * self.radio
circulo = circle(6)

print(f"El area del circulo es: {circulo.area()}")
print(f"El perimetro del circulo es: {circulo.perimetro()}")