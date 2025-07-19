#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
Quite a simple task - just to start learning strings...

Input data will contain a single string of small latin letters and few spaces.
Answer should contain the string of the same length with the same characters but in reverse order.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e30 Reverse String.txt','r')
P= a.readlines()

string=str(P[0].strip())

print(string)
"""
string='cactus stay turn fare jeopardy white yield job'

respuesta=''
for x in range(len(string)-1,-1,-1):
    respuesta+=string[x]
print(respuesta)