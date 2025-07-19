#Author: Sebastian Ochoa. Date: 08/18/2024
# -*- coding: utf-8 -*-

"""
This problem is very simple: just find the way out of the maze.

Hint: you can choose any algorithm you know/like but a kind of wave propagation method is recommended.

Maze is given as a rectangular matrix of 0 and 1 characters. Exit is in top-left corner. You are to find the ways from top-right, bottom-left and bottom-right corners, i.e.

X-----A            1110001
-------            0010001
-------            1111111
-------            0000101
B-----C            1111101
For example in 7 * 5 rectangle (on the left) we should find ways from corners A, B and C to corner X. And for topology given (on the right) paths should be:

from A: DDLLLLUULL
from B: RRRRUULLUULL
from C: UULLLLUULL
Where U denotes step up, L is one step left, R and D are steps right and down respectively. We will use short form like:

from A: 2D4L2U2L
from B: 4R2U2L2U2L
from C: 2U4L2U2L
You see, each letter is preceded by amount of steps in this direction, like - 2 down, 4 left, 2 up, 2 left etc.

Input data will contain width and height of the maze in first line (both are odd values).
Then maze itself will follow, with 1 depicting passages and 0 for impassable walls.
Answer should contain three paths, space separated, in the format explained above.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e66 Caesar Cipher Cracker.txt','r')
P= a.readlines()

ne_str=P[0].strip().split()
ne=[]
for x in ne_str:
    X=int(x)
    ne.append(X)

codices=[]
for x in range(1,ne[0]+1):
    f=P[x].strip().split()
    codices.append(f)

print(codices)
"""
codices=[['YG', 'ECNN', 'JGT', 'VJG', 'YQOCP', 'YJQ', 'FKF', 'PQV', 'ECTG', 'HQWT', 'UEQTG', 'CPF', 'UGXGP', 'AGCTU', 'CIQ'], ['JURA', 'ZL', 'THVGNE', 'TRAGYL', 'JRRCF', 'GHEAF', 'NYY', 'NEBHAQ', 'OHG', 'QBRF', 'ABG', 'ZBIR'], ['ZNK', 'YKIXKZ', 'UL', 'NKGZNKX', 'GRK', 'OL', 'HRUUJ', 'HK', 'ZNK', 'VXOIK', 'UL', 'ZNK', 'GJSOXGRZE'], ['ZU', 'AY', 'OT', 'URJKT', 'YZUXOKY', 'TUX', 'OXUT', 'HGXY', 'G', 'IGMK', 'OZ', 'IGT', 'HK', 'IGAMNZ', 'HAZ', 'TUZ', 'ZNXUCT'], ['ST', 'XTTSJW', 'XUTPJS', 'YMFS', 'GWTPJS', 'YMFY', 'FQQ', 'RJS', 'FWJ', 'HWJFYJI', 'JVZFQ', 'YMJ', 'KTTQ', 'YMJWJ', 'BFX', 'FSI', 'MJ', 'RFIJ', 'MNX', 'UWFDJW']]

abecedario=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
palabras_ing=['THE', 'BE', 'TO', 'OF', 'AND', 'A', 'IN', 'THAT', 'HAVE', 'I', 'IT', 'FOR', 'NOT', 'ON', 'WITH', 'HE', 'AS', 'COULD', 'YOU', 'DO', 'AT', 'THIS', 'BUT', 'HIS', 'BY', 'FROM', 'THEY', 'WE', 'SAY', 'HER', 'SHE', 'OR', 'AN', 'WILL', 'MY', 'ONE', 'ALL', 'WOULD', 'THERE', 'THEIR', 'WHAT', 'SO', 'UP', 'OUT', 'IF', 'ABOUT', 'WHO', 'GET', 'WHICH', 'GO', 'ME','MAKE','MAKES','VERY']
decodex=[]
respuestas=[]
valores=[]
for x in codices:
    for w in range(1,26):
        fradeco=''
        for y in x:
            paldeco=''
            for z in y:
                if z != '.':
                    codi=abecedario.index(z)
                    decodi=codi-w
                    paldeco+=abecedario[decodi]
                else:
                    paldeco+=z
            fradeco+=paldeco+' '
        palasdecos=fradeco.split()
        cont=0
        for a in palasdecos:
            for b in palabras_ing:
                if a == b:
                    cont+=1
                    #print(cont)
                    if cont == 2:
                        valor=w
                        #print(a,b,fradeco,cont)
                        valores.append(w)
                        respuestas.append(fradeco)
                        break

respuestas=list(respuestas)
respuesta=''
for x in range(len(respuestas)):
    X=respuestas[x].split()
    for y in range(0,3):
        respuesta+=X[y]+' '
    respuesta+=str(valores[x])+' '
        
print(respuesta)
