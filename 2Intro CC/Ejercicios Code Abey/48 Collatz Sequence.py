#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
Este es uno de los problemas matematicos más misteriosos del siglo pasado -- porque su planteamiento es extremadamente simple- y porque la prueba es aún desconocida. Sin embargo, ofrece un buen ejercicio de programación para novatos.

Suponga que selecionamos un valor inicial 'X' y luego construimos una secuencia de valores siguiendo las reglas a continuación:

si X es par (es decir, X modulo 2 = 0) entonces
    Xsiguiente = X / 2
  sino
    Xnext = 3 * X + 1
Es decir, si X es impar, la secuencia crecerá -- y si es par, la secuencia decrecerá. Por ejemplo, con X = 15 tenemos la secuencia:

15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1
Después de que la secuencia alcanza '1' entra en el loop 1 4 2 1 4 2 1....

La intriga está en el hecho de que dado cualquier numero inicial 'X' la secuencia tarde o temprano alcanza '1' - sin embargo imaginate que esta conjetura de Collatz fue expresada en '1937' y hasta el momento nadie ha logrado probar o encontrar un contraejemplo (Es decir, un numero para el cual la secuencia no termina en '1' --ya sea un entero para el cual el loop es más grande que un loop creciendo hasta infinitamente) de que la conjetura es para cualquier 'X'.

Tu tarea es que para los numeros dados calcules cuantos pasos son necesarios para llegar a '1'

Datos de entrada en la primera linea contiene el numero de casos a calcular.
La segunda linea contiene los casos de prueba- Es decir, los valores para los cuales el calculo debe ser hecho. Respuesta debe contener la misma cantidad de resultados, cada una de ellas dando la cuenta del numero de pasos en la secuencia de Collatz para llegar a ´1´.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e48 Collatz Sequence.txt','r')
P= a.readlines()

l=P[1].strip().split()
numeros=[]
for x in range(int(P[0])):
    X=int(l[x])
    numeros.append(X)

print(numeros)
"""
numeros=[30, 2695, 34, 167, 100, 1297, 1572, 149, 573, 43, 388, 41, 36, 11, 50, 9068, 12704, 258, 241, 3275, 33157, 32, 10, 2690]

respuesta=''
for x in numeros:
    cont=0
    while x != 1:
        cont+=1
        if x%2 ==0:
            x/=2
        else:
            x=(x*3)+1
    respuesta+=str(cont)+' '
print(respuesta)