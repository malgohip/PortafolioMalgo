#Author: Sebastian Ochoa. Date: 08/06/2024
# -*- coding: utf-8 -*-

"""
5. Ejercicio

Diseñe un código que permita calcular la evaluación del polinomio p(x) = {n}sum{i=0} (3i+1)x^{2i}. 
El usuario puede escoger el valor de n y el valor de x. El código debe ser tan eficiente en la evaluación, 
como el algoritmo de Horner.
"""

def coeficientes (n=int):
    cof=[]
    for x in range(0,n+1):
        cof.append(3*x+1)
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
    return Eval

EvalHorn(coeficientes(8),2)

print("Hola, hoy te ayudaré a calcular la sumatoria p(x) = (n)sum(i=0) ix^i")
n=int(input("Dime el valor que quieres que tome n: "))
x=float(input("Dime el valor que quieres que tome x: "))
coef=coeficientes(n)
print(f"La sumatoria p(x) = (n)sum(i=0) (3i+1)x^[2i] con un valor de n de {n} y un valor de x de {x} da como resultado p({x}) = {EvalHorn(coef,x)}")