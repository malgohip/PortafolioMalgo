#Author: Sebastian Ochoa. Date: 08/01/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 1

Diseñe un programa que permita calcular la suma de las distancias entre los vértices de una cadena (camino) 
poligonal (https://es.wikipedia.org/wiki/Cadena_poligonal).

    * Las coordenadas de los puntos del camino las da el usuario, en el orden en que se recorre el camino. Las 
    coordenadas deben guardarse en una lista.

    * La función que calcula la distancia entre dos puntos de un plano debe ser de tipo lambda.

    * La función que calcula la distancia total del camino debe definirse usando el  comando `reduce` del cálculo 
    lambda.
"""

from functools import reduce
from math import sqrt

print("Hola, hoy te ayudaré a calcular la suma de las distancias de una cadena polional.")
n=int(input("Para iniciar, dime la cantidad de puntos que tendrá tu cadena: "))
coordenadas=[]
for i in range(1,n+1):
    cord_x=float(input(f"Dime la componente en x del punto {i}: "))
    cord_y=float(input(f"Dime la componente en y del punto {i}: "))
    cord=(cord_x,cord_y)
    coordenadas.append(cord)

distancia = lambda a, b: round(sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2), 2)

puntos_seguidos=[]
for i in range(0,len(coordenadas)-1):
    puntos_seguidos.append((coordenadas[i], coordenadas[i + 1]))

distancias = list(map(lambda p: distancia(p[0], p[1]), puntos_seguidos))

suma = reduce(lambda x,y : x + y,distancias)

print(f"Las distancias entre los puntos de la lista {coordenadas} son {distancias} (aproximados) y la suma de estas distancias es {suma}")