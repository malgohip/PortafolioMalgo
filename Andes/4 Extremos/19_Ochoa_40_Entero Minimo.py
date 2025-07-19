# -*- coding: utf-8 -*-
"""
Descripción del problema
Dados tres números enteros positivos 1, n y d, escribe una función que retorne x. siendo x el minimo entero positivo que es divisible por d, y que no pertenece al rango de números [f, r]. Notese que el rango incluye los valores l y r
"""

def entero_minimo(l: int, r: int, d: int)->int:
    """ Entero Mínimo
    Indica cual sería el entero minimo divisible.
    Parámetros:
      l (int): El número entero positivo que describe el número inferior del rango [l,r]
      r (int): El número entero positivo que describe el número superior del rango [l,r]
      d (int): El número entero positivo por el cual la respuesta x debe ser divisible, para ser válida.
    Retorno:
      int: El entero positivo más pequeño que cumple con ser divisible entre l número d, y no pertenece al rango de números [l,r]
    """
    x=d
    if not x < l or x > r:
      x = ((r//d)+1)*d
    return x

