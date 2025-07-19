#Author: Sebastian Ochoa. Date: 08/19/2024
# -*- coding: utf-8 -*-

"""
Dice game of Yacht is played with 5 standard dice (having from 1 to 6 points on their sides). The player's goal is to gather some beautiful combination of points. Suppose, the following combinations are respected:

two of dice have the same points, like 3 6 5 6 1 - called pair;
three of dice have the same points, like 2 4 5 4 4 - called three;
four of dice have the same points, like 1 4 1 1 1 - called four;
all five dice have the same points, like 2 2 2 2 2 - called yacht;
two pairs at once, like 3 6 5 3 5 - called two-pairs;
pair and three at once, like 1 6 6 1 6 - called full-house;
sequence from 1 to 5, like 2 4 3 5 1 - called small-straight (see notes);
sequence from 2 to 6, like 6 3 4 2 5 - called big-straight.
Note1: combinations named with two words are written with dash, same as answers which our code should produce.
Note2: "small-straight" should be called "little-straight", this was mistakenly borrowed from "Yachtzee" game rules, where it denotes straight of 4 dice - but now it is too late to change checker code, sorry :)

Such combinations increase player's score by different values, but it is not important now.

Our goal is to write a program which for given combination of dice will determine its type.

Input data contains a number of test-cases in the first line.
Next lines contain 5 values each - points of player's dice.
Answer should contain the name for each of combinations. Names could be pair, two-pairs, three, four, yacht, full-house, small-straight, big-straight or none, separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e75 Yacht or Dice Poker.txt','r')
P= a.readlines()

dados=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    dados.append(F)

print(dados)
"""
dados=[[2, 3, 4, 5, 6], [6, 6, 6, 6, 6], [6, 3, 4, 6, 2], [3, 1, 4, 4, 2], [2, 3, 4, 5, 1], [5, 2, 1, 5, 1], [2, 3, 4, 5, 6], [6, 3, 6, 2, 3], [2, 5, 1, 2, 4], [2, 3, 4, 5, 1], [2, 5, 5, 6, 5], [2, 3, 4, 1, 5], [5, 4, 3, 6, 4], [5, 5, 5, 5, 3], [2, 3, 4, 5, 1], [6, 3, 1, 2, 3], [2, 3, 4, 5, 1], [2, 5, 4, 2, 6], [4, 4, 4, 1, 6], [2, 3, 4, 5, 1], [2, 3, 4, 5, 1], [2, 3, 4, 5, 1], [2, 3, 4, 5, 6], [1, 2, 4, 4, 3], [3, 6, 3, 1, 2]]

respuesta=''
for x in dados:
    x.sort()
    #print(x)
    if x[0] == 1 and x[1] == 2 and x[2] == 3 and x[3] == 4 and x[4] == 5:
        respuesta+='small-straight '
    elif x[0] == 2 and x[1] == 3 and x[2] == 4 and x[3] == 5 and x[4] == 6:
        respuesta+='big-straight '
    cantidades={}
    for dado in x:
        if dado in cantidades:
            cantidades[dado] += 1
        else:
            cantidades[dado] = 1
    #print(cantidades)
    pares=0
    trios=0
    for z in cantidades.values():
        if z == 2:
            pares+=1
        elif z==3:
            trios+=1
        elif z==4:
            respuesta+='four '
            break
        elif z==5:
            respuesta+='yacht '
            break
    #print(pares,trios)
    if pares == 1 and trios == 1:
        respuesta+='full-house '
    elif pares == 2:
        respuesta+='two-pairs '
    elif trios == 1:
        respuesta+='three '
    elif pares == 1:
        respuesta+='pair '
print(respuesta)