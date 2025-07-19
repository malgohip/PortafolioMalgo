#Author: Sebastian Ochoa. Date: 08/19/2024
# -*- coding: utf-8 -*-

"""
The face of analog clock has two hands and is proportionally divided by 12 marks. The shorter hour hand makes the whole turn (360 degrees) in 12 hours, while the longer minute hand makes the whole circle each hour. See Clock Face on wiki for more details.

Suppose, the Cartesian Coordinate System (i.e. ordinary rectangular coordinate grid) is placed upon the clock face so that the center of the face has coordinates 10, 10 and Y axis is directed upwards while X axis is directed to the right (i.e. at 3:00 minute hand is parallel to Y axis and hour hand is parallel to X axis).

Assuming the length of the minute hand be 9 and the length of the hour hand be 6 you are to find coordinates of the hand ends for each given time - e.g. (16 10) and (10 19) for the time 3:00.

Input data contain the number of test cases.
Following line contains the testcases themselves in form 03:15, 21:44 etc.
Answer should contain four real numbers for each test case - X and Y coordinates for hour hand, then X and Y coordinate for minute hand. All values should be simply separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e74 Clock Hands.txt','r')
P= a.readlines()

horas=[]
f=P[1].strip().split()
for x in f:
    F=x.split(':')
    ff=[]
    for y in F:
        Y=int(y)
        ff.append(Y)
    horas.append(ff)

print(horas)
"""
from math import sin,cos,pi
horas=[[22, 17], [17, 17], [10, 52], [16, 16], [5, 40], [19, 23], [21, 2]]

respuesta=''
for a in horas:
    if a[0] >= 12:
        a[0]-=12
    angh=(a[0]*30+a[1]/2)*(pi/180)
    angm=(a[1]*6)*(pi/180)
    xh=(6*sin(angh))+10
    yh=(6*cos(angh))+10
    xm=(9*sin(angm))+10
    ym=(9*cos(angm))+10
    respuesta+=str(xh)+' '+str(yh)+' '+str(xm)+' '+str(ym)+' '
print(respuesta)
