#Escriba una clase para implementar pow(x, n)


class potencia:
    def __init__(self, num, pote):
        self.num = num
        self.pote = pote

    def calcu_potencia(self):
        self.resu = pow(self.num, self.pote)

    def mostrar_resu(self):
        print(f"El resultado de la potemcia es:{self.resu}")

total = potencia (2,4)
total.calcu_potencia()
total.mostrar_resu()
