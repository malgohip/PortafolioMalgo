#Author: Sebastian Ochoa. Date: 08/06/2024
# -*- coding: utf-8 -*-

"""
3. Ejercicio

En un archivo de datos llamado "Alturas.txt" se tienen guardadas las alturas de una colección de plantas de un 
jardín botánico. Se requiere un programa que lea el archivo y determine el número de plantas que hay con 
alturas en un intervalo [a,b] en donde a y b son dadas por el usuario. La respuesta del cálculo debe 
quedar en otro archivo denominado "Resultados.txt" con un mensaje que diga "El número de plantas en el rango 
[a,b] es: _____"
"""

from math import sqrt

f=open('Parciales\Parcial 2\TXTs y JSON\Alturas.txt', 'w')

n=int(input("Hola, dime la cantidad de datos de la altura de las plantas del jardín botánico que desees incluir en el archivo: "))

f.write('Los datos de la altura de las plantas del jardín botánico son:\n')
for x in range(1,n+1):
    valor=float(input("Dime el valor de su altura: "))
    linea=str(valor)+'\n'
    f.write(linea)
f.close()

f=open('Parciales\Parcial 2\TXTs y JSON\Alturas.txt', 'r')
L = f.readlines()

l=len(L)
datos=[]
for x in range(1,l):
    a=float(L[x].replace('\n', ''))
    datos.append(float(a))
print(datos)
g=open('Parciales\Parcial 2\TXTs y JSON\Resultados.txt','w')

print("Perfecto, ahora necesito los datos del intervalo que quieres revisar entre las alturas de las plantas.")
men_val=float(input("Dime el menor valor que tendrá tu intervalo: "))
may_val=float(input("Dime el mayor valor que tendrá tu intervalo: "))

en_rango=[]

for i in datos:
    if i >= men_val and i <= may_val:
        en_rango.append(i)

resultado=f'El número de plantas en el rango [{men_val},{may_val}] es: {len(en_rango)}'

g.write(resultado)
g.close()