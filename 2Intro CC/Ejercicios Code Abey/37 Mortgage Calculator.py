#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
Banking provides us with many interesting programming problems. The following one is more complicated than Savings calculator which you perhaps learned earlier.

After Joel bought a boat he has got the new idea - to buy a house. Since he did not want to wait until necessary sum is collected, he considers a mortgage, which is to get a loan from bank and buy a house immediately, while loan is secured by this house (i.e., in case of borrower's default bank gets the house in compensation).

Mathematically, mortgage works by the following algorithm:

Joel borrows big money sum P from bank (and performs purchase);
bank tells him its interest rate R in percents - the speed of growth of the debt;
at the end of each month the debt is increased by R / 12 percents;
immediately after it Joel gives to bank some predefined small sum M to decrease the debt;
debt is considered settled when its value is reduced to zero (this could take several years).
For example, Joel takes P = $800,000 from bank with interest rate of R = 6%. He is willing to pay M = $10000 at the end of each month.

Month     P        P * (R/12)%      -M       new P
  1    $800000       $4000       -$10000    $794000
  2    $794000       $3970       -$10000    $787970
  3    $787970       $3940       -$10000    $781910
 ...
 12    $732325       $3662       -$10000    $725987
 ...
 24    $654138       $3271       -$10000    $647408
 ...
 103     $4188         $21        -$4209         $0
So after 103 months (which is about 8.5 years) the debt could be payed out. The last payment of course could be less than M (since P need not to become negative). Note that he will pay out about:

102 * $10000 + $4209 = 1024209
which is 25% more than the cost of the house.

Joel asks you (the mighty programmer) to help him with the calculation of necessary monthly payment M.

Input data contains values for loan size P, interest rate R and length of time to pay out L in months.
Answer should contain the required monthly payment M rounded up to whole dollars (i.e. if you get non-integer result, increase it to nearest integer which is greater).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e37 Mortgage Calculator.txt','r')
P= a.readlines()

l=P[0].strip().split()
datos=[]
for x in range(len(l)):
    X=int(l[x])
    datos.append(X)

print(datos)
"""
datos=[3300000, 3, 180]

r = datos[1] / (12 * 100)  # Convertir la tasa anual a tasa mensual en decimales
if r == 0:
    M = datos[0] / datos[2]
else:
    M = datos[0] * (r * (1 + r) ** datos[2]) / ((1 + r) ** datos[2] - 1)
    decimal= M-int(M)
    if decimal != 0:
        M=int(M)+1
    respuesta=str(M)
print(respuesta)