#Author: Sebastian Ochoa. Date: 07/30/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 4.

Diseñe un programa que haga uso de una función definida recursivamente y  que genere la 
siguiente serie numérica  1, 1,  5, 10, 19, 37, 69 … Observe que cada término de la serie 
(a partir del cuarto) se obtiene al sumar los trés términos anteriores y agregar 3.

Se considerará bien resuelto el ejercicio, si el diseño de la función,  incluye llamados así misma 
para el cálculo de los valores que van del cuarto término en adelante.
"""

def ejercicio_4(n):
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 5
    else:
        return ejercicio_4(n-1) + ejercicio_4(n-2) + ejercicio_4(n-3) + 3

lista=[]
valores=10
for i in range(1, valores+1):
    lista.append(ejercicio_4(i))
print(f"La lista de la serie con {valores} valores es: {lista}")