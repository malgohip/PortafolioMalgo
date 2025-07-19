#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Muchos problemas matemáticos en programación no son resueltos exactamente, sino aproximadamente, mediante varias computaciones del resultado, cada de una de las cuales se acerca cada vez más al objetivo.

Practiquemos con el siguiente enfoque el método de cálculo aproximado de la raíz cuadrada:

Busca la raíz cuadrada r del valor dado X.
Usa algún valor arbitrario, por ejemplo r = 1 como la primera aproximación (seguramente no es la más adecuada).
Para un cálculo apropiado de la raíz cuadrada, la ecuación r = X / r debe cumplirse.
Calcula d = X / r (d no sería igual a r, ya que r no es la raíz exacta).
Toma el promedio entre r y d como la nueva aproximación.
Ej.: La fórmula general de cada iteración del cálculo es (:= es una asignación):

      r  +  X / r
r := -------------
           2
Remítete al artículo de Aproximación de la Raíz Cuadrada para más detalles sobre el Método de Herón.

Se nos dan entonces valores de X para los cuales se realizarán los cálculos y el número de iteraciones N a ejecutar.
Usa r = 1 al comienzo, y muestra la aproximación resultante (después de las N iteraciones).

Los Datos de entrada darán el número de casos de prueba en la primera línea.
Las siguientes líneas contendrán los casos de prueba en sí mismos, cada uno conteniendo un valor X, para el cual la raíz cuadrada debería ser calculada, y N - el número de iteraciones de cálculo.
La Respuesta debería contener las aproximaciones calculadas para cada caso, separadas por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e18 Square Root.txt','r')
P= a.readlines()

pruebas=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    pruebas.append(F)

print(pruebas)
"""
pruebas=[[37, 1], [50, 9], [63390, 11], [4287, 13], [86785, 6], [7134, 3], [208, 1], [59142, 5], [957, 4], [9607, 11], [78, 12], [842, 7]]

respuesta=''
for x in pruebas:
    r=1
    for y in range(x[1]):
        r=(r+x[0]/r)/2
    respuesta+=str(r)+' '
print(respuesta)