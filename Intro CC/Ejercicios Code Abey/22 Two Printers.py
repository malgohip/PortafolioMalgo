#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Juan y María fundaron la editorial J & M y compraron dos impresoras antiguas para equiparla.

Ahora tienen su primer encargo: imprimir un documento que consta de páginas N.

Las impresoras trabajan a diferentes velocidades. Una imprime una página en X segundos y otra en Y segundos.

Ahora, los fundadores de la empresa, quieren saber el tiempo mínimo necesario para imprimir todo el documento con las dos impresoras.

Datos de entrada número de casos de prueba en la primera línea. Luego seguirán los casos de prueba, cada uno en una línea separada. Cada caso de prueba contiene tres valores enteros, X Y N, donde N no superara la cantidad de 1,000,000,000. X e Y son los segundos/pag. de cada impresora.

La respuesta (salida) será los tiempos de impresión mínimos para cada uno de los casos de prueba, separados por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e22 Two Printers.txt','r')
P= a.readlines()

casos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    casos.append(F)

print(casos)
"""
casos=[[3507, 11550, 77399], [263411, 600388, 832], [140140318, 64273448, 7], [293, 693, 1010695], [5, 1, 49946910], [9090072, 13584355, 55], [13, 15, 6932306], [1, 1, 726651399], [1, 1, 732439897], [2, 7, 94956701], [1, 1, 821648715], [15831168, 8009317, 50], [12078, 16900, 31317], [964, 1833, 415590], [4, 3, 201826589], [4, 9, 63773609], [35874, 93658, 8529], [1384, 2607, 349287], [7528, 87194, 3431], [1, 1, 580385955]]

respuesta=''
for i in casos:
    x=i[0]
    y=i[1]
    n=i[2]
    menor = 0
    maxi = min(x, y) * n

    while menor < maxi:
        prom = (menor + maxi) // 2
        paginas_impresas = (prom // x) + (prom // y)

        if paginas_impresas >= n:
            maxi = prom 
        else:
            menor = prom + 1
    respuesta+=str(menor)+' '
print(respuesta)