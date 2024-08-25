#Programa para calcular la distancia recorrida en un movimiento rectilíneo. 
#Recuerde x=v*t donde v es velocidad y t es tiempo. 
#Solicitar al usuario velocidad en kilómetros por hora (Km/h) y tiempo en horas (h) para obtener la distancia en kilómetros (Km).

velocidad = int(input("ingrese la velocidad en km/h: "))
horas = int(input("ingrese el tiempo en horas: "))

distancia = velocidad * horas

print(f"La distancia recorrida en kilometros es {distancia} km")