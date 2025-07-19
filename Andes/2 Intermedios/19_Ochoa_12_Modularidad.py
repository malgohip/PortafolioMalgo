# -*- coding: utf-8 -*-
"""
Descripcion del problema
Escriba una función que reciba dos números enteros n y d , y determine si n es divisible por 2d, n es divisible por d, o  no es divisible ni por d  ni por 2d.

Recuerde que ningún número es divisible por 0  e intentarlo producirá un error.
"""
def es_divisible (n: int, d: int)->int:
  """
  es divisible
  Indica si un numero es divisible por el doble del otro, solo por el o por ninguno.
  Parametros:
    n (int): un numero entero.
    d (int): un número entero.
  Retorno:
    int: Si el número n es divisible por 2d, retorna 2. Si el número n es divisible entre d pero no entre 2d, retorna 1. De lo contrario, retorna 0.
  """
  respuesta=0
  if n%(2*d)==0:
    respuesta=2
  elif n%d==0:
    respuesta=1
  return respuesta