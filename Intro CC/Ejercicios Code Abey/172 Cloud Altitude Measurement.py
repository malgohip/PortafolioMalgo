#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Supposing you have already learned Tree Height Measurement, let us discuss more interesting task. It could arose in two cases:

either the tree we are measuring is not directly accessible (it is on the other bank of the river!) and we could not measure distance to it simply by walking;
or we are trying to measure the altitude of a cloud (or aircraft, or even the moon) - any object which has no "trunk" to which we can walk to measure the distance.
We nevertheless can solve this puzzle! Look at the picture above - we need to make angle measurement twice (instead of once) from two different points, and also measure distance between them. E.g. we choose two points (on the same line with the tree or cloud) and take angles A and B from them. We could not measure distance D2 (either because it is over the river, or because an object have no vertical "trunk"), but we measure D1 instead. Now we get the two equations involving two tangents instead of one:

H   =   tan(B) * D2
H   =   tan(A) * (D1 + D2)   =   tan(A) * D1  +  tan(A) * D2
Now it should be easy for you to exclude unknown D2 and calculate the height!

Of course in real case it becomes bit more tricky since while you run distance between two points, the cloud can move so it is better to have two observers performing synchronized measurements. Also for large clouds it is important to choose a single point to aim both times.

Input data will contain the amount of clouds (or aircrafts) we are curious about.
Each line describes D1, A and B for a single cloud.
Answer should contain altitudes of the objects, rounded to nearest integer.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e172 Cloud Altitude Measurement.txt','r')
P= a.readlines()

numeros=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=float(x)
        F.append(X)
    numeros.append(F)

print(numeros)
"""
import math
numeros=[[3470.0, 23.1384, 62.0766], [2088.0, 22.8775, 51.3402], [2289.0, 26.451, 59.875], [981.0, 39.8092, 66.252], [920.0, 28.0165, 68.1827], [1764.0, 26.1104, 52.3916], [1340.0, 33.6853, 52.4027], [1520.0, 22.0409, 58.6357], [1094.0, 22.127, 53.1301], [1395.0, 33.866, 56.9676], [1466.0, 31.0665, 52.7661], [1377.0, 23.3134, 63.9246], [3149.0, 22.7921, 51.3472], [1396.0, 22.6178, 56.5911], [385.0, 36.9412, 52.7523], [3192.0, 21.8014, 57.3864], [2499.0, 22.0428, 56.9893]]

def altura_H(D1, A, B):
    A_rad = math.radians(A)
    B_rad = math.radians(B)
    H = (math.tan(B_rad) * math.tan(A_rad) * D1) / (math.tan(A_rad) - math.tan(B_rad))
    return round(-H)

respuesta=''
for x in numeros:
    respuesta+=str(round(altura_H(x[0],x[1],x[2])))+' '

print(respuesta)