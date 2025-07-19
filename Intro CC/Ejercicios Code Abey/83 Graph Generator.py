#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
You may want to read about Graphs before approaching this and similar tasks.

For the task Dijkstra in the Network we will need to use a large graph to prevent you from using less efficient algorithms, like Floyd-Warshall's.

So we are going to use the graphs of about 1000 vertices. But where we are to take such amount of data? The good option is to create an algorithm which can generate them using the random sequence generator. Then if we use the same seed for randomizer we can reproduce the same graph easily.

Since it would be unfair to bereave you of writing such graph generator, let us detach it into this separate problem. Here is what you need to do to succeed with the task:

You will be given two values N - the amount of vertices (nodes) of the graph and X0 - the seed for random generator. We will mark vertices with numbers from 1 to N.
Use Linear Congruential Generator with parameters A = 445, C = 700001, M = 2097152 and initial value X = X0 - it will be passed with input data.
All the random numbers generated further should be transformed by formula Y = X % N + 1 - this will make them fit into range 1 ... N.
For each vertex from 1 to N you will then try to generate two edges connecting them to other random vertices and having random weights (lengths).
To accomplish this, for current vertex Vi (you will have a loop for i = 1 ... N) generate two pairs of random values V1 D1 V2 D2 and then connect Vi to V1 with an edge of weight D1 and to V2 with an edge of weight D2. All edges should be undirected (i.e. two-way).
Do not create edges connecting Vi with itself. Also do not create an edge from Vi to V1 or V2 if another edge already exists between them. Just skip them in both cases.
Let us study an example. Suppose you are given N = 10 and X0 = 0. The first few numbers you'll get from random generator are:

700001 1821950 1967079 1537772 1336989 68938 2017283 809880 ...
After you apply formula Y = X % N + 1 to them they are transformed into:

2 1 10 3 10 9 4 1 8 3 2 1 6 7 8 1 4 3 6 5 8 ...
Now for the 1-st vertex you get two pairs of numbers: 2 1 and 10 3 - this means that you make edges:

between 1 and 2 of the length 1
between 1 and 10 of the length 3
For the 2-nd vertex you get pairs 10 9 and 4 1 - i.e. you create edges:

between 2 and 10 of the length 9
between 2 and 4 of the length 1
So if you continue, you will get the graph described by following values:

1: 2-1 10-3
2: 1-1 3-1 4-1 8-9 10-9
3: 2-1 8-3
4: 2-1 5-3 6-7 8-1
5: 4-3 6-5
6: 4-7 5-5 8-7 9-7
7: 8-1 10-1
8: 2-9 3-3 4-1 6-7 7-1 10-7
9: 6-7
10: 1-3 2-9 7-1 8-7
Here for each of vertices from 1 to 10 you see a list of values in pairs - first number of the pair is the vertex to which the edge goes and the second is the weight of that edge. There are only 16 edges (each mentioned twice), because the 4 were skipped (two of them trying to connect vertices 6 and 10 to themselves).

Just such a graph is represented at the picture above (though weights of edges are not marked).

Input data contain only two values - number of vertices N and seed for random generator X0.
Answer should contain for each vertex in order the sum of weights of all edges incident to it.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e83 Graph Generator.txt','r')
P= a.readlines()

datos=[]
for x in range(len(P)):
    f=P[0].strip().split()
    for x in f:
        X=int(x)
        datos.append(X)

print(datos)
"""
datos=[19, 147]

def generate_graph_weights(N, X0):
    A = 445
    C = 700001
    M = 2097152

    X = X0
    edges = {i: {} for i in range(1, N+1)}
    
    for i in range(1, N + 1):
        X = (A * X + C) % M
        V1 = X % N + 1
        X = (A * X + C) % M
        D1 = X % N + 1
        
        X = (A * X + C) % M
        V2 = X % N + 1
        X = (A * X + C) % M
        D2 = X % N + 1
        if V1 != i and V1 not in edges[i]:
            edges[i][V1] = D1
            edges[V1][i] = D1
        if V2 != i and V2 != V1 and V2 not in edges[i]:
            edges[i][V2] = D2
            edges[V2][i] = D2
    weight_sums = [sum(edges[i].values()) for i in range(1, N + 1)]
    
    return weight_sums

respuesta=''
result = generate_graph_weights(datos[0], datos[1])
for x in result:
    respuesta+=str(x)+' '
print(respuesta)