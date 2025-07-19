#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
If you know the old game Bulls and Cows, this programming problem will look familiar to you.

Andrew and Peter play the code-guessing game. Andrew chooses a secret number consisting of 3 digits. Peter tries to guess it, proposing several values, one by one.

For each guess Andrew should answer how many digits are correct - i.e. are the same in the proposed value and in his secret number - and are placed in the same position. For example, if secret number is 125 and Peter calls 523, then Andrew answers with 1. Here is the sample of the game:

Andrew chooses a secret number 846

Peter's guess             Andrew's answer
      402                        0
      390                        0
      816                        2
      848                        2
      777                        0
      815                        1
      846                        3
So Peter have guessed correct number after 6 attempts.

You are to write program which reads guesses given by Peter (except the last) and prints out the secret number choosen by Andrew. It is guaranteed that exactly one solution exists.

Input data will contain number of guesses in the first line.
Then answers with attempts will follow - each contains the number told by Peter and the answer given by Andrew.
In contrast with examples numbers will be of 4 digits.
Answer should contain the secret number (also 4 digits).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e36 Code Guesser.txt','r')
P= a.readlines()

intentos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    intentos.append(f)

print(intentos)
"""
intentos=[['0632', '1'], ['2654', '0'], ['2617', '0'], ['4617', '0'], ['8634', '0'], ['4260', '0'], ['7072', '2'], ['7218', '0'], ['5606', '0'], ['7480', '0'], ['7028', '1'], ['3752', '1'], ['5181', '0'], ['1300', '0'], ['6991', '0']]

def check_guess(secret, guess):
    return sum(1 for s, g in zip(secret, guess) if s == g)

for secret in range(0, 10000):
    secret_str = str(secret).zfill(4)
    if all(check_guess(secret_str, guess) == int(bulls) for guess, bulls in intentos):
        resultado=str(secret_str)
        break
print(resultado)