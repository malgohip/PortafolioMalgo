#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Cuando los programas procesan números que tienen una parte decimal, algunas veces queremos redondear tales valores a números enteros. Necesitaremos esto para programar algunos problemas posteriores (por ejemplo, para hacer las respuestas más sencillas), así que dediquemos el siguiente ejercicio a aprender este truco.

Hay varios pares de números. Para cada par, dividirás el primer número entre el segundo y mostrarás el resultado redondeado al entero más cercano.

En ciertos casos, cuando el resultado contenga exactamente 0.5 como parte decimal, el valor debería ser redondeado hacia arriba (ej.: sumando otro 0.5). Nota que para valores negativos, "mayor que" quiere decir "más cercano a cero". Revisa la página de Wikipedia sobre Redondeo para explicación más detallada.

En cualquier problema posterior, cuando se mencione redondeo - se asume que es el mismo algoritmo de redondeo (a menos que explícitamente se especifique otro).

Los Datos de entrada darán un número de casos en la primera línea.
Cada una de las siguientes líneas contendrá un caso de prueba (ej.: un par de números).
La Respuesta debería contener los resultados divididos y redondeados para cada par, separados por espacios.
"""
"""
a = open( 'Ejercicios Code Abey\TXTs\e6 Rounding.txt','r')
P= a.readlines()

valores=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    valores.append(tuple(F))

print(valores)
"""
valores=[(-1312131800, -280400), (95556396, 773736), (0, -70045), (271652920, 15664), (1979471698, 5000), (-2141851728, 133088), (1884522097, -90441), (974443692, -88824), (798075177, -48058), (1202637878, -72522), (1735765974, 179028), (20455050, 980), (1930583286, -211212), (-280339907, -64681), (-1744113930, 88820), (0, 321), (360769097, 35955)]

divisiones_rond=''
for x in valores:
    division=x[0]/x[1]
    decimal=division-int(division)
    if abs(int(decimal*10)) != 5:
        division_rond=int(round(division))
    else:
        
        if division < 0:
            division_rond=int(division)-1
        else:
            division_rond=int(division)+1
    divisiones_rond+=str(division_rond)+" "
    #print(f"El restultado de la división de {x[0]} y {x[1]} es: {division}, y este redondeado es {division_rond}")
print(divisiones_rond)