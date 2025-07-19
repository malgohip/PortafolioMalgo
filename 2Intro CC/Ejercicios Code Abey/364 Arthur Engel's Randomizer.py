#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Problem Statement
Given initial value for X (e.g. "seed"), produce a random sequence according to the formula above. Split the range [0 .. 1) into a number of buckets and count how many values fall into every bucket.

Some issue to care about is that real values tend to be handled slightly differently by various programming languages and hardware. Let's try avoiding discrepancies by truncating values to 7 digits after decimal point on each iteration.

For example, let's start with X = 0.2023 and produce 10 values, spreading them into 10 buckets (e.g. [0 .. 0.1), [0.1 .. 0.2) and so on):

0.1445274   0.7592904   0.1094414   0.7789513   0.524233
0.77205     0.3091387   0.3087502   0.2083622   0.3065843
The resulting distribution is:

0 2 1 3 0 1 0 3 0 0
Input is just 3 values: X0 (for seed), B (for amount of buckets) and T (for "times").
Produce B * T random values (so that ideally every of B buckets should get some value exactly T times).

Answer should give B values, telling real distribution - e.g. how many values fell into every bucket.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e364 Arthur Engels Randomizer.txt','r')
P= a.readlines()

valores=[]
f=P[0].strip().split()
for x in f:
    X=float(x)
    valores.append(X)

print(valores)
"""
valores=[0.4592, 27.0, 300.0]

import math

def generate_distribution(X0, B, T):
    pi = 3.1415926
    num_values = B * T
    distribution = [0] * B
    X = X0
    for _ in range(num_values):
        X = (X + pi) ** 8
        X = X - int(X)
        X = int(X * 10**7) / 10**7
        
        bucket_index = int(X * B)
        
        distribution[bucket_index] += 1
    
    return distribution


distribution = generate_distribution(valores[0],int(valores[1]),int(valores[2]))
print(" ".join(map(str, distribution)))
