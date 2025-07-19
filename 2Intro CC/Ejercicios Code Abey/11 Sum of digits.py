#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Los Datos de entrada están en el siguiente formato:

la primera línea contiene N - el número de valores a procesar;
y después siguen N líneas que describen los valores para los cuales la suma de dígitos debe ser calculada mediante 3 enteros A B C;
para cada caso, necesitarás multiplicar A por B y sumar C (ej.: A * B + C) - luego calcular la suma de dígitos del resultado.
La Respuesta debería constar de N resultados, separados también por espacios. Por ejemplo:
"""
"""
a = open('Ejercicios Code Abey\TXTs\e11 Sum of digits.txt','r')
P= a.readlines()

numeros=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    numeros.append(tuple(F))

print(numeros)
"""
numeros=[(88, 92, 33), (81, 283, 156), (222, 266, 149), (18, 296, 54), (227, 157, 61), (287, 124, 97), (68, 207, 187), (362, 194, 35), (349, 15, 51), (228, 200, 187), (309, 66, 199)]

respuesta=''

def digitos(num):
    if num < 10:
        return [num]
    else:
        return digitos(num // 10) + [num % 10]

for x in numeros:
    numero=x[0]*x[1]+x[2]
    digit=digitos(numero)
    suma=0
    for y in digit:
        suma+=y
    respuesta+=str(suma)+' '
print(respuesta)
