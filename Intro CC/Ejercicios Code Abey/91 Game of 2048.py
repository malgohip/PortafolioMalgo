#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Have you ever played 2048 Game? If no, then probably it is worth trying :)

Many programmers spend many hours on this (both instead of work and instead of sleep). However, though it is addictive enough it is still simple to code. And now we are going to try - and try to invent solution which does not look too clumsy.

You will be given a 4-by-4 field randomly covered with values 2 and 4 along with the sequence of player moves, specified with letters U for "up", D for "down", L for "left" and R for "right".

At each move all numbers at the field start sliding in a given direction and if two "tiles" with the same values are "pressed" against each other by this move, they combine producing a single tile with the sum value. Of course this frees one square of the board.

In case when more than 2 tiles with same numbers are so "pressing" in one line, firstly two "front" are combined, i.e. if moving "down" and we have 3 similar tiles in column, two lowest are joined.

For example:

initial         D            R            D

2 2 4 2      - - - -      - - - -      - - - -
4 2 2 4      2 2 4 2      - 4 4 2      - - 4 2
2 2 2 2      4 4 2 4      - 8 2 4      - 4 2 4
2 4 2 2      4 4 4 4      - - 8 8      - 8 8 8
Here three steps after initial position are shown - "down", "right" and "down". As you can see the last move joins nothing, only aligns tiles against the edge of the field.

Input data will contain initial setup - 4 lines of 4 values each.
The 5-th line will contain the sequence of moves.
Answer should contain the counts of tiles of each kind after these moves, in order - i.e. first the amount of 2-s, then amount of 4-s etc.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e91 Game of 2048.txt','r')
P= a.readlines()

tablero=[]
for x in range(len(P)-1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    tablero.append(F)
f=P[4].strip().split()
tablero.append(f)
        
print(tablero)
"""
tablero=[[4, 2, 2, 2], [4, 4, 4, 2], [4, 2, 4, 4], [4, 2, 4, 2], ['U', 'U', 'D', 'L', 'L', 'D', 'D', 'U', 'L']]

movimientos=tablero.pop(-1)

def deslizar_mezclar(fila):
    fila_nueva = [num for num in fila if num != 0]
    for i in range(len(fila_nueva) - 1):
        if fila_nueva[i] == fila_nueva[i + 1]:
            fila_nueva[i] *= 2
            fila_nueva[i + 1] = 0
    fila_nueva = [num for num in fila_nueva if num != 0]
    return fila_nueva + [0] * (len(fila) - len(fila_nueva))

def mover_izq(tablero):
    return [deslizar_mezclar(fila) for fila in tablero]

def mover_der(tablero):
    return [deslizar_mezclar(fila[::-1])[::-1] for fila in tablero]

def transponer(tablero):
    return [list(fila) for fila in zip(*tablero)]

def mover_ar(tablero):
    transpuesto = transponer(tablero)
    movido = mover_izq(transpuesto)
    return transponer(movido)

def mover_ab(tablero):
    transpuesto = transponer(tablero)
    movido = mover_der(transpuesto)
    return transponer(movido)

def count_tiles(tablero):
    from collections import Counter
    flat_tablero = [num for fila in tablero for num in fila]
    counts = Counter(flat_tablero)
    max_tile = max(counts)
    return [counts.get(2 ** i, 0) for i in range(1, max_tile.bit_length() + 1)]

def juega_2048(tablero, movimientos):
    for move in movimientos:
        if move == 'L':
            tablero = mover_izq(tablero)
        elif move == 'R':
            tablero = mover_der(tablero)
        elif move == 'U':
            tablero = mover_ar(tablero)
        elif move == 'D':
            tablero = mover_ab(tablero)
    
    return count_tiles(tablero)

tablero=juega_2048(tablero,movimientos)
for x in range(len(tablero)-1,0,-1):
    if tablero[x] == 0:
        tablero.pop()
    else:
        break

respuesta=''
for y in tablero:
    respuesta+=str(y)+' '
print(respuesta)