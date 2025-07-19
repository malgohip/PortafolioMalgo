#Author: Sebastian Ochoa. Date: 08/19/2024
# -*- coding: utf-8 -*-

"""
Many computer games are played by moving some pieces or heroes over a map or a field of some kind. There are two popular kinds for geometry of such maps:

rectangular grid - the field is tiled by rectangles or squares;
hexagonal grid - the field is tiled by hexagons.
Well-known game Heroes of Might and Magic for example utilized both variants - rectangular grid is used on the world map while riding between castles (with ability of diagonal movements), while hexagonal grid is used as a battle field in combat mode.

Hexagonal tiling looks more beautiful for user, but the programming its geometry is slightly more tricky. That is what we are going to practice now.

Problem statement

Suppose the "hero" is placed at some cell of hexagonal grid. Then he can move in six directions. On the picture above X marks the initial cell and letters A, B, C, D, E, F - the possible movements for 1 step. A moves the hero directly to the right and other directions are named in the counter-clockwise order.

You will be given a sequence of steps, performed by hero, each step described by a corresponding letter. You are to tell after all these steps, how far the hero is now from his initial position (measured by straight line, i.e. "Euclidean distance").

We agree that the hero is always placed at the center of the cell and that distance between centers of two adjacent cells (i.e. sharing a side) is 1.0.

Input data will contain number of test-cases in the first line.
Next lines will contain the sequence of steps (one sequence per line) as a string of letters.
Answer should contain the distances between starting and ending point for each of sequences, separated by spaces and with accuracy of 1e-7 at least.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e73 Hexagonal Grid.txt','r')
P= a.readlines()

movimientos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    movimientos.append(f)

print(movimientos)
"""
from math import sqrt
movimientos=['AFEEDBDECBAAF', 'ACECEBAECAAEEAD', 'FBCADFDBFEECCDBECCADBCCEFED', 'EECBDAEECCBFCDBADBFDDBE', 'BACFEDBFACBCBADAEFADFECCACEFFBAE', 'DFBEFAFAECDA', 'BFBFCBBCBCFCFEDFFAFFE', 'BBC', 'ABBCBCAEBAFF', 'EEFBCDCFCDBCBD', 'DBAEBDCFBAEECFEBEBCFEEC', 'BDCECBACC', 'EFAF', 'CFEEBBECDECAEDBFECCDBFEEAAAD', 'DAFFCEBCBCDFCFAEDBDACFFAAAABD', 'FFEEBEDEACFCEAEEBDFDEDFBBB', 'EADECEDFEDBD', 'BDACADEDDECFECDFCCAAECBFD', 'CEDBEADCEEEAAAAEEADCBF', 'ABACBEAFAEDEEFFBFDFDBEE', 'BFEAEEDDCBFFBE', 'DBBE', 'ABABAACAFAC']

def distancia_hexagonal(movimientos):
    x, y = 0.0, 0.0
    for movimiento in movimientos:
        if movimiento == 'A':
            x += 1
        elif movimiento == 'B':
            x += 0.5
            y += sqrt(3) / 2
        elif movimiento == 'C':
            x -= 0.5
            y += sqrt(3) / 2
        elif movimiento == 'D':
            x -= 1
        elif movimiento == 'E':
            x -= 0.5
            y -= sqrt(3) / 2
        elif movimiento == 'F':
            x += 0.5
            y -= sqrt(3) / 2
    return sqrt(x**2 + y**2)

def calcular_distancias(test_cases):
    distancias = []
    for movimientos in test_cases:
        distancias.append(f"{distancia_hexagonal(movimientos):.7f}")
    return " ".join(distancias)

print(calcular_distancias(movimientos))