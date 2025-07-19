#Author: Sebastian Ochoa. Date: 02/29/2024

"""
Depending on your programming language syntax could be different and else part is almost always optional. You can read more in wikipedia article on Conditional statements.

Of two numbers, please, select one with minimum value. Here are several pairs of numbers for thorough testing.

Input data will contain number of test-cases in the first line.
Following lines will contain a pair of numbers to compare each.
For Answer please enter the same amount of minimums separated by space, for example:
"""

def minimo_de_2(lst: list)->str:
  menores=""
  for x in lst:
    menor=100000000000000000000000
    for y in x:
      if y<menor:
        menor=y
    menores+=str(menor)+" "
  menores=menores[:-1]
  return menores

print(minimo_de_2(
  [
    [2817319, 1662301],
    [1984668, -6724090],
    [180467, 6220600],
    [-9643211, 8837298],
    [-4362777, 3565965],
    [-2102696, -6092646],
    [4848333, -3381145],
    [-1909465, 7957994],
    [7377441, 5377203],
    [9247423, -3811744],
    [572979, 9650322],
    [-6768096, -5881366],
    [2861741, -2785465],
    [-3838721, -657347],
    [-4808139, 5552745],
    [581696, -5494863],
    [-2588245, -3443377],
    [1211378, 5523170],
    [209031, -1186213],
    [9212639, -6774655],
    [-4184888, -3346609],
    [-6673480, -6441758],
    [-1817174, -8316573],
    [-9716178, -2046210],
    [7717326, 5354236],
    [-3300629, 6704362],
    [-7237948, 9795483],
    [6733187, 5704800],
]))