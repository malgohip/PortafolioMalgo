#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Cuando hablamos sobre la progresión aritmética (o secuencia aritmética) nos referimos a una serie de números con una propiedad especial - cada valor es seguido por otro que es mayor por una cantidad predefinida (incremento), ej.: la diferencia del (K+1)-ésimo and K-ésimo valor es una constante. A continuación ejemplos de tales secuencias:
Vas a calcular la suma de los primeros miembros de la secuencia aritmética. El artículo de Wikipedia sobre progresión aritmética podría ser de gran ayuda para quien haya escuchado sobre ella por primera vez.

Datos de entrada: La primera línea contiene el número de casos de prueba.
Las otras líneas contienen los casos de prueba en forma de tríos de valores A B N donde A es el primer valor de la secuencia, B es el tamaño del incremento y N y es el número de términos que deberían ser calculados.
Respuesta: Muestra los resultados (la suma of N términos) de cada secuencia separados por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e8 Arithmetic Progression.txt','r')
P= a.readlines()

secuencia=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    secuencia.append(tuple(F))

print(secuencia)
"""
secuencia=[(9, 15, 63), (2, 6, 12), (6, 16, 35), (17, 5, 69), (3, 20, 47), (1, 20, 14), (9, 15, 49), (24, 12, 24), (14, 1, 85), (28, 7, 41)]

str_suma=''
for x in secuencia:
    lista=[]
    suma=0
    for y in range(0,x[2]):
        lista.append(x[0]+y*x[1])
        suma+=x[0]+y*x[1]
        #print(f"repeticion {y+1} del {x}")
    str_suma+=str(suma)+" "
print(str_suma)

