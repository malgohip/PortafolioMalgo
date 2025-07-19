#Author: Sebastian Ochoa. Date: 03/01/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 5.

Diseñe un código que le permita a un usuario introducir una lista de números tan larga como quiera. El algoritmo debe calcular la suma de los números que no son divisible por 3 y por 7. El código debe tener:
* Una función que permita construir la lista de números
* Una función que permita escoger los números que no son divisibles por 3 y por 7.
* Una función que calcule la suma que se indica en el enunciado.
"""

def crear_lista()->list:
    cont=0
    lista=[]
    cant=int(input("Dime que cantidad de valores deseas en la lista: "))
    while cont < cant:
        valor=int(input("Dime el valor para la lista: "))
        lista.append(valor)
        cont+=1
    return lista

def lista_excluyente(lst: list)->list:
    excluye=list(filter(lambda x: x%3 != 0 and x%7 != 0, lst))
    return excluye

def ejer_5()->int:
    lst_1=crear_lista()
    lst_2=lista_excluyente(lst_1)
    suma=0
    for z in lst_2:
        suma+=z
    return suma 

print(ejer_5())