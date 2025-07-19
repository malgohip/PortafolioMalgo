#Author: Sebastian Ochoa. Date: 03/05/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 4.(20 Ptos)
Diseñe un programa que cuente el número de vocales (incluyendo vocales tildadas) y de consonantes presentes en cualquier oración que un  usuario le suministre al programa.
El programa debe recibir la oración y mostrar un título que diga:

“El número de vocales en la oración es __ y el de consonantes es ___.”
"""

def ejer_4():
    frase=str(input("Hola, dime que frase quieres analizar (en minuscula): "))
    vocales=["a","á","e","é","i","í","o","ó","u","ú"]
    cant_vocales=0
    cantidad_espacios=0
    for x in frase:
        if x == " ":
            cantidad_espacios+=1
        else:
            for y in vocales:
                if x == y:
                    cant_vocales+=1
    cant_consonantes=len(frase)-(cant_vocales+cantidad_espacios)

    return f"El número de vocales en la oración es {cant_vocales} y el de consonantes es {cant_consonantes}"


print(ejer_4())