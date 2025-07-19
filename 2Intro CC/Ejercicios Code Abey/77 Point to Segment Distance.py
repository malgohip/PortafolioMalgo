#Author: Sebastian Ochoa. Date: 08/19/2024
# -*- coding: utf-8 -*-

"""
Very common problem in computational geometry is to find distance between the point and the line segment. It is heavily exploited in programming 3D video games when recalculating visibility of walls for player while redrawing each frame (i.e it is could be solved for 1000 wall fragments in each frame and about 50 frames are completely recalculated during each second).

The definition of the distance between point and segment is like following:

draw a line through both ends of a segment (i.e. the line to which this segment belongs);
from our point cast a perpendicular to this line - the length of this perpendicular is the distance between the point and the line;
if the other end of the perpendicular belongs to our segment (i.e. lays between its ends), then the distance to this segment equals to distance to this line;
otherwise distance from point to segment equals to distance to nearest of its ends.
For example, see the picture above - line segment is drawn with blue and perpendiculars from 2nd and 3rd points fall directly onto this segment, so they represent the distance from these points. On other hand perpendiculars from 1st and 4th points fall out of segment (and they are not shown), so that distances are defined simply by the nearest end of a segment (distances from all points are represented with grey lines). The line on which the segment lays is shown with light-green.

Input data will contain the number of test-cases in first line.
The following lines contain six values each: x1 y1 x2 y2 xp yp - denoting the segment between points (x1,y1) and (x2,y2) and the point (xp,yp) to which a distance should be calculated.
Answer should contain distances from points to segments for each test-case, separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e77 Point to Segment Distance.txt','r')
P= a.readlines()

puntos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    puntos.append(F)

print(puntos)
"""
puntos=[[3, 11, 19, 9, 7, 14], [2, 7, 15, 5, 19, 4], [7, 2, 18, 12, 11, 2], [8, 20, 14, 11, 8, 5], [5, 15, 0, 1, 14, 16], [14, 12, 2, 14, 18, 17], [4, 19, 6, 20, 11, 9], [16, 0, 1, 9, 13, 6], [19, 18, 16, 6, 11, 14], [18, 7, 19, 18, 16, 19], [11, 8, 0, 6, 17, 8], [3, 20, 7, 9, 18, 17], [16, 1, 9, 10, 8, 15], [12, 1, 14, 19, 8, 12], [6, 5, 13, 1, 7, 16], [13, 13, 0, 20, 15, 17], [10, 6, 2, 8, 14, 15], [7, 18, 0, 19, 8, 3], [11, 18, 1, 0, 2, 0], [18, 5, 1, 3, 11, 5], [19, 16, 16, 2, 12, 19]]

import math

def distancia_punto_segmento(x1, y1, x2, y2, xp, yp):
    # Vector AB
    ABx = x2 - x1
    ABy = y2 - y1
    
    # Vector AP
    APx = xp - x1
    APy = yp - y1
    
    # Proyección escalar de AP en AB
    ab2 = ABx ** 2 + ABy ** 2
    if ab2 == 0:
        # Si el segmento es un punto, retorna la distancia al punto
        return math.sqrt(APx ** 2 + APy ** 2)
    
    # Proyección escalar
    t = (APx * ABx + APy * ABy) / ab2
    
    # Punto proyectado en la línea
    if t < 0.0:
        # Más cercano a A
        closest_x, closest_y = x1, y1
    elif t > 0.0 and t <= 1.0:
        # Dentro del segmento
        closest_x, closest_y = x1 + t * ABx, y1 + t * ABy
    else:
        # Más cercano a B
        closest_x, closest_y = x2, y2
    
    # Distancia desde el punto P al punto más cercano en el segmento
    dx = xp - closest_x
    dy = yp - closest_y
    
    return math.sqrt(dx ** 2 + dy ** 2)

def resolver_distancias(casos):
    resultados = []
    for caso in casos:
        x1, y1, x2, y2, xp, yp = caso
        distancia = distancia_punto_segmento(x1, y1, x2, y2, xp, yp)
        resultados.append(f"{distancia:.12f}")
    return " ".join(resultados)

print(resolver_distancias(puntos))