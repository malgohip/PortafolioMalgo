#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Este problema plantea un ejercicio para aprender la idea principal del algoritmo de ordenamiento de burbuja (bubble-sort), el cual veremos un poco más adelante.

Dada la matriz de enteros, debemos iterar a través de todos los pares de elementos vecinos, comenzando desde el principio, e intercambiar los miembros de cada par en el caso de que el primer elemento sea mayor que el segundo.

Por ejemplo, consideremos una pequeña serie de elementos 1 4 3 2 6 5, marcando qué pares se intercambian y cuáles no:

(1  4) 3  2  6  5  - pasar al siguiente par
1 (4  3) 2  6  5   - intercambiar
1  3 (4  2) 6  5   - intercambiar
1  3  2 (4  6) 5   - pasar al siguiente par
1  3  2  4 (6  5)  - intercambiar
1  3  2  4  5  6   - fin
Esta operación mueve algunos elementos grandes hacia la derecha (hacía el final de la matriz) y algunos elementos más pequeños hacia la izquierda (hacia el principio de la matriz).

Lo más importante es que: el elemento más grande necesariamente se mueve a la última posición.

Datos de entrada contienen la secuencia de elementos de la matriz, todos positivos. Después de este valor sigue -1 para marcar el final (que no debe ser incluido en la matriz).

La respuesta debe contener dos valores: el número de intercambios realizados y la suma de comprobación (checksum) de la matriz después del proceso realizado (separado por espacios). La suma de comprobación (Checksum) se debe calcular exactamente con el mismo método que en la tarea Suma de comprobación de matriz (Array Checksum)
"""
"""
a = open('Ejercicios Code Abey\TXTs\e23 Bubble in Array.txt','r')
P= a.readlines()

l=P[0].strip().split()
numeros=[]
for x in range(len(l)-1):
    X=int(l[x])
    numeros.append(X)

print(numeros)
"""
numeros=[15, 9587, 430, 927, 8178, 6, 3446, 48, 6038, 4, 5970, 43236, 2776, 9964, 5, 0, 2, 37188, 35, 83486, 562, 74094, 3, 19, 53367, 4537, 730, 994, 87, 2665, 71096, 2, 9, 41257, 1, 136, 206, 3]

respuesta=''
cont=0
for x in range(len(numeros)-1):
    i=numeros[x]
    j=numeros[x+1]
    prov=0
    if i > j:
        prov=i
        numeros[x]=j
        numeros[x+1]=prov
        cont+=1

seed=113
limit=10000007
checksum=0
for x in numeros:
    checksum=(checksum+x)*seed
    if checksum > limit:
        checksum%=limit
respuesta+=str(cont)+' '+str(checksum)
print(respuesta)