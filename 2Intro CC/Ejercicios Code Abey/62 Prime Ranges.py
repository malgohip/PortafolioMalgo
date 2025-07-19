#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
If you already solved Prime Numbers Generation - here is an inverse version of it.

Given several pairs of primes (like a, b) you are to tell for each of them the total quantity of primes in the range limited by these values (inclusive), i.e. such p-s that:

isPrime(p) = true

    and

a <= p <= b
Input data: will contain the amount of pairs in the first line.
Next lines will contain one pair of primes each, the first value is always less than the second. All values will be less than 3000000.
Answer should contain the quantity of primes in the ranges specified by these pairs.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e62 Prime Ranges.txt','r')
P= a.readlines()

rangos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    rangos.append(F)

print(rangos)
"""
rangos=[[1620121, 2601089], [1494047, 2454719], [2378797, 2469407], [2497751, 2506541], [2071073, 2147309], [2544523, 2563007], [1669537, 1700477], [1325431, 2240533], [2070317, 2397631], [1768057, 2571733], [2723363, 2746199], [1642943, 2454719], [1831399, 2147309], [1376317, 1604737], [1737497, 2506541], [2147309, 2469407], [1872301, 2266921], [1604737, 2419187], [2309471, 2447009], [2535233, 2578993], [1739461, 1744777], [2335009, 2625247], [1669537, 2378797], [1376317, 1570199], [2378797, 2563007], [1951867, 2625247]]

import math

def colador_de_eratostenes(limite):
    if limite < 2:
        return []

    colador = [True] * (limite // 2)
    colador[0] = False  # El número 1 no es primo

    # Solo necesitamos comprobar números impares y empezamos desde 3
    for i in range(3, int(math.sqrt(limite)) + 1, 2):
        if colador[i // 2]:
            colador[i*i // 2 :: i] = [False] * len(colador[i*i // 2 :: i])

    primos = [2] + [2*i + 1 for i in range(1, limite // 2) if colador[i]]
    return primos

respuesta=''
for i in rangos:
    primos = colador_de_eratostenes(i[1])
    intervalo=[]
    for j in primos:
        if j >= i[0]:
            intervalo.append(j)
    respuesta+=str(len(intervalo)+1)+' '
print(respuesta)