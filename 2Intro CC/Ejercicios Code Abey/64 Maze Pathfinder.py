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
a = open('Ejercicios Code Abey\TXTs\e64 Maze Pathfinder.txt','r')
P= a.readlines()

j=P[0].strip().split()
J=[]
for x in j:
    X=int(x)
    J.append(X)
print(J)
laberinto=[]
for x in range(1,int(J[1])+1):
    f=P[x].strip()
    laberinto.append(f)

print(laberinto)
"""
laberinto=['11101010111111111111111110101110101', '00101010100010000000000000101000101', '11111110101011101011111011111111101', '00001010101000101010000000100010001', '11101010111010111110101011101111101', '10101000001010101000101010000010101', '10101010111110101111101011111010101', '10001010001000001010101000101000001', '11111011111011101010111111101111101', '00100000100000100010100000001010101', '11111011111010111110101111111010111', '00001000101010001000101010100000100', '10101111101011111110101010101111111', '10101000000000100000000000000010101', '10111010101011111111101111101110101', '10100010101000100000000000100010100', '10101010111011101111101011111110111', '10101010101010100010101000000010000', '11101111101010101010101011101111101', '10100010000000101000101010000000001', '10101111101110111110111011111010111', '10100010001000001010100010000010100', '10101010111110101011111110111011111', '00001010100000100010001010001010001', '10111011111110101110111010101011101', '10100000100000101010000000101000001', '11111111111111111011101111101010111', '10000000000010001000100010101010001', '11101111111110111011111110111111111']
J=[35, 29]

from collections import deque

def bfs(maze, start, target):
    width, height = len(maze[0]), len(maze)
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    queue = deque([start])
    visited = [[False] * width for _ in range(height)]
    parent = [[None] * width for _ in range(height)]
    
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == target:
            break
        
        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y, direction)
                queue.append((nx, ny))
    
    # Reconstruir el camino
    path = []
    x, y = target
    while (x, y) != start:
        px, py, direction = parent[x][y]
        path.append(direction)
        x, y = px, py
    
    return ''.join(reversed(path))

def compress_path(path):
    if not path:
        return ''
    
    compressed = []
    count = 1
    
    for i in range(1, len(path)):
        if path[i] == path[i-1]:
            count += 1
        else:
            compressed.append(f"{count}{path[i-1]}")
            count = 1
    
    compressed.append(f"{count}{path[-1]}")
    
    return ''.join(compressed)

def solve_maze(width, height, maze):
    start = (0, 0)
    paths = {}
    
    # Coordenadas para A, B y C
    A = (0, width - 1)
    B = (height - 1, 0)
    C = (height - 1, width - 1)
    
    # Encontrar caminos desde A, B, y C hacia X
    paths['A'] = bfs(maze, A, start)
    paths['B'] = bfs(maze, B, start)
    paths['C'] = bfs(maze, C, start)
    
    # Comprimir los caminos
    compressed_A = compress_path(paths['A'])
    compressed_B = compress_path(paths['B'])
    compressed_C = compress_path(paths['C'])
    
    return f"{compressed_A} {compressed_B} {compressed_C}"

print(solve_maze(J[0],J[1],laberinto))
