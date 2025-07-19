#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
The Travelling Salesman Problem, also known by abbreviation TSP has a very simple statement:

There is a Merchant (or Salesman) who wants to visit N cities (buying and selling goods there). The cities are connected by the network of roads of the known length. We want to find the path consisting of N-1 roads and visiting all N cities, which have minimum possible length.

Though the statement is short, the solution could be not that easy to find and implement. To demonstrate this, we'll try to create program solving the TSP on a small network of 20 cities.

You should start from city 0 and finish anywhere you like, but all 20 cities should be visited, path should be the chain of 19 roads and its length should be minimal. All roads would be bi-directional, i.e. graph is "undirected".

Input data contains 20 lines, each describing roads from the given city.
Every line will start with the number of the city it is describing (just for convenience).
Then several pairs of numbers will follow in the form T:L where T is the target city of the given road and L is its length.
Answer should contain 20 values describing the path - simply the numbers of the cities visited in proper order.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e102 Travelling Salesman.txt','r')
P= a.readlines()

caminos=[]
for x in range(len(P)):
    f=P[x].strip()
    caminos.append(f)

print(caminos)
"""
caminos=['0 1:90 19:22 18:25 5:45 16:81 17:87', '1 0:90 8:59 10:29 4:53 2:84 17:46', '2 7:34 1:84 3:32 5:97 9:43', '3 2:32 5:50 7:74 13:58 8:52 11:24 18:48', '4 1:53 7:82 13:18 11:10', '5 3:50 2:97 0:45 8:93 12:90 13:82 14:24 19:40', '6 14:63 12:31 10:75 15:35 16:41', '7 2:34 3:74 4:82 8:59 19:26 9:80 11:38', '8 1:59 5:93 7:59 3:52 13:72 11:64', '9 7:80 13:12 11:54 2:43 16:72 18:10', '10 1:29 6:75 12:87 19:56 17:72 13:89', '11 4:10 8:64 9:54 7:38 13:24 3:24 14:24 19:58', '12 6:31 10:87 5:90 19:58 17:90 13:89', '13 3:58 4:18 8:72 9:12 11:24 12:89 10:89 5:82', '14 6:63 19:10 5:24 11:24 17:77', '15 17:10 16:91 6:35', '16 15:91 0:81 6:41 9:72 19:39', '17 10:72 12:90 15:10 0:87 14:77 1:46', '18 0:25 19:12 9:10 3:48', '19 0:22 7:26 10:56 12:58 14:10 18:12 5:40 16:39 11:58']

def nearest_neighbor_tsp(graph, start=0):
    n = len(graph)
    visited = set()
    current_city = start
    path = [current_city]
    visited.add(current_city)
    
    while len(visited) < n:
        next_city = None
        min_distance = float('inf')
        
        for neighbor, distance in graph[current_city].items():
            if neighbor not in visited and distance < min_distance:
                next_city = neighbor
                min_distance = distance
        
        if next_city is None:  # Si no hay más vecinos no visitados, termina.
            break
        
        current_city = next_city
        visited.add(current_city)
        path.append(current_city)
    
    return path
    
graph = {}
    
for line in caminos:
    parts = line.strip().split()
    city = int(parts[0])
    graph[city] = {}
    for road in parts[1:]:
        target_city, length = map(int, road.split(':'))
        graph[city][target_city] = length
    
best_path = nearest_neighbor_tsp(graph)

    
print(" ".join(map(str, best_path)))