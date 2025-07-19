# -*- coding: utf-8 -*-
"""
Descripción del problema
Dada una matriz cuadrada, escriba una función que calcule la suma de los elementos que están en alguna de sus dos diagonales. Se garantiza que todos los valores de la matriz son enteros. La diagonal que se pide calcular está dada por otro parámetro booleano, diagonal_mayor, que es True si se quiere la diagonal principal o False de lo contrario. Recuerde que la diagonal principal empieza en la esquina superior izquierda de la matriz y termina en la esquina inferior derecha.
"""

def calcular_suma_diagonal(diagonal_mayor: bool, matriz: list)->int:
    """ calcular suma diagonal
    Suma las diagonal mayor de una matriz.
    Parámetros:
      diagonal_mayor (bool): bool que indica a cual de las diagonales se debe calcularle la suma. Si es True, se quiere calcular la suma de la diagonal mayor.
      matriz (list): Lista de listas, representa la matriz cuadrada sobre la cual se quiere calcular la suma de alguna de sus diagonales. Todos los elementos de cada una de sus listas son enteros.
    Retorno:
      int: Entero con la suma acumulada sobre la diagonal solicitada de la matriz cuadrada que llega por parámetro.
    """
    suma = 0
    n = len(matriz)
    for x in range(n):
        if diagonal_mayor:
            suma += matriz[x][x]
        else:
            suma += matriz[x][n-x-1]
    return suma