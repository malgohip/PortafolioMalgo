# -*- coding: utf-8 -*-
"""
Descripción del problema:
El ingeniero Pedro tiene 2 piscinas en el hotel que acaban de terminar, pero le pidieron que diga cual es la diferencia del volumen de agua que esta entre ambas piscinas.

Realiza un programa el cual recibiendo los velores de las medidas de las 2 piscinas pueda devolver cual es la diferencia entre sus volumenes.
"""

from Ochoa_3_volumen_de_una_piscina import volumen_piscina
def diferencia_piscinas(largo_1: float, ancho_1: float, profundo_1: float, largo_2: float, ancho_2: float, profundo_2: float)->float:
    """
    Diferencia piscinas
    Indica cuanto es la diferencia entre el volumen de las piscinas.
    Parámetros:
        largo_1 (float): Largo de la primera piscina (recibe valores entre 1 y 1012).
        ancho_1 (float): Ancho de la primera piscina (recibe valores entre 1 y 1012).
        profundo_1 (float): Profundidad de la primera piscina (recibe valores entre 0.1 y 45).
        largo_2 (float): Largo de la segunda piscina (recibe valores entre 1 y 1012).
        ancho_2 (float): Ancho de la segunda piscina (recibe valores entre 1 y 1012).
        profundo_2 (float): Profundidad de la segunda piscina (recibe valores entre 0.1 y 45).
    Retorno:
        float: Diferencia del volumen de estas piscinas.
    """
    volumen_1=volumen_piscina(largo_1, ancho_1, profundo_1)
    volumen_2=volumen_piscina(largo_2, ancho_2, profundo_2)
    diferencia=abs(volumen_1-volumen_2)
    return diferencia 