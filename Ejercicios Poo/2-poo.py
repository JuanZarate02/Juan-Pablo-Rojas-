#Escriba una clase llamada Rectangle construida por una longitud y anchura y un método que calculará 
# el área de un rectángulo


class rectangle:
    def __init__(self):
        self.longitud = float(input("Ingrese nuemro para la longitud "))
        self.anchura = float(input("Ingrese numero para anchura "))

    def calcular_area(self):
        area = self.longitud * self.anchura
        print("El área del rectangle es:", area)

recta = rectangle()
recta.calcular_area()
