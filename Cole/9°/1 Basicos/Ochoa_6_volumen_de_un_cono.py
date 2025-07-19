# -*- coding: utf-8 -*-
"""
Descripción del problema:
Antonio salio al cine con su novia, Susana, y cuando iban a entrar al cine les sirvieron sus crispetas en un cono de papel. Susana quedo con la duda de que volumen de crispetas comerán.

Realiza un programa el cual al recibir el radio y la altura del cono sea capaz de definir su volumen.
"""

import math as mt

def volumen_cono(radio: float, altura: float)->float:
    """
    Volumen cono
    Indica cuanto sería el volumen de un cono.
    Parámetros:
        radio (float): Medida del radio del cono.
        altura (float): Medida del altura del cono.
    Retorno:
        float: Valor de el volumen que posee el cono.
    """
    volumen=(mt.pi*(radio**2)*(altura))/3
    return round(volumen,2)