#Author: Sebastian Ochoa. Date: 08/18/2024
# -*- coding: utf-8 -*-

"""
You may refer to Fibonacci Sequence task if you are unfamiliar with the subject.

Given usual Fibonacci Sequence, starting with 0 and 1:

0 1 1 2 3 5 8 13 21 34 ...
and some value M you will be asked to find the index of the first non-zero member of this list, which is evenly divisible by this M, e.g. if you are given M = 17 the answer is 9 (the index of the element 34).

Input data in the first line will contain the number of test-cases.
Next line will contain exactly this of divisors M (not exceeding 10000) for which you should give answers.
Answer should contain indices of members of Fibonacci Sequence, separated by spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e69 Fibonacci Divisibility.txt','r')
P= a.readlines()

l=P[1].strip().split()
numeros=[]
for x in range(int(P[0])):
    X=int(l[x])
    numeros.append(X)

print(numeros)
"""
numeros=[7801, 8478, 5401, 5026, 3226, 2475, 6000, 3153, 7053, 8254, 8703, 3001, 4352, 5627, 3302, 6677, 3075, 7652]

def fibonacci():
    fibonacci_ser=[0,1]
    cont=0
    while cont != 1000:
        nuevo=fibonacci_ser[len(fibonacci_ser)-2]+fibonacci_ser[len(fibonacci_ser)-1]
        fibonacci_ser.append(nuevo)
        cont+=1
    return fibonacci_ser

serie_fibonacci=fibonacci()
respuesta=''
for x in numeros:
    for y in range(3,len(serie_fibonacci)):
        if serie_fibonacci[y]%x == 0:
            respuesta+=str(y)+' '
            break
print(respuesta)