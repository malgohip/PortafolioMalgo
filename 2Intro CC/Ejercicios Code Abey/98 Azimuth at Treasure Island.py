#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
A group of pirates was lucky to lay their hands on the map of the Treasure Island.

To their disappointment the map does not contain a vague drawings with a small black cross - but instead just several lines like the following:

at the southern beach of the Island find the pole stuck into the sand with the plaque Start attached;
turn azimuth 50 and go 300 feet;
proceed 500 feet by azimuth 270;
stride 150 feet more by azimuth 300;
dig here!
Pirates read in Wikipedia that azimuth 0 is the direction to the North, azimuth 90 is the direction to the East and so on.

However, they use a kind of GPS-navigator in place of compass. Instead of directions the device can show coordinates or offsets in feets.

So pirates need to solve the following problem: suggesting that the point of "the pole with the plaque Start" is the origin of coordinate system with Y axis pointing to the North and X axis pointing to the East - what are the coordinates of the treasure point?

Input data will be in format close to the directions inscribed on a map:
The first line contains words Stand at the pole with the plaque START - you can safely ignore this.
Next lines contain words go X feet by azimuth Y - you are to extract numbers from them.
Last line contains phrase Dig here!
Answer should contain coordinates of the point where the Treasure is hidden, rounded to closest integers.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e98 Azimuth at Treasure Island.txt','r')
P= a.readlines()

instrucciones=[]
for x in range(len(P)):
    f=P[x].strip().split()
    instrucciones.append(f)

print(instrucciones)
"""
from math import sin, cos, pi
instrucciones=[['Stand', 'at', 'the', 'pole', 'with', 'the', 'plaque', 'START'], ['go', '380', 'feet', 'by', 'azimuth', '341'], ['go', '140', 'feet', 'by', 'azimuth', '284'], ['go', '440', 'feet', 'by', 'azimuth', '80'], ['go', '420', 'feet', 'by', 'azimuth', '358'], ['go', '280', 'feet', 'by', 'azimuth', '1'], ['go', '120', 'feet', 'by', 'azimuth', '273'], ['go', '500', 'feet', 'by', 'azimuth', '271'], ['go', '40', 'feet', 'by', 'azimuth', '352'], ['go', '400', 'feet', 'by', 'azimuth', '300'], ['go', '340', 'feet', 'by', 'azimuth', '36'], ['go', '500', 'feet', 'by', 'azimuth', '326'], ['go', '320', 'feet', 'by', 'azimuth', '50'], ['go', '500', 'feet', 'by', 'azimuth', '305'], ['Dig', 'here!']]

def azimuth_radian(azim):
    """sexagecimal=(-(azim+90)-180)+360
    if sexagecimal % 360 == 0:
        sexagecimal=0
    radian=sexagecimal*pi/180"""
    # Convertir azimut a ángulo en radianes
    angle_degrees = (90 - azimuth) % 360
    radian = angle_degrees * pi / 180
    return radian
    return radian

cordx=0
cordy=0
for x in range(1,len(instrucciones)-1):
    pies=int(instrucciones[x][1])
    azimuth=int(instrucciones[x][-1])
    grados=azimuth_radian(azimuth)
    dx=pies*cos(grados)
    dy=pies*sin(grados)
    cordx += dx
    cordy += dy
respuesta=str(round(cordx))+' '+str(round(cordy))
print(respuesta)