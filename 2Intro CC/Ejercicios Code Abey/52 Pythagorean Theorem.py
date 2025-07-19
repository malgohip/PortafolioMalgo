#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
In the complex dice-based games players can use several dice and with number of sides other than 6. For example, the damage given by some powerful sword could be calculated as the sum of 3 dice with 8 sides each (i.e. having numbers from 1 to 8) - this means the weakest possible damage is 3 and strongest is 24, however most probable values would be 13 and 14.

The notation used in the descriptions of such games looks like 3d8 - i.e. 3 dice with 8 sides, or 2d6 for more common variant of 2 dice with 6 sides each. Tossing of 5 coins each of which has only 2 sides would be written as 5d2.

In this task you will be given results of casting some dice set many times. Your task would be to determine how many dice are in the set and how many sides dice have. Supposedly you'll need some program to calculate statistics on these results to classify them.

Due to probabilistic nature of the problem you may fail at first attempt, however try a few times - and if your algorithm is correct, your answer will be accepted.

For this problem dice could have 2, 4, 6, 8, 10 or 12 sides. The number of dice could be from 1 to 5.

Input data contain 303 values in 3 lines.
Each line contains 100 non-zero results of casting (sums of dice points), terminated with spare 0 which should not be counted (it only marks the end of the line).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e52 Pythagorean Theorem.txt','r')
P= a.readlines()

triangulos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    triangulos.append(F)

print(triangulos)
"""
from math import sqrt
triangulos=[[792, 1485, 1722], [1104, 322, 1134], [637, 2184, 2306], [99, 132, 141], [288, 120, 312], [380, 285, 561], [693, 2376, 2475], [476, 1632, 1723], [284, 213, 355], [1608, 469, 1655], [360, 105, 370], [1080, 315, 1123], [1164, 485, 1352], [304, 570, 646], [16, 12, 20], [270, 144, 312], [972, 405, 1018], [168, 70, 169], [686, 2352, 2397], [240, 180, 300], [1680, 490, 1796], [345, 184, 391], [664, 1245, 1384]]

respuesta=''
for x in triangulos:
    x=sorted(x)
    sup_hyp=sqrt(x[0]**2+x[1]**2)
    if sup_hyp < x[2]:
        respuesta+='O'+' '
    elif sup_hyp > x[2]:
        respuesta+='A'+' '
    else:
        respuesta+='R'+' '
print(respuesta)