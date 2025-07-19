#Author: Sebastian Ochoa. Date: 03/03/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 10
Diseñe un algoritmo que permita generar la serie numérica  1, -1,  3, 7, 13, 27,51 … observe que cada término de la serie (a partir del cuarto) se obtiene al sumar los trés términos anteriores y agregar 4. El número de valores a mostrar lo indica el usuario.
"""

def ejer_10()->list:
    cant=int(input("Hola, dime que tan larga quieres tu orden de Fibonacci pirata: "))
    a,b,c=1,-1,3
    fibo=[a,b,c]
    for x in range(3,cant):
        F = a + b + c + 4
        fibo.append(F)
        a, b, c = b, c, F
    return fibo

print(ejer_10())