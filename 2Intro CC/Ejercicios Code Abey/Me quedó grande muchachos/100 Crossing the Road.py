#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Game Rules
There is a road consisting of several lines - see the demo above. The cars depicted as $ are travelling from right to left. The cars at topmost line have speed of 5 - i.e. they move 5 positions left on each turn. The cars at the second line have the speed of 6, at the third - 7 and so on. Symbols + mark the future position of each car for convenience (though at the current move these places are as empty as others, marked with -).

The distance between cars in the first line is 18 (i.e. there are 17 empty spaces between them), in the second - 19 and so on, also increasing by 1 with each line.

There is a guy trying to cross the road. He starts from the leftmost position of the first line. We use mark @ for him. At each move he can do one of three things: either step back to previous line (except when he is at the topmost of them), step forth to the next line, or stay where he is.

You can control guy with keys z to move forward, q to step back and a to stay for one turn.

After guy's move cars' positions are adjusted too. If at this point it appears that some car run over this unhappy person, he is smashed and dead. The game is over.

This condition is determined as follows - if before its move the car (on the same line with the guy) was at position x>=0 and after the move its position is x<=0 then the deadly accident have occured (suggesting that 0 is the coordinate of leftmost ends of lines, where guy crosses the road).

Player wins if the guy advances forth from the last line (i.e. to the sidewalk of the opposite side).

Play the demo a bit to understand the rules better - or consider the following example:

Initial position                             After the first move
@----------+----$------------+----$-----     ------+----$------------+----$----------
--+-----$------------+-----$------------     @-$------------+-----$------------------
------+------$------------+------$------     ------$------------+------$-------------
-+-------$------------+-------$---------     -$------------+-------$-----------------
-----+--------$------------+--------$---     -----$------------+--------$------------
--+---------$------------+---------$----     --$------------+---------$--------------
-----+----------$-----------------------     -----$------------+----------$----------
-+-----------$------------+-----------$-     -$------------+-----------$-------------
Problem statement
You will be given description of the initial position of the cars (only first car in each line since others follow at the known distance) - and you need to find out the minimum number of turns in which the game could be won.

For example, the game with initial position shown above could be solved in 19 turns (i.e. the 19-th step will bring the guy from the last line to safety on a sidewalk).

Note that in contrast with demo above, you will face a road with 11 lines to avoid giving you too easy task!

Input data will contain the number of games in the first line.
Then each line will give 11 values - starting positions of the closest car in each line.
Answer should give the minimum number of steps after which each game could be won or -1 if there is no winning sequence of moves.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e100 Crossing the Road.txt','r')
P= a.readlines()

numeros=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    numeros.append(f)

print(numeros)
"""
numeros=['12 11 11 18 18 18 21 22 10 5 4', '17 16 6 11 2 4 20 11 4 1 17', '13 6 11 7 16 18 23 7 4 3 17', '16 9 11 11 16 2 23 10 1 1 24', '17 6 17 5 7 5 1 15 22 26 23', '9 9 16 4 1 15 9 24 9 12 9', '10 17 17 9 18 18 4 5 3 15 4', '5 14 11 6 21 1 1 23 23 20 14', '7 7 17 2 5 6 15 17 22 6 15', '8 6 8 17 15 14 8 11 8 14 22', '12 8 11 13 14 16 23 10 24 3 3', '17 7 8 1 9 4 11 20 4 14 22', '16 13 14 16 5 5 3 21 18 25 25', '7 18 9 19 18 9 14 2 4 15 18', '13 14 6 12 14 1 10 15 25 23 21']

from collections import deque

def is_safe(car_positions, line, pos, distance, speed):
    # Verifica si la posición 'pos' en la línea 'line' está ocupada por un coche
    for car_start in car_positions[line]:
        # Verifica si el coche cubre la posición actual del personaje
        if (car_start - pos) % distance < speed:
            return False
    return True

def min_moves_to_win(start_positions):
    # Parámetros
    LINES = 11
    DISTANCE = [18 + i for i in range(LINES)]  # Distancias entre coches en cada línea
    speeds = [5 + i for i in range(LINES)]  # Velocidades de los coches
    
    # Cola BFS con (línea, posición, pasos)
    queue = deque([(0, 0, 0)])  # (línea, posición, movimientos)
    visited = set((0, 0))
    
    while queue:
        current_line, current_pos, steps = queue.popleft()
        
        # Verifica si el personaje ha salido del tablero
        if current_line == LINES:
            return steps
        
        # Actualiza las posiciones de los coches
        car_positions = []
        for line in range(LINES):
            speed = speeds[line]
            dist = DISTANCE[line]
            # Calcula las posiciones actuales de los coches en esta línea
            car_positions.append([(start_positions[line] - (speed * steps) + i * dist) % dist for i in range((dist // speed) + 1)])
        
        # Verifica si el personaje está a salvo
        if not is_safe(car_positions, current_line, current_pos, DISTANCE[current_line], speeds[current_line]):
            continue
        
        # Probar los movimientos posibles
        for move in [(-1, 0), (0, 1), (1, 0)]:  # (línea, posición)
            new_line = current_line + move[0]
            new_pos = (current_pos - move[1] * speeds[current_line]) % DISTANCE[current_line]
            if 0 <= new_line < LINES and (new_line, new_pos) not in visited:
                if is_safe(car_positions, new_line, new_pos, DISTANCE[new_line], speeds[new_line]):
                    visited.add((new_line, new_pos))
                    queue.append((new_line, new_pos, steps + 1))
    
    return -1  # Si no hay forma de ganar

def solve_game(input_lines):
    results = []
    for line in input_lines:
        start_positions = list(map(int, line.split()))
        result = min_moves_to_win(start_positions)
        results.append(result)
    return results

print(solve_game(numeros))