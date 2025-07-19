# -*- coding: utf-8 -*-
"""
Descripción del problema:
El ingeniero Max, le pusieron como trabajo el ordenar dependiendo de la situación ordene dos números de menos a mayor o de mayor a menor.

Realiza un programa que al recibir los dos números y un texto, el cual debe decir "MAYOR" si se requiere que se organice de mayor a menor o "MENOR" si se dbe organizar de menor a mayor. Esta funcion se debe de retornar un texto el cual sean los números ordenados o en caso de que sean iguales que así lo indique.
"""
def ordenador_numeros(numero_1: int, numero_2: int, orden:str)->str:
    """
    Norma de la suma
    ordena los numeros dados en la forma en la que se indique 
    Parámetros:
        numero_1 (int): Primer número a ordenar.
        numero_2 (int): Segundo número a ordenar.
        orden (str): Texo que indica como se debe ordenar (recibe valores entre 'MAYOR' y 'MENOR').
    Retorno:
        str: Texto que indica cual es el orden de los números .
    """
    orden_mayuscula=orden.upper()
    respuesta='Redacte una opcion valida'
    if orden_mayuscula == 'MAYOR':
        if numero_1 > numero_2:
            respuesta=numero_1,numero_2
        if numero_1 < numero_2:
            respuesta=numero_2,numero_1
    elif orden_mayuscula == 'MENOR':
        if numero_1 < numero_2:
            respuesta=numero_1,numero_2
        if numero_1 > numero_2:
            respuesta=numero_2,numero_1
    return respuesta