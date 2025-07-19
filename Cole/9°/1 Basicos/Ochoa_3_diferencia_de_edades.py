# -*- coding: utf-8 -*-
"""
Descripciópn del problema:
Un profesor quiere saber cual de los tres hermanos de la familia Cicua a los que le da clase es el mayor, así que necesita una función que le de este dato, además tiene los datos de los nombres de los hermanos.
Realice una función que le permita rápidamente al profesor saber cual de los 3 hermanos es el mayor y retorne el nombre del hermano mayor.
"""
def diferencia_edades(nombre_1: str, nombre_2: str, nombre_3: str, edad_1 :int, edad_2 :int, edad_3 :int)->str:
    """
    diferencia de edades
    Indica cual o cuales los hermanos que son mayores.
    Parámetros:
        nombre_1 (str): Nombre del primer hermano.
        nombre_2 (str): Nombre del segundo hermano.
        nombre_3 (str): Nombre del tercer hermano.
        edad_1 (int): Edad del primer hermano.
        edad_2 (int): Edad del segundo hermano.
        edad_3 (int): Edad del tercer hermano.
    Retorno:
        str: Nombre  del hermano de mayor edad
    """
    mayor='Los 3 hermanos tienen la misma edad.'
    if edad_1 > edad_2 and edad_1 > edad_3:
        mayor=nombre_1,'es el mayor.'
    elif edad_2 > edad_1 and edad_2 > edad_3:
        mayor=nombre_2,'es el mayor.'
    elif edad_3 > edad_1 and edad_3 > edad_2:
        mayor=nombre_3,'es el mayor.'
    elif edad_1 == edad_2 and edad_1 > edad_3:
        mayor=nombre_1,'y',nombre_2,'son los mayores.'
    elif edad_1 > edad_3 and edad_1 > edad_2:
        mayor=nombre_1,'y',nombre_3,'son los mayores.'
    elif edad_2 == edad_3 and edad_2 > edad_1:
        mayor=nombre_2,'y',nombre_3,'son los mayores.'
    return mayor