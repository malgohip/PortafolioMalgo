#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
The game of Blackjack has very simple rules: players should take cards one by one trying to collect more points than opponents, but not exceeding 21 (refer Wikipedia for complete rules).

The deck contains all cards from 2 to 10 inclusive, which are counted according to their value, also Kings, Queens and Jacks which cost 10 points each and also Aces, which could be counted as 1 or 11 points, whatever is better.

Let us learn the programming of scoring algorithm for such game.

Input data will contain the number of test-cases in the first line.
Then test-cases will follow on separate lines. Each test-case consists of several cards expressed with symbols:
2, 3, 4, 5, 6, 7, 8, 9,
T, J, Q, K - for 10, Jack, Queen, King,
A - for Ace.
Answer should contain the number of points in each test-case, not exceeding 21 - or the word Bust if the total is greater than 21 (i.e. player immediately loss).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e42 Blackjack Counting.txt','r')
P= a.readlines()

manos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    manos.append(f)

print(manos)
"""
from functools import reduce
manos=[['4', 'A', 'J', '8'], ['T', 'A'], ['J', '2', 'J'], ['4', 'A', '3'], ['A', '6'], ['4', '3', '2', 'Q'], ['A', '8'], ['T', 'Q'], ['4', 'A', '8', 'K'], ['9', '5', 'K'], ['2', 'Q', 'T'], ['6', 'A'], ['K', 'A'], ['T', '4', 'K'], ['2', 'A', '9', 'K'], ['K', 'Q'], ['3', '6', '8'], ['3', 'Q', '2', '7'], ['J', 'A'], ['2', '7', '2', 'A', '5'], ['A', '2', '8']]

def blackjack(lst):
    nums=[]
    for x in lst:
        if x == '2':
            nums.append(2)
        if x == '3':
            nums.append(3)
        if x == '4':
            nums.append(4)
        if x == '5':
            nums.append(5)
        if x == '6':
            nums.append(6)
        if x == '7':
            nums.append(7)
        if x == '8':
            nums.append(8)
        if x == '9':
            nums.append(9)
        if x == 'T':
            nums.append(10)
        if x == 'J':
            nums.append(10)
        if x == 'Q':
            nums.append(10)
        if x == 'K':
            nums.append(10)
    return nums

resultado=''
for x in manos:
    n=blackjack(x)
    suma=reduce(lambda x,y: x+y, n)
    for y in x:
        if y == 'A':
            if suma+11 > 21:
                suma+=1
            else:
                suma+=11
    if suma > 21:
        resultado+='Bust '
    else:
        resultado+=str(suma)+' '
print(resultado)
