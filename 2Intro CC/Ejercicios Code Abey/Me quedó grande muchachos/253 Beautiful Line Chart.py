#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Imagine we want to output some line chart, representing the change of some value (like temperature or stock price) over sequence of days - but we have only text output (either alpha numeric display or printer). This was a common situation years ago - but even nowadays such problem happens when printing to text files, some kinds of electronics displays, POS-terminal paper slips etc.

Let's try to do this - for given sequence of values, print a chart in exactly 10 lines. Some auto-scaling needs to be done, of course: find the minimum and maximum value, and divide range between them into 10 equal subranges. For each value put an asterisk higher or lower, according to your subranges boundaries.

Input
The first line gives N - total amount of values.
The next line has these N values, space separated.

Answer should provide the chart in 10 lines, as explained above.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e253 Beautiful Line Chart.txt','r')
P= a.readlines()

f=P[1].strip().split()
valores=[]
for x in f:
    X=float(x)
    valores.append(X)

print(valores)
"""
valores=[7.637, 7.183, 6.562, 5.81, 4.99, 4.214, 3.621, 2.906, 2.165, 1.457, 0.837, 0.357, 0.068, 0.008, 0.197, 0.631, 1.273, 2.053, 2.864, 3.569, 3.986, 4.261, 4.843, 5.579, 6.361, 7.084, 7.645, 7.957, 7.961, 7.642, 7.037, 6.239, 5.386, 4.639, 4.146, 3.998, 3.799, 3.299, 2.573, 1.735, 0.932, 0.316, 0.016, 0.105, 0.58, 1.349, 2.249, 3.086, 3.686, 3.966, 4.006, 4.17, 4.622, 5.346, 6.233, 7.101, 7.746, 8.0, 7.782, 7.138, 6.231, 5.294, 4.551, 4.13, 4.004, 3.991, 3.846, 3.419, 2.683, 1.747, 0.826, 0.179]

def generate_line_chart(values):
    min_val = min(values)
    max_val = max(values)
    range_step = (max_val - min_val) / 9 
    levels = [min_val + i * range_step for i in range(10)]
    chart = [' ' * len(values) for _ in range(10)]
    
    for i, value in enumerate(values):
        level = 0
        for j in range(9):
            if value >= levels[j] and value < levels[j + 1]:
                level = j
                break
        else:
            level = 9

        chart[9 - level] = chart[9 - level][:i] + '*' + chart[9 - level][i+1:]

    for line in chart:
        print(line)

generate_line_chart(valores)