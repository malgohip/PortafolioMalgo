#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Today I wanted to create new task and found it is April 1 2014 - the Fool's Day when people are trying to overjoke each other.

So here is a small programming problem without the problem statement. Nevertheless you can do it! Good luck! :)

Example:

input data:
5
1 2
1 2 3
2 3 4
2 4 6 8 10
7 11 19

answer:
5 14 29 220 531
"""
"""
a = open('Ejercicios Code Abey\TXTs\e94 Fools Day 2014.txt','r')
P= a.readlines()

valores=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    valores.append(F)

print(valores)
"""
valores=[[3, 7, 10], [5, 7], [3, 6, 10, 12, 16], [1, 3], [5, 7, 11, 15, 18], [4, 7, 12, 14, 17, 22, 25], [4, 9, 11, 16], [3, 6, 9, 13, 15, 20], [1, 6], [1, 4, 7, 9, 12, 17], [1, 3, 5, 10, 12, 17], [5, 7, 9], [5, 10, 15, 17, 22, 25, 28], [3, 7], [2, 6, 11, 13, 18, 22], [1, 4], [3, 5, 8]]

respuesta=''
for x in valores:
    sum_of_squares = sum(y**2 for y in x)
    respuesta+=str(sum_of_squares)+' '
print(respuesta)