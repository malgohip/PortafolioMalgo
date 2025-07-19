#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Un triángulo es un objeto compuesto de tres segmentos de recta (los lados del triángulo) conectados en sus extremos. El artículo de Wikipedia proporciona una explicación más detallada.

Si tenemos tres segmentos de recta con longitudes A B C - hay dos posibilidades: que podamos construir un triángulo con ellos
(por ejemplo, con 3 4 5 o 3 4 7 - aunque este último tendría un área de cero) o que sea imposible (por ejemplo 1 2 4).

Se te dan varios tríos de valores que representan las longitudes de los lados de los triángulos. Deberías indicar con cuales tríos es posible construir un triángulo y con cuales no lo es.

Datos de entrada: La primera línea contendrá el número de tríos.
Las otras líneas contendrán los tríos en sí (cada uno en una línea separada).
Respuesta: Deberías mostrar 1 o 0 para cada trío (1 si el triángulo puede ser construido; de lo contrario muestra 0).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e9 Triangles.txt','r')
P= a.readlines()

lados=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    lados.append(tuple(F))

print(lados)
"""
lados=[(579, 345, 644), (316, 238, 596), (859, 2317, 1059), (579, 2260, 1150), (869, 464, 331), (625, 398, 269), (816, 445, 312), (2736, 1179, 618), (645, 635, 1275), (483, 374, 960), (2941, 1512, 991), (502, 206, 273), (516, 1185, 814), (301, 227, 391), (380, 477, 216), (374, 462, 1093), (156, 254, 438), (893, 1656, 4095), (150, 304, 145), (1011, 1407, 619), (825, 1101, 1489), (947, 1227, 1297), (341, 404, 420), (921, 1217, 1871), (585, 995, 2121), (758, 2206, 1465), (898, 919, 1062), (937, 1469, 2356), (586, 1388, 581)]

respuestas=''
for x in lados:
    if x[0]+x[1] <= x[2] or x[1]+x[2] <= x[0] or x[0]+x[2] <= x[1]:
        respuestas+='0 '
    else:
        respuestas+='1 '
print(respuestas)