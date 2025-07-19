#Author: Sebastian Ochoa. Date: 08/18/2024
# -*- coding: utf-8 -*-

"""
Dos ciclistas empiezan a moverse simultaneamente desde ciudades diferentes para encontrarse en algún lugar en el medio (no exactamente en el punto medio, dado que ellos viajan a diferentes velocidades)

La carretera está trazada en linea recta entre las dos ciudades.

Te serán dadas las distancia entre las ciudades S (en kilometros) y la rapidez para los dos ciclistas (A y B en kilometros por hora). Tu tarea es encontrar el punto de encuentro (la distancia medida desde la primera ciudad)

Datos de entrada tendrá el numero de casos de prueba en la primera linea.
Las siguientes lineas tendrán tres valores cada una S A B.
Respuesta debe contener las distancias entre la primera ciudad y el punto de encuentro (es decir, la distancia recorrida por el primer cilista antes del cruce entre ellos), separado con espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e68 Bicycle Race.txt','r')
P= a.readlines()

rutas=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    rutas.append(F)

print(rutas)
"""
rutas=[[62, 24, 16], [144, 25, 15], [13, 26, 19], [75, 26, 25], [11, 11, 14], [21, 14, 29], [31, 26, 21], [112, 11, 26], [16, 21, 29], [94, 11, 12], [21, 13, 20], [212, 14, 25], [45, 29, 20], [15, 16, 11], [58, 12, 10], [55, 13, 19], [208, 12, 22], [10, 11, 24], [80, 13, 22], [117, 24, 10]]

respuesta=''
for x in rutas:
    vf=x[1]+x[2]
    tf=x[0]/vf
    respuesta+=str(tf*x[1])+' '
print(respuesta)