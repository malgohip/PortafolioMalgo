#Author: Sebastian Ochoa. Date: 08/05/2024
# -*- coding: utf-8 -*-

"""
6. Ejercicio

Diseñe un código que permita calcular la evaluación del polinomio p(x) = (n)sum(i=0) ix^i. El usuario 
puede escoger el valor de n y el valor de x. El cógigo debe ser tan eficiente en la evaluación, como el 
algoritmo de Horner.
"""

def coeficientes (n=int):
    cof=[]
    for x in range(0,n+1):
        cof.append(x)
    return cof

def EvalHorn(A,x):
    l = len(A)
    n = l-1
    B = A[n-1]
    C = A[n]
    Eval = B + C*x
    for i in range(n-2,-1,-1):
        B = A[i]
        C = Eval
        Eval = B + C*x
    return Eval

print("Hola, hoy te ayudaré a calcular la sumatoria p(x) = (n)sum(i=0) ix^i")
n=int(input("Dime el valor que quieres que tome n: "))
x=float(input("Dime el valor que quieres que tome x: "))
coef=coeficientes(n)
print(f"La sumatoria p(x) = (n)sum(i=0) ix^i con un valor de n de {n} y un valor de x de {x} da como resultado p({x}) = {EvalHorn(coef,x)}")