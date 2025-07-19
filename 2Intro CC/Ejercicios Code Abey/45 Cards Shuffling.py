#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
Note: you may find it useful to solve Card Names before this

For any type of card game it is important to be able to shuffle the deck. Since only few of the programming languages have built-in functions to randomly shuffle an array (like PHP) it is necessary to learn some useful algorithm.

Let us agree to use the following symbols to describe cards:

ranks: A, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K
suits: C, D, H, S
so that CQ is the "Queen of Clubs", HT is the "Ten of Hearts", D2 is the "Two of Diamonds" and SA is the "Ace of Spades".

There are 52 cards in total, so they should be put into an array of 52 elements before shuffling. Initial ordering of the array is the following: 13 cards of Clubs, then 13 cards of Diamonds, then 13 cards of Hearts and at last 13 cards of Spades. Inside of each suit cards are arranged from Ace to King, so the whole deck looks like:

[ CA, C2, C3, ..., CQ, CK, DA, D2, ..., DK, HA, H2, ..., HK, SA, S2, ..., SK ]
Then you should for each card generate some random number in the range 0 ... 51 and swap this card with another, occupying the selected position (let indexes of array start from 0). This may look like:

FOR i = 0 ... 51 :
    LET j = RANDOM(0 ... 51)
    SWAP deck[i] WITH deck[j]
For example, we take the first card CA and generate random value 15 for it - this means that card should be moved to position 15, where D3 was - and D3 should be moved back to position 0. Then we take C2 from the position 1 and generate next random number 50 - so C2 is swapped with SQ. And so on.

You will be given the sequence of non-negative integer random numbers - if they are greater than necessary, trim them to required range by taking modulo 52, like in the Double Dice Roll task. Perform the shuffling and print the new order of cards as an answer.

Input data will contain 52 non-negative integer numbers, which you should use to shuffle the deck as described.
Answer should contain cards from shuffled array, separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e45 Cards Shuffling.txt','r')
P= a.readlines()

valores_str=P[0].strip().split()
valores=[]
for x in valores_str:
    X=int(x)
    valores.append(X)

print(valores)
"""
valores=[7, 73, 7898, 89, 61, 54, 2924, 9336, 82, 68, 6264, 3482, 2797, 4710, 87, 1706, 886, 9600, 25, 5500, 7567, 930, 8006, 98, 9, 99, 9471, 535, 298, 2433, 46, 7429, 8118, 40, 37, 682, 34, 91, 6744, 581, 5052, 6561, 4326, 3499, 882, 86, 3943, 7652, 27, 167, 2163, 33]

cartas=['CA','C2','C3','C4','C5','C6','C7','C8','C9','CT','CJ','CQ','CK','DA','D2','D3','D4','D5','D6','D7','D8','D9','DT','DJ','DQ','DK','HA','H2','H3','H4','H5','H6','H7','H8','H9','HT','HJ','HQ','HK','SA','S2','S3','S4','S5','S6','S7','S8','S9','ST','SJ','SQ','SK']
cambios=[]
resultado=''
for x in valores:
    cambios.append(int(x%52))
for y in range(0,52):
    t=cartas[y]
    cartas[y]=cartas[cambios[y]]
    cartas[cambios[y]]=t
for z in cartas:
    resultado+=z+' '
print(resultado)

