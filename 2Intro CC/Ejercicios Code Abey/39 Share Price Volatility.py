#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
Prolific trader Paul Penniless wants to be millionaire. He is trying to buy or sell shares and make profit on the changing prices. I.e. if he is lucky to buy 200 shares for 20 dounds apiece and sell in a week for 23, he gains 600 dounds in just few days.

Paul read an article on Standard Deviation and has the new idea now. He at once realized that the main problem is that the broker (the company who provides service for playing at market) takes comission of 1% for each deal. So regarding example above Paul loses 40 dounds when buying shares and 46 more when selling them back. So the real profit is not 600 but only 600 - 40 - 46 = 514 dounds.

It is obvious for him now, that he should prefer operations with shares which are more volatile - i.e. the price of which changes in wider range, so that his profit from changing price is more significant when compared to broker's comission.

For example, if initial price of shares was 50 (rather than 20) and it had grown to 52 when Paul sold them, his profit for 200 shares would be only 400 dounds. However, comission would be 100 dounds when buying and 104 when selling, so his real gain is only 196 dounds - more than half money was taken by broker!

Paul decided that he will choose whether to deal with shares of some kind or not depending on the following rule: standard deviation of prices for these shares over the last fortnight should be at least four times greater than broker's comission (which is 1%), i.e. for share with mean price 50 comission is 0.5 and standard deviation should be equal or greater than 2.

For example if the price was 99 dounds for 7 days and 101 for other 7 days, then the average price is 100, and broker comission (per share) is 1 dound. Standard deviation would be 1 dound also, so these shares do not deserve being bought or sold.

Input data will contain number of stocks (share types or names) for which calculations should be done.
Next lines contain descriptions of stock - the stock name (four latin letters) and then 14 values - prices for each day over last fortnight.
Answer should contain names of stocks which are volatile enough by Paul's criteria (in the same order as they were given in the input).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e39 Share Price Volatility.txt','r')
P= a.readlines()

acciones=[]
for x in range(1,int(P[0].strip())+1):
    f=P[x].strip().split()
    F=[f[0]]
    for y in range(1,len(f)):
        F.append(int(f[y]))
    acciones.append(F)

print(acciones)
"""
from math import sqrt
acciones=[['JABA', 20, 23, 21, 22, 19, 16, 17, 14, 16, 16, 13, 15, 13, 16], ['GOLD', 22, 21, 22, 25, 26, 24, 22, 25, 28, 29, 27, 28, 29, 27], ['SUGR', 55, 53, 51, 52, 53, 49, 49, 48, 45, 46, 44, 40, 44, 47], ['INSX', 46, 44, 43, 43, 44, 45, 44, 42, 39, 37, 37, 35, 32, 35], ['VDKL', 234, 235, 234, 234, 235, 235, 237, 236, 235, 234, 233, 235, 237, 239], ['WOWY', 113, 110, 110, 111, 114, 112, 112, 114, 115, 114, 111, 114, 113, 112], ['FLNT', 166, 165, 166, 165, 164, 164, 165, 164, 163, 164, 165, 164, 165, 165], ['DALG', 70, 69, 71, 68, 68, 70, 67, 66, 62, 63, 61, 59, 55, 52], ['ASDF', 37, 39, 36, 38, 39, 40, 39, 42, 40, 42, 45, 43, 45, 45], ['MARU', 62, 64, 68, 66, 63, 60, 60, 57, 54, 58, 57, 53, 53, 53], ['FANT', 45, 43, 45, 44, 43, 44, 46, 47, 46, 46, 45, 44, 46, 45], ['SLVR', 53, 52, 52, 52, 53, 52, 52, 53, 52, 52, 52, 53, 53, 54], ['PNSN', 60, 60, 62, 64, 65, 64, 66, 67, 68, 70, 70, 70, 69, 70], ['ZEOD', 25, 23, 21, 22, 21, 23, 22, 20, 19, 20, 19, 17, 16, 15], ['IMIX', 44, 41, 39, 41, 38, 41, 43, 44, 40, 38, 36, 40, 36, 39], ['BLEP', 50, 49, 49, 48, 48, 49, 50, 50, 50, 50, 51, 52, 51, 50], ['CKCL', 233, 231, 228, 229, 226, 225, 224, 223, 226, 226, 225, 223, 226, 225], ['FOTA', 195, 197, 199, 197, 199, 196, 194, 193, 190, 188, 185, 187, 190, 189], ['JEOP', 236, 237, 238, 237, 236, 237, 237, 237, 236, 236, 236, 236, 236, 235], ['OBAM', 88, 87, 87, 89, 86, 84, 83, 81, 78, 78, 81, 83, 86, 87], ['YUKA', 67, 67, 68, 67, 66, 67, 69, 70, 72, 73, 74, 71, 73, 76], ['SAKK', 25, 24, 22, 23, 25, 25, 26, 28, 29, 31, 29, 30, 32, 33]]

resultado=''
ganancia=[]
for x in acciones:
    sum_pro=0
    for y in range(1,len(x)):
        sum_pro+=x[y]
    pro=sum_pro/(len(x)-1)
    sum_dev=0
    for y in range(1,len(x)):
        sum_dev+=(x[y]-pro)**2
    devi=sqrt(sum_dev/(len(x)-1))
    com_bro=pro*0.01
    if devi >= com_bro*4:
        ganancia.append(1)
    else:
        ganancia.append(0)
for z in range(len(ganancia)):
    if ganancia[z]:
        resultado+=acciones[z][0]+' '
print(resultado)
