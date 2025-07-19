#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""

Joel wants to buy a boat which costs $10000. However, he currently has only $1000. One of the ways to increase money is to put them into bank account and wait. For example, if account is incresed by 8% each year:

year     money
  0       1000
  1       1080
  2       1166.4
  3       1259.71
  4       1360.48
  5       1469.31
  6       1586.85
    .....
 29       9316.82
 30      10062.16
then Joel can grow his money in 30 years. Moreover, if account is increased not annually but monthly (with the same interest rate of 8% per year) then the sum will be collected in only 29 years! Quite funny :)

In this task you need to help Joel to calculate how many years he need to wait depending on given starting amount of money S, required sum R and bank's interest rate P. At the end of each year account is increased and rounded down to whole cents (as in example above).

Input data contain number of test-cases in the first line.
Each of the following lines contain three numbers S, R and P.
Answer should contain number of years to wait for each case, separated by spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e35 Savings Calculator.txt','r')
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
casos=[[50, 250, 20], [250, 2500, 15], [1000, 9000, 15], [1000, 25000, 1], [500, 7500, 2], [50, 500, 40], [2500, 37500, 2], [100, 1500, 3], [50, 900, 10], [250, 3500, 50], [250, 1750, 8], [250, 3750, 2], [250, 2500, 30], [2500, 42500, 35], [2500, 40000, 15], [250, 6250, 3], [100, 1500, 3], [250, 3750, 1]]

respuesta=''
for x in casos:
    ano=0
    while x[0] < x[1]:
        ano+=1
        x[0]+=round(x[0]*(x[2]/100),2)
    respuesta+=str(ano)+' '
print(respuesta)