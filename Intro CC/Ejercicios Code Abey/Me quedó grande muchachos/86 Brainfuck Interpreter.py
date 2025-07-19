#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
We are going to make extension for our site - to add problems which should be solved in Brainfuck programming language.

But of course we need an executing system (interpreter) for this funny esoteric language.

In this problem you should create such interpreter. Do not be afraid - it is easier to write Brainfuck interpreter itself than to write Brainfuck problems for such interpreter.

We ask you to implement slightly altered version of the language - Brainfuck++ which includes two additional comandos ; and :.

Please, refer to the wiki article by the link above to read specification of the language.

Input data will contain two lines.
The first input line contains Brainfuck program without any spare characters.
The second line contains a sequence of numbers which would be consumed as input.
Answer should contain output of the program.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e86 Brainfuck Interpreter.txt','r')
P= a.readlines()

simbolos=[]
for x in range(len(P)):
    if x == 0:
        f=P[x].strip()
        simbolos.append(f)
    elif x == 1:
        f=P[x].strip().split()
        F=[]
        for x in f:
            X=int(x)
            F.append(X)
        simbolos.append(F)

print(simbolos)
"""
"""
simbolos=[';>;<:>:<[>+<-]>:<[>+<-][->+>+<<]>>[-<<+>>]<<[->+>+<<]>>[-<<+>>]<<[->+>+<<]>>[-<<+>>]<<>;<[->+>+<<]>>[-<<+>>]<<>;<>++++<+++:>;<[->++<][->+>+<<]>>[-<<+>>]<<>;<>:<;[->+>+<<]>>[-<<+>>]<<>;<[->++<]>-<;;:>;<+:>-:<[->++<]>;<[->+<][->+<][>+<-]+:>-:<>-<;>:<[->+>+<<]>>[-<<+>>]<<>:<>-<>++++<>++++<[>+<-][->+<][->+>+<<]>>[-<<+>>]<<>;<+:>-:<:>:', [9, 14, 10, 9, 19, 15, 9, 10, 11, 4, 9, 14, 2, 18]]

cinta = [0] * 30000
apuntador = 0
input_apuntador = 0
output = []
salto_adelante = {}
salto_atras = {}
ciclo_staxx = []
for i, comando in enumerate(simbolos[0]):
    if comando == '[':
        ciclo_staxx.append(i)
    elif comando == ']':
        inicio = ciclo_staxx.pop()
        salto_adelante[inicio] = i
        salto_atras[i] = inicio
i = 0
while i < len(simbolos[0]):
    comando = simbolos[0][i]
    
    if comando == '>':
        apuntador += 1
    elif comando == '<':
        apuntador -= 1
    elif comando == '+':
        cinta[apuntador] = (cinta[apuntador] + 1) % 256
    elif comando == '-':
        cinta[apuntador] = (cinta[apuntador] - 1) % 256
    elif comando == '.':
        output.append(str(cinta[apuntador]))
    elif comando == ',':
        if input_apuntador < len(simbolos[1]):
            cinta[apuntador] = simbolos[1][input_apuntador]
            input_apuntador += 1
    elif comando == ';':
        if input_apuntador < len(simbolos[1]):
            cinta[apuntador] = (cinta[apuntador] + simbolos[1][input_apuntador]) % 256
            input_apuntador += 1
    elif comando == ':':
        output.append(str(cinta[apuntador]))
    elif comando == '[':
        if cinta[apuntador] == 0:
            i = salto_adelante[i]
    elif comando == ']':
        if cinta[apuntador] != 0:
            i = salto_atras[i]
    print(f"Comando: {comando}, Apuntador: {apuntador}, Cinta[{apuntador}]: {cinta[apuntador]}, Input Apuntador: {input_apuntador}, Output: {' '.join(output)}")
    i += 1
print(" ".join(output))