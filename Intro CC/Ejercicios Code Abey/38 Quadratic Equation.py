#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
Now we are to create a program for solving quadratic equation. Supposedly you have learnt in school that such equation has a form of:

A * x^2 + B * x + C = 0
where A, B and C are some constants (called "coefficients" of equation) and x is a variable. To solve such equation means to find x for which the formula becomes true. For example with coefficients 3, -5 and -2 we have equation:

3 * x^2 - 5 * x - 2 = 0
and we can see that value x = 2 is quite suitable.

General formula for finding such values (or "roots") via coefficients of equation is the following:

x1 = (-B + sqrt(B^2 - 4*A*C)) / (2*A)
x2 = (-B - sqrt(B^2 - 4*A*C)) / (2*A)
For example above these expressions will produce:

x1 = (5 + sqrt(5^2 + 4*3*2)) / (2*3) = (5 + 7) / 6 = 2
x2 = (5 - sqrt(5^2 + 4*3*2)) / (2*3) = (5 - 7) / 6 = -1/3
I.e. the equation really has two roots. Strictly speaking, here are always two roots. However, they could be: - either distinct, when expression under sqrt is positive; - or equal, when expression under sqrt is zero; - and in other cases even complex numbers - i.e. values like U+V*i where i = sqrt(-1).

Refer to wikipedia for more about Complex Numbers or Quadratic Equations at whole.

Input data will contain number of test-cases in the first line.
Each of test-cases will consist of three values (for A, B and C respectively).
Answer should contain a pair of roots for each case (even when they are equal). Use space to separate values of the pair and use semicolon followed by space to separate pairs themselves. Complex numbers should be given like 5-2i or -1+1i.

Note also:

order of values inside the pair is important - for real roots output the bigger one first; for complex roots output a+bi first and a-bi last;
roots would be always expressed with integer numbers in this task, so print no any decimal points etc.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e38 Quadratic Equation.txt','r')
P= a.readlines()

coeficientes=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    coeficientes.append(F)

print(coeficientes)
"""
from math import sqrt
coeficientes=[[5, -50, 250], [8, 8, -48], [7, 14, -336], [1, 7, 0], [1, -5, -14], [6, 96, 984], [1, -5, -24], [8, -16, 296], [3, -24, 348], [7, -84, 819], [7, 35, -42], [5, -55, 90], [6, -60, 750], [2, 16, 64]]

respuesta=''
for X in coeficientes:
    if (X[1]**2 - 4*X[0]*X[2]) < 0:
        rx=-X[1] / (2*X[0])
        ix1=sqrt(-(X[1]**2 - 4*X[0]*X[2])) / (2*X[0])
        x1 =str(int(rx))+'+'+str(int(ix1))+'i'
        ix2=sqrt(-(X[1]**2 - 4*X[0]*X[2])) / (2*X[0])
        x2 =str(int(rx))+'-'+str(int(ix2))+'i'
        respuesta+=x1+' '+x2+'; '
    else:
        x1 = int((-X[1] + sqrt(X[1]**2 - 4*X[0]*X[2])) / (2*X[0]))
        x2 = int((-X[1] - sqrt(X[1]**2 - 4*X[0]*X[2])) / (2*X[0]))
        respuesta+=str(x1)+' '+str(x2)+'; '
respuesta=respuesta[:-2]
print(respuesta)