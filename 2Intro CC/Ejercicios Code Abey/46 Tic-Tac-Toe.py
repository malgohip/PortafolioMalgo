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
a = open('Ejercicios Code Abey\TXTs\e46 Tic-Tac-Toe.txt','r')
P= a.readlines()

posiciones=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    posiciones.append(f)

print(posiciones)
"""
posiciones=[['6', '3', '8', '5', '9', '1', '4', '7', '2'], ['7', '6', '3', '4', '8', '5', '2', '1', '9'], ['6', '9', '3', '7', '8', '2', '4', '1', '5'], ['4', '6', '8', '9', '3', '5', '7', '1', '2'], ['5', '6', '2', '4', '7', '9', '8', '1', '3'], ['1', '9', '3', '4', '5', '6', '7', '8', '2'], ['2', '8', '3', '4', '9', '6', '1', '5', '7'], ['7', '8', '5', '3', '1', '9', '6', '4', '2'], ['8', '3', '9', '1', '4', '7', '6', '5', '2'], ['6', '2', '5', '7', '1', '4', '8', '3', '9'], ['7', '4', '3', '6', '8', '5', '9', '1', '2'], ['8', '4', '7', '1', '5', '2', '3', '6', '9'], ['1', '2', '5', '8', '9', '3', '6', '7', '4'], ['2', '9', '8', '5', '1', '3', '6', '7', '4'], ['6', '7', '2', '4', '9', '8', '5', '1', '3'], ['4', '1', '8', '9', '6', '2', '7', '5', '3']]

respuesta=''
for x in posiciones:
    tablero=['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for y in range(len(x)):
        if y%2==0:
            tablero[int(x[y])-1]='X'
        else:
            tablero[int(x[y])-1]='O'
        if tablero[0]==tablero[1] and tablero[1]==tablero[2] or tablero[3]==tablero[4] and tablero[4]==tablero[5] or tablero[6]==tablero[7] and tablero[7]==tablero[8] or tablero[0]==tablero[3] and tablero[3]==tablero[6] or tablero[1]==tablero[4] and tablero[4]==tablero[7] or tablero[2]==tablero[5] and tablero[5]==tablero[8] or tablero[0]==tablero[4] and tablero[4]==tablero[8] or tablero[2]==tablero[4] and tablero[4]==tablero[6]:
            respuesta+=str(y+1)+' '
            break
    else:
        respuesta+='0'+' '
print(respuesta)