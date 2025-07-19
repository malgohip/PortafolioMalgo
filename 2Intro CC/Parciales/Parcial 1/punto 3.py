#Author: Sebastian Ochoa. Date: 03/05/2024
# -*- coding: utf-8 -*-

"""Ejercicio 3.(20 Ptos.)
Diseñe un algoritmo que compare dos oraciones cualesquiera dadas por el usuario y que posteriormente muestre las palabras comunes en ambas oraciones sobre una lista. Por ejemplo, si las oraciones son:
* "El perro come pan y toma leche"
* "El gato come carne y toma leche"
el programa debe reportar ["El","come","y","toma","leche"].
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

def ejer_3():
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


print(ejer_3())