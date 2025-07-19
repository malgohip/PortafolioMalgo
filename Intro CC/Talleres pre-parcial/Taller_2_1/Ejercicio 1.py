#Author: Sebastian Ochoa. Date: 07/24/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 1.


Diseñe un código que lea los extremos de una par de segmentos AB y CD de un archivo txt llamado "Datos.txt" 
y que reporte sobre el mismo archivo, reporte si se presenta, traslapo de los segmentos, corte en un único 
punto o ninguno de los casos anteriores.

"""

f=open('Talleres pre-parcial\Taller_2_1\TXTs y JSON\Datos.txt', 'r+')

L = f.readlines()

AB,CD=[],[]
for i in range(1,3):
    a=L[i].strip().split(',')
    A=[]
    for x in a:
        X=float(x)
        A.append(X)
    b=L[i+4].strip().split(',')
    B=[]
    for x in b:
        X=float(x)
        B.append(X)
    AB.append(A)
    CD.append(B)

mAB=(AB[1][1]-AB[0][1])/(AB[1][0]-AB[0][0])
mCD=(CD[1][1]-CD[0][1])/(CD[1][0]-CD[0][0])
resultado="\nLos segmentos no se traslapan ni se cortan en un unico punto."
if mCD == mAB:
    if AB[0] == CD [0] and AB[1] == CD [1] or AB[0] == CD [1] and AB[1] == CD [0]:
        resultado="\nLos segmentos se traslapan"
else:
    cAB=mAB*(-AB[0][0])+AB[0][1]
    cCD=mCD*(-CD[0][0])+CD[0][1]
    x=(cCD-cAB)/(mAB-mCD)
    y=mAB*x+cAB
    corte=[x,y]
    if corte[0] <= AB[0][0] and corte[0] >= AB[1][0] and corte[0] <= AB[0][1] and corte[1] >= AB[1][1] or corte[0] <= AB[0][0] and corte[0] >= AB[1][0] and corte[0] >= AB[0][1] and corte[1] <= AB[1][1] or corte[0] >= AB[0][0] and corte[0] <= AB[1][0] and corte[0] <= AB[0][1] and corte[1] >= AB[1][1] or corte[0] >= AB[0][0] and corte[0] <= AB[1][0] and corte[0] >= AB[0][1] and corte[1] <= AB[1][1]:
        resultado="\nLos segmentos cortan en un unico punto"

f.write(resultado)
f.close()