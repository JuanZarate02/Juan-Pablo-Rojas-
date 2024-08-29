#reporte de salud muestra una tabla diferente del índice de masa corporal IMC de una persona que se calcula con la fórmula IMC=P/(E*E) en donde P es el peso en Kg. y E es la estatura en metros. Lea un valor de P y de E, calcule el IMC y muestre su estado
peso = float(input("ingrese su peso en kg"))
estatura = float(input("ingrese si estatura en metros"))

IMC = peso / (estatura * estatura)
print(f"su imc es {IMC}")

if IMC < 18.5:
    print("usted tiene un IMC: desnutrido")
elif IMC >= 18.5 and IMC <= 25:
    print(("usted tiene un IMC: normal"))
elif IMC > 25 and IMC < 30:
    print(("usted tiene un IMC: sobrepeso"))
elif IMC > 30 and IMC < 35:
    print(("usted tiene un IMC: obesidad grado 1"))
elif IMC > 35 and IMC < 40:
    print(("usted tiene un IMC: obesidad grado 2"))
elif IMC > 40 and IMC < 50:
    print(("usted tiene un IMC: obesidad grado 3"))
elif IMC >= 50:
    print(("usted tiene un IMC: obesidad grado 4"))
