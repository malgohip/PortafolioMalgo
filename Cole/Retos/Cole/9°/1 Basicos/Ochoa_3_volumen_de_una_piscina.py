# -*- coding: utf-8 -*-
"""
Descripción del problema:
El arquitecto Andrés está construyendo su casa de verano y quiere hacer una piscina, pero antes quiere hallar el volumen que esta ocupará.
Realice una función que le permita a Andrés hallar el volumen de la piscina y retorne el volumen con decimales.
"""
def volumen_piscina(largo: float, ancho: float, profundo: float)->float:
    """
    volumen piscina
    Indica el volumen de una piscina.
    Parámetros:
        largo (float): Largo de la piscina (recibe valores entre 1 y 1012).
        ancho (float): Ancho de la piscina (recibe valores entre 1 y 1012).
        profundo (float): Profundidad de la piscina (recibe valores entre 0.1 y 45).
    Retorno:
        float: Valor del volumen de la piscina.
    """
    volumen=largo*ancho*profundo
    return volumen