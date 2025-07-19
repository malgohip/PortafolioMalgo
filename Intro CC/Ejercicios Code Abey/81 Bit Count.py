#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""

As you probably know, all values inside a computer are represented in binary system. In this simple task you are to write a program which counts the number of non-zero bits in a given value.

We are using 32-bit integer values, so there should be from 0 to 32 non-zero bits.

Please note that unlike most languages Python pretends that numbers are infinite-length (this will not prevent you from solving this task, though some of methods usable for other languages may not work as expected).

For example:

value             binary                count
  1   00000000000000000000000000000001      1
100   00000000000000000000000001100100      3
 -1   11111111111111111111111111111111     32
Input data will contain a number of values to process.
Next line will contain the values themselves, each in range -2 000 000 000 .. 2 000 000 000.
Answer should contain the counts of bits set to 1 for each of values, separated by spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e81 Bit Count.txt','r')
P= a.readlines()

l=P[1].strip().split()
numeros=[]
for x in range(int(P[0])):
    X=int(l[x])
    numeros.append(X)

print(numeros)
"""
numeros=[-583388207, 890406350, -63, -16, -18045, 269465725, -19634, 17, 1733813, 16971249, 107, -20, -97, -99446293, 116, -165360, 12569704, 12, -14827738, 266182, -189, 1186953069, 119660, 1319438, 183320770, 19, -11387, 1188, 11, 815247102, 1461, -35, -731131224, -949, 515, -176, -53087, -194, -1890919336, 1, -5609, 16, 17430, 1798490, 19262550, 942499, -4801657, -189089025, 159, 52142, -3, 767178, 12934431, -18542650, 641, -434715932, -4941039, 12, -63496304]

def a_binario(n):
    if n == 0:
        return '0'
    str_binario = ''
    while n > 0:
        residuo = n % 2
        str_binario = str(residuo) + str_binario
        n = n // 2
    
    return str_binario

def add_binary(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        total = bit1 + bit2 + carry
        carry = total // 2
        result_bit = total % 2
        result.append(str(result_bit))
    if carry:
        result.append('1')
    return ''.join(result[::-1])

respuesta=''
for x in numeros:
    if x >= 0:
        binario=a_binario(x)
        binario=binario.zfill(32)
    else:
        binario_pos=a_binario(-x)
        binario_pos=binario_pos.zfill(32)
        binario=''
        for y in binario_pos:
            if y=='0':
                binario+='1'
            else:
                binario+='0'
        binario=add_binary(binario,'1')
    cont=0
    for z in binario:
        if z == '1':
            cont+=1
    respuesta+=str(cont)+' '
print(respuesta)