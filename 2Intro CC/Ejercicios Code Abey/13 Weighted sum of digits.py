#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Este programa se asemeja a algoritmos más complejos usados para la verificación por redundancia cíclica (CRC) y otras sumas de verificación (checksum), y también en funciones hash para cadenas de caracteres. Por otro lado, te proporcionará un ejercicio más para practicar la separación de valores en dígitos decimales. Quizá quieras intentar Sum of Digits antes de esto.

Calculemos una suma de dígitos, como lo hicimos previamente, pero esta vez multiplicando cada dígito por su posición (contando las posiciones desde la izquierda, y empezando desde 1). Por ejemplo, dado el valor 1776, calculamos la suma ponderada de sus dígitos (llamémosla "spd") como:

spd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60
Los Datos de entrada darán el número de casos de prueba en la primera línea.
Los valores en sí están en la segunda línea. Para cada uno de estos valores vas a calcular su respectiva suma ponderada de dígitos.
Respuesta: Tal como es usual, coloca los resultados en una línea, separándolos con espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e13 Weighted sum of digits.txt','r')
P= a.readlines()


for x in range(1,int(P[0])+1):
    f=P[1].strip().split()
    numeros=[]
    for x in f:
        X=int(x)
        numeros.append(X)

print(numeros)
"""
numeros=[262307204, 174668, 900468, 614432, 123431, 1159, 509, 436811, 3005299, 21, 431722, 5922986, 7740, 196008536, 4894, 38, 6236, 7180, 8, 129816, 9296795, 24, 23411, 263998, 4621, 22, 29, 3255779, 65029, 436036075, 450, 180437557, 597937]

respuesta=''
def digitos(num):
    if num < 10:
        return [num]
    else:
        return digitos(num // 10) + [num % 10]

for x in numeros:
    digt=digitos(x)
    suma=0
    for x in range(len(digt)):
        suma+=((x+1)*digt[x])
    respuesta+=str(suma)+' '
print(respuesta)