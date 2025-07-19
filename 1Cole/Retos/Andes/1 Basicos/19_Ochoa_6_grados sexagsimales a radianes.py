import math
# -*- coding: utf-8 -*-
"""
Descripción del problema
En geometría, la temperatura se mide en grados sexagesimales.
Cree una función que reciba como parámetro el número de grados sexagesimales a convertir, y retorne los grados en radianes (redondeados a un decimal).
"""


def grados_a_radianes(grados: float)->float:
    """grados a radianes
    Indica cuantos radianes son los grados grados sexagesimales dados.
    Parámetros:
      Grados (float): Cantidad de grados a convertir.
    Retorno:
      float: Cantidad de radianes (redondeado a un decimal).
    """
    radianes=((grados)*(math.pi/180))
    return round(radianes,1)