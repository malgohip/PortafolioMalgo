#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Hay dos sistemas ampliamente extendidos para medir la temperatura - Celsius y Fahrenheit. El primero es muy popular en Europa y el segundo es muy usado en los Estados Unidos por ejemplo.

Según la escala de Celsius, el agua se congela a 0 grados y hierve a 100 grados. Según la de Fahrenheit el agua se congela a 32 grados y hierve a 212 grados. Puedes aprender más en el artículo de Wikipedia sobre la escala de Fahrenheit. Usa estos dos puntos como bases para la conversión de otras temperaturas.

Vas a escribir un programa para convertir grados de Fahrenheit a Celsius.

Los Datos de entrada contiene N+1 valores: el primero de ellos es N en sí (Nota que no deberías intentar convertirlo).
La Respuesta debería contener exactamente N resultados, redondeados al entero más cercano y separados por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e7 Fahrenheit to Celsius.txt','r')
P= a.readlines()

farenheit=[]
f=P[0].strip().split()
for x in range(1,int(f[0])+1):
    X=int(f[x])
    farenheit.append(X)

print(farenheit)
"""
farenheit=[389, 474, 276, 326, 571, 547, 178, 164, 595, 545, 315, 298, 161, 570, 51, 135, 462, 593, 135, 441, 427, 564, 176, 137, 298, 172, 544, 520, 115, 483, 412, 457]

str_celsius=""
for x in farenheit:
    y=(x-32)/1.8
    str_celsius+=str(round(y))+" "

#print(f"Los grados farenheit {farenheit} en celsius son: {str_celsius}")
print(str_celsius)