#Author: Sebastian Ochoa. Date: 08/17/2024
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
a = open('Ejercicios Code Abey\TXTs\e65 Transitive Closure on Candy States.txt','r')
P= a.readlines()

caminos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for y in range(len(f)):
        if y%2==0:
            F.append(f[y])
    caminos.append(F)

rutas=[]
for z in range(int(P[0])+2,int(P[0])+2+int(P[int(P[0])+1])):
    f=P[z].strip().split()
    F=[]
    for y in range(len(f)):
        if y%2==0:
            F.append(f[y])
    rutas.append(F)

print(caminos,rutas)
"""
caminos=[['Carnival', 'Troffle'], ['Honepy', 'Troffle'], ['Strobry', 'Cowsome'], ['Pikpak', 'Sugger'], ['Mocca', 'Honepy'], ['Mikliday', 'Cowsome'], ['Mikliday', 'Pikpak'], ['Maycorn', 'Troffle'], ['Sugger', 'Carnival'], ['Cowsome', 'Mocca'], ['Sugger', 'Mocca'], ['Troffle', 'Pikpak'], ['Mocca', 'Strobry']]
rutas=[['Sugger', 'Troffle'], ['Cowsome', 'Maycorn'], ['Pikpak', 'Mocca'], ['Mikliday', 'Sugger'], ['Strobry', 'Carnival'], ['Sugger', 'Strobry'], ['Troffle', 'Mocca'], ['Mikliday', 'Mocca'], ['Strobry', 'Troffle'], ['Cowsome', 'Carnival'], ['Mikliday', 'Strobry'], ['Cowsome', 'Troffle'], ['Sugger', 'Honepy'], ['Maycorn', 'Mocca']]

from collections import deque

def encuentra_camino_corto(caminos, inicio, destino):
    queue = deque([(inicio, 0)])  # Cola para BFS, con el estado inicial y distancia 0
    visited = set()  # Conjunto para mantener las posiciones visitadas

    while queue:
        current_state, dist = queue.popleft()

        if current_state == destino:
            return dist

        visited.add(current_state)

        for camino in caminos:
            if camino[0] == current_state and camino[1] not in visited:
                queue.append((camino[1], dist + 1))
            elif camino[1] == current_state and camino[0] not in visited:
                queue.append((camino[0], dist + 1))

    return 10000000  # Si no hay ruta

def encuentra_rutas(caminos, rutas):
    respuesta = ''

    for x in rutas:
        inicio, destino = x
        tamaño_camino_corto = encuentra_camino_corto(caminos, inicio, destino)
        respuesta += str(tamaño_camino_corto) + ' '

    return respuesta.strip()

print(encuentra_rutas(caminos,rutas))