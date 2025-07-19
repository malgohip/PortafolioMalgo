#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Una rama importante de las matemáticas que usa extensivamente la programación es la estadística - ej.: cálculo de características de algún conjunto de datos (Piensa en las estadísticas de visitantes/visualizaciones de página del sitio, etc.). El aprendizaje de esta disciplina se inicia usualmente familiarizándose con el concepto de valor promedio.

El valor promedio (o media) de varios números puede ser calculado como su suma dividida por su cantidad. Por ejemplo:

prom(2, 3, 7) = (2 + 3 + 7) / 3 = 4
prom(20, 10) = (20 + 10) / 2 = 15
Te serán dados varios vectores, para cada uno de los cuales encontrarás un valor promedio.

Los Datos de entrada darán el número de casos de prueba en la primera línea.
Después seguirán los casos de prueba en sí, un caso por línea.
Cada caso de prueba describe un vector de números enteros, con el valor 0 señalando su finalización (¡¡¡este cero no debe ser incluido en los cálculos!!!).
La Respuesta debería contener valores promedios para cada vector, redondeados al entero más cercano (ver la tarea sobre Redondeo), y separados por espacios.
"""
"""
a = open( 'Ejercicios Code Abey\TXTs\e16 Average of an array.txt','r')
P= a.readlines()

valores=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in range(len(f)-1):
        X=int(f[x])
        F.append(X)
    valores.append(F)

print(valores)
"""
valores=[[1324, 1066, 3067, 4054, 2494, 949, 642, 2374, 1360, 2792], [3334, 2322, 1960, 1025, 460, 876, 4095, 3811, 291, 3414, 1102, 3873, 3293], [1305, 446, 237, 265, 1600, 1956], [488, 12, 286, 120, 283, 238, 187, 392, 48], [2305, 1925, 2880, 11390, 2273, 4456, 12035, 2687, 8446, 6746, 1075, 9922, 14011], [266, 501, 254, 78, 130, 345, 329, 25, 89, 209, 294, 285, 185, 281], [8069, 1065, 7016, 3144, 3450, 7006, 2325, 1395, 1075], [435, 1102, 5717, 9997, 11110, 15956, 6662, 6728], [3701, 5423, 5911, 3474, 882, 4618, 5026, 8069, 561, 5676, 5259], [9802, 8903, 7797, 3319, 2820, 14182], [83, 361, 445, 325, 73, 498, 329, 193, 234, 495, 437, 312, 72, 38, 319]]

def redondear(num):
    decimal= num-int(num)
    if abs(int(decimal*10)) != 5:
         num_rond=int(round( num))
    else:
        
        if  num < 0:
             num_rond=int(num)-1
        else:
             num_rond=int(num)+1
    return num_rond

respuesta=''
for x in valores:
    suma=0
    for y in x:
        suma+=y
    promedio=suma/len(x)
    respuesta+=str(redondear(promedio))+' '
print(respuesta)