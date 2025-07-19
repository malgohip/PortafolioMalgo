# -*- coding: utf-8 -*-
"""
Descripción del problema:
Simón es un trabajador de una fabrica, el cual debe de revisar que los valores de presion de una maquina permanezcan entre 1 y 10 atm, de lo contrario la producción se detendrá y la maquinaria se dañará.

Realiza un programa el cual permita a Simón recibiendo el valor de la presión determinar si esta entre los valores apropiados y retorne un texto que así lo indique.
"""

def rango_1_10(valor: float)->str:
    """
    Rango 1 10
    Indica si un número se encuentra en el rango del 1 al 10
    Parámetros:
        valor (int): Número a confirmar su valor.
    Retorno:
        str: Texto que indica si se encuentra en el rango.
    """
    respuesta='El número no se encuentra en el rango'
    if 1 <= valor <= 10:
        respuesta='El número se encuentra en el rango'
    return respuesta