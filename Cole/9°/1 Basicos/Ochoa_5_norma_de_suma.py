# -*- coding: utf-8 -*-
"""
Descripción del problema:
Estando en clase de matematicas, Juliana se encuentra con un problema el cual quiere resolver rapidamente.
El problema es:
Se tienen 3 números diferentes, diga si cualquiera de los 3 es la suma de los otros 2.

Genera un programa el cual recibiendo como parametros los 3 números, devuelva: "La norma se cumple" si con cualquiera de los numeros se cumple la norma, o "La  norma no se cumple si esto no sucede".
"""
def norma_suma(numero_1: int, numero_2: int, numero_3: int)->str:
    """
    Norma de la suma
    Indica si uno de los numeros es la suma de los otros 2.
    Parámetros:
        numero_1 (int): Primer número a evaluar si es suma de los otros.
        numero_2 (int): Segundo número a evaluar si es suma de los otros.
        numero_3 (int): Tercer número a evaluar si es suma de los otros.
    Retorno:
        str: Texto que dice si la norma se cumple con cualquiera de los números.
    """
    respuesta='La norma no se cumple'
    if numero_1+numero_2==numero_3 or numero_1+numero_3==numero_2 or numero_2+numero_3==numero_1:
        respuesta='la norma se cumple'
    return respuesta
