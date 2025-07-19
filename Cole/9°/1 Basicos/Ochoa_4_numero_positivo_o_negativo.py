# -*- coding: utf-8 -*-
"""
Descripción del problema:
Sara está estudiando para su evaluación de álgebra y debe hallar si el resultado de su expresión es positivo o negativo.
Realice un programa que le diga a Sara si el número que le dio es positivo o negativo retornando un texto.
"""
def postitivo_negativo(numero: float)->str:
    """
    positivo negativo
    Indica si un numero es positivo o es negativo.
    Parámetros:
        numero (float): Número a evaluar.
    Retorno:
        str: Texto que dice si el número es positivo o negativo.
    """
    resultado=''
    if numero < 0:
        resultado='el numero es negativo.'
    elif numero > 0:
        resultado='el numero es positivo.'
    else:
        resultado='el numero es 0.'
    return resultado