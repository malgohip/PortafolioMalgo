#Author: Sebastian Ochoa. Date: 02/29/2024
# -*- coding: utf-8 -*-

"""
To have more practice with conditional statements we are going to write a program which uses complex condition. I.e. one if ... else statement could be (and should be) nested inside other to solve this problem.

Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected minimums of triplets, separated by spaces.
"""

def minimo_de_3(lst: list)->str:
  menores=""
  for x in lst:
    menor=100000000000000000000000
    for y in x:
      if y<menor:
        menor=y
    menores+=str(menor)+" "
  menores=menores[:-1]
  return menores

print(minimo_de_3(
  [
    [7741222, -2048972, -4441060],
    [3972733, 4906024, 1419731],
    [-350932, 2607199, -6785662],
    [9115932, -4618618, -4209109],
    [-7234486, -4032554, -802070],
    [4188066, -4488101, -8540510],
    [-5189500, -59292, 7093454],
    [7286959, 8785694, -3628607],
    [-4823682, 6873677, 3603526],
    [9016280, -6396147, -6060220],
    [-7667361, -1417963, -3118812],
    [-4555903, -1968104, -5104140],
    [8812070, 3133421, 744956],
    [-280531, -5928900, 201519],
    [2709640, -9554291, 275868],
    [6327840, 4917907, 9829867],
    [8656370, -779076, -434582],
    [-5605396, 2725816, -6612911],
    [3531216, -7453779, 6771369],
    [358623, -5714774, 2070331],
    [8604593, -9337002, 1051702],
    [-4488937, 2314992, -9257194],
    [6658542, -1342853, 1117349],
]))