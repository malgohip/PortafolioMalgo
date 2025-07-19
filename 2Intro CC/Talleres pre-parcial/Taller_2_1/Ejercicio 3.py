#Author: Sebastian Ochoa. Date: 07/24/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 3.

Diseñe un código que permita construir un archivo de datos llamado "Longitud.txt" que guarde las 
longitudes de una colección de escarabajos rinoceronte para un estudio de campo. Además, el código debe 
leer la información del archivo y calcular  el promedio y la desviación estandar de las longitudes, dichos 
resultados deben ser escrito en un archivo llamado "Resultados.txt" con un mensaje que diga "El promedio  
de  las longitudes de los escarabajos rinoceronte es: _____ y la desviación estándar es:_______".
"""

import math as mt

f=open('Talleres pre-parcial\Taller_2_1\TXTs y JSON\Longitud.txt', 'w')

n=int(input("Hola, dime la cantidad de datos de la longitud de los escarabajos rinocerontes que desees incluir en el archivo: "))

f.write('Los datos de la longitud de los escarabajos rinoceronte son:\n')
for x in range(1,n+1):
    valor=float(input("Dime el valor de su longitud: "))
    linea=str(valor)+'\n'
    f.write(linea)
f.close()

f=open('Talleres pre-parcial\Taller_2_1\TXTs y JSON\Longitud.txt', 'r')
L = f.readlines()

l=len(L)
datos=[]
for x in range(1,l):
    a=L[x].strip()
    datos.append(float(a))

g=open('Talleres pre-parcial\Taller_2_1\TXTs y JSON\Resultados.txt','w')

N=len(datos)
sumatoria_d=0
for x in datos:
    sumatoria_d+=x
promedio=sumatoria_d/N

sumatoria_des=0
for y in datos:
    sumatoria_des+=(y-promedio)**2

desviacion=mt.sqrt(sumatoria_des/N)

resultado=f'El promedio  de  las longitudes de los escarabajos rinoceronte es: {promedio} y la desviacion estandar es: {desviacion}.'

g.write(resultado)
g.close()