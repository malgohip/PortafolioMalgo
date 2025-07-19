#Author: Sebastian Ochoa. Date: 07/24/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 2.

Diseñe un código que permita calcular la evaluación del polinomio p(x) = sum n i=0 (i+4)x^{2i}. 
El usuario puede escoger el valor de n y el valor de x. El código debe ser tan eficiente en la evaluación, 
como el algoritmo de Horner.
"""

def coeficientes (n=int):
    cof=[]
    for x in range(0,n+1):
        cof.append(x+4)
    return cof

def EvalHorn(A,x):
    l = len(A)
    n = l-1
    B = A[n-1]
    C = A[n]
    Eval = B + C*x**2
    for i in range(n-2,-1,-1):
        B = A[i]
        C = Eval
        Eval = B + C*x**2
    print(f"\n p({x}) = {Eval}")

EvalHorn(coeficientes(8),2)