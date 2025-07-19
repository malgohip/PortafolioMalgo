#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
In this task we are going to implement the primes generator. Primes are positive integers which have no other divisors except 1 and itself. You may read more in wiki article. Most popular algorithms to practice are either Sieve of Eratosthene or Trial division. You are encouraged to google for them if you need more details.

So let us create the array (or list) of prime numbers in ascending order, i.e.:

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...]
And then print the primes corresponding to the indices given in the input data.

Input data will contain the amount of primes to print in the first line.
Next line will contain indices of array of primes for which values should be printed. They will be in range from 1 to 200000.
Answer should contain prime numbers corresponding the specified positions of the array.

Note that for this task we start indexing an array from 1 rather than 0 (this may help you in checking your program with many lists of primes which could be found online).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e61 Prime Numbers Generation.txt','r')
P= a.readlines()

l=P[1].strip().split()
indices=[]
for x in range(0,int(P[0])):
    F=[]
    X=int(l[x])
    indices.append(X)

print(indices)
"""
indices=[139974, 137073, 135118, 130874, 102020, 129853, 134067, 108633, 116971, 110958, 121753, 150340]

import math

def colador_de_eratostenes(limite):
    colador = [True] * (limite + 1)
    colador[0] = colador[1] = False
    for num in range(2, int(math.sqrt(limite)) + 1):
        if colador[num]:
            for multiplo in range(num*num, limite + 1, num):
                colador[multiplo] = False
    
    primos = [i for i, is_prime in enumerate(colador) if is_prime]
    return primos

def encontra_primeros_n_primos(n):
    
    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 1
    
    primos = colador_de_eratostenes(limit)
    
    return primos[:n]

respuesta=''
mayor=max(indices)
primos = encontra_primeros_n_primos(mayor+1)
for i in indices:
    respuesta+=str(primos[i-1])+' '
print(respuesta)