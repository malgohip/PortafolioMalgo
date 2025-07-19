# -*- coding: utf-8 -*-
"""
Descripción del problema
La distancia Manhattan es una medida que alude al diseño de las calles de Manhattan, donde la distancia entre dos puntos no está dada por la línea recta que une los dos puntos, ya que es muy probable que dicha recta atraviese varios inmuebles por los que no es posible transitar, sino que se calcula como la longitud de cualquier camino que una los dos puntos mediante segmentos horizontales y verticales.

Formalmente se dice que la distancia Manhattan entre dos puntos es la suma de las diferencias absolutas de sus coordenadas, lo que quiere decir que entre dos puntos  y  la distancia se calcula como .

.... ............. 

Cree una función que reciba como parámetro cuatro enteros, que indican las coordenadas de dos puntos en un plano, y calcule la distancia Manhattan entre esto
"""

def distancia_manhattan(x1: int, y1: int, x2: int, y2: int)->int:
    """
    distancia Manhattan
    Indica cuanto sería al distancia entre 2 puntos en Manhattan.
    Parámetros:
      x1 (int): Coordenada en X del primer punto
      y1 (int): Coordenada en Y del primer punto
      x2 (int): Coordenada en X del segundo punto
      y2 (int): Coordenada en Y del segundo punto
    Retorno:
      int: Distancia Manhattan entre las dos coordenadas dadas como parámetro
    """
    distancia=abs(x1-x2)+abs(y1-y2)
    return distancia