#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
This is an old game for two players, often played with paper and pen. Modern version is also known as Mastermind.

First player, let it be Alice - chooses a secret 4-digit code (like 1492), with all digits different.

The second player, let it be Barbara - makes several attempts to guess this code. She can offer any combinations of 4 digits (without repetitions) - and for each attempt the Alice should answer with a hint.

The hint consists of two values:

first tells how many digits are guessed correctly and are in correct positions;
second tells how many digits are guessed correctly but are in wrong positions.
For example, if the secret value is 1492 and Barbara's guess is 2013 - Alice should answer with 0-2.
And if the guess is 1865, then the hint would be 1-0.

This game could also be played with 4-letter words, but in this case it may require the knowledge of the language.
Further information could be found in the dedicated wikipedia article.

Problem statement
Your goal is to write a program which calculates the values which should be told as a hint to the given guess.

Input data will contain the secret value and the number of guesses in the first line.
Second line will contain the specified amount of guesses.
Answer should contain hints for these guesses, they should be given in format X-Y and separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e59 Bulls and Cows.txt','r')
P= a.readlines()

numeros=[]
for x in range(len(P)):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    numeros.append(F)
numeros[0].pop()

print(numeros)
"""
numeros=[[9864], [2315, 3428, 4216, 9812, 2463, 4235, 8362, 6594, 6938, 8941, 4865, 9314, 4593]]

def digitos (num):
    digs=[int(digito) for digito in str(num)]
    return digs

respuesta=''
digs_sec=digitos(numeros[0][0])
for x in numeros[1]:
    digs_inte=digitos(x)
    picas=0
    fijas=0
    vistos=[]
    for i in range(0,4):
        if digs_sec[i] == digs_inte[i]:
            fijas+=1
        else:
            vistos.append(digs_sec[i])
    for i in range(0,4):
        if digs_sec[i] != digs_inte[i] and digs_inte[i] in vistos:
            picas+=1
            vistos.remove(digs_inte[i])
    respuesta+=str(fijas)+'-'+str(picas)+' '
print(respuesta)
    