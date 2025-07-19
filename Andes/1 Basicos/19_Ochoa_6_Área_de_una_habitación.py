# -*- coding: utf-8 -*-
"""
Descripción del problema
Escriba una función que reciba el largo y ancho (en metros) de una habitación 
rectangular. Su función debe calcular y retornar el área del lugar a partir de 
esos parámetros.

Tanto el ancho como el largo son números flotantes, y la respuesta debe estar 
redondeada a dos decimales.
"""
def area_habitacion(largo: float, ancho: float)->float:
    """ Área de una habitación
    Indica cual sería el area de una habitación.
    Parámetros:
      largo (float): Largo de la habitación
      ancho (float): Ancho de la habitación
    Retorno:
      float: Número (float) que representa el área de la habitación redondeada con dos decimales.
    """
    area=largo*ancho
    return round (area,2)