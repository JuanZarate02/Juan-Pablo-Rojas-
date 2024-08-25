#Solicitar al usuario una distancia en metros y transformar a km., cm. y mm.

Distancia = int(input("Ingrese la distancia en metros: "))

km = Distancia / 1000
cm = Distancia * 100
mm = Distancia * 1000 

print(f"La distancia en kilometros es: {km} km")
print(f"La distancia en centimetros es: {cm} cm")
print(f"La distancia en centimetros es: {mm} mm")
