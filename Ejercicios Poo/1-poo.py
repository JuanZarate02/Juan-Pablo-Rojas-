import datetime

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

    def pico_y_placa(self, fecha=None):

        if fecha is None:
            fecha = datetime.date.today()

        ultimo_digito = int(self.placa[-1])
        dia_semana = fecha.weekday()

        if 0 <= dia_semana <= 4:
            if dia_semana % 2 == 0:
                return ultimo_digito % 2 == 0
            else:
                return ultimo_digito % 2 != 0
        else:
            return False 

carro = Vehiculo("ABF129")

print("Hoy:", carro.pico_y_placa())

fecha_especifica = datetime.date(2024, 9, 18)
print("18 de septiembre de 2024:", carro.pico_y_placa(fecha_especifica))