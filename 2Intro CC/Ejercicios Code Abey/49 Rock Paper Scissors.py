#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""

There is a game which is of special importance in the Computer Science because it though simple itself, could be used for creating very cunning Artificial Intelligence algorithms to play against human (or each other) with predicting the opponent's behavior.

This ancient game is played between two participants who simultaneously cast one of three figures by their fingers - Rock, Paper or Scissors.

If both cast the same figure, the round is considered a draw. Otherwise the following rules are applied:

Rock beats Scissors (by blunting them)
Scissors beat Paper (by cutting it)
Paper beats Rock (by covering it)
Often the game is played on the staircase. Player who wins the round advances one step. One who reaches the end of the staircase first is the winner.

You will be given several records of the played games. You are to tell for each of them who of players won.

Input data will contain the number of matches played in the first line.
Then the matches description is written in separate lines.
Each line contain several pairs of letters, like PR (first casts Paper, second casts Rock), or SS (both cast Scissors), separated with spaces.
Answer should for each of matches specify whether first player wins (by value 1) or second (by value 2). There would be no draws.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e49 Rock Paper Scissors.txt','r')
P= a.readlines()

l=P[1].strip().split()
rondas=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    rondas.append(f)

print(rondas)
"""
rondas=[['RS', 'RR', 'RR', 'SP', 'PS', 'PS', 'PS'], ['RR', 'RR', 'SP', 'PR', 'SR', 'PS', 'RR', 'SP'], ['RR', 'SS', 'PP', 'PP', 'SP', 'PP', 'SP', 'RP', 'RS', 'RP', 'SS', 'RP', 'SS', 'SS', 'RS'], ['RS', 'PR', 'SS', 'PR', 'SR', 'RR', 'RP', 'PP', 'PP', 'SS', 'RS', 'PS', 'PP', 'RR', 'SS', 'RR', 'RS'], ['RR', 'PP', 'RP', 'SP', 'PS', 'PR', 'SP'], ['PP', 'RS', 'PP', 'SS', 'PR', 'SS', 'RR', 'RS', 'PR', 'PP', 'RP', 'PR', 'RP', 'PP', 'SP'], ['RR', 'SS', 'PP', 'RR', 'SP', 'PP', 'RS', 'PR', 'RR', 'PR', 'PS', 'SP'], ['RP', 'SP', 'RP', 'SR', 'RP'], ['RP', 'SR', 'RS', 'PS'], ['SP', 'RS', 'SR', 'PR', 'RP', 'PP', 'SR', 'SP', 'PS', 'PS'], ['RR', 'PS', 'RP', 'PP', 'PR', 'PS', 'SP', 'RR', 'SP', 'PP', 'SP', 'RR', 'RP', 'PR'], ['PS', 'PS', 'RS', 'PR', 'RP'], ['RR', 'SP', 'PR', 'RR', 'SS', 'SP', 'RS'], ['RP', 'PP', 'SR', 'RS', 'RR', 'PP', 'RR', 'PS'], ['SS', 'RS', 'PR', 'SP', 'RS', 'PR', 'RR', 'PS', 'RP', 'PS', 'PS', 'SS', 'SS', 'RP', 'SR'], ['SR', 'SP', 'PS', 'PS', 'RS', 'SR', 'RR', 'PP', 'SR', 'PS'], ['SR', 'PR', 'SS', 'SR', 'PP', 'PP', 'RS', 'RS', 'SR', 'SR', 'SR'], ['PR', 'SR', 'PR', 'RS', 'SS', 'SS', 'RP', 'RP', 'PP', 'RP'], ['PP', 'SR', 'PR', 'PS', 'RR', 'SS', 'SS', 'SR', 'SR'], ['SS', 'RS', 'PR', 'SP'], ['RR', 'PS', 'SR', 'RP', 'RS', 'PR', 'PS'], ['PP', 'SS', 'PS', 'SS', 'SS', 'SP', 'SR', 'PR', 'PR', 'RR', 'SR', 'PP', 'SS', 'RP'], ['PP', 'SR', 'RR', 'RS', 'SS', 'PS', 'SS', 'RS', 'SS', 'PS', 'PS', 'RR', 'SS', 'SS', 'RS', 'RR', 'SP', 'SS', 'PS', 'SR'], ['RS', 'RR', 'SS', 'RP', 'RS', 'RP', 'RR', 'RS'], ['PR', 'PR', 'RS', 'RP', 'PR', 'SP'], ['PP', 'SP', 'PR', 'RP', 'RR', 'SR', 'SP'], ['SR', 'RP', 'RP'], ['SP', 'RS', 'SR', 'SS', 'RP', 'SS', 'RS', 'RS', 'PR', 'PS', 'PP', 'SR', 'PR'], ['RR', 'SP', 'SS', 'RP', 'SP', 'RR', 'RR', 'PS', 'PP', 'RP', 'RR', 'RR', 'PR', 'PP', 'PS', 'SP', 'RS', 'PR'], ['PR', 'RP', 'RR', 'RS', 'PS', 'RP', 'SS', 'SS', 'PR', 'PP', 'RR', 'RP']]

resultado=''
for x in rondas:
    g_1=0
    g_2=0
    for y in x:
        if y == 'RS' or y == 'SP' or y == 'PR':
            g_1+=1
        elif y == 'SR' or y == 'PS' or y == 'RP':
            g_2+=1
    if g_1 > g_2:
        resultado+='1'+' '
    else:
        resultado+='2'+' '
print(resultado)