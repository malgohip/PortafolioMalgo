#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
Probablemente ya resolvistes el problema Mínimo de tres, ¿ No fue un gran reto ? Los programadores debemos mejorar nuestra lógica (y no solo los conocimientos en lenguajes de programación), cambiaremos el ejercicio para hacerlo más complicado.

Tendrás de nuevo una tripleta de números, pero ahora debes elegir el del medio de ellos, es decir, ni el más grande, ni el más pequeño. Este número se llama Mediana (del conjunto, matriz, etc.).

Asegúrate de que la solución no sea simplemente "otro ejercicio estúpido" - ya que se utiliza como parte de poderosos algoritmos, QuickSort, por ejemplo.

Datos de entrada contendrán en la primera línea el número de la tripletas a tratar. Las siguientes líneas contendrán una tripleta cada una.
La respuesta medianas seleccionadas de las tripletas, separados por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e41 Median of Three.txt','r')
P= a.readlines()

trios=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    trios.append(F)

print(trios)
"""
trios=[[779, 738, 81], [15, 19, 14], [1121, 306, 325], [808, 785, 776], [46, 93, 11], [9, 17, 24], [971, 901, 8], [148, 7, 3], [62, 10, 4], [865, 773, 861], [94, 1376, 949], [10, 19, 746], [184, 179, 192], [14, 19, 6], [6, 784, 741], [1084, 1449, 84], [4, 3, 847], [5, 14, 906], [107, 194, 2], [369, 69, 368], [76, 7, 158], [9, 385, 347], [194, 82, 115], [1, 45, 895]]

def buble_sort(lst):
    for i in range(len(lst)):
        toca=0
        for j in range(0,len(lst)-i-1):
            if lst[j] > lst[j+1]:
                t = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = t
                toca=1
        if not toca:
            break
    return lst

respuesta=''
for x in trios:
    x=buble_sort(x)
    med=x.pop(1)
    respuesta+=str(med)+' '
print(respuesta)