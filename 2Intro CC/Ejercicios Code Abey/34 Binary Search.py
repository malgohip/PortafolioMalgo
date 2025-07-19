#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
Programming of Binary Search is the common task since it is used for searching through sorted arrays (that's why we learnt sorting) as well as for solving math equations. Let us practice the latter application. Please kindly refer to the Binary Search article for thorough explanations if you feel not well acquainted with the idea of the algorithm.

The goal is to solve the equation which has the following form:

A * x + B * sqrt(x ^ 3) - C * exp(-x / 50) - D = 0
here A, B and C all would be positive so that function is monotonic. Solution is guaranteed to exist somewhere in range 0 <= x <= 100.

Solution should be calculated with precision 0.0000001 = 1e-7 or better.

Input data will contain number of test-cases in the first line.
Next lines will contain four numbers for each test-case, i.e. A B C D separated by values.
Answer should contain solutions - i.e. values of x which satisfy equation with given coefficents - several answers (for several test-cases) should be separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e34 Binary Search.txt','r')
P= a.readlines()

casos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=float(x)
        F.append(X)
    casos.append(F)

print(casos)
"""
import math as mt
casos=[[10.63962531, 0.52945809, 844.80369503, 817.82667803], [11.9933237, 1.96517321, 1537.61717376, -706.68238885], [8.73491925, 1.3904801, 1664.95030451, 1100.37139334], [10.60092416, 0.87253782, 1862.13142977, 369.02731594], [10.06598502, 0.93091897, 366.00268649, 1399.16374454], [15.26071526, 0.61972212, 1990.18874578, -193.36222405], [6.66544943, 1.08658218, 449.00497722, -24.54907815], [11.90071006, 1.43482148, 387.08534762, -162.23101172]]

def f(x, A, B, C, D):
    return A * x + B * mt.sqrt(x ** 3) - C * mt.exp(-x / 50) - D

def binary_search(A, B, C, D, bajo, alto, preci):
    while alto - bajo > preci:
        med = (bajo + alto) / 2.0
        if f(med, A, B, C, D) == 0:
            return med
        elif f(med, A, B, C, D) > 0:
            alto = med
        else:
            bajo = med
    return (bajo + alto) / 2.0

respuesta=''
for x in casos:
    root = binary_search(x[0],x[1],x[2],x[3], 0, 100, 1e-7)
    respuesta += str(root)+' '
print(respuesta)