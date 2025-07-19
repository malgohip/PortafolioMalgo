#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
If you solved the task about Neumann's Random Generator you are already aware that not all methods of generating pseudo-random sequences are good. Particularly, Neumann's method is not suitable for anything except programming exercises.

Here is the other method which is more widespread (it is implemented in most of programming languages and libraries) and still simple enough: let us start with some initial number and generate each new member Xnext of a sequence by the current Xcur using the following rule:

Xnext = (A * Xcur + C) % M
So we need three constants to define such a sequence (and an initial number). Not all combinations of constants are good (you may read details at Random Numbers), however, here are many good variants which allow to produce sequences with period of M, i.e. significantly long.

In this task we are going to build this algorithm to tell the value of n-th member of a sequence.

Input data will contain the number of test-cases in the first line.
Then test-cases will follow, each in separate line.
Test-case consists of five values: A, C, M, X0, N where first three are the same as in formula, while X0 is the initial member of a sequence and N is the number of a member which we want to calculate.
Answer should contain N-th member's value for each test-case, separated by spaces.If you solved the task about Neumann's Random Generator you are already aware that not all methods of generating pseudo-random sequences are good. Particularly, Neumann's method is not suitable for anything except programming exercises.

Here is the other method which is more widespread (it is implemented in most of programming languages and libraries) and still simple enough: let us start with some initial number and generate each new member Xnext of a sequence by the current Xcur using the following rule:

Xnext = (A * Xcur + C) % M
So we need three constants to define such a sequence (and an initial number). Not all combinations of constants are good (you may read details at Random Numbers), however, here are many good variants which allow to produce sequences with period of M, i.e. significantly long.

In this task we are going to build this algorithm to tell the value of n-th member of a sequence.

Input data will contain the number of test-cases in the first line.
Then test-cases will follow, each in separate line.
Test-case consists of five values: A, C, M, X0, N where first three are the same as in formula, while X0 is the initial member of a sequence and N is the number of a member which we want to calculate.
Answer should contain N-th member's value for each test-case, separated by spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e25 Linear Congruential Generator.txt','r')
P= a.readlines()

casos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    casos.append(F)

print(casos)
"""
casos=[[69, 458, 18685, 16358, 24], [1357, 91529, 54, 23, 12], [237, 735469, 6209, 2771, 5], [1139, 960, 82932, 65888, 16], [1307, 68197, 431564, 70309, 25], [1259, 230468, 24, 9, 24], [703, 8405, 60, 11, 12], [1633, 99502, 35, 14, 21], [1563, 2525, 7101, 5691, 17], [159, 857, 7, 0, 10], [1709, 813421, 79, 53, 3], [167, 38851, 8267, 4900, 5], [1953, 2125, 79, 46, 5], [49, 29, 7, 4, 15]]

resultado=''
for x in casos:
    Xcur = x[3]
    for _ in range(x[4]):
        Xcur = (x[0] * Xcur + x[1]) % x[2]
    resultado+=str(Xcur)+' '
print(resultado)