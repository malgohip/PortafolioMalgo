#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Problem Statement
Construction company just have built skyscraper of immense height, but with only single appartment on each floor. Appartment cost is X at the lowest floors, but is incremented by 1000 every M floors. The goal is to calculate how much profit the company gets by selling the whole building of N storeys.

To clarify: if N = 30 and price starts with X = 10000, incrementing every M = 10 floors, then first ten apartments (at floors 0 .. 9, where 0 means "ground floor") are sold for 10000 each, next ten (at floors 10 .. 19) go for 11000, and ten last for 12000.

Input gives the number T of testcases in the first line.
Then T lines follow, each with three values N M X.

Answer should give building total prices for every testcase, space-separated. Prices are integers, no cents, pennies or kopeeks please :)
"""
"""
a = open('Ejercicios Code Abey\TXTs\e301 Skyscraper Price.txt','r')
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
numeros=[[5, 17, 6500], [92, 7, 3000], [51, 20, 4000], [0, 1, 3500], [12, 4, 5000], [6, 16, 2500], [29, 11, 4000], [24, 14, 500], [16, 12, 3000], [39, 18, 1000], [24, 9, 1000], [0, 9, 5500], [21, 13, 3000], [4, 14, 6000], [17, 16, 4500], [18, 14, 6500], [36, 13, 3000], [49, 20, 2500]]

def calculate_total_profit(N, M, X):
    total_profit = 0
    current_price = X
    while N > 0:
        floors_in_block = min(M, N)
        total_profit += floors_in_block * current_price
        N -= floors_in_block
        current_price += 1000
    return total_profit

respuesta=''
for x in numeros:
    ganancia=calculate_total_profit(x[0], x[1], x[2])
    respuesta+=str(ganancia)+' '
print(respuesta)