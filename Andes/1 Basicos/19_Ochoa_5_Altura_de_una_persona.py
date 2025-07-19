# -*- coding: utf-8 -*-
"""
Descripción del problema
En muchos países, la altura de una persona se mide en pies y pulgadas. Cree una función que reciba como parámetro el número de pies y el número de pulgadas que componen la altura de una persona, y retorne la altura en metros (redondeada a dos decimales).

Recuerde que:

1 pie corresponde a 12 pulgadas
1 pulgada corresponde a 2,54 centímetros.
"""


def altura_en_mts(pies: int, pulgadas: int)->float:
    """ Altura de una persona
    Da la altura de una persona en metros recibiendola en pies y pulgadas.
    Parámetros:
      pies (int): Número de pies que componen la altura de la persona
      pulgadas (int): Número de pulgadas que componen la altura de la persona
    Retorno:
      float: Altura de la persona en metros, la cual debe estar redondeada a dos cifras decimales.
    """
    pi_pu=12*pies
    pu_m=0.0254*(pulgadas+pi_pu)
    a_m=pu_m
    a_m_r=round(a_m,2)
    return a_m_r