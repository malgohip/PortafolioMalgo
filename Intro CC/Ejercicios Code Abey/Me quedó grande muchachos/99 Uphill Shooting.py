#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
What reasons underlay the creation of the very first computers? It is not a secret that there were military interests.

The art of war yields many interesting problems in math, physics, logic etc. The calculations for ballistics are among them. Let us try to solve a simple task in this field.

The CodeAbbey is building the tank (i.e. armoured vehicle) able of firing the laughter - the main goal is to create the weapon of the peace. Now we are engaged in testing the prototype.

Today brethren conduct the experiments with shooting up the hill. The tank is brought before the ascending slope and shoots the bomb of joy against it.

We can measure both the initial velocity of the projectile and the angle of shooting. All we want to calculate is where the bomb should hit the slope - to check whether the real trajectory is similar to ideal one.

Technical details

Our tank is quite small, almost micro-tank, so you can safely assume that the trajectory starts from the point (0, 0).

The shooting range is 160 metres long and the slope is built of the large cubes having the side of 4 metres. So the profile of the slope is given by 40 integers, specifying the height of the pillar of the blocks, for example:

0 0 1 1 1 2 2
describes the slope of the following form:

                                        X X X X X X X X  8
                                        X X X X X X X X
                                        X X X X X X X X
                                        X X X X X X X X
                X X X X X X X X X X X X X X X X X X X X  4
                X X X X X X X X X X X X X X X X X X X X 
                X X X X X X X X X X X X X X X X X X X X 
                X X X X X X X X X X X X X X X X X X X X 
- - - - - - - - - - - - - - - - - - - - - - - - - - - -  0
0       4       8       12      16      20      24
You see that up to distance of 8 metres there are no blocks, then from mark 8 to 20 there are lying three blocks and in two next positions (from 20 and from 24) there are two stacks of two blocks.

The slope is never descending, so that integers in array will be in increasing order.

The acceleration due to gravitation is exactly 9.81 m / s^2 and the drag (the mechanical resistance of the air) should not be taken into consideration.

Tank is tested against 3 slopes and performs 3 shot at each.

Input data will contain three blocks.
Each block starts from the line of 40 integers describing the slope profile.
Then three lines follow describing three shots made - each contains V - initial velocity (m / s) and the angle of elevation of the barrel A expressed in degrees.
Answer should contain 9 integers - the distance at which the bomb hits the slope, rounded down.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e99 Uphill Shooting.txt','r')
P= a.readlines()

casos=[]
for x in range(len(P)):
    if x == 0 or x == 4 or x == 8:
        f=P[x].strip()
        casos.append(f)
    else:
        f=P[x].strip().split()
        F=[]
        for y in f:
            Y=int(y)
            F.append(Y)
        casos.append(F)

print(casos)
"""
casos=['0 0 0 0 0 1 2 3 3 3 4 4 4 5 5 5 6 6 7 7 8 8 8 8 9 9 9 10 11 12 12 13 13 13 14 14 15 15 16 16', [42, 70], [38, 37], [38, 48], '0 0 0 0 0 0 1 1 1 2 2 2 2 3 3 3 3 3 3 3 4 5 5 5 5 6 7 7 7 7 8 8 8 9 9 10 10 11 12 13', [43, 34], [43, 67], [33, 30], '0 0 0 0 0 1 1 1 1 1 2 2 3 3 3 4 5 6 7 7 8 9 10 10 11 11 11 12 13 13 14 14 14 14 14 14 15 15 16 17', [33, 39], [37, 66], [41, 62]]

import math

def degrees_to_radians(degrees):
    return degrees * math.pi / 180

def calculate_impact_distance(velocity, angle_degrees, slope_profile):
    g = 9.81
    angle_radians = degrees_to_radians(angle_degrees)
    time_of_flight = (2 * velocity * math.sin(angle_radians)) / g
    range_x = velocity * math.cos(angle_radians) * time_of_flight
    distance = int(range_x // 4) * 4
    block_index = distance // 4
    if block_index < len(slope_profile):
        slope_height = slope_profile[block_index] * 4
    else:
        slope_height = 0
    height_at_impact = (velocity**2 * (math.sin(angle_radians)**2)) / (2 * g)
    if height_at_impact <= slope_height:
        return distance
    else:
        return distance - 4

def process_cases(cases):
    results = []
    index = 0
    for _ in range(3): 
        slope_profile = list(map(int, cases[index].split()))
        index += 1
        for _ in range(3): 
            velocity, angle = cases[index]
            index += 1
            impact_distance = calculate_impact_distance(velocity, angle, slope_profile)
            results.append(impact_distance)
    return results

resultados = ''
for x in process_cases(casos):
    resultados+=str(x)+' '
print(resultados)