#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Tickets in public transportation system have unique numbers. We have a funny superstition or omen about them:

If the sum of digits in the first half of number equals to sum of digits in the second half - such ticket is considered "Lucky" - one should at once recollect some long-wished dream and eat this ticket - then the dream surely will come to reality!

Number is split into halves of equal length, of course. If the number contains an odd amount of digits - the middle of them is simply ignored. So the numbers like 117234 or 4493278 are examples of lucky ones:

1 + 1 + 7 = 2 + 3 + 4 = 9
4 + 4 + 9 = 2 + 7 + 8 = 17   (3 is ignored)
Of course the number may have trailing zeroes, for example 6-digit numbers start from 000000, 000001 and end with 999998, 999999.

We are going to undertake a great reform - ministry of transportation wants to create tickets with new number format - it would contain N digits, each of them in numeral system with base B. Numeral systems of up to hexadecimal would be used (i.e. B <= 16) and numbers could be of up to 24 digits.

You are to count how much "lucky tickets" exist for given pair of N and B. You may safely assume that numbers with great value of N will use smaller values of B to simplify the matter for you.

Input data contains the number of test-cases in the first line.
Next lines contain a pair of values N and B each.
Answer should contain the amount of lucky tickets for each case:
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e109 Lucky Tickets.txt','r')
P= a.readlines()

tiquetes=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    tiquetes.append(F)

print(tiquetes)
"""
tiquetes=[[16, 3], [4, 16], [1, 11], [7, 3], [3, 3], [7, 8], [11, 2], [16, 5], [1, 12], [8, 5], [2, 10], [15, 2], [20, 2]]

def count_lucky_tickets(N, B):
    if N % 2 != 0:
        N -= 1 
    half_N = N // 2
    max_sum = half_N * (B - 1)
    dp = [1] + [0] * max_sum
    for _ in range(half_N):
        new_dp = [0] * (max_sum + 1)
        for s in range(max_sum + 1):
            for d in range(B):
                if s + d <= max_sum:
                    new_dp[s + d] += dp[s]
        dp = new_dp
    total_lucky_tickets = sum(x * x for x in dp)
    return total_lucky_tickets

respuesta=''
for x in tiquetes:
    respuesta+=str(count_lucky_tickets(x[0],x[1]))+' '
print(respuesta)