#Author: Sebastian Ochoa. Date: 08/06/2024
# -*- coding: utf-8 -*-

"""
1. Ejercicio

* Construya ucódigo que le solicite al usuario una colección de coordenadas de puntos del plano que debe 
guardarse en una lista $L$.  
* Suponga que el usuario da las coordenadas de un par de puntos  $A$ y $B$ adicionales del plano. El código 
  debe tener una función tipo lambda que permita calcular la distancia entre cada uno de los puntos adicionales  
  dados por el usuario y cada uno de los puntos de la lista $L$.
* Las distancias para cada punto $A$ y $B$  deben guardarse en un par de listas $LA$ y $LB$.
* El código debe tener una función tipo `lambda`  la suma de las distancias para cada lista  $LA$ y $LB$.
* El código debe indicar para cuál punto $A$ o $B$ la suma de la distancias es máxima.
"""

from functools import reduce
from math import sqrt

print("Hola, hoy te ayudaré a calcular la suma de las distancias de una lista de coordenadas y 2 puntos dados por ti.")
n=int(input("Para iniciar, dime la cantidad de puntos que tendrá la lista de coordenadas: "))
coordenadas=[]
for i in range(1,n+1):
    cord_x=float(input(f"Dime la componente en x del punto {i}: "))
    cord_y=float(input(f"Dime la componente en y del punto {i}: "))
    cord=(cord_x,cord_y)
    coordenadas.append(cord)

print("Perfecto, ahora necesito los componentes de los 2 puntos que me vas a dar.")
comp_x_a=float(input("Dime la componente en x del primer punto: "))
comp_y_a=float(input("Dime la componente en y del primer punto: "))
A=(comp_x_a,comp_y_a)
comp_x_b=float(input("Dime la componente en x del segundo punto: "))
comp_y_b=float(input("Dime la componente en y del segundo punto: "))
B=(comp_x_b,comp_y_b)

def distancia (a:tuple):
    return round(sqrt((a[0]-A[0])**2+(a[1]-A[1])**2),2)
LA=list(map(distancia,coordenadas))

def distancia (a:tuple):
    return round(sqrt((a[0]-B[0])**2+(a[1]-B[1])**2),2)
LB=list(map(distancia,coordenadas))

SLA = reduce(lambda x,y : x + y,LA)
SLB = reduce(lambda x,y : x + y,LB)

if SLA > SLB:
    print(f"Las distancias entre los puntos de la lista {coordenadas} y los puntos {A} y {B} son {LA} y {LB} (aproximados) respectivamente y de estas para el punto {A} la suma de sus distancias con respecto a {coordenadas} es máxima.")
elif SLA < SLB:
    print(f"Las distancias entre los puntos de la lista {coordenadas} y los puntos {A} y {B} son {LA} y {LB} (aproximados) respectivamente y de estas para el punto {B} la suma de sus distancias con respecto a {coordenadas} es máxima.")
else:
    print(f"Las distancias entre los puntos de la lista {coordenadas} y los puntos {A} y {B} son {LA} y {LB} (aproximados) respectivamente y de estas la suma de las distancias con respecto a {coordenadas} tanto para {A} como para {B} tienen el mismo valor.")