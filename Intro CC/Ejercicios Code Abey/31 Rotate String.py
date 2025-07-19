#Author: Sebastian Ochoa. Date: 08/14/2024
# -*- coding: utf-8 -*-

"""
Rotar la cadena de caracteres en ´K' significa cortar esos caracteres desde el inicio y transferirlos al final de la cadena. Si 'K' es negativo, los caracteres al contrario deben ser transferidos desde el final hasta el inicio.

Datos de entrada contendrán el numero de casos de prueba en la primera linea. 
Las siguientes lineas contendran el numero 'K' y alguna cadena 'S' separada por espacio- un par en cada linea. La cadena 'S' contendra unicamente letras en minusculas. 'K' no excederá la mitad de la longitud de 'S' en valor absoluto. 
Respuesta debe contener cadenas rotadas de acuerdo con la regla anteriormente dada, separadas por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e31 Rotate String.txt','r')
P= a.readlines()

strings=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    X=int(f[0])
    F.append(X)
    F.append(f[1])
    strings.append(F)

print(strings)
"""
strings=[[3, 'zyuzhwljisrlioli'], [7, 'sgqbkumyyjcitotmsk'], [6, 'zrnfeepsueknnhylmoz'], [7, 'eetfvpoaiasjyzgmph'], [4, 'snrlykeidiifahcmit'], [-6, 'ifabbofkbkokehwon'], [5, 'pifciaxusbterjwzjt'], [2, 'ijwaeznieeioeyzvplfuaa'], [5, 'bvtfysaxjucwgwus']]

respuesta=''
for x in strings:
    n_string=''
    if x[0] > 0:
        t=x[1][0:x[0]]
        x[1]=x[1].replace(t,'')
        x[1]+=t
    elif x[0] < 0:
        x[1]+=' '
        t=x[1][x[0]-1:-1]
        x[1]=x[1].replace(t,'')
        x[1]=t+x[1]
    else:
        n_string='None'
    respuesta+=x[1]+' '
print(respuesta)