#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
After solving the task Bubble Sort we are supposed to learn about sorting arrays. Now we have a bit more complicated programming problem for you, since it is important to have practice in sorting and handling not only primitive values but also more complex objects.

As previously, we are given an array of numbers. It should be sorted first (in strictly increasing order, for simplicity all values are unique) - and then for each value its initial index should be printed (indexes start from 1).

I.e., suppose we have an array 50 98 17 79 which after sorting becomes 17 50 79 98. Now:

17 was at 3-rd place initially
50 was at 1-st place initially
79 was at 4-th place initially
98 was at 2-nd place initially

so result is
3 1 4 2
Initial data will contain array size at first line and array values itself in the second (integers separated by spaces).
Answer should contain initial indexes of the array members after they are reordered by sorting.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e29 Sort with Indexes.txt','r')
P= a.readlines()

l=P[1].strip().split()
numeros=[]
for x in range(int(P[0])):
    X=int(l[x])
    numeros.append(X)

print(numeros)
"""
numeros=[625, 862, 415, 568, 322, 89, 714, 667, 240, 136, 48, 369, 815, 913, 280, 182, 765, 469, 528]

respuesta=''
ordenados=numeros.copy()
for i in range(len( ordenados)):
    toca=0
    for j in range(0,len( ordenados)-i-1):
        if  ordenados[j] >  ordenados[j+1]:
            t =  ordenados[j]
            ordenados[j] =  ordenados[j+1]
            ordenados[j+1] = t
            toca=1
    if not toca:
        break

for x in ordenados:
    ind=numeros.index(x)+1
    respuesta+=str(ind)+' '
print(respuesta)