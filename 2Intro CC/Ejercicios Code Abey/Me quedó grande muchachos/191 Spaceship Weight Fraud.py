#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
When merchant spaceship is fully loaded its total mass is expressed by long integer number, like 31415926. The Ship's Master want to tweak this value in documents to increase his profit, because both tax to be paid for the ship and the wages he will receive for jounrney are proportional to this mass.

He discovered that if he only swaps two digits (not necessarily adjacent) - no one will notice this.

So he want to know two things:

to which smallest value this number could be transformed by such a swap, to decrease tax he should pay;
also to what largest value the number could be transformed, to increase the wages he is going to receive.
He can perform only one swap - and there is limitation that resulting value should not start with 0 (so its length is decreased which could be easily noticed).

For the sample value given above the smallest value is 11435926 and the largest is 91415326.

Note that input values will never start with 0 - thanks to Nicolas Patrois for pointing out this bug!

Input data will have the total quantity of test cases in the first line.
Next lines will contain a single integer each in hexadecimal (no longer than 30 digits, first of them is non-zero).
Answer should contain a pair of min and max values for each mass in the input.
"""
#"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e191 Spaceship Weight Fraud.txt','r')
P= a.readlines()

hexadecimales=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    hexadecimales.append(f)

print(hexadecimales)
#"""
#hexadecimales=

def mayor_y_menor (n):
    lst_n=list(n)
    lst_n.sort()
    #print(lst_n)
    menor=list(n)
    t_m=lst_n[0]
    menor[menor.index(t_m)]=menor[0]
    menor[0]=t_m
    if lst_n[0] == '0':
        t_m=lst_n[0]
        menor[0]=menor[1]
        menor[1]=t_m
        if menor[0] > lst_n[1]:
            t_m=lst_n[1]
            menor[menor.index(t_m)]=menor[0]
            menor[0]=t_m
    elif lst_n[0]==lst_n[1]:
        c_1=menor.pop(0)
        t_m=lst_n[0]
        menor[menor.index(t_m)]=menor[0]
        menor[0]=t_m
        menor.insert(0,c_1)
    mayor=list(n)
    t_M=lst_n[-1]
    mayor[mayor.index(t_M)]=mayor[0]
    mayor[0]=t_M
    if lst_n[-2]==lst_n[-1]:
        c_1=mayor.pop(-1)
        t_m=lst_n[0]
        t_M=lst_n[-1]
        mayor[mayor.index(t_M)]=mayor[0]
        mayor[0]=t_M
    str_menor=''
    str_mayor=''
    for x in range(len(mayor)):
        str_menor+=menor[x]
        str_mayor+=mayor[x]
    return str_menor,str_mayor

respuesta=''
for x in hexadecimales:
    menor,mayor=mayor_y_menor(x)
    respuesta+=menor+' '+mayor+' '
print(respuesta)