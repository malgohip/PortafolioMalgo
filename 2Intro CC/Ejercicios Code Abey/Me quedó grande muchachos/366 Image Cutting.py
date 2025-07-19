#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
TV screens have a fixed width to height ratio. This is usually 16:9. Images that are shown in the television have to have this exact aspect ratio.

If you want to show your image in a device which accepts images with a fixed aspect ratio, you must first cut it to the requested ratio. But you do not want to lose too much of your image. What is the biggest area of the image you can cut for a given aspect ratio, in pixel squares if your image has a certain width and height in pixels?

Input data: First line will contain number of images to be cut. Other lines will contain width and height of the image WxH and the aspect ratio of the display W:H separated by space.
Answer: You should output the area of the fitting part of the image.
"""

a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e366 Image Cutting.txt','r')
P= a.readlines()

pantallas=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for y in range(len(f)):
        if y == 0:
            j=f[y].split('x')
            for z in j:
                Z=int(z)
                F.append(Z)
        else:
            j=f[y].split(':')
            for z in j:
                Z=int(z)
                F.append(Z)
    pantallas.append(F)

print(pantallas)

#pantallas=[[1721, 2009, 9, 16], [827, 1683, 5, 4], [5912, 3824, 3, 2], [313, 5193, 3, 2], [1710, 3311, 2, 1], [772, 4207, 3, 2], [2882, 4657, 9, 16], [4397, 3464, 16, 9], [1883, 1820, 2, 1], [4406, 3798, 2, 3], [1460, 2170, 2, 3], [268, 4722, 5, 4], [4158, 3863, 16, 9], [4545, 4983, 5, 4], [736, 1938, 5, 4], [5147, 3109, 5, 4], [1278, 3735, 5, 4]]

def calcular_area_max(ancho, alto, aspecto_a, aspecto_h):
    if aspecto_a >= aspecto_h:
        if ancho >= alto:
            if cort_h*aspecto_a/aspecto_h < 
            cort_h=alto
            cort_a=cort_h*aspecto_a/aspecto_h
        else:
            cort_a=ancho
            cort_h=cort_a*aspecto_h/aspecto_a
    else:
        if ancho < alto:
            cort_a=ancho
            cort_h=cort_a*aspecto_h/aspecto_a
        else:
            cort_h=alto
            cort_a=cort_h*aspecto_a/aspecto_h
    return cort_a*cort_h

respuesta=''
for x in pantallas:
    print(x)
    max_area=calcular_area_max(x[0],x[1],x[2],x[3])
    respuesta+=str(int(max_area))+' '
print(respuesta)