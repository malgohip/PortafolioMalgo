#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
The Rabbit is going to cross the river. There is a straight chain of tiny isles across the flow and the animal should jump from one to another because it surely could not swim.

At each of the isles there are some candies. When the Rabbit arrives to the new isle, it collects all the candies here.

However, the Rabbit could not jump directly to the next isle in the chain - it just is too strong to make short jumps. So, instead, it can jump over the one or two isles (i.e. from the 1st for example to 3rd or 4th but not to 2nd or 5th and further). Also the Rabbit could not jump back.

You can see the sample of the Rabbit's path on the drawing above. It visits 1st, 3rd, 6th and 8th isles and collects:

11 + 3 + 13 + 7 = 34
the amount of 34 candies. Obviously he could do better if the path is chosen more wisely.

Your task is to choose the best path for Rabbit over the given chain of isles - i.e. to maximize the amount of the candies collected. Note that Rabbit starts from 1st isle and finishes either on the Nth or (N-1)th where N is the total number of isles (because from these two it will necessarily jump immediately to the other bank).

Input data will contain the number of test-cases in the first line.
Next lines contain one test-case each - i.e. one chain of isles, described by the array of numbers - amounts of candies at each isle.
Answer should contain the maximum possible amount of candies gathered for each test case.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e60 Sweet Harvest.txt','r')
P= a.readlines()

caminos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    caminos.append(F)

print(caminos)
"""
caminos=[[13, 8, 17, 8, 11, 17, 6, 3, 17, 15, 7, 2, 9, 4, 3, 3, 11, 5, 17, 10, 9, 13, 9, 18, 8, 4, 13, 4, 7, 13, 14, 6, 8, 2, 11], [16, 15, 7, 16, 17, 19, 10, 4, 14, 2, 2, 16, 15, 10, 12, 7, 13, 8, 13, 7, 6, 18, 14, 17, 12, 8, 18, 5, 9, 3, 17, 2, 17, 16, 10], [15, 14, 14, 16, 19, 12, 10, 5, 4, 14, 10, 12, 7, 14, 10, 12, 8, 13, 19, 4, 11, 3], [13, 9, 16, 19, 15, 5, 9, 7, 19, 11, 3, 4, 10, 4, 14, 17, 19, 10, 8, 19, 7, 10, 7, 12, 11, 13, 6, 10, 4, 19, 9, 17], [11, 9, 11, 19, 8, 19, 4, 19, 9, 16, 16, 10, 13, 19, 14, 11, 12, 17, 11, 16, 18], [13, 16, 7, 9, 18, 15, 5, 17, 18, 4, 5, 6, 14, 11, 9, 3, 10, 5, 12, 13, 7, 14, 10, 8, 19, 12, 6, 17], [16, 12, 5, 5, 19, 11, 5, 9, 14, 12, 17, 13, 14, 11, 13, 8, 7, 15, 7, 4, 10, 3, 11, 5, 7, 12, 12, 19, 6, 14, 13], [4, 3, 12, 6, 7, 5, 16, 4, 4, 12, 7, 6, 3, 7, 5, 6, 15, 3, 7, 3, 18, 11, 3], [10, 5, 15, 3, 15, 7, 10, 11, 8, 8, 7, 5, 15, 10, 6, 19, 13, 2, 15, 11, 18, 5, 9, 15, 4], [15, 11, 13, 4, 3, 14, 2, 15, 8, 11, 2, 12, 10, 8, 3, 8, 12, 17, 12, 7, 2, 14, 5, 18, 10, 15, 14], [11, 12, 13, 11, 7, 2, 12, 17, 10, 15, 5, 12, 18, 18, 19, 5, 16, 19, 18, 11, 2, 15, 8, 6, 14, 8, 14, 10, 19, 8, 3, 2, 2, 15, 15], [8, 7, 3, 8, 10, 3, 12, 19, 9, 15, 11, 12, 7, 15, 15, 11, 9, 8, 2, 8], [19, 9, 4, 16, 7, 17, 4, 15, 8, 13, 19, 6, 16, 10, 12, 5, 4, 7, 14, 16, 17, 3, 16, 5, 15], [19, 11, 3, 5, 4, 6, 5, 8, 9, 9, 4, 5, 6, 11, 18, 10, 13, 16, 6, 16, 5], [15, 18, 15, 15, 6, 16, 16, 18, 10, 6, 2, 19, 6, 16, 19, 3, 8, 8, 7, 6, 3, 6, 13, 17, 11], [11, 16, 2, 4, 10, 8, 15, 6, 18, 19, 16, 15, 12, 8, 19, 4, 7, 4, 10, 5, 17, 19, 5, 19, 2, 19, 6, 8, 2, 4, 17, 17, 9, 6], [13, 15, 8, 11, 19, 13, 9, 7, 4, 3, 11, 5, 17, 5, 6, 11, 8, 8, 17, 7, 2, 12, 2, 17, 5, 14], [12, 18, 7, 15, 17, 18, 3, 12, 19, 8, 6, 16, 4, 7, 7, 8, 16, 6, 16, 12, 2, 15, 11, 16, 8, 4, 2, 12, 14, 16, 19, 2, 15, 16], [16, 18, 10, 11, 2, 19, 16, 5, 13, 19, 2, 17, 17, 15, 2, 13, 6, 4, 8, 19, 2, 3, 3, 18, 15, 5, 17, 7]]

def max_candies(islands):
    n = len(islands)
    if n == 0:
        return 0
    if n == 1:
        return islands[0]
    if n == 2:
        return islands[0]
    dp = [0] * n
    dp[0] = islands[0]
    dp[1] = islands[0] 
    dp[2] = islands[0] + islands[2]
    for i in range(3, n):
        dp[i] = max(dp[i - 2], dp[i - 3]) + islands[i]
    return max(dp[-1], dp[-2])

resultado=''
for x in caminos:
    resultado+=str(max_candies(x))+' '
print(resultado)