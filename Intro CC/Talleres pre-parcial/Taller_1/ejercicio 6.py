#Author: Sebastian Ochoa. Date: 03/01/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 6.
Diseñe un programa que solicite al usuario:

* n números enteros positivos que deberán ser ingresados uno a uno.
* El programa debe construir un conjunto con los enteros ingresados (sin hacer uso de la estructura lista).
* El programa debe mostrar en  conjuntos separados:

  * Los enteros que son divisibles por 3 o por 2, pero no por 6.
  * Los enteros que no son divisible por 3.
"""

def ejer_6()->str:
    cont=0
    cant=int(input("Hola, dime que tantos números quieres en tu conjunto: "))
    conjunto=set()
    while cont < cant:
        valor=int(input("Dime los valores enteros para el conjunto: "))
        conjunto.add(valor)
        cont+=1
    conjunto_divisible=set(filter(lambda x: (x%3 == 0 or x%2 == 0) and x%6 != 0, conjunto))
    conjunto_no_divisible=set(filter(lambda x: x%3 != 0, conjunto))
    return f"El conjunto introducido por el usuario es: {conjunto}, sus conjuntos derivados son: Conjunto con aquellos enteros divisibles por 3 o por 2 pero no por 6: {conjunto_divisible} y el conjunto con aquellos enteros que no son divisibles por 3: {conjunto_no_divisible}"

print(ejer_6())