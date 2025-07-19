#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Once upon a time there was a famine in the country. Luckily the Friars of the CodeAbbey invented a device producing food from the solar or wind energy. That is how the land was saved.

This story gives us the task on usage of Priority Queue which can be implemented with either Binary Heap or a simple array (though inefficiently).

Imagine that about 10000 hungry visitors came to monastery during the day. Each has some degree of starvation expressed by the positive integer not exceeding 999.

New visitor arrives each second, so the first comes at the moment t = 0, next at the moment t = 1 etc.

Food machine also starts working at t = 0 and produces new ration each 2 seconds. The ration is given to one of the persons already arrived with the greatest degree of starvation.

So the example of beginning of the day may look like:

t = 0       - visitor with degree 5 arrives
t = 1       - visitor with degree 7 arrives
t = 2       - a unit of food is produced and is given to visitor with degree 7, he leaves
t = 2       - visitor with degree 2 arrives
t = 3       - visitor with degree 3 arrives
t = 4       - a unit of food is produced and is given to visitor with degree 5, he leaves
t = 4       - visitor with degree 8 arrives
...
Note that on even-numbered seconds monks at first distribute food among the visitors already waiting in the queue and only then receive a newcomer.

By and by the daily flow of people ends, so for example if N visitors are to come, then starting from t = N no more visitors are added to queue.

However food generator continues working at the same speed, until the last visitor is fed at t = 2 * N.

Friars are interested in improving the routine, so they want to calculate the "total discomfort" of starving people (and perhaps to find a way of reducing it). Your task is to help thim with this computation.

Total discomfort is the sum over each people of their personal discomforts, which in turn are expressed as:

personal_discomfort = starvation_degree * (feeding_time - arrival_time)
So for example if the visitor with degree 7 came at moment t = 1 and was fed at moment t = 2 his personal discomfort is

7 * (2 - 1) = 7
Another, with degree 5, arriving at t = 0 and fed on t = 4 has discomfort of 20, etc. Of course the degree of starvation does not increase during the day.

Data generation

You are to generate input data for this problem using Linear Congruential Generator with parameters A = 445, C = 700001, M = 2097152 - and initial value X0 will be given to you.

For each next visitor generate the random value and convert it using the formula:

starvation_degree = (rnd % 999) + 1
So you will only need the total amount of visitors N and the seed for random generator X0.

Input-Output Specification
Input data contain N - number of visitors and X0 - the seed for randomizer in a single line.
Answer should contain a single value - total discomfort of people who come this day to Abbey.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e93 Starving Priority Queue.txt','r')
P= a.readlines()

comandos=[]
f=P[0].strip().split()
for x in f:
    X=int(x)
    comandos.append(X)

print(comandos)
"""
comandos=[10667, 30]

import heapq

def generate_starvation_degrees(N, X0):
    A = 445
    C = 700001
    M = 2097152
    starvation_degrees = []
    X = X0
    for _ in range(N):
        X = (A * X + C) % M
        starvation_degrees.append((X % 999) + 1)
    return starvation_degrees

def calculate_discomfort(N, X0):
    starvation_degrees = generate_starvation_degrees(N, X0)
    heap = []
    total_discomfort = 0
    current_time = 0
    
    for i in range(N):
        heapq.heappush(heap, (-starvation_degrees[i], current_time))

        if current_time % 2 == 0 and heap:
            degree, arrival_time = heapq.heappop(heap)
            degree = -degree 
            discomfort = degree * (current_time - arrival_time)
            total_discomfort += discomfort
        
        current_time += 1

    while heap:
        if current_time % 2 == 0 and heap:
            degree, arrival_time = heapq.heappop(heap)
            degree = -degree
            discomfort = degree * (current_time - arrival_time)
            total_discomfort += discomfort
        
        current_time += 1
    
    return total_discomfort

resultado=calculate_discomfort(comandos[0],comandos[1])
print(resultado)