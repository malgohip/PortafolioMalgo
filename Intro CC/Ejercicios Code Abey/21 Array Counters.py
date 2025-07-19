#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
De este problema aprenderemos un truco popular de programación utilizado en muchas variantes de cálculos estadísticos.

Imagina que un guardia forestal está intentando contar pinos, abetos y abedules en alguna sección del bosque. El guardia puede ir a través de esta sección en tres ocasiones, contando sólo los pinos en la primera pasada, sólo abetos en la segunda y sólo abedules en la tercera.

Una manera más eficiente es realizar una sola pasada a través del bosque y anotar un punto en una de las tres páginas de su cuaderno - la primera página es para los pinos, la siguiente para los abetos y la última para los abedules. Esa es la idea para contar elementos similares en una secuencia, utilizando un vector de contadores (en vez del cuaderno).

Aquí hay una matriz de longitud M con números en un rango de 1 ... N, donde N es menor o igual a 20. Tenemos que recorrerla y contar cuántas veces se encuentra cada número, ej.: es similar a la tarea de contar vocales, pero necesitamos mantener más de un contador. Asegúrate de usar un vector separado para ellos, para no crear un montón de variables separadas.

Los Datos de entrada contienen M y N en la primera línea.
La segunda (y más larga) línea contendrá M números separados por espacios.
La Respuesta debería contener exactamente N valores, separados por espacios. Primero debería mostrarse la cantidad de 1, segundo - la cantidad de 2 y así sucesivamente.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e21 Array Counters.txt','r')
P= a.readlines()

marcas=[]
k=P[0].strip().split()
F=P[1].strip().split()
for x in range(0,int(k[0])):
    marcas.append(int(F[x]))

print(marcas)
"""
P='378 18'
k=P.strip().split()

marcas=[18, 2, 16, 6, 14, 13, 15, 13, 17, 8, 18, 3, 4, 5, 15, 8, 9, 12, 6, 13, 17, 10, 14, 15, 4, 3, 6, 4, 10, 16, 14, 2, 4, 13, 10, 6, 3, 6, 3, 5, 4, 11, 1, 5, 9, 12, 9, 4, 13, 6, 12, 3, 13, 15, 2, 17, 7, 1, 12, 11, 8, 6, 7, 16, 8, 5, 12, 15, 5, 7, 4, 10, 12, 15, 3, 1, 13, 15, 1, 8, 8, 13, 7, 10, 10, 12, 13, 7, 12, 2, 1, 2, 1, 2, 9, 18, 17, 14, 10, 3, 14, 6, 4, 10, 10, 1, 5, 18, 16, 6, 3, 6, 9, 7, 17, 18, 13, 12, 8, 11, 1, 10, 7, 18, 14, 9, 15, 1, 15, 10, 10, 8, 4, 7, 9, 3, 4, 11, 13, 10, 6, 1, 10, 11, 10, 13, 3, 3, 2, 11, 18, 7, 4, 5, 6, 6, 16, 16, 8, 10, 7, 3, 3, 3, 15, 11, 10, 5, 3, 11, 13, 1, 1, 11, 8, 15, 14, 7, 9, 17, 18, 9, 15, 11, 5, 5, 18, 13, 6, 8, 1, 3, 1, 1, 10, 16, 18, 16, 16, 17, 4, 2, 14, 11, 12, 10, 1, 10, 9, 13, 10, 2, 5, 17, 11, 8, 10, 17, 11, 8, 5, 2, 8, 16, 17, 8, 11, 10, 11, 18, 12, 11, 15, 10, 1, 2, 4, 13, 17, 2, 16, 4, 1, 9, 12, 14, 4, 15, 8, 9, 6, 18, 8, 17, 3, 1, 15, 14, 8, 16, 17, 2, 9, 5, 12, 18, 10, 15, 17, 3, 15, 7, 11, 7, 13, 16, 12, 10, 13, 4, 4, 8, 9, 17, 17, 8, 8, 6, 16, 10, 16, 18, 3, 1, 15, 7, 8, 15, 13, 14, 12, 2, 4, 12, 8, 13, 4, 12, 12, 9, 5, 14, 5, 1, 10, 6, 1, 6, 11, 17, 7, 18, 1, 15, 9, 10, 5, 2, 13, 14, 1, 8, 2, 15, 9, 18, 4, 6, 12, 9, 1, 14, 5, 15, 18, 14, 14, 2, 10, 10, 6, 8, 16, 9, 18, 4, 1, 13, 17, 1, 13, 12, 9, 8, 9, 5, 16, 3, 6, 16, 12, 16, 2, 2, 13, 17, 8, 12]

respuesta=''
numeros={}
for x in range(1,int(k[1])+1):
    var=f"cont_{x}"
    numeros[var]=0

for y in range(1,int(k[1])+1):
    for x in marcas:
        if x == y:
            var=f"cont_{y}"
            numeros[var]+=1
j=numeros.values()
for z in j:
    respuesta+=str(z)+' '
print(respuesta)