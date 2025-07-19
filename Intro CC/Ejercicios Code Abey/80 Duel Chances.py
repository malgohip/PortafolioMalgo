#Author: Sebastian Ochoa. Date: 08/19/2024
# -*- coding: utf-8 -*-

"""
Two friends, Alan and Bob are engaged in a deathly duel. They agreed to stand in front of each other and shoot until one of them is mortally wounded.

Since they have only one pistol, they will shoot in turns. Casting lots determined that Alan is first to fire.

Before duelling they want to get life insurance. Insurance manager then needs to determine what are their chances to die, to calculate proper insurance cost.

You are to help the manager in his calculations. You will be given the probability for both duellers to hit and hurt opponent critically with a single shot - and you asked to write a program which will tell Alan's chances to win (then Bob's chances to win could be calculated by manager himself as Alan's chances to die).

Input data will contain the number of test-cases in first line.
Next lines will contain two numbers pA and pB each - the chance to kill opponent with a shot for Alan and Bob respectively, expressed in percents (so the values would be integer).
Answer should contain the chance for Alan to win (and for Bob to die) in percents, rounded to nearest integer. Separate several answers with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e80 Duel Chances.txt','r')
P= a.readlines()

chances=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    chances.append(F)

print(chances)
"""
chances=[[69, 22], [11, 40], [29, 80], [34, 47], [64, 30], [43, 14], [26, 57], [60, 16], [39, 34], [34, 25], [13, 12], [68, 71], [52, 47], [37, 13], [77, 86], [76, 76], [54, 39], [90, 47], [56, 14], [42, 72]]

respuesta=''
for x in chances:
    p_a=x[0]/100
    p_b=x[1]/100
    Prob_A=round(p_a/(1-(1-p_a)*(1-p_b)),2)
    respuesta+=str(int(Prob_A*100))+' '
print(respuesta)