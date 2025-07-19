#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
It looks like none of beginner's courses on programming avoids practicing Euclid's algorithm for calculation of the greatest common divisor of two numbers.

Greatest Common Divisor or GCD of a and b is such an integer value c that both of a, b are divisible by it (e.g. leave no remainder) - and also c is the largest possible. For example gcd(20, 35) = 5 and gcd(13, 28) = 1. Euclid's algorithm is quite simple - we keep on subtracting smaller value (of a and b) from larger - and repeat this operation until values become equal - this last value will be gcd. For speeding up the process we can use modulo operation instead of subtraction.

For example:

20      35      - subtract first from second
20      15      - subtract second from first
5       15      - now subtract first from second twice
5       5       - and here is GCD
Least Common Multiple (or LCM) of a and b is such an integer d that it is divisible by both of them (and is the smallest of all possible). It can be found with the following rule:

lcm(a, b) = a * b / gcd(a, b)
By the way, if this task feels too easy, check the advanced LCM of a range version!

The task
Input data contain number of test-cases in the first line.
Then lines with test-cases follow, each containing two numbers - for A and B.
Answer should contain GCD and LCM for each pair, surrounded by brackets and separated by spaces, for example:
"""
"""
a = open('Ejercicios Code Abey\TXTs\e26 Greatest Common Divisor.txt','r')
P= a.readlines()

casos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    casos.append(F)

print(casos)
"""
casos=[[7023, 4], [1020, 220], [456, 7], [88, 735], [192, 74], [943, 598], [1786, 3478], [230, 8922], [2, 2], [4428, 2700], [910, 845], [10, 98], [2, 100], [6632, 37], [3404, 3496], [1044, 2484], [552, 912], [15, 739], [2232, 828], [8741, 31], [17, 2], [91, 8394], [572, 3640], [1426, 3968]]

respuesta=''
def gcd (lst):
    a=lst[0]
    b=lst[1]
    while a != b:
        if a > b:
            a-=b
        else:
            b-=a
    return a

for x in casos:
    maxdiv=gcd(x)
    minmul=x[0]*x[1]/maxdiv
    respuesta+='('+str(maxdiv)+' '+str(int(minmul))+')'+' '
print(respuesta)    