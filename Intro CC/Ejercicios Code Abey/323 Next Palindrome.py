#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Numbers which are palindromes read the same forwards and backwards. So 35453, 2992 and 6 are palindromes but 1121 is not. In this problem you are given a number and must find the smallest positive amount that can be added to the number in order to create a palindrome. For example, for the number 5862 we need to add 23 to obtain the palindrome 5885. 23 is the smallest addition for which we can create a palindrome. So 5885 is the next palindrome after 5862. If the starting number is already a palindrome you must find the smallest positive number which, when added to it, creates another palindrome. So, for an input of 373 we must add 10 to obtain the next palindrome 383. None of the input numbers will contain more than 18 digits.

Input and Answer
The first line of the problem will be a single integer N denoting the number of test cases.
Each of the following N lines will hold a single number. For each number you must find the smallest addition to it (greater than 0) which will create a palindrome. Give these answers, separated by spaces, as a single string.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e323 Next Palindrome.txt','r')
P= a.readlines()

numeros=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    numeros.append(int(f))

print(numeros)
"""
numeros=[4, 61, 86, 420, 703, 1913, 9966, 19475, 26129, 282610, 962361, 3853184, 8158123, 28525242, 99999999, 139999955, 522436469, 799999986, 7256481021, 49519857810, 99999999999, 289999999907, 563996172136, 1568465957459, 3251484590400, 17153310314494, 33744851042018, 401376419378230, 589999999999006, 5827761459616912, 9162284743160822, 16514544286333424, 39122102859820477, 648482225570121667, 947931388087440675]

def next_palindrome(n):
    s = str(n)
    length = len(s)
    if length == 1:
        return n
    
    if all(c == '9' for c in s):
        return int('1' + '0' * (length - 1) + '1')
    
    half_len = (length + 1) // 2
    left_half = s[:half_len]
    if length % 2 == 0:
        candidate = int(left_half + left_half[::-1])
    else:
        candidate = int(left_half + left_half[-2::-1])
    
    if candidate > n:
        return candidate
    
    left_half = str(int(left_half) + 1)
    if length % 2 == 0:
        candidate = int(left_half + left_half[::-1])
    else:
        candidate = int(left_half + left_half[-2::-1])
    
    return candidate

def sig_palindromo(n):
    next_pal = next_palindrome(n + 1)
    return next_pal - n

respuesta=''
for x in numeros:
    respuesta+=str(sig_palindromo(x))+' '
print(respuesta)