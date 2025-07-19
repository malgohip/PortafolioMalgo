#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Las sumas de verificación (checksums) son valores pequeños calculados a partir de una gran cantidad de datos para probar si estos son consistentes, ej.: si contienen o no errores.

Por ejemplo si Ana envía algún archivo a Bob, ella puede calcular la suma de verificación y decírsela a Bob, quien calculará la suma de verificación del archivo que recibió y la comparará con el valor dado por Ana.

Otro ejemplo aún más común - cualquier tarjeta bancaria que uses tiene una suma de verificación en el último dígito de su número de tal manera que cualquier dispositivo evitaría que introduzcas un número equivocado por error (puedes leer más de esto en el ejercicio del Algoritmo de Luhn).

Para varias tareas de programación posteriores usaremos un método similar para verificar si el vector resultante es correcto o no. Para evitar problemas con tales tareas, practiquemos ahora el algoritmo para el cálculo de sumas de verificación que estará involucrado.

Enunciado del problema
Se te dará el vector para el cual la suma de verificación debería ser calculada. Realiza los cálculos como sigue: adiciona cada elemento del vector (iniciando desde el comienzo) a la variable resultado y multiplica esta suma por 113 - el módulo o residuo de este nuevo valor entre 10000007 se convertiría en el nuevo valor de la variable resultado, y así sucesivamente.

Lee el artículo de la suma de verificación para una descripción detallada de este algoritmo. Un ejemplo del cálculo se encuentra allí

Los Datos de entrada tendrán en su primera línea la longitud del vector.
Los valores del vector están en la segunda línea, separados por espacios.
La Respuesta debería contener un único valor - la suma de verificación calculada.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e17 Array Checksum.txt','r')
P= a.readlines()

l=P[1].strip().split()
numeros=[]
for x in range(int(P[0])):
    X=int(l[x])
    numeros.append(X)

print(numeros)
"""
numeros=[8, 781, 3133, 63, 92419, 785498, 0, 995459, 9762168, 9786963, 7478, 55989, 2, 35288, 45948, 66, 8500, 604, 79475, 33394971, 22748]

seed=113
limit=10000007
respuesta=0
for x in numeros:
    respuesta=(respuesta+x)*seed
    if respuesta > limit:
        respuesta%=limit
print(str(respuesta))