#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Esta tarea proporciona práctica en la propiedad fundamental de la operación del residuo en la aritmética - la persistencia del residuo sobre la adición y la multiplicación. Esta importante propiedad es a menudo usada para verificar los resultados de los cálculos, en las competencias de programación, en los cálculos de sumas de verificación (checksums) y especialmente para el cifrado.
Revisa Modular arithmetic para una explicación más detallada.

Tenemos aquí una especie de cálculo aritmético extenso, y se nos pide el módulo del resultado con otro número (resultado % M en varios lenguajes).

Si tienes curiosidad acerca por qué la aritmética modular es tan importante, puedes darle un vistazo a los ejercicios Public Key Cryptography Intro y RSA Cryptography.

Los Datos de entrada tendrán:

Número entero inicial en la primera línea;
Una o más líneas describiendo las operaciones, según el formato signo valor donde el signo es + o * y el valor es un entero;
La última línea con la misma forma anterior pero con el signo % en su lugar, y un número entre el cual el resultado debe ser dividido para obtener el residuo.
La Respuesta debería dar el residuo del resultado de todas las operaciones aplicadas secuencialmente (empezando por el número inicial) y dividido entre el último número.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e14 Modular Calculator.txt','r')
P= a.readlines()

operaciones=[]
for x in range(len(P)):
    f=P[x].strip().split()
    if len(f) > 1:
        F=[f[0],int(f[1])]
    else:
        F=f
    operaciones.append(F)

print(operaciones)
"""
operaciones=[['4576'], ['*', 302], ['*', 3], ['*', 4067], ['*', 3], ['*', 425], ['*', 177], ['+', 7351], ['+', 408], ['+', 7], ['*', 60], ['+', 2077], ['+', 1503], ['+', 4], ['*', 4], ['+', 83], ['+', 849], ['*', 799], ['+', 6815], ['+', 3512], ['+', 909], ['+', 8], ['*', 6], ['+', 5228], ['*', 585], ['*', 35], ['+', 918], ['+', 8], ['+', 93], ['+', 539], ['*', 116], ['+', 3352], ['+', 10], ['*', 657], ['*', 1426], ['*', 8], ['*', 7], ['+', 6], ['+', 6], ['+', 7824], ['*', 7], ['*', 8728], ['+', 201], ['+', 527], ['+', 5582], ['*', 7], ['*', 3816], ['+', 918], ['+', 1], ['%', 7435]] 

numero=int(operaciones[0][0])
divisor=operaciones[len(operaciones)-1][1]
for x in range(1,len(operaciones)-1):
    if operaciones[x][0] == '+':
        numero+=operaciones[x][1]
    elif operaciones[x][0] == '*':
        numero*=operaciones[x][1]
    numero%=divisor
print(str(numero))
