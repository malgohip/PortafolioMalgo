import math
# -*- coding: utf-8 -*-
"""
Descripción del problema
En trigonometría, los angulos se mide en radianes.
Cree una función que reciba como parámetro el número de radianes a convertir, y retorne los radianes en grados sexagesimales (redondeados a un decimal).
"""


def radianes_a_grados(radianes: float)->float:
    """Radianes a grados
    Indica cuantos grados sexagesimales son los grados radianes dados.
    Parámetros:
      Radianes (float): Cantidad de radianes a convertir.
    Retorno:
      float: Cantidad de grados sexagesimales (redondeado a un decimal).
    """
    grados=((radianes*180)/math.pi)
    return round(grados,1)