#Author: Sebastian Ochoa. Date: 08/05/2024
# -*- coding: utf-8 -*-

"""
4. Ejercicio

Diseñe un código que permita construir un archivo de datos llamado "Alturas.txt" que guarde las alturas de una 
colección de plantas de un jardín botánico . Además, el código debe leer la información del archivo y calcular 
el promedio y la desviación estandar de las alturas, dichos resultados deben ser escrito en un archivo llamado 
"Resultados.txt" con un mensaje que diga "El promedio  de  las altura de las plantas es: _____ y la 
desviación estándar es:_______".
"""

from math import sqrt

f=open('Talleres pre-parcial\Taller_2_2\TXTs y JSON\Alturas.txt', 'w')

n=int(input("Hola, dime la cantidad de datos de la altura de las plantas del jardín botánico que desees incluir en el archivo: "))

f.write('Los datos de la altura de las plantas del jardín botánico son:\n')
for x in range(1,n+1):
    valor=float(input("Dime el valor de su altura: "))
    linea=str(valor)+'\n'
    f.write(linea)
f.close()

f=open('Talleres pre-parcial\Taller_2_2\TXTs y JSON\Alturas.txt', 'r')
L = f.readlines()

l=len(L)
datos=[]
for x in range(1,l):
    a=float(L[x].replace('\n', ''))
    datos.append(float(a))

g=open('Talleres pre-parcial\Taller_2_2\TXTs y JSON\Resultados.txt','w')

N=len(datos)
sumatoria_d=0
for x in datos:
    sumatoria_d+=x
promedio=sumatoria_d/N

sumatoria_des=0
for y in datos:
    sumatoria_des+=(y-promedio)**2

desviacion=sqrt(sumatoria_des/N)

resultado=f'El promedio  de  las altura de las plantas es: {promedio} y la desviación estándar es: {desviacion}.'

g.write(resultado)
g.close()