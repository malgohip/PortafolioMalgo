# -*- coding: utf-8 -*-
"""
Cree una función que reciba tres caracteres, que representan centenas, decenas y unidades respectivamente, y retorne el número entero que forman dichos dígitos.

Por ejemplo, si se recibe ‘9’, ‘1’, ‘4’ se debe retornar 914.
"""


def caracteres_a_entero(centenas: str, decenas: str, unidades: str)->int:
    """ Caracteres a entero
    Indica cual sería en tipo int las cadenas de caracteres dadas.
    Parámetros:
      centenas (str): Centenas del número dadas como un str (recibe valores entre 0 y 9).
      decenas (str): Decenas del número dadas como un str (recibe valores entre 0 y 9).
      unidades (str): Unidades del número dadas como un str (recibe valores entre 0 y 9).
    Retorno:
      int: Número conformado por las decenas, centenas y unidades.
    """
    numero_str=centenas+decenas+unidades
    numero=int(numero_str)
    return numero