# -*- coding: utf-8 -*-
"""
Descripción del problema
Un matemático perezoso desea saber de manera sencilla si un número  x es una enésima potencia de algún otro número. Para esto ha diseñado una función que le permite resolver su problema.

Desarrolle una función que dados dos número enteros x y n, calcule si existe un número entero i que elevado a la n dé como resultado x.

Como precaución, cuando n sea 1, 0 o un número negativo, siempre se debe retornar False.
"""

def potenciador(x: int, n: int)->bool:
    """ Potenciador
    Indica si un numero es alguna potencia de otro.
    Parámetros:
      x (int): Número sospechoso como posible número elevado del número misterioso.
      n (int): Potencia a la cual se debe elevar el número misterioso.
    Retorno:
      bool: Valor booleano que indica si existe un número entero que elevado a la n, da como resultado x
    """
    re=0
    y=x**(1/n)
    if (y%1)!=0:
      re=1
    return bool(re)