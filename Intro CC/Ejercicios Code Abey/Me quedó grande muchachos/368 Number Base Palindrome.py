#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Numbers which are palindromes read the same forwards and backwards. So 35453, 2992 and 6 are palindromes but 1121 is not. The number 178 is not a palindrome when written in base 10. However, when written in base 8 it becomes the palindrome 262. The number 5 is a single digit palindrome in base 10 but is the three-digit palindrome 101 in base 2. It can also be written as the two-digit palindrome 11 in base 4. Many integers can be written as palindromes in several different bases but all integers can be written as palindromes in some base. The trivial example of this is to write the integer N as the single-digit palindrome N. This can be done in any base which is larger than N. The palindromes are more interesting when they consist of more than one digit. The number 60 (base 10) is very interesting because it can be written as a multi-digit palindrome in no fewer than 6 different bases. (You may like to find them all) The smallest base in which 60 can be written as a multi-digit palindrome is base 9; when 60 is written as 66.

In this problem you will be given an integer N and are asked to find the smallest number base (greater than or equal to 2) in which the integer N can be written as a palindrome.

Input and Answer

The first line of the problem will be a single integer T denoting the number of test cases. Each of the following T lines will hold a single integer N. For each N you must find the smallest number base (greater than 1) in which N is written as a palindrome. Give these answers, separated by spaces, as a single string.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e368 Number Base Palindrome.txt','r')
P= a.readlines()

numeros=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    numeros.append(int(f))

print(numeros)
"""
numeros=[17, 48, 123, 498, 811, 5116, 7002, 27308, 133316, 293535, 1383745, 3488988, 10857547, 35415334, 101941487, 182468572, 1000584558, 3302828460, 6423117856, 25151717410, 87655613647, 108821067802]

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def to_base(n, b):
    """Convert a number n to a string representation in base b."""
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return ''.join(str(d) for d in digits[::-1])

def smallest_palindrome_base(n):
    """Find the smallest base >= 2 in which n is a palindrome."""
    base = 2
    while True:
        representation = to_base(n, base)
        if is_palindrome(representation):
            return base
        base += 1

def main(input_lines):
    """Process input lines and find the smallest base for each number."""
    T = int(input_lines[0])
    results = []
    for i in range(1, T + 1):
        N = int(input_lines[i])
        result = smallest_palindrome_base(N)
        results.append(result)
    return ' '.join(map(str, results))

# Ejecución
print(main(numeros))
