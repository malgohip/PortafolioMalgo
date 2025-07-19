#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
After solving Dice Rolling, we already know how to convert fractional value between 0.0 and 1.0 to an integer number from within the specific range - for example to values between 1 and 6, simulating the throwing of the die.

However, many programming languages (like C/C++, PHP, Pascal) use random number generator which on contrary gives only integer values in the range from 0 to some (very large) maximum. How to convert such numbers to dice points?

It happens that this case is even simpler. We can use the following approach:

Divide the random value R by the N (number of distinct values we want - e.g. 6 for dice) and take the remainder. This remainder is necessarily the integer value in the range from 0 to N - 1.
Now to shift it to the necessary range, simply add 1 (i.e. the minimum of the range we want) - and you'll get the value in the range from 1 to N.
This method is not well precise if N is not small enough in compare to max of the generator. However it will be all right for most everyday needs (tossing coins, rolling dice, shuffling cards etc.)

To have practice, let us proceed with the following exercise:

Input data will contain the number of test-cases (dice throws) in the first line.
Next lines will have test-cases - each consisting of two random integer numbers - for throwing a pair of dice. These numbers are non-negative (from 0 to some value above 2,000,000,000) and they should be converted to dice points using the algorithm proposed above.
Answer should contain the sum of each throw of the pair of dice, values should be separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e44 Double Dice Roll.txt','r')
P= a.readlines()

valores=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    valores.append(F)

print(valores)
"""
valores=[[36025559, 148559128], [1710527284, 1344072922], [991449841, 1560485199], [1351148039, 363112729], [1515742599, 1205558380], [1319496078, 480294316], [1285501619, 822889731], [367230383, 85782166], [1636591590, 482413722], [1293502194, 516366721], [711361030, 1203383496], [2069713217, 2059105966], [880861097, 2048869539], [140777391, 1109455359], [310915833, 299825687], [852207110, 1083078136], [547739543, 1282274634], [361576400, 1625466743], [1550344553, 1903830086], [1684681980, 1589293377]]

resultado=''
for x in valores:
    z=0
    for y in x:
        z+=int(y%6)+1
    resultado+=str(z)+' '
print(resultado)