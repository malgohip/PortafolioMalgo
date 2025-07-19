#Author: Sebastian Ochoa. Date: 08/18/2024
# -*- coding: utf-8 -*-

"""
The task is just the same as Fibonacci Divisibility, however, input values here are greater to prevent you from implementing straightforward calculations using long arithmetics (this allows users in Java or Python to solve the mentioned task easily enough).

You should implement solution which works fast. A second or two is sufficient to run the proper solution (even with not very modern computer).

Hint: you need not long arithmetic for this task.

Input data in the first line will contain the number of test-cases.
Next line will contain exactly this of divisors M for which you should give answers.
Answer should contain indices of members of Fibonacci Sequence, separated by spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e71 Fibonacci Divisibility Advanced.txt','r')
P= a.readlines()

l=P[1].strip().split()
numeros=[]
for x in range(int(P[0])):
    X=int(l[x])
    numeros.append(X)

print(numeros)
"""
numeros=[691251, 732856, 599638, 1007599, 965954, 1040881, 524746, 766169, 574657, 241652, 266678, 999279, 624627, 274991, 324942, 333263, 225019, 233328, 891051, 682886, 374884, 657942]

def periodo_pisano(m):
    a, b = 0, 1
    for i in range(m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1
    return None

def modulo_fibo(n, m):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, (a + b) % m
        return b

def fibo_divisible_encuentra(m):
    perio_pisano = periodo_pisano(m)
    a, b = 0, 1
    for i in range(2, perio_pisano + 1):
        a, b = b, (a + b) % m
        if b == 0:
            return i
    return None

def resolver_ejercicio(divisores):
    resultados = []
    for m in divisores:
        indice = fibo_divisible_encuentra(m)
        resultados.append(indice)
    return resultados

respuesta=''
for x in resolver_ejercicio(numeros):
    respuesta+=str(x)+' '
print(respuesta)