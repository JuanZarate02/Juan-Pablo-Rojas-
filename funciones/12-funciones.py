#Escriba una función que compruebe si una cadena frase o palabra pasada es palíndromo o no. 
# Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. 


def es_palindromo(cadena):
  """Comprueba si una cadena es un palíndromo.

  Args:
    cadena: La cadena a evaluar.

  Returns:
    True si la cadena es un palíndromo, False en caso contrario.
  """

  cadena = cadena.lower().replace(" ", "")

  
  cadena_invertida = cadena[::-1]


  return cadena == cadena_invertida

palabra = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra):
  print("Es un palíndromo.")
else:
  print("No es un palíndromo.")