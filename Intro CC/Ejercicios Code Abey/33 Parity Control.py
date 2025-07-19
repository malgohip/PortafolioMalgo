#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
Anna lives at Algol and Bob lives at Betelgeuse. Long distance separates them since these stars are in different constellations - Perseus and Orion.

They found a way to communicate via e-mail. However, due to big distance, some letters could be changed during transmission. Simple form of error-checking is proposed by Anna:

All letters are transmitted in usual ASCII code, one byte per symbol. Each byte consists of 8 bits, but the highest bit is not used for English language - it is normally always 0.

Let us set this bit to either 0 or 1 in order that sum of bits in the whole byte is always even (2, 4, 6 or 8). That is how some letters are encoded:

symbol     ascii-code     binary     num-of-bits    encoded-binary   encoded-dec

 'A'           65        01000001         2            01000001           65
 'B'           66        01000010         2            01000010           66
 'C'           67        01000011         3            11000011          195
 '.'           46        00101110         4            00101110           46
 ' '           32        00100000         1            10100000          160
It is supposed that communication line could not change more than one bit in each of the transmitted bytes. So the bytes which have odd amount of bits are considered corrupted.

We are given the message in this protected encoding. Our task is to check each letter and remove those which are corrupted. Others should be converted to normal ASCII and printed as characters.

Input data will contain bytes of the message transmitted (represented by the sequence of decimal values, separated with spaces).
Original message consists only of latin letters (small and capital), digits and spaces.
The end of message is signalled by dot character '.' - you can assume this will never be corrupted.
Answer should contain message with corrupted bytes removed, highest bits cleared - and represented as characters rather than numbers.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e33 Parity Control.txt','r')
P= a.readlines()

l=P[0].strip().split()
codices=[]
for x in range(len(l)):
    X=int(l[x])
    codices.append(X)

print(codices)
"""
codices=[111, 245, 232, 57, 201, 213, 118, 181, 86, 184, 115, 160, 94, 108, 118, 85, 211, 201, 177, 237, 99, 185, 231, 184, 160, 177, 160, 195, 202, 78, 101, 160, 177, 66, 86, 207, 251, 160, 89, 249, 68, 243, 77, 229, 210, 244, 198, 245, 55, 66, 120, 82, 204, 116, 183, 209, 181, 201, 90, 128, 199, 69, 72, 183, 32, 235, 86, 178, 64, 240, 22, 171, 128, 216, 160, 160, 90, 184, 194, 215, 160, 67, 90, 35, 108, 105, 104, 160, 160, 86, 101, 67, 201, 215, 121, 223, 178, 168, 216, 111, 46]

def a_bin(num):
    if num == 0:
        return "0"
    bina = ""
    while num > 0:
        bina = str(num % 2) + bina
        num = num // 2
    if len(bina) < 8:
        bina=bina.zfill(8)
    return(int(bina))

def a_dec(num):
    deci = 0
    po = 1
    num=str(num)
    for bit in reversed(num):
        if bit == '1':
            deci += po
        po *= 2
    return deci

respuesta=''
for x in codices:
    binario=a_bin(x)
    lst_binario=list(str(binario))
    cont_1=0
    for y in lst_binario:
        if y == '1':
            cont_1+=1
    if cont_1%2 == 0:
        if binario >= 10000000:
            binario-=10000000
        decimal=a_dec(binario)
        respuesta+=chr(decimal)
print(respuesta)