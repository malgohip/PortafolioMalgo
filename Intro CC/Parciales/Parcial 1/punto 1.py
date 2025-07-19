#Author: Sebastian Ochoa. Date: 03/05/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 1.(20 Ptos)

Diseñe un programa que permita:

(A) Crear dos listas conformadas por conjuntos y con tantos conjuntos como quiera el usuario.

(B)  El programa debe usar las listas para crear cuatro conjuntos  A ,  B  ,  C  y  D  que contengan, la unión y la intersección respectivas de cada lista y posteriormente, calcular unión de diferencias simétricas. Los resultados deben reportarse como se indica a continuación:
*   Las dos listas ingresadas.
*   El conjunto unión A de la primera lista.
*   El conjunto intersección B de la primera lista.
*   El conjunto unión C de la segunda lista.
*   El conjunto intersección D de la segunda lista.
*   El conjunto unión de diferencias simétricas F =[(A-C) \cup (C-A)]⋃[(B-D)\cup (D-B)].
"""

def crear_lista(cant):
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

def union(lst):
    union=[]
    union=set(union)
    for x in lst:
        union=union|x
    return union

def interseccion (lst):
    interseccion=union(lst)
    for x in lst:
        interseccion=interseccion&x
    return interseccion

def ejer_1 ():
    cant_1=int(input("Dime que cantidad de conjuntos deseas en la lista 1: "))
    lista_1=crear_lista(cant_1)
    cant_2=int(input("Dime que cantidad de conjuntos deseas en la lista 2: "))
    lista_2=crear_lista(cant_2)
    A=union(lista_1)
    B=interseccion(lista_1)
    C=union(lista_2)
    D=interseccion(lista_2)
    E=(A^C)|(B^D)

    return f"Las listas dadas por el usuario son {lista_1} y {lista_2}, la union de la primera lista es A={A}, la interseccion de la primera lista es B={B} la union de la segunda lista es C={C}, la interseccion de la segunda lista es D={D} y la union entre las diferencias simetrica entre (A y C) y (B y D) es E={E}"

print(ejer_1())