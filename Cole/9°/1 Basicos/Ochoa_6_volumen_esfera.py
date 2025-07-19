# -*- coding: utf-8 -*-
"""
Descripción del problema:
Jorge es un revisor de una fabrica de pelotas de tenis, estas deben de tener un volumen especificon para pasar por control de calidad.

Realiza un programa el cual recibiendo el radio de la pelota devuelva su volumen para ser revisado.
"""

import math as mt

def volumen_esfera(radio: float)->float:
    """
    Volumen esfera
    Indica cuanto sería el volumen de una esfera.
    Parámetros:
        radio (float): Medida del radio de la esfera.
    Retorno:
        float: Valor de el volumen que posee el esfera.
    """
    volumen=(4/3)*mt.pi*radio**3
    return round(volumen,2)