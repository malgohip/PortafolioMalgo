#Author: Sebastian Ochoa. Date: 02/29/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 2.

Diseñe un código que permita crear una lista de palabras (digitadas en letra minúscula y sin acentos) del tamaño deseado por el usuario. El programa debe retornar  las palabras de la lista que son de longitud por lo menos 4 y que tienen por lo menos tres vocales (distintas o repetidas).
"""

def ejer_2()->str:
    tamaño=int(input("Hola, dime que tantas palabras quieres en tu lista: "))
    cont=0
    lst=[]
    while cont < tamaño:
        palabra=str(input("Dime la palabra para guardar en la lista (en minuscula y sin acentos): "))
        lst.append(palabra)
        cont+=1
    vocales=["a","e","i","o","u"]
    validas=[]
    for x in lst:
        cant_vocales=0
        for y in vocales:
            for z in x:
                if z == y:
                    cant_vocales+=1
        if len(x) >= 4 and cant_vocales >= 3:
            validas.append(x)
    return validas

print(ejer_2())