# -*- coding: utf-8 -*-
"""
Descripción del problema
Escriba una función que reciba un número positivo n y retorne la suma de todos los enteros positivos desde 1 hasta **n**.

Esta suma puede calcularla usando la fórmula:
"""

def suma_n_enteros_positivos(n: int)->int:
    """ Suma de los primeros n enteros positivos
    indica cuanto será la suma de cuerta cantidad de enteros positivos.
    Parámetros:
      n (int): Número entero hasta el cual se quiere calcular la suma, desde 1
    Retorno:
      int: Suma de los primeros n enteros positivos.
    """
    suma=((n*(n+1))/2)
    return int(suma)