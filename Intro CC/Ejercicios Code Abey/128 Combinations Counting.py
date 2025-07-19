#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
When I was in army, sometimes (about once a week) our unit was faced a charming alternative:

most of the hands are to be sent to fields for weeding cabbage and potato;
few people were to be left in charge of the quarters, cleaning, washing, drying etc.
Surely there always were many variants to choose the people for each of two occupations.

So here we have an example of Combinations - different ways of choosing several elements from the given set (not regarding the order). For example, if the boy have 4 candies (of different kinds) and should take only 2 of them, leaving others to his younger sister, he have the following variants:

A B C D - four sorts of candies

A+B, A+C, A+D, B+C, B+D, C+D - six way to choose a pair of them.
How many combinations of K elements from the set of N exist (assuming all N elements are different). It could be easily found that the math formula is:

      N!
------------- = C(N, K) - the number of different combinations
K! * (N - K)!
Where X! is the factorial of X, i.e. product 1 * 2 * 3 * ... * X.

Problem statement
You are to calculate exactly this value C(N, K) for given N and K. Note that though some languages (Python and Java for example) have built-in long arithmetics, it would be good if you'll find a way to minimize intermediate results in calculations. It would be crucial for C/C++ sometimes.

If it is too simple for you, please try to write program for Enumerating Combinations task!

Input data will contain the amount of test-cases.
Next lines will contain one test-case each in form of two values (N K).
Answer should contain C(N, K) for each case.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e128 Combinations Counting.txt','r')
P= a.readlines()

numeros=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    numeros.append(F)

print(numeros)
"""
import math
numeros=[[96, 89], [60, 8], [96, 7], [83, 8], [74, 8], [111, 104], [106, 7], [68, 60], [93, 86], [69, 8]]

def combinatoria(n,k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

respuesta=''
for x in numeros:
    respuesta+=str(combinatoria(x[0],x[1]))+' '
print(respuesta)