#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
https://www.codeabbey.com/index/task_view/life-is-simple
The game of Life by John Conway is played on a grid. At start we place several "organisms" into some cells (only one organism per cell), leaving other cells empty. Cells which are touching by side or corner are neighboring, so each organism may have from 0 to 8 neighbors.

After this, at each turn the colony of organisms evolve by the following rules:

any organism which have less than 2 or more than 3 neighbors will die (not passing to next turn);
at the same in each empty cell, which is surrounded by exactly 3 neighbor organisms, a new one is born.
It is important, that birth and dying are performed simultaneously. So when programming you need work like this:

mark all places where new life will be born;
mark all organisms which will die;
remove all marked organisms;
fill all marked empty cells with new organisms.
Instead of marking cells you can store their coordinates in two dedicated arrays or lists to process them later.

Let us see an example:

- - - - -      - - - - -      - - - - -
- - - - -      - - X - -      - - - - -
- X X X -  =>  - - X - -  =>  - X X X -
- - - - -      - - X - -      - - - - -
- - - - -      - - - - -      - - - - -
Here is a colony of 3 organisms. Obviously, at the first turn two of them (left and right) should die. However, before dying they will participate in giving birth to another two ones. Really, empty cells just above the central and just below it have exactly 3 neighbors. So after first turn the colony looks the same but rotated by 90°. Of course after second move the configuration will return to exactly such form as it was initially.

In this problem you will run the given configuration for 5 turns and print the number of organisms after each step.

Input data will contain 5 lines of 7 characters each. They represent a 5 by 7 fragment of the game field.
Dash characters "-" represent empty cells, while each "X" represent a cell containing a live organism.
Answer should contain 5 values separated by spaces - the amounts of live organisms after each turn.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e56 Life is Simple.txt','r')
P= a.readlines()

mundo=[]
for x in P:
    f=x.strip()
    f=list(f)
    mundo.append(f)

print(mundo)
"""
mundo=[['X', 'X', '-', '-', '-', '-', '-'], ['-', '-', 'X', '-', 'X', '-', 'X'], ['-', 'X', '-', '-', 'X', '-', 'X'], ['-', '-', '-', '-', '-', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', '-']]

def buscaminas(mapa):
    filas = len(mapa)
    columnas = len(mapa[0])
    resultado = [[0] * columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            contador = 0
            for x in range(max(0, i-1), min(filas, i+2)):
                for y in range(max(0, j-1), min(columnas, j+2)):
                    if mapa[x][y] == 'X':
                        contador += 1
            if mapa[i][j] == 'X':
                resultado[i][j] = contador-1
            else:
                resultado[i][j] = contador
    return resultado

respuesta=''
for a in range(0,6):
    #print(a)
    mapa_buscaminas=buscaminas(mundo)
    for x in range(len(mundo)):
        #print(f"{mundo[x]}\t{mapa_buscaminas[x]}")
        for y in range(len(mundo[x])):
            if mundo[x][y]=='-' and mapa_buscaminas[x][y] == 3:
                mundo[x].pop(y)
                mundo[x].insert(y,'X')
            elif mundo[x][y]=='X' and mapa_buscaminas[x][y] < 2 or mapa_buscaminas[x][y] > 3:
                mundo[x].pop(y)
                mundo[x].insert(y,'-')
    cont=0
    for b in mundo:
        for x in b:
            if x == 'X':
                cont+=1
    respuesta+=str(cont)+' '
print(respuesta)