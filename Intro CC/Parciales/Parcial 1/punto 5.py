#Author: Sebastian Ochoa. Date: 03/05/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 5.(20 Ptos.) 
Diseñe un algoritmo que permita generar la serie numérica  1,  1, 2, 8, 15,29,56,  … Observe que cada término de la serie (a partir del cuarto) se obtiene al sumar los trés términos anteriores y agregar 4. El número de valores a mostrar lo indica el usuario.
"""

def ejer_5():
    cant=int(input("Hola, dime que tan larga quieres tu orden de Fibonacci pirata: "))
    a,b,c=1,1,2
    fibo=[a,b,c]
    for x in range(3,cant):
        F = a + b + c + 4
        fibo.append(F)
        a, b, c = b, c, F
    return fibo

print(ejer_5())