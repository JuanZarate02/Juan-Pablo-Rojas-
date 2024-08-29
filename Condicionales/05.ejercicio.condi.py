#Solicitar cinco (5) notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0. 
nota1 = float(input("Ingrese la primera nota (0.0 a 5.0): "))
nota2 = float(input("Ingrese la segunda nota (0.0 a 5.0): "))
nota3 = float(input("Ingrese la tercera nota (0.0 a 5.0): "))
nota4 = float(input("Ingrese la cuarta nota (0.0 a 5.0): "))
nota5 = float(input("Ingrese la quinta nota (0.0 a 5.0): "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f"El promedio es: {promedio}")

if promedio >= 3.0:
    print("El usuario Aprobó")
else:
    print("El usuario No aprobó")

print("Fin del programa")