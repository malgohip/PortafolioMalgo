#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
As the official rendering clearly shows, CodeAbbey is surrounded by oak trees, which drop plenty of acorns. Many squirrels congregate on the grounds to eat those acorns.

This morning you observed a piteous scene: a tiny squirrel picked up an acorn and tried to bite into it, only to discover it couldn't. After a few minutes of trying, the squirrel gave up and hopped away.

That got you thinking. A particular squirrel can clearly bite into an acorn only if the strength of its jaws s is equal to or larger than the strength a required to break this acorn's shell.

According to the ancient tome you've obtained in the Abbey's library, the strengths of the acorns and of the squirrels can be obtained as the outputs of a Linear Congruential Generator with the following parameters: A = 7 ^ 5 = 16807, C = 0, and M = 2 ^ 31 - 1 = 2147483647, with a given seed value X (your puzzle input). You wonder how many pairs (acorn, squirrel) out of all possibilities would lead to the acorn being consumed.

Let's work through a simple example. Let's say your seed value is 1 and there are three acorns and three squirrels. The first three values produced by the generator are 16807, 282475249, 1622650073 - these are the acorns' strengths. The next three are 984943658, 1144108930, 470211272 - these are the squirrels' strength. Out of the 3 * 3 = 9 possible (acorn, squirrel) pairings, the following 6 satisfy the requirement of s >= a and will result in the squirrel eating the acorn:

16807, 984943658
16807, 1144108930
16807, 470211272
282475249, 984943658
282475249, 1144108930
282475249, 470211272
Feel free to check that if there are 10 acorns and 10 squirrels (using the same seed value 1), the total number of pairings where the squirrel cracks the acorn is 39 out of 100.

The problem, however, is that there are many acorns, and also many squirrels. Currently there are 316228 acorns on the ground, and also 316228 hungry squirrels hopping about. Also, since the little rodents are very hungry, you have just one minute to solve the problem after you are given your input data; please reload the page to get new input before calculating and submitting the answer.

The input is a single number: the seed for the pseudo-random generator (use the parameters A, C, and M listed above). Use the generator to return 316228 numbers (acorns' strengths), followed by 316228 more (squirrels' strengths). Please respond with a single number: the count of all possible pairings where the squirrel eats the acorn.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e291 Squirrels vs. Acorns.txt','r')
P= a.readlines()

codigo=int(P[0])

print(codigo)
"""
codigo=1437473734

def linear_congruential_generator(seed, a=16807, c=0, m=2147483647, count=632456):
    values = []
    x = seed
    for _ in range(count):
        x = (a * x + c) % m
        values.append(x)
    return values

def count_valid_pairings(acorns, squirrels):
    # Sort the strengths of acorns and squirrels
    acorns.sort()
    squirrels.sort()
    
    # Count valid pairings using a two-pointer technique
    valid_count = 0
    j = 0  # Pointer for squirrels
    
    for acorn in acorns:
        while j < len(squirrels) and squirrels[j] < acorn:
            j += 1
        valid_count += len(squirrels) - j
    
    return valid_count


acorns = linear_congruential_generator(codigo, count=316228)
squirrels = linear_congruential_generator(codigo, count=316228)

acorns_strengths = acorns[:316228]
squirrels_strengths = squirrels[:316228]

result = count_valid_pairings(acorns_strengths, squirrels_strengths)
print(result)