# -*- coding: utf-8 -*-
"""
Descripción del problema
En muchos países, la temperatura se mide en grados Fahrenheit.
Cree una función que reciba como parámetro el número de grados centigrados a convertir, y retorne la temperatura en fahrenheit (redondeada a un decimal).
"""


def centigrados_a_fahrenheit(grados_centigrados: float)->float:
    """ Centígrados a Fahrenheit
    Indica cuantos grados farenheit son los grados centigrados dados.
    Parámetros:
      grados_centigrados (float): Cantidad de grados centigrados a convertir (recibe valores entre -273.15 y 5498.85).
    Retorno:
      float: Cantidad de grados farenheit (redondeado a un decimal).
    """
    grados_farenheit=(((9/5)*grados_centigrados)+32)
    return round(grados_farenheit,1)

print(centigrados_a_fahrenheit(5498.85))