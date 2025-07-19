# -*- coding: utf-8 -*-
"""
Descripción del problema:
Tarquino requiere convertir los números que le dan al sistema de escritura romano.

Escribe un programa el cual recibiendo un número del 1 al 5, retorne su notación romana.
"""

def numero_romano(numero: int)->str:
  """
  Número romano
  Indica como sería un número del 1 al 5 en romano.
  Parámetros:
    numero (int): Número el cual cambiará de notación (recibe valores del 1 al 5).
  Retorno:
    str: Letras que simbolizan  el número en cuestión.
  """
  respuesta = 'Escribe un número del 1 al 5'
  if numero == '1':
    respuesta = 'El valor del numero es I'
  elif numero == '2':
    respuesta = 'El valor del numero es II'
  elif numero == '3':
    respuesta = 'El valor del numero es III'
  elif numero == '4':
    respuesta = 'El valor del numero es IV'
  elif numero == '5':
    respuesta = 'El valor del numero es V'
  return respuesta