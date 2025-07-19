#Author: Sebastian Ochoa. Date: 03/03/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 9.
Diseñe un algoritmo que permita que compare dos oraciones cualquiera dadas por el usuario y que posteriormente muestre las palabras comunes en ambas oraciones.
"""

def separa_frase (frase):
    palabras=[]
    palabra_actual=''
    for caracter in frase:
        if caracter != " ":
            palabra_actual+=caracter
        else:
            if palabra_actual:
                palabras.append(palabra_actual)
                palabra_actual=''
    if palabra_actual:
        palabras.append(palabra_actual)
    return palabras

def ejer_9()->list:
    frase_1=str(input("Hola, dime la primera frase quieres comparar: "))
    frase_2=str(input("Hola, dime la segunda frase quieres comparar: "))
    palabras_1=separa_frase(frase_1)
    palabras_2=separa_frase(frase_2)
    iguales=[]
    for x in palabras_1:
        for y in palabras_2:
            if x==y:
                iguales.append(x)
    return iguales

print(ejer_9())