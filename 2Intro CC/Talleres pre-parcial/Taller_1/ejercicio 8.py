#Author: Sebastian Ochoa. Date: 03/03/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 8.
Diseñe un algoritmo le permita a un usuario ingresar una oración  cualquiera y que posteriormente muestre las palabras que tienen tres vocales distintas. El algoritmo debe recibir la oración mediante un input, es decir, con formato string.
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

def ejer_8()->list:
    frase=str(input("Hola, dime que frase quieres analizar: "))
    vocales=["a","á","e","é","i","í","o","ó","u","ú"]
    palabras=separa_frase(frase)
    vocales_palabras=[]
    for x in palabras:
        vocales_palabra=[]
        for z in x:
            if z in vocales:
                vocales_palabra.append(z)
        vocales_palabra=set(vocales_palabra)
        vocales_palabras.append(vocales_palabra)
    validas=[]
    for x in vocales_palabras:
        if len(x) == 3:
            posi=vocales_palabras.index(x)
            validas.append(palabras[posi])
    return validas

print(ejer_8())