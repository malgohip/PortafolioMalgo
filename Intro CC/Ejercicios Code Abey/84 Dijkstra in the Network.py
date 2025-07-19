#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Dijkstra's algorithms solves very popular task - it allows to find the sortest paths from the given node of a graph to all other nodes.

Of course this can find applications in logistics etc., but far more common usage is in communication networks.

For example, think of Zig-Bee network, consisting of N modules. These small devices are capable of determining the shortest route to destination extremely fast, notwithstanding that the network geometry can change over time - some modules can go offline, some other could be installed on vehicles etc. So most routers in almost every network technology utilize this method or some derivative (like A*).

In this task you are to implement Dijkstra's algorithm - the details you can find in the corresponding Wikipedia article.

The simplest form (without min-priority queue) would be sufficient.

The graph is described the same way as in Graph Generator problem - by specifying the number of vertices and the seed for randomizer.

For example, if we use the same graph with 10 nodes and initialize random generator with the same seed 0 and will run the Dijkstra's algorithm starting from node 1, we'll get the following paths to each of destinations:

dest.          path            length
  1            1                  0
  2            1-2                1
  3            1-2-3              2
  4            1-2-4              2
  5            1-2-4-5            5
  6            1-2-4-6            9
  7            1-2-4-8-7          4
  8            1-2-4-8            3
  9            1-2-4-6-9         16
  10           1-10               3
The tree of these paths is marked with green lines in the picture above.

Input data will contain three numbers N - the number of nodes, X0 - seed for random generator and S the index of starting vertex (from where we are to search for paths to others).
Answer should contain the route length to each vertex in the graph.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e84 Dijkstra in the Network.txt','r')
P= a.readlines()

datos=[]
for x in range(len(P)):
    f=P[0].strip().split()
    for x in f:
        X=int(x)
        datos.append(X)

print(datos)
"""
datos=[1043, 535, 710]

import heapq

def generar_grafo(N, X0):
    A = 445
    C = 700001
    M = 2097152

    X = X0
    aristas = {i: {} for i in range(1, N+1)}
    
    for i in range(1, N + 1):
        X = (A * X + C) % M
        V1 = X % N + 1
        X = (A * X + C) % M
        D1 = X % N + 1
        
        X = (A * X + C) % M
        V2 = X % N + 1
        X = (A * X + C) % M
        D2 = X % N + 1
        
        if V1 != i and V1 not in aristas[i]:
            aristas[i][V1] = D1
            aristas[V1][i] = D1
        
        if V2 != i and V2 != V1 and V2 not in aristas[i]:
            aristas[i][V2] = D2
            aristas[V2][i] = D2

    return aristas

def dijkstra(grafo, inicio):
    N = len(grafo)
    distancia = {i: float('inf') for i in range(1, N + 1)}
    distancia[inicio] = 0
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
        distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancia[vertice_actual]:
            continue
        
        for veci, tamaño in grafo[vertice_actual].items():
            distance = distancia_actual + tamaño
            
            if distance < distancia[veci]:
                distancia[veci] = distance
                heapq.heappush(cola_prioridad, (distance, veci))
    
    return [distancia[i] for i in range(1, N + 1)]

respuesta=''
grafo = generar_grafo(datos[0], datos[1])
result = dijkstra(grafo, datos[2])
for x in result:
    respuesta+=str(x)+' '
print(respuesta)