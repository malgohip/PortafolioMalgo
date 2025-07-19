#Author: Sebastian Ochoa. Date: 08/18/2024
# -*- coding: utf-8 -*-

"""
The task Matching Words allows easy but ineffective solution because it works with very small input data.

This problem is similar, but you will need to proceed almost one million words and choose a single, most frequent of them - it is very often and very important task - for example performed by search engines over web pages. You will need to use efficient algorithm, otherwise your program will work for hours and perhaps days.

Since it is not practical to provide test-cases consisting of so many letters along with problem statement, you will generate the words yourself.

Use algorithm from the task Funny Words Generator to create a list of exactly 900000 words, each 6 letters long.
You should use exactly the same Linear Congruential Generator as random generator. The only input parameter would be the seed for your random number generator (LCG).

Input data will contain a single value - the seed for random generator which you will use to generate list of words.
Answer should contain a single word - one most frequently encountered in the list.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e70 Most Frequent Word.txt','r')
P= a.readlines()

cantidad=int(P[0])

print(cantidad)
"""
cantidad=42538

consonantes='bcdfghjklmnprstvwxz'
vocales='aeiou'
palabras=[]
Xcur = cantidad
for _ in range(900000):
    valoresr=[]
    for _ in range(6):
        Xcur = (445 * Xcur + 700001) % 2097152
        valoresr.append(Xcur)
    palabra=''
    for y in range(len(valoresr)): 
        if y % 2 == 0:
            letra=consonantes[valoresr[y]%19]
        else:
            letra=vocales[valoresr[y]%5]
        palabra+=letra
    palabras.append(palabra)

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
palabra_frecuente = max(contador, key=contador.get)

print(palabra_frecuente)