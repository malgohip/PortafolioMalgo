# -*- coding: utf-8 -*-
"""
Descripción del problema
Construya una función que reciba dos vectores (con 3 componentes cada uno) y retorne un nuevo vector que sea la suma de los dos vectores recibidos. Cada vector debe recibirse como una tupla con tres valores flotantes.
"""

def suma_vectorial(vector_1:tuple,vector_2:tuple)->tuple:
    """ suma_vectorial
    Suma 2 vetores 3D.
    Parámetros:
      vector_1 (tuple): El primer vector a sumar.
      vector_2 (tuple): El segundo vector a sumar.
    Retorno:
      tuple: El vector resultado de la suma como una tupla.
    """
    x=vector_1[0]+vector_2[0]
    y=vector_1[1]+vector_2[1]
    z=vector_1[2]+vector_2[2]
    suma=(x,y,z)
    return suma