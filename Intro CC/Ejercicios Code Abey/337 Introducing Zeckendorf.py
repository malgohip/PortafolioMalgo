#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
The Fibonacci series is very well known. Every number in the series (except for the first two numbers) is the sum of the previous two numbers. The first two numbers are usually taken to be 0 and 1. However, for the purpose of this problem we will take the first two numbers to be 1 and 2. This creates the Fibonacci series 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

The Belgian mathematician Edouard Zeckendorf formulated an interesting theorem about the representation of integers as sums of Fibonacci numbers.

Zeckendorf's theorem states that every positive integer can be represented uniquely as the sum of one or more distinct Fibonacci numbers in such a way that the sum does not include any two consecutive Fibonacci numbers. For example, 50 = 3 + 13 + 34 is an allowed representation. Conversely 23 = 5 + 5 + 13 is not an allowed representation because of the repeated use of 5. 36 = 2 + 5 + 8 + 21 is also not an allowed representation because 5 and 8 are consecutive Fibonacci numbers.

In this problem you will be given some positive integers and are to represent each of these as a unique Zeckendorf sum. The numbers should be given in ascending order, separated by spaces. So the answer for 50 would be 3 13 34

Input/Output description: The first line of the input data will contain a single integer N, the number of values to convert.
N lines will follow. Each line contains a single number (less than 10^18). Convert the number to its Zeckendorf representation, in ascending order, separated by single spaces. Combine all answers into a single string, separated by spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e337 Introducing Zeckendorf.txt','r')
P= a.readlines()

numeros=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    numeros.append(int(f))

print(numeros)
"""
numeros=[2, 14, 820, 5811, 69691, 756976, 4917373, 32732277, 458470170, 2813796310, 12177068182, 346245889263, 7165253672597, 89521697040002, 285393426264328, 6465316540864119, 61479625299306213, 826199866944108666]

def generate_fibonacci_up_to(max_value):
    fibs = [1, 2]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > max_value:
            break
        fibs.append(next_fib)
    return fibs

def zeckendorf_representation(n, fibs):
    representation = []
    while n > 0:
        for fib in reversed(fibs):
            if fib <= n:
                representation.append(fib)
                n -= fib
                break
    return representation


max_number = max(numeros)
fibs = generate_fibonacci_up_to(max_number)
    
results = []
for number in numeros:
    representation = zeckendorf_representation(number, fibs)
    results.extend(sorted(representation))
    
print(" ".join(map(str, results)))