# -*- coding: utf-8 -*-
"""
Descripción del problema:
Escriba una función que reciba una cadena de caracteres y una letra. Su función debe retornar la misma cadena que recibió, pero cambiando todas las vocales por la letra que también llegó por parámetro. Por ejemplo, si la cadena original era “Hola, Mundo!” y la letra entregada fue ‘I’, el resultado debería ser “HIlI, MIndI!”.
"""

def cambio_vocales(frase: str, letra: str)->str:
  """
  cambio vocales
  Indica como quedaría una cadena de caracteres si le cambiamos sus vocales por una letra elegida.
  Parámetros:
    frase (str): Cadena de tipo string a la cual se le desea cambiar las vocales.
    letra (str): Valor de tipo string el cual remplace las vocales.
  Retorno:
    str: Cadena de tipo string que contiene la frase con las vocales cambiadas.
  """
  vocales='aeiouAEIOU'
  cambio=''
  for x in frase:
    if x in vocales:
      cambio+=letra
    else:
      cambio+=x
  return cambio

"""
Descripción del problema:
Escriba una función que reciba dos cadenas de caracteres. La función debe retornar 1 si las cadenas son idénticas, 2 si las cadenas sólo se diferencian por las mayúsculas y minúsculas, o 0 de lo contrario.
"""

def comparacion_cadenas(cadena_1: str, cadena_2: str)->int:
  """
  comparacion cadenas
  Indica si 2 cadenas son similares, iguales o diferentes.
  Parámetros:
    cadena_1 (str): Primera cadena la cual se desea comparar.
    cadena_2 (str): Segunda cadena la cual se desea comparar.
  Retorno:
    int: Valor que representa si las cadenas son iguales, solo se diferencian por mayusculas o minusculas o si son diferentes.
  """
  respuesta=0
  if cadena_1 is cadena_2:
    respuesta=1
  if cadena_1 == cadena_2:
    respuesta=2 
  return respuesta

"""
Descripción del problema:
Escriba una función que reciba dos cadenas de caracteres que sólo van a contener letras mayúsculas y minúsculas. La función debe retornar -1 si en un diccionario la primera cadena debería ir antes que la segunda, debe retornar 1 si la segunda cadena debe ir antes que la primera, o 0 si las dos cadenas son la misma (ignorando mayúsculas y minúsculas).
"""
def comparar_cadenas(cadena_1: str, cadena_2: str)->int:
  """
  comparar cadenas
  Indica cual seríea el orden de las cadenas en un diccionario.
  Parámetros:
    cadena_1 (str): Primera cadena la cual se desea comparar.
    cadena_2 (str): Segunda cadena la cual se desea comparar.
  Retorno:
    int: Valor que representa cual de las cadenas debe estar primero o si son iguales.
  """
  cadena_1_lower=cadena_1.lower()
  cadena_2_lower=cadena_2.lower()
  respuesta=0
  if cadena_1_lower < cadena_2_lower:
    respuesta = -1
  if cadena_1_lower > cadena_2_lower:
    respuesta = 1
  return respuesta

"""
Escriba una función que reciba una cadena de caracteres y cuente las palabras que aparecen en la cadena. Usted puede suponer que la cadena tendrá letras (mayúsculas y minúsculas) y espacios, pero no tendrá ningún signo de puntuación ni espacios seguidos.

Tres equipos de futbol participaron en un pequeño torneo en que jugaron entre ellos 3 partidos. Escriba una función que reciba el nombre de los tres equipos y los marcadores de los tres partidos, y que retorne una tabla con las posiciones de los equipos al finalizar el torneo. La función recibirá entonces 9 parámetros: primero los nombres de los tres equipos y luego 6 enteros con los marcadores de los 3 partidos. Cada partido ganado entregaba 3 puntos y cada partido empatado entregaba 1 punto. La tabla con el resultado del torneo tiene que ser una cadena de caracteres con la información organizada en columnas bien alineadas. Las columnas deben estar organizadas de la siguiente forma:

posición,

nombre del equipo,

puntos obtenidos,

partidos jugados,

partidos ganados,

partidos empatados,

partidos perdidos,

goles a favor,

goles en contra,

diferencia de goles

Escriba una función que, dada la altura de un edificio, retorne una cadena como en el siguiente ejemplo: “Un objeto que cae de un edificio de 30 metros tarda 2.47 segundos en llegar al piso y alcanza una velocidad de 24.25 metros por segundo.” Su programa debe usar las funciones de formato de cadenas.

Ayuda: El tiempo que tarda la caída es igual a la raíz cuadrada de dos veces la altura sobre la aceleración de la gravedad (9.8 m/s2). La velocidad que alcanza el objeto es igual al tiempo de la caída multiplicado por la aceleración de la gravedad.

Escriba una función que dados el nombre de un país, la cantidad de habitantes en millones y el Producto Interno Bruto en millones de USD, retorne una cadena como en el siguiente ejemplo: “Colombia……………..=45 millones=    336599 USD Million”. La primera columna debe estar alineada a la izquierda, debe tener 25 caracteres y ocupar los espacios vacíos con .; la segunda columna debe estar centrada, tener 25 caracteres y ocupar los espacios vacíos con *; la tercera columna debe estar alineada a la derecha, tener 10 caracteres más el espacio ocupado por USD Million y debe ocupar los espacios vacíos con espacios.

"""
