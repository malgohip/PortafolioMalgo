#Author: Sebastian Ochoa. Date: 07/30/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 5.

Usando cálculo Lambda diseñe un programa que permita evaluar cualquier lo polinomio cúbico de la 
forma p(x) = ax^3 + bx^2 + cx + d, en donde a,b,c y d son constantes y x es la variable. 
El código debe permitirle al usuario evaluar  cualquier polinomio cúbico y para cualquier valor 
numérico que tome  x, en consecuencia el programa debe perdirle al usuario los coeficientes a,b,c 
y d y el valor de x.
"""

def polinomio(a,b,c,d):
    return lambda  x : a*x**3 + b*x**2 + c*x + d

print("\n**** Hola, hoy te ayudaré a resolver un polinomio cubico ****")
A=float(input("\nDime el valor del primer coeficiente (a): \n"))
B=float(input("\nDime el valor del segundo coeficiente (b): \n"))
C=float(input("\nDime el valor del tercer coeficiente (c): \n"))
D=float(input("\nDime el valor del cuarto coeficiente (d): \n"))
coeficientes=polinomio(A,B,C,D)
X=float(input("\nPor ultimo dime el valor de la variable (x): \n"))
print(f"El resultado del polinomio cubico p({X}) = {A}x^3 + {B}x^2 + {C}x + {D} es: {coeficientes(X)}")
preg=str(input("\nQuieres volver a probar el programa con otro valor de x?\n\tSí(s)\tNo(n)\n"))
while preg == 's':
    X=float(input("\nDime el nuevo valor de la variable (x): \n"))
    print(f"El resultado del polinomio cubico p({X}) = {A}x^3 + {B}x^2 + {C}x + {D} es: {coeficientes(X)}")
    preg=str(input("\nQuieres volver a probar el programa con otro valor de x?\n\tSí(s)\tNo(n)\n"))
print("/////Gracias por usar mi codigo/////")