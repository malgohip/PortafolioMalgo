#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Let's practice the geometry programming of rotations. Such functionality is quite popular in graphic editors, but it is not the only use.

For example here is the widget Sphere Tag Cloud which can be used in creating funny design of the web-page. Dragging the mouse over the cloud you should see it scrolling like a globe. The effect is achieved by performing just two rotations around two axes (for each of floating element).

We'll start with something simpler. Suggest we have a planar map with points on it. For example it could be the picture of a sky with stars shining.

The task is to perform rotation of the map by the given angle. Round the resulting coordinates to nearest integer.

To check the result please output the names of stars sorted by Y coordinate and then by X (if the Ys are equal).

Input data contain the number of stars N and the rotation angle A (counterclockwise, from 0 to 360 degrees).
Next lines will contain data about one star each in form Name X Y. Coordnates would be integer, not exceeding 1000 in absolute value.
Answer should give the names of stars sorted by Y and then by X after rotation (and rounding).

Note: sorting should be performed in ascending order, i.e. from smallest values to largest.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e85 Rotation in 2D Space.txt','r')
P= a.readlines()

l=P[0].strip().split()
estrellas=[]
for x in range(1,int(l[0])+1):
    f=P[x].strip().split()
    F=[]
    F.append(f[0])
    for y in range(1,3):
        Y=int(f[y])
        F.append(Y)
    estrellas.append(F)
estrellas.append(int(l[1]))
print(estrellas)
"""
estrellas=[['Procyon', -613, 743], ['Thabit', 733, -948], ['Aldebaran', 504, -981], ['Albireo', -296, -729], ['Jabbah', 494, 602], ['Nembus', -26, 920], ['Alcor', 631, 822], ['Media', -912, 72], ['Fomalhaut', -405, 856], ['Alcyone', -623, -945], ['Sirius', -664, 638], ['Polaris', 898, 237], ['Heka', 727, 278], ['Altair', -278, -544], ['Gemma', 184, 59], ['Vega', -107, 53], ['Rigel', -147, -396], ['Zosma', -311, 773], ['Pherkad', 575, -97], ['Diadem', 900, -50], ['Unuk', -620, 94], ['Kochab', 478, -372], ['Kastra', -482, -804], ['Mizar', -993, 229], ['Mira', -632, -917], ['Yildun', -862, -412], ['Lesath', 217, -345], ['Betelgeuse', 549, 963], ['Electra', 623, -972], ['Bellatrix', 786, 681], ['Castor', 986, 973], ['Capella', 124, -772], ['Deneb', 693, 458], ['Algol', 908, 484], 311]
grados=estrellas.pop(-1)

from math import sin,cos,pi

def rotarpunt(x, y, grados):
    radianes = grados*(pi/180)
    xp= x * cos(radianes) - y * sin(radianes)
    yp = x * sin(radianes) + y * cos(radianes)
    
    return round(xp), round(yp)

respuesta=''
n_pos=[]
for x in estrellas:
    n_es=[x[0]]
    nx,ny=rotarpunt(x[1],x[2],grados)
    n_es.append(nx)
    n_es.append(ny)
    n_pos.append(n_es)
estrellas_orden = sorted(n_pos, key=lambda x: (x[2], x[1]))
for y in estrellas_orden:
    respuesta+=y[0]+' '
print(respuesta)