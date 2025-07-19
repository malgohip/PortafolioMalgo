# -*- coding: utf-8 -*-
import math
"""
Descripción del problema
El volumen de un cilindro se puede calcular multiplicando el área de su base circular por su altura. Cree una función que reciba el radio de la base y la altura del cilindro, y calcule su volumen.

Retorne el resultado redondeado a un solo decimal.
"""

def volumen_cilindro(radio: float, altura: float)->float:
    """ Volumen de un cilindro
    Indica cuanto sería el volumen de u cilindro.
    Parámetros:
      radio (float): Radio de la base del cilindro
      altura (float): Altura del cilindro
    Retorno:
      float: El volumen del cilindro redondeado a un decimal
    """
    volumen=(math.pi)*(radio**2)*altura
    return round(volumen,1)