#Author: Sebastian Ochoa. Date: 08/05/2024
# -*- coding: utf-8 -*-

"""
2. Ejercicio

Construya un código que permita ingresar una colección de coordenadas de puntos del plano que debe guardarse 
en una lista.  

* Suponga que un usuario da las coordenadas de un punto  adicional.El código debe tener una función tipo lambda 
  que permita calcular las distancias entre el punto dado por el usuario y cada uno de los puntos de la lista.
* Las distancias calculadas deben guardarse en una lista.
* El código debe tener una función  que calcule la distancia mínima de la lista anterior.
* El código debe indicar las coordenadas del punto más próximo al punto dado por el usuario.
"""

from math import sqrt

def minima(dist: list):
    min=10000000000000000000000000000
    for i in dist:
        if min > i:
            min=i
    return min

print("Hola, hoy te ayudaré a calcular las distancias de una lista de puntos con un punto adicional, de estas calcular cual es la menor de ellas y las cordenadas del punto más proximo al ingresado")
n=int(input("Para iniciar, dime la cantidad de puntos que tendrá la lista inicial: "))
puntos=[]
for i in range(1,n+1):
    comp_x=float(input(f"Dime la componente en x del punto {i}: "))
    comp_y=float(input(f"Dime la componente en y del punto {i}: "))
    cord=(comp_x,comp_y)
    puntos.append(cord)

print("\nExcelente, ahora vamos con el punto nuevo")
comp_x=float(input("\nDime la componente en x del nuevo punto: "))
comp_y=float(input("Dime la componente en y del nuevo punto: "))
punto=(comp_x,comp_y)

def distancia (a:tuple):
    return round(sqrt((a[0]-punto[0])**2+(a[1]-punto[1])**2),2)
distancias=list(map(distancia,puntos))

menor=minima(distancias)
prox=puntos[distancias.index(menor)]
print(f"Las distancias entre los puntos de la lista {puntos} y el punto {punto} son {distancias} (aproximados) y de estas la menor distancia es {menor} por lo tanto el punto más proximo a {punto} es {prox}.")