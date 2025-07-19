#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
This is a game for two players - you can find its variations in books about popular math.

Two players have a heap of M matches. Each player in turn should take up to K matches from it, thus reducing the heap. One who takes the last match - wins.

For example, here 5 matches and each player can take up to 3 in turn. The first player can win picking 1 match at first - then for any response of the opponent it is possible to secure all remaining matches.

"Inverse" variation of winning rule also exist - who takes the last match - loses the game.

Problem Statement
You will be told M and K and also whether the winning rule is "normal" or "inverted". Your opponent offers you to make the first move if you want. If you agree, you should tell which first move can secure a win for you (if further you play optimally).

Input data will contain amount of test-cases in the first line.
Each line contains integers M and K and also letter n for normal rules or i for inverted.
Answer should tell your first move for each case or 0 if you want your opponent to move first.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e184 Matches Picking.txt','r')
P= a.readlines()

movimientos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for y in range(len(f)):
        if y != 2:
            Y=int(f[y])
            F.append(Y)
        else:
            F.append(f[y])
    movimientos.append(F)

print(movimientos)
"""
movimientos=[[30, 4, 'i'], [160, 15, 'n'], [24, 6, 'i'], [83, 5, 'n'], [55, 13, 'n'], [105, 14, 'n'], [325, 19, 'i'], [171, 16, 'n'], [36, 2, 'i'], [201, 13, 'i'], [41, 9, 'i'], [306, 16, 'n'], [273, 16, 'i'], [237, 11, 'i'], [274, 8, 'n'], [341, 12, 'i'], [460, 16, 'i'], [159, 9, 'n'], [64, 6, 'i'], [88, 5, 'i'], [60, 8, 'n'], [243, 10, 'i'], [383, 13, 'i']]

def mejor_primer_mov(M, K, rule):
    if rule == 'n':
        if M % (K + 1) == 0:
            return 0 
        else:
            return M % (K + 1) 
    else:
        if (M - 1) % (K + 1) == 0:
            return 0  
        else:
            return (M - 1) % (K + 1)

respuesta=''
for x in movimientos:
    respuesta+=str(mejor_primer_mov(x[0],x[1],x[2]))+' '
print(respuesta)
