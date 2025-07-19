# -*- coding: utf-8 -*-
"""
Descripción del problema
Cree una función que reciba un nombre y un entero, y retorne la cadena 'Hola' 
seguida del nombre recibido por parámetro, pero con la letra 'o' repetida tantasveces como indique el entero recibido, así como la letra 'a' la mitad de las veces que la 'o' (si la mitad no es exacta, se debe tomar la parte entera).

Por ejemplo, si se reciben como parámetros 'Egan' y 5, la cadena a retornar será 'Hooooolaa Egan'
"""

def saludar_repetidas_veces(nombre: str, veces: int)->str:
  """ Saludo prolongado
  Indica como quedaria un saludo prologando sus vocales.
  Parámetros:
  nombre (str): Nombre a incluir en el saludo
  veces (int): Cantidad de veces a repetir las letras
  Retorno:
    str: Cadena con el saludo con letras repetidas
  """
  saludo=('H'+('o'*veces)+'l'+('a'*(veces//2))+' '+nombre)
  return saludo