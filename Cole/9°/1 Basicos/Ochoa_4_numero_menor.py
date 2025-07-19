# -*- coding: utf-8 -*-
"""
Descripción del problema:
El profesor Juan Esteban está evaluando dos números aleatorios y debe averiguar cuál de los dos números que le han dado es menor. 
Realice una función que retorne en texto cuál número es menor y le permita al profesor averiguar cuál de los dos números es menor.
"""
def numero_menor(numero_1: float, numero_2: float)->str:
    """
    número menor
    Indica cual de los números suministrados es el menor.
    Parámetros:
        numero_1 (float): Primer número a evaluar.
        numero_2 (float): Segundo número a evaluar.
    Retorno:
        str: Texto que dice cuál de los dos números es menor.
    """
    menor=''
    if numero_1 > numero_2:
        menor='El segundo número es menor.'
    elif numero_1 < numero_2:
        menor='El primer número es menor.'
    else:
        menor='Los dos números son iguales'
    return menor