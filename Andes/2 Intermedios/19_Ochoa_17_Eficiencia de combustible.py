# -*- coding: utf-8 -*-
"""
Descripción del problema
En los Estados Unidos, la eficiencia de un combustible para vehículos se expresa en millas por galón (MPG). En Canadá, la eficiencia se expresa en litros por cada 100 kilómetros (L/100km).

Cree una función que permita convertir una eficiencia en MPG a L/100km.

Recuerde que una milla equivale a 1.6 kms, y un galón equivale a 3.78 litros.

El valor de retorno debe estar redondeado a dos decimales.
"""

def convertir_eficiencia_combustible(millas_por_galon: float)->float:
    """ Eficiencia de combustible
    Indica cuanto seria la eficiencia de un conbustible en km/L.
    Parámetros:
      millas_por_galon (float): Eficiencia de combustible en millas por galón
    Retorno:
      float: Eficiencia de combustible en litros por 100 km con dos decimales.
    """
    eficiencia=(1/millas_por_galon)*(1/1.6)*100*3.78
    return round(eficiencia,2)