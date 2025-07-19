# -*- coding: utf-8 -*-
"""
Descripción del problema
Cree una función que recibe 3 enteros y retorna una cadena con los números ordenados, de esta forma: “mayor, intermedio, menor” (sin espacios).

Ayuda: Puede hacer uso de las funciones max y min.
"""

def ordenar_enteros(a: int, b: int, c: int)->str:
    """ Ordenar 3 enteros
    Ordena 3 enteros dados de mayor a menor.
    Parámetros:
      a (int): El primero de los enteros a ordenar
      b (int): El segundo de los enteros a ordenar
      c (int): El tercero de los enteros a ordenar
    Retorno:
      str: Cadena de caracteres con los enteros ordenados de  mayor a menor, separados por coma
    """
    n_mayor=max(a,b,c)
    n_menor=min(a,b,c)
    n_medio=(a+b+c)-n_mayor-n_menor
    orden=str((n_mayor,n_medio,n_menor))
    return orden