#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
El pequeño Merlin quiere ser meteorologo. El mide la temperatura del aire cada hora así que despues de varios dias el tiene una larga secuencia de valores.

Sin embargo, sus instrumentos no son ideales por lo que las mediciones no son exactas--pues aleatoreamente saltan hacia arriba y hacia abajo algunos grados del valor real.

observando esto, Merlin decide hacer los datos más suaves. Para lograrlo, el solo necesita que cada valor sea substituido por el promedio de sus dos vecinos. Por ejemplo, si el tiene una secuencia de cinco valores como esta:

3 5 6 4 5
Entonces el segundo (i.e. 5) debe ser sustituido por (3 + 5 + 6) / 3 = 4.66666666667,
el tercero (i.e. 6) debe ser sustituido por (5 + 6 + 4) / 3 = 5,
el cuarto (i.e. 4) debe ser sustituido por (6 + 4 + 5) / 3 = 5.
Por convencion, los valores primero y ultimo permanecerán iguales.

En la imagen de arriba la linea azul muestra los datos sin procesar, mientras que la roja los muestras suavizados.

Tienes que escribir un programa que le ayude al pequeño Merlin con este algoritmo de procesamiento digital de señales.

Datos de entrada En esta primera linea, se dará la longitud de la secuencia de datos de la segunda linea.
La segunda linea contendra las mediciones. Respuesta debe contener la secuencia procesada. Todos los valores deben ser calculados con una precision minima de 1e-7.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e57 Smoothing the Weather.txt','r')
P= a.readlines()

l=P[1].strip().split()
valores=[]
for x in range(int(P[0])):
    X=float(l[x])
    valores.append(X)

print(valores)
"""
valores=[29.0, 35.1, 40.3, 32.8, 47.3, 59.9, 52.5, 46.7, 47.2, 42.5, 35.3, 35.2, 30.1, 24.5, 20.1, 15.2, 0.2, 10.3, 11.5, 15.4, 17.4, 15.9, 19.4, 38.5, 22.3, 35.2, 35.5, 48.3, 48.0, 49.4, 40.5, 49.2, 52.2, 49.3, 40.3, 34.5, 30.0, 20.7, 20.0, 15.9, 10.3, 10.7, 10.1, 11.1, 8.6, 17.6, 19.5, 16.2, 19.8, 35.2, 40.0, 33.9, 47.8, 36.9, 50.0, 48.2, 57.2, 43.4, 44.7, 35.2, 30.0, 32.2, 11.4, 18.5, 14.7, 10.1, -3.3, -2.6, 12.7, 15.6, 25.6, 24.2, 30.2, 38.4, 42.0, 32.1, 46.0, 48.2, 47.9, 52.7, 51.3, 40.6, 44.7, 35.4, 29.0, 24.8, 6.7, 12.9, 4.7, 12.3, 9.2, 25.7, 19.5, 15.9, 18.4, 25.7, 29.9, 35.1, 39.2, 44.4, 47.0, 38.4, 50.0, 53.1, 59.0, 48.1, 27.5, 34.4, 27.9, 38.1, 20.0, 15.5, 13.3, 8.3, -1.7, 7.3, 15.8, 14.3, 18.3, 23.9, 30.0, 46.9, 29.8, 34.6, 52.7, 45.9, 50.8, 51.0, 47.3, 46.8, 40.0, 35.2, 18.7, 26.2, 24.3, 10.0, 7.5, 13.8, 10.0, 10.5, 9.6, 15.9, 16.1, 24.8, 40.2, 34.8, 34.6, 44.1, 39.9, 55.2, 49.3, 49.7, 48.6, 36.5, 43.1, 35.2, 30.0, 20.3, 20.0, 24.4, 11.3, 18.1, 8.6, 9.6, 11.1, 20.8, 20.5, 39.4, 36.8, 35.2, 40.0, 44.1, 34.9, 56.4, 52.0, 49.6, 45.8, 41.8, 47.7, 48.4, 23.7, 24.2, 20.0, 15.0, 13.4, 10.8, 3.7, 10.8, 27.7, 15.9, 15.3, 10.3, 29.6, 36.6, 35.1, 42.8, 45.7, 45.6, 50.0, 40.7, 41.7, 41.2, 50.2, 34.3, 32.9, 26.3, 20.2, 15.8, 19.3, 10.7, 14.1, 8.3, 12.5, 15.4, 19.9, 24.9]

respuesta=''
proms=[]
for i in range(len(valores)):
    if i == 0 or i == len(valores)-1:
        proms.append(valores[i])
    else:
        prom=(valores[i-1]+valores[i]+valores[i+1])/3
        proms.append(prom)
for x in proms:
    respuesta+=str(x)+' '
print(respuesta)
