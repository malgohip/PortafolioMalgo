#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
If you feel this problem too easy for you, try Caesar Cipher Cracker instead!

Cryptography is one of most interesting branches of programming. Studying its algorithms usually begins with the simple method named after famous Roman emperor Julius Caesar who used it for communicating his military secrets (and perhaps for love letters to Cleopatra).

We will practice deciphering encrypted messages in this problem.

The idea of the algorithm is simple. Each letter of the original text is substituted by another, by the following rule:

find the letter (which should be encrypted) in the alphabet;
move K positions further (down the alphabet);
take the new letter from here;
if "shifting" encountered the end of the algorithm, continue from its start.
For example, if K = 3 (shift value used by Caesar himself), then A becomes D, B becomes E, W becomes Z and Z becomes C and so on, according to the following table:

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

| | | | | | | | | | | | | | | | | | | | | | | | | |
V V V V V V V V V V V V V V V V V V V V V V V V V V 

D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
So if the source message was VENI VIDI VICI then after encoding it becomes YHQL YLGL YLFL.

On the other hand encrypted message should be "shifted back" to decode it - or shifted by 26 - K which is the same.

So if we have encoded message HYHQ BRX EUXWXV, we can apply shift of 26 - K = 26 - 3 = 23 and find the original text to be EVEN YOU BRUTUS.

Input data will contain two integers - the number of lines of encrypted text and the value of K.
The following lines will contain encrypted text, consisting of capital latin letters A ... Z, each line is terminated with a dot . which should not be decoded. Answer should contain the decrypted message (in a single line, no line splitting is needed).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e47 Caesar Shift Cipher.txt','r')
P= a.readlines()

ne_str=P[0].strip().split()
ne=[]
for x in ne_str:
    X=int(x)
    ne.append(X)
print(ne)

codices=[]
for x in range(1,ne[0]+1):
    f=P[x].strip().split()
    codices.append(f)

print(codices)
"""
ne=[7, 12]
codices=[['M', 'PMK', 'MF', 'FTQ', 'DMOQE', 'FTQ', 'AZOQ', 'MZP', 'RGFGDQ', 'WUZS', 'ITA', 'IMZFE', 'FA', 'XUHQ', 'RADQHQD.'], ['SUHQ', 'KAGD', 'DAAWE', 'NGF', 'ZAF', 'PUXMDMY.'], ['XQF', 'TUY', 'FTDAI', 'FTQ', 'RUDEF', 'EFAZQ.'], ['FTQ', 'PQMP', 'NGDK', 'FTQUD', 'AIZ', 'PQMP.'], ['M', 'ZUSTF', 'MF', 'FTQ', 'ABQDM', 'FA', 'GE', 'UZ', 'AXPQZ', 'EFADUQE.'], ['MZP', 'RADSUHQ', 'GE', 'AGD', 'PQNFE', 'MZP', 'EA', 'KAG', 'FAA', 'NDGFGE.'], ['RAGD', 'EOADQ', 'MZP', 'EQHQZ', 'KQMDE', 'MSA', 'YQF', 'M', 'IAYMZ', 'MF', 'FTQ', 'IQXX', 'UZ', 'MZOUQZF', 'BQDEUM', 'FTQDQ', 'IME', 'M', 'WUZS.']]

abecedario=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
decodex=[]
respuesta=''
for x in codices:
    fradeco=''
    for y in x:
        paldeco=''
        for z in y:
            if z != '.':
                codi=abecedario.index(z)
                decodi=codi-ne[1]
                paldeco+=abecedario[decodi]
            else:
                paldeco+=z
        fradeco+=paldeco+' '
    respuesta+=fradeco
print(respuesta)
        
