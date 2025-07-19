#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
Programming of game playing algorithms, like Chess, have two principal tasks:

assessing position, at least by checking which pieces could be taken;
constructing a kind of minimax algorithm to select a move leading to position with best value.
Let us start by solving a simple problem:

There is a chessboard with 8 x 8 squares. There are the White King and Black Queen on it. Check whether the Queen could take the King.

Remember - Queen could move to any distance vertically, horizontally or along any of two diagonals.

8  - Q - - - - - -     - - - - - - - -
7  - - - - Q - - -     - - - - - - Q -
6  - - - - - - - -     - - - - - - - -
5  - - - - - - - -     - - - Q - - - -
4  - K - - - - Q -     - - Q - - - - -
3  - - - - - - - -     - - - - - - - -
2  - - - Q - - - -     - - - - - K - -
1  - - - - - - - -     - Q - - - - - -
   a b c d e f g h     a b c d e f g h
See these two examples, with schematically drawn boards. On both the King is shown with letter K while marks Q shows variants of placing the Queen.

on the left scheme the King could be "eaten" by any of the four Queens;
on the right scheme the King is in safe position - none of the four Queens can move to take him.
Notice how the squares of the board are addressed. Columns (called files) are marked with latin letters from a to h, while rows (called ranks) are marked with digits from 1 to 8. So the King on the left diagram sits on the b4 square - and on the right diagram on the f2. We shall use this notation.

Input data contain the number of test-cases in the first line.
Next lines describe placement of the King and Queen for each testcase, by specifying their squares (King's first).
Answer should give only letter Y or N for each of test-cases, meaning that King could be taken or not respectively. Separate letters with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e53 King and Queen.txt','r')
P= a.readlines()

posiciones=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    posiciones.append(f)

print(posiciones)
"""
posiciones=[['d6', 'b5'], ['g5', 'b6'], ['g4', 'e3'], ['h5', 'b8'], ['f6', 'f1'], ['e4', 'g6'], ['b5', 'd7'], ['b5', 'b3'], ['a5', 'g3'], ['h3', 'd2'], ['h2', 'd1'], ['h3', 'h8'], ['e2', 'g8'], ['b6', 'f8'], ['c7', 'e1'], ['b3', 'g8'], ['f5', 'd2'], ['c6', 'c7'], ['h2', 'd4'], ['d5', 'f5']]

respuesta=''
for x in posiciones:
    if x[0][0] == x[1][0] or x[0][1] == x[1][1] or (ord(x[0][0])-int(x[0][1])) == (ord(x[1][0])-int(x[1][1])) or (ord(x[0][0])+int(x[0][1])) == (ord(x[1][0])+int(x[1][1])):
        respuesta+='Y'+' '
    else:
        respuesta+='N'+' '
print(respuesta)