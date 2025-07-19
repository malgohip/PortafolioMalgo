#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Un problema muy común en la programación computacional es determinar la ley subyacente a la cual un fenómeno obedece. Para propósitos de aprendizaje, practiquemos una variante sencilla - descubrir la dependencia lineal de dos observaciones dadas (por ejemplo, cómo el precio de un producto depende de su tamaño, peso, etc.)

Una función lineal está definida por la ecuación:
Donde a y b son unas constantes.
y(x) = ax + b
Por ejemplo, con a=3, b=2 la función arrojará los valores y = 2, 5, 8, 11... cuando x = 0, 1, 2, 3...

Tu tarea es determinar a y b usando dos puntos que pertenecen a la función, ej.: Se te indican dos pares de valores (x1, y1), (x2, y2) los cuales satisfacen la ecuación de la función - y deberás restaurar la ecuación en sí.

Los Datos en entrada tienen el número de casos de prueba en la primera línea y luego, en líneas separadas, los casos en sí.
Cada caso contiene 4 enteros (x1 y1 x2 y2).
Las Respuestas deberían ser enteros también y deben escribirse en una línea, separadas con espacios y encerrando cada par en paréntesis, por ejemplo:
"""
"""
a = open('Ejercicios Code Abey\TXTs\e10 Linear Function.txt','r')
P= a.readlines()

puntos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    A=[]
    B=[]
    for x in range(0,2):
        X=int(f[x])
        Y=int(f[x+2])
        A.append(X)
        B.append(Y)
    punto=[]
    punto.append(tuple(A))
    punto.append(tuple(B))
    puntos.append(punto)

print(puntos)
"""
puntos=[[(324, -20227), (-749, 49518)], [(187, -17496), (-504, 48149)], [(652, 1305), (609, 1219)], [(-110, 6690), (-52, 3326)], [(-966, 28656), (-394, 12068)], [(-961, -14598), (-939, -14246)], [(172, 10513), (-951, -57990)], [(-214, -6392), (-291, -9010)], [(-329, -1698), (-593, -3018)], [(-106, -8982), (568, 46960)], [(-478, 10158), (-763, 16428)], [(409, -29189), (-350, 23941)]]

respuesta=''
for x in puntos:
    a=(x[1][1]-x[0][1])/(x[1][0]-x[0][0])
    b=x[0][1]-a*x[0][0]
    respuesta+='('+str(int(a))+' '+str(int(b))+') '
print(respuesta)