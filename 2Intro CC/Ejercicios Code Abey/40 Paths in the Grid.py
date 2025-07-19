#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
Dynamic Programming is an approach for solving problems very popular among competitive programmers and problemsetters at the resources like TopCoder. Very common example which should be learned is counting number of paths through rectangular grid (for example, districts of the city etc).

Imagine a map of a swamped ground represented by a rectangular grid:

@ + + + +
+ + + X X
+ X + + +
+ + + X +
+ X + + X
+ + + + $
where X depicts a pit (an impassable square, where person will be certainly drowned) while + are safe patches.

A hero should travel from upper left corner (marked with @) to lower right corner (marked with $). He only can move by safe squares, and from each square he only can move in two directions - either right or down (as seen on a map). I.e. backward movements are forbidden - our hero could not waste time due to the lack of food in his knapsack.

We are interested in how many different paths there exist from one corner to another under given rules.

Input data will contain number of rows and columns of the field in the first line - M and N.
Then the field itself will come in M lines, each of which contains N characters separated by spaces. Impassable squares are marked with X symbols.
Answer should contain the only number - the number of existing paths.

It is guaranteed that the result does not exceed 2,000,000,000.
However, it could happen that there is no any path at all.
"""
""""
a = open('Ejercicios Code Abey\TXTs\e40 Paths in the Grid.txt','r')
P= a.readlines()

P[0]=P[0].strip().split()
t=[]
for x in P[0]:
    X=int(x)
    t.append(X)
P[0]=t

mapa=[]
for x in range(1,P[0][0]+1):
    f=P[x].strip().split()
    mapa.append(f)

print(mapa)
"""
P=[[14,20]]
mapa=[['@', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', '+', '+', '+', '+', 'X', '+', '+', '+', '+', '+'], ['+', '+', '+', 'X', '+', '+', '+', '+', '+', '+', 'X', 'X', '+', 'X', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', 'X', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', 'X', '+', '+'], ['+', '+', '+', 'X', '+', '+', 'X', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', '+'], ['+', 'X', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', '+', '+', '+', '+', 'X', '+'], ['+', '+', '+', '+', '+', '+', 'X', 'X', '+', '+', 'X', '+', '+', '+', 'X', '+', '+', 'X', '+', '+'], ['+', 'X', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+'], ['+', 'X', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', '+', '+', '+', 'X', '+', 'X', '+'], ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', '+', 'X', '+'], ['+', '+', '+', 'X', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', 'X', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', '+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'X', 'X', '+', '+', '+', '+', '+', '$']]

dp = [[0] * P[0][1] for _ in range(P[0][0])]
dp[0][0] = 1 if mapa[0][0] == '@' else 0
for i in range(P[0][0]):
    for j in range(P[0][1]):
        if mapa[i][j] == 'X':
            dp[i][j] = 0
        else:
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
resultado=str(dp[P[0][0]-1][P[0][1]-1])
print(resultado)