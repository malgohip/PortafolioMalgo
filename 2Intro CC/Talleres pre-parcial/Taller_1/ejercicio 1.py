#Author: Sebastian Ochoa. Date: 02/29/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 1.


Diseñe un programa que permita:

(A) Crear dos listas tan larga como se quiera conformada por conjuntos.

(B) El programa debe usar la lista para crear cuatro conjuntos A,  B , C y D que contengan,   la unión unión y la intersección respectivas de cada lista y posterioremente calcule la diferencia simétrica de estos dos conjuntos. El programa  debe reportar:

*   Las listas ingresadas
*   El conjunto unión A de la primera lista.
*   El conjunto intersección B de la primera lista.
*   El conjunto unión C de la segunda lista.
*   El conjunto intersección D de la segunda lista.
*   El conjunto diferencia simétrica E =(A-C) \cup (C-A).
"""

def crear_lista(cant: int)->list:
    cont=0
    lista=[]
    while cont < cant:
        valores=int(input("Dime el número de valores del conjunto: "))
        conjunto=[]
        for x in range(0,valores):
            valor=int(input("Dime el valor para el conjunto: "))
            conjunto.append(valor)
        conjunto=set(conjunto)
        lista.append(conjunto)
        cont+=1
    return lista

def union(lst: list)->set:
    union=[]
    union=set(union)
    for x in lst:
        union=union|x
    return union

def interseccion (lst: list)->set:
    interseccion=union(lst)
    for x in lst:
        interseccion=interseccion&x
    return interseccion

def ejer_1 ()->str:
    cant_1=int(input("Dime que cantidad de conjuntos deseas en la lista 1: "))
    lista_1=crear_lista(cant_1)
    cant_2=int(input("Dime que cantidad de conjuntos deseas en la lista 2: "))
    lista_2=crear_lista(cant_2)
    A=union(lista_1)
    B=interseccion(lista_1)
    C=union(lista_2)
    D=interseccion(lista_2)
    E=A^C

    return f"Las listas dadas por el usuario son {lista_1} y {lista_2}, la union de la primera lista es A={A}, la interseccion de la primera lista es B={B} la union de la segunda lista es C={C}, la interseccion de la segunda lista es D={D} y la diferencia simetrica entre A y C es E={E}"

print(ejer_1())