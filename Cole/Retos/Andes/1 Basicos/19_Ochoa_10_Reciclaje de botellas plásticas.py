# -*- coding: utf-8 -*-
"""
Descripción del problema
Un depósito que recibe botellas plásticas para reciclaje paga 0,10USD Por cada botella de máximo 500ml, y 0.25 USD por cada botella de litro y medio o más que se lleve para reciclar.

Cree una función que reciba la cantidad de botellas de 500 ml o menos, y la cantidad de botellas de litro y medio o más a reciclar, y retorne el dinero a pagar a quien llevó las botellas.

El resultado debe tener dos decimales.
"""

def calcular_pago_botellas(cant_pequenias: int, cant_grandes: int)->float:
    """ Reciclaje de botellas plásticas
    Indica cuanto dinero se habrá de pagar en base al número de botellas plasticas pequeñas y grandes recicladas.
    Parámetros:
      cant_pequenias (int): Cantidad de botellas pequeñas entregadas
      cant_grandes (int): Cantidad de botellas grandes entregadas
    Retorno:
      float: Cantidad de dinero a pagar por las botellas plásticas para reciclaje con dos decimales.
    """
    dinero=(cant_pequenias*0.1)+(cant_grandes*0.25)
    return round(dinero,2)