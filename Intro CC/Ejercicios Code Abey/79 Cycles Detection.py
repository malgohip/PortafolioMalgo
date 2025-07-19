#Author: Sebastian Ochoa. Date: 08/19/2024
# -*- coding: utf-8 -*-

"""
The King of Ruritania seeks for a way to reduce funding on road maintenance in his kingdom.

Kingdom of Ruritania consists of several cities connected by several roads. Each road connects only two cities, and for any pair of cities there exists at least one way between them (the way could be a chain of several roads).

The King just have come to the bright idea - if there is any cycle (or loop) in the road network, then between some cities there exist more than one way (for example between two cities in this cycle you can travel either clockwise or counterclockwise) - so, obviously, at least one road could be removed and cities will nevertheless remain connected.

Your task is to help the King in finding whether the road map contains cycles or not.

Input data contains the amount of test-cases in the first line.
Next lines contain one road map each - it starts with the number of roads in this map followed by road descriptions in form A-B meaning that the road connects cities A and B (all places are named with a single capital letter).
Answer should have 0 for maps with no cycles and 1 for maps which could be "optimized". As usual, separate values with spaces.

Note: there will be no roads connecting the city to itself.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e79 Cycles Detection.txt','r')
P= a.readlines()

rutas=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    X=int(f[0])
    for y in range(1,X+1):
        F.append(f[y])
    rutas.append(F)

print(rutas)
"""
rutas=[['C-F', 'I-F', 'S-I', 'H-S', 'Q-C', 'G-Q', 'X-C', 'N-F', 'E-S'], ['O-J', 'Q-J', 'N-J', 'U-Q', 'Y-O', 'H-Y', 'K-Y', 'E-N', 'B-J', 'R-B', 'P-H', 'K-N'], ['Q-I', 'R-I', 'N-Q', 'P-I', 'E-P', 'S-N'], ['F-M', 'T-M', 'V-M', 'E-V', 'X-V', 'Q-F', 'P-T', 'S-P', 'K-S', 'H-X', 'J-M', 'R-E'], ['C-P', 'N-P', 'V-C', 'H-N', 'G-P', 'J-H', 'W-H', 'S-W', 'K-P', 'D-W', 'I-N', 'F-I'], ['M-G', 'W-G', 'I-W', 'F-G', 'P-F', 'B-M', 'N-M', 'A-G', 'Q-A', 'C-B', 'R-B'], ['D-A', 'V-A', 'U-D', 'T-A', 'S-U', 'C-V', 'X-V', 'I-D', 'O-X', 'D-U'], ['V-T', 'O-T', 'X-V', 'J-V', 'Z-T', 'L-V', 'M-X', 'C-Z', 'R-J', 'H-T'], ['R-D', 'M-R', 'S-M', 'V-M', 'Y-S', 'J-D', 'L-S', 'Z-Y', 'B-Z', 'F-L', 'X-B', 'Q-S', 'P-D', 'H-V', 'I-V', 'E-I', 'G-S', 'O-F', 'T-F', 'A-P', 'U-D', 'H-D'], ['A-U', 'P-U', 'M-A', 'J-P', 'X-A', 'N-U', 'Z-A', 'V-A', 'T-Z', 'C-T', 'O-C', 'G-C', 'A-J'], ['P-X', 'I-X', 'L-I', 'M-I', 'R-I', 'T-X', 'Z-T', 'W-P', 'O-Z', 'H-O', 'Y-W', 'C-P', 'S-I', 'J-P', 'G-H', 'F-T', 'K-W', 'V-K', 'A-R', 'Q-J', 'B-X', 'U-H', 'R-K'], ['K-H', 'L-H', 'S-K', 'F-K', 'Y-L', 'P-H', 'B-S', 'R-L', 'W-K', 'G-H', 'V-P', 'I-B', 'A-R', 'E-S', 'U-P', 'T-K', 'D-P'], ['Z-P', 'H-P', 'A-H', 'I-H', 'N-H', 'V-I', 'M-N', 'F-P', 'K-H', 'Y-Z', 'B-M', 'G-Y', 'U-I', 'E-B', 'Q-A', 'R-H', 'J-N', 'D-N', 'W-N', 'S-M'], ['A-R', 'O-R', 'Z-O', 'T-O', 'K-O', 'C-Z', 'L-K', 'Q-C', 'W-O', 'S-Q', 'B-C', 'F-T', 'G-B', 'E-G', 'M-E', 'J-A', 'I-M', 'N-S'], ['U-P', 'J-P', 'V-J', 'H-V', 'E-J', 'I-U', 'O-H', 'W-E', 'C-I', 'R-H', 'N-R', 'F-J', 'Y-C', 'Z-U', 'T-Y', 'X-P', 'D-O', 'A-E', 'K-F', 'B-Z', 'L-A', 'G-X'], ['P-Y', 'W-Y', 'E-Y', 'M-Y', 'L-P', 'X-E', 'I-E', 'R-E', 'U-M'], ['X-F', 'O-X', 'C-X', 'A-X', 'J-X', 'G-X', 'S-J', 'W-A'], ['H-R', 'Z-H', 'U-H', 'J-Z', 'M-U', 'V-R', 'O-J', 'P-Z', 'X-R', 'G-U', 'T-G', 'L-H', 'I-J', 'Q-T', 'A-G', 'C-M', 'D-X', 'Y-Q', 'S-L', 'N-D'], ['I-F', 'V-F', 'A-F', 'S-I', 'U-S', 'Q-U', 'R-V', 'X-Q', 'B-S', 'G-U', 'B-I'], ['B-J', 'M-B', 'S-J', 'V-B', 'X-J', 'P-B', 'L-M', 'K-L', 'T-V', 'O-T', 'Q-J', 'D-Q', 'F-O', 'I-O', 'Z-O', 'H-P', 'R-X', 'C-P', 'W-P', 'N-O', 'A-H', 'U-K']]

def es_ciclo(rutas):
    from collections import defaultdict
    graph = defaultdict(list)
    for ruta in rutas:
        start, end = ruta.split('-')
        graph[start].append(end)
        graph[end].append(start)
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    visited = set()
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

respuesta=''
for x in rutas:
    #print(x)
    if es_ciclo(x):
        #print(1)
        respuesta+='1 '
    else:
        #print(0)
        respuesta+='0 '
print(respuesta)