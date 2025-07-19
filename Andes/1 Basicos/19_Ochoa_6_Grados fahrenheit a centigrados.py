# -*- coding: utf-8 -*-
"""
Descripción del problema
En muchos países, la temperatura se mide en grados centígrados.
Cree una función que reciba como parámetro el número de grados Fahrenheit a convertir, y retorne la temperatura en centígrados (redondeada a un decimal).
"""


def fahrenheit_a_centigrados(grados_fahrenheit: float)->float:
    """ Centígrados a Fahrenheit
    Indica cuantos grados centigrados son los grados farenheit dados.
    Parámetros:
      grados_fahrenheit(float): Cantidad de grados fahrenheit a convertir.
    Retorno:
      float: Cantidad de grados centígrados (redondeado a un decimal).
    """
    grados_centigrados=((grados_fahrenheit-32)*(5/9))
    return round(grados_centigrados,1)
