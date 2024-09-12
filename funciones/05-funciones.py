#Escriba un programa para invertir una invertir. Cadena de ejemplo: "1234abcd" Resultado esperado: "dcba4321"


def invertir_cadena(cadena):
  return cadena[::-1]

cadena_original = "420juanp"
cadena_invertida = invertir_cadena(cadena_original)
print(cadena_invertida)