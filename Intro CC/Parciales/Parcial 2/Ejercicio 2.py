#Author: Sebastian Ochoa. Date: 08/06/2024
# -*- coding: utf-8 -*-

"""
2. Ejercicio

Diseñe un programa que haga uso de la recursividad para definir una función que genere la siguiente serie 
numérica 1, 2, 3, 1, 4, 3, 7, 4, 11, 7,  … Observe que a partir del tercer término, los términos en las 
posiciones impares de la lista, se calculan como la suma de los dos términos inmediatamente anteriores y los 
términos en las posiciones pares se calculan como la diferencia de los dos términos inmediatamente anteriores. 
Se reitera que se considerará bien resuelto el ejercicio, si el diseño de la función incluye llamados así misma 
para el cálculo de los valores que van del quinto término en adelante.
"""

def ejercicio_2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if n %2 ==1:
        return ejercicio_2(n-1) + ejercicio_2(n-2)
    elif n%2 ==0:
        return ejercicio_2(n-1) - ejercicio_2(n-2)

lista=[]
valores=10
for i in range(1, valores+1):
    lista.append(ejercicio_2(i))
print(f"La lista de la serie con {valores} valores es: {lista}")