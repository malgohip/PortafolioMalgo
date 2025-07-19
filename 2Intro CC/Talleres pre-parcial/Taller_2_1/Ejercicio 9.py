#Author: Sebastian Ochoa. Date: 07/30/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 9.

Se tiene una colección de coordenadas de puntos del plano que debe guardarse en una lista. Un usuario da las 
coordenadas de un punto  adicional. Se requiere un programa que permita calcular la suma de las distancias entre 
el punto adicional y cada uno de los puntos que conforman la colección.

* Debe implementarse una función tipo lambda que permita calcular las distancias entre el punto adicional y cada 
uno de los puntos de la colección.
* Las distancias calculadas deben guardarse en una lista.
* La función que calcula la suma de las distancias total debe tener como argumento una lista y debe definirse 
usando el comando reduce del cálculo lambda
"""

from functools import reduce
from math import sqrt

puntos=[(2.5, 3.75),(4.2, -1.6),(-3.8, 5.1),(0.0, 0.0),(-2.3, -4.7)]
print(f"Hola, vamos a añadir un punto en el plano cartesiano a la lista {puntos}.")
cord_x=float(input("\nDime la cordenada x del punto a añadir: \n"))
cord_y=float(input("\nDime la cordenada y del punto a añadir: \n"))
punto=(cord_x,cord_y)
def distancia (a:tuple):
    return round(sqrt((a[0]-punto[0])**2+(a[1]-punto[1])**2),2)
distancias=list(map(distancia,puntos))
suma = reduce(lambda x,y : x + y,distancias)
print(f"Las distancias entre los puntos de la lista {puntos} y el punto {punto} son {distancias} (aproximados) y la suma de estas distancias es {suma}")