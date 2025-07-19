#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
This task is inspired by the discussion in the Blog on algorithms by Faisal Rahman on similar task from ProjectEuler

As we know, the Pythagorean Theorem tells us about the simple equation:

a^2 + b^2 = c^2
There really exist such triples a, b, c of integer numbers, which satisfy this equation. This is not self-evident fact, moreover there are no such triples for any other powers except 2 - this is the famous Fermat Theorem which could not be solved for more than 350 years.

However, for the power of 2 there are countless amount of such triples. One of them 3, 4, 5, for example.

Nevertheless, it is not always easy to find a triple satisfying some specific conditions:

In this problem you need to write a program which for given value of s = a + b + c will find the only triple which satisfies the equation.

For example, given sum of 12 the only 3, 4, 5 triple fits, for sum 30 the only 5, 12, 13 etc.

Input data will contain the number of test-cases in the first line.
Other lines will contain a single value each - the sum for which triple should be found.
Answer should contain the values of c^2 for each triple found (it is equal to a^2 + b^2 of course), separated with spaces.

Note: the real values of s would be large enough, about 10e+7 - so the simplest solutions could be inefficient.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e54 Pythagorean Triples.txt','r')
P= a.readlines()

sumas=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    F=int(f)
    sumas.append(F)

print(sumas)
"""
sumas=[18211964, 18270926, 22009826, 15362572, 17026482, 18296690, 12819482, 19425426]

respuesta = ''
for s in sumas:
    sirve = False
    for a in range(1, s // 3 + 1):
        num = (s * (s - 2 * a)) 
        den = 2 * (s - a)
        
        if num % den == 0:
            b = num // den
            c = s - a - b
            if a * a + b * b == c * c:
                respuesta += str(c * c) + ' '
                sirve = True
                break

print(respuesta)