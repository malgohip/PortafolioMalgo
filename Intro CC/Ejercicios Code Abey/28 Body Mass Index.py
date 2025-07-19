#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
Let us apply our programming skills to some quasi-scientific problem - since it is bit dull to learn only abstract things.

The simple measure of body constitution was proposed at the middle of XIX century. It depends only on the height and weight of a person - and is called Body Mass Index or BMI. It is defined as:

BMI = weight / height^2
Where weight is taken in kilograms and height in meters.

Four general grades are proposed:

Underweight     -           BMI < 18.5
Normal weight   -   18.5 <= BMI < 25.0
Overweight      -   25.0 <= BMI < 30.0
Obesity         -   30.0 <= BMI
For example, if I have weight of 80 kg and height of 1.73 m I can calculate:

BMI = 80 / (1.73)^2 = 26.7
i.e. somewhat overweight.

We will not discuss how proper or improper this gradation is. Instead you should simply calculate grades for several people.

Input data contain number of people in the first line.
Other lines will contain two values each - weight in kilograms and height in metres.
Answer should contain words under, normal, over, obese for each corresponding test-case, separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e28 Body Mass Index.txt','r')
P= a.readlines()

casos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=float(x)
        F.append(X)
    casos.append(F)

print(casos)
"""
casos=[[111.0, 1.73], [69.0, 1.7], [101.0, 2.19], [55.0, 1.29], [116.0, 1.87], [113.0, 2.27], [108.0, 1.81], [110.0, 2.71], [78.0, 1.93], [48.0, 1.39], [119.0, 1.82], [92.0, 1.81], [103.0, 1.99], [89.0, 2.62], [51.0, 1.43], [90.0, 1.73], [86.0, 2.39], [113.0, 2.51], [52.0, 1.41], [60.0, 1.35], [91.0, 1.64], [87.0, 1.83], [42.0, 1.22], [110.0, 2.24], [111.0, 1.86], [86.0, 2.07], [80.0, 2.17], [111.0, 2.36]]

respuesta=''
for x in casos:
    str_bmi='under'
    bmi=x[0]/(x[1]**2)
    if 18.5 <= bmi and bmi < 25:
        str_bmi='normal'
    elif 25<= bmi and bmi < 30:
        str_bmi='over'
    elif 30 < bmi:
        str_bmi='obese'
    respuesta+=str_bmi+' '
print(respuesta)