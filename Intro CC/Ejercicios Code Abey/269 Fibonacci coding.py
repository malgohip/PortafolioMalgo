#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Fibonacci Numeral System
Every integer number could be represented as sum of fibonacci values, all different. This gives us binary system with "weights" of bits not related to powers of 2, but instead to fibonacci numbers! So the lowest bit stands for 1, next for 2, third for 3, fourth for 5 and so on. For example value 32 becomes:

32  =  3 + 8 + 21  =  1010100 (fib)
Curious property of such representation is that every value could be represented without consecutive 1s. Really two 1s together could be instead represented by single 1 in the next position!

Problem Statement
You get a bit-stream. It contains bytes as Fibonacci numerals, least significant bit first (i.e. contrary to how we write numbers in European style). End of every byte is marked by additional 1, so it is easy to distinguish (as most significant bit is necessarily 1 too) by two 1s.

Decode it to ASCII.

Input gives a "bit-stream" split to several strings of 0s and 1s. For convenience first line gives the total number of "chunks" following.

Answer should contain encoded text.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e269 Fibonacci coding.txt','r')
P= a.readlines()

codigos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    codigos.append(f)

print(codigos)
"""
codigos=['10010010111000010011101000101100100010110101001011', '01010010111000010011010100101101010010110001010011', '00100010110100001011010100101100101011001010001110', '00101011000000101100000010110000000001100101011001', '00100111001001011100001001110000100110100001011101', '00100110010001011100100101101000010110010101100101', '01011100001001110000100110000010011100001001100000', '10011001010110100010011001000101101000010110000010', '01110001010111000010011010100101100101011100000000', '11000101001110010010111010100011001000101101000010', '11010100101100101011100001001110101010111010001011', '01001000110000101011100100101100010100110100100011', '00001010111000010011010100101100101011001010001100', '10001011010000101110000100111010010011100001001101', '001000110000010011']

def decode_fibonacci_bitstream(bit_chunks):
    fibonacci_sequence = [1, 2]
    while sum(fibonacci_sequence) < 256: 
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    def decode_fibonacci_number(fib_str):

        if fib_str.endswith('11'):
            fib_str = fib_str[:-1]

        number = 0
        index = 0
        for bit in fib_str:
            if bit == '1':
                number += fibonacci_sequence[index]
            index += 1
        return number

    def convert_to_ascii(fib_str):
        result = []
        while len(fib_str) > 0:

            end_pos = fib_str.find('11')
            if end_pos == -1:
                break

            byte_str = fib_str[:end_pos+2]
            fib_str = fib_str[end_pos+2:]

            number = decode_fibonacci_number(byte_str)
            
            if 0 <= number <= 127:
                result.append(chr(number))
        
        return ''.join(result)

    full_bitstream = ''.join(bit_chunks)
    decoded_text = convert_to_ascii(full_bitstream)
    
    return decoded_text

print(decode_fibonacci_bitstream(codigos))