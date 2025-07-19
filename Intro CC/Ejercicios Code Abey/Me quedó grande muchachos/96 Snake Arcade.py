#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
The Snake game is known since 1970-s: the snake is creeping through the field, eating food and avoiding collisions with itself and with borders.

In this problem you are to write program which simulates this game. You will be given the initial field setup and the chain of moves performed by the snake.

You should determine at which step and which point the snake will collide with itself.

The field will be given in the following form:

X X X - - - - - $ - - - - - $ - - $ $ - -
$ - - - - - - - - $ - - $ $ - - $ - $ - -
$ - - $ - $ $ - - - - - - - $ - - - - - -
- $ - - $ - - $ - - - - - $ $ $ $ $ - $ $
$ - - - $ $ - - - - - - - - - - - $ - - -
- $ $ - - - - - - - - - - - - $ - - - - $
$ - - - - - - - - $ - - - - - $ $ - - - -
$ - - - $ - - $ $ - - - $ - $ $ - - - - -
- - - - $ $ - - - - - - $ $ - - - - - - $
- $ - - - $ - - - - - - - $ - - - - $ - $
- - - - - $ - $ - - - - - $ $ - - - - - -
- - - - - $ - - $ - - $ - - - - - - - - $
- - $ - - $ - - - - - - $ - - - $ - - $ -
It will always be of the 21 x 13 size and the snake will always have the size 3 and will start from the top-left corner, moving initially to the right.

The sequence of moves will look like:

12 D 4 L 10 U 1 R 6 D 7 R 9 U 9 L 16
this should be read as:

make 12 steps (advance 1 cell each time);
turn "head" down (without making step);
make 4 steps more;
turn left;
make 10 steps;
turn up;
make 1 step;
turn right;
make 6 steps;
and so on...
With each step the snake moves its head to the adjacent cell according to current direction, and then draws its tail from its last position (so after the 1-st step the cell (0,0) becomes empty etc.) Note that the "turn of the head" does not make a step - it does not change the length or position of the snake, it is an "imaginary" operation (though if we print the head cell differently according to where the snake is looking to - we'll see the change).

However, if at the current step the snake advances to the cell containing the food (marked with $ sign) it does not remove its "tail" from the last cell so that its length is increased by 1 (since the "head" moves anyway).

input data will contain 13 lines depicting 21 cells each with marks - for empty cells, $ for food and X for cells occupied with snake.
Next line will contain the sequence of steps as described above (numbers and letters U, D, L, R).
Answer should contain X and Y coordinates of the cell where snake collides with itself and then N - the number of steps befor collision occured.

Notes

the snake will never hit the border, you need not check this;
coordinates start from 0 and the origin is in the top left corner (as usual in computer graphics);
the chain of moves will contain several more elements even after snake collides with itself - and even can collide with itself once more - but you should register the first collision!
Example:

input data:
X X X - $ - - $ $ - $ $ $ - - - - - - - $
- - - $ - - - - - - - $ - - - - - $ $ $ -
$ $ $ - - - - - $ - - - - $ $ - - - - $ $
- $ - - - - - - $ $ - - - $ - - $ - - - -
- $ $ - - - - $ - - - $ - - - - - - - - -
$ - - $ - - $ - - $ - $ - - - - - - - - -
- - - - - $ - - - - - - $ - - - - $ - - $
- - - - - $ $ - $ - - $ - - - - $ $ - - -
- $ - - - - - $ - $ - $ - - - - - - $ - -
- $ $ - $ - - - - - - - $ - - - $ - $ - $
- - - - - - - - - - - - - - $ $ $ - - - -
- - - $ - - - - - - - - - $ - - - $ - - $
- - - - - - - - - $ - - - - - - $ $ $ - -
5 D 1 L 1 U 1 L 3

answer:
6 0 8
In this example after the first 6 moves the picture will look like:

- - - - X X X X $ - $ $ $ - - - - - - - $
- - - $ - - - X - - - $ - - - - - $ $ $ -
$ $ $ - - - - - $ - - - - $ $ - - - - $ $
- $ - - - - - - $ $ - - - $ - - $ - - - -
- $ $ - - - - $ - - - $ - - - - - - - - -
$ - - $ - - $ - - $ - $ - - - - - - - - -
- - - - - $ - - - - - - $ - - - - $ - - $
- - - - - $ $ - $ - - $ - - - - $ $ - - -
- $ - - - - - $ - $ - $ - - - - - - $ - -
- $ $ - $ - - - - - - - $ - - - $ - $ - $
- - - - - - - - - - - - - - $ $ $ - - - -
- - - $ - - - - - - - - - $ - - - $ - - $
- - - - - - - - - $ - - - - - - $ $ $ - -
You may see that the snake has eaten 2 units of food and now have length of 5.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e96 Snake Arcade.txt','r')
P= a.readlines()

mapa=[]
for x in range(len(P)):
    f=P[x].strip()
    mapa.append(f)

print(mapa)
"""
mapa=['X X X $ - - - - - $ - - - $ - $ - - - $ -', '$ - - - - - - $ $ - - - - $ - - - - - - $', '- - - - - $ - - $ - - $ - - $ - - $ - $ -', '$ - $ - - - $ $ - - - - - - - - - - $ $ -', '- - - $ $ - - $ - - - $ - - - $ - $ - - -', '$ - - - - - - - - - - $ - - - - - - - $ -', '- - - $ - $ $ - - $ - - $ $ $ - $ - - $ -', '- - - - - $ - $ - - - - $ - - - - $ - - -', '- - $ - - - $ - - - - $ $ - - - $ - $ $ -', '- - - - - - - - - $ - - - - $ $ - - - - -', '- $ - - $ - - - - - - - - - - - - - - - $', '- - $ $ $ - - - - - - - $ $ - - - - - - $', '- - - - - - - - - $ - - $ - - - - $ - $ -', '16 D 7 L 1 D 1 L 4 U 5 R 5 U 3 L 1 D 11 L 6 U 10']

movimientos=mapa.pop(-1)

from collections import deque

def simulate_snake_game(field, moves):
    grid = [list(row) for row in field]
    snake = deque([(0, 0), (0, 1), (0, 2)])
    direction = (0, 1)
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    def is_valid(x, y):
        return 0 <= x < 13 and 0 <= y < 21
    index = 0
    steps = 0
    while index < len(moves):
        if moves[index].isdigit():
            step_count = int(moves[index])
            for _ in range(step_count):
                head_x, head_y = snake[-1]
                new_head_x = head_x + direction[0]
                new_head_y = head_y + direction[1]
                if not is_valid(new_head_x, new_head_y):
                    return None
                
                if (new_head_x, new_head_y) in snake:
                    return new_head_x, new_head_y, steps + 1
                snake.append((new_head_x, new_head_y))
                if grid[new_head_x][new_head_y] == '$':
                    grid[new_head_x][new_head_y] = '-'  
                else:
                    snake.popleft()
                
                steps += 1
        else:
            direction = directions[moves[index]]
        
        index += 1
    
    return None


move_list = []
current_move = ""
for char in movimientos:
    if char.isdigit():
        current_move += char
    else:
        if current_move:
            move_list.append(current_move)
            current_move = ""
        if char != ' ':
            move_list.append(char)
if current_move:
    move_list.append(current_move)

collision = simulate_snake_game(mapa, move_list)
if collision:
    print(f"{collision[0]} {collision[1]} {collision[2]}")
else:
    print("No collision detected")    