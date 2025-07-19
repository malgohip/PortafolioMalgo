# -*- coding: utf-8 -*-
"""
Descripción del problema
Cree una función que reciba una duración de un periodo de tiempo en términos de días, horas, minutos y segundos (es decir, debe recibir 4 parámetros) y retorne el total  de segundos equivalente a esta duración.
"""

def tiempo_a_segundos(dias: int, horas: int, mins: int, seg: int)->int:
    """tiempo a segundos
    Cambia la cantidad de tiempo dada a segundos.
    Parámetros:
      dias (int): Número de dias del periodo de tiempo
      horas (int): Número de horas del periodo de tiempo
      mins (int): Número de minutos del periodo de tiempo
      seg (int): Número de segundos del periodo de tiempo
    Retorno:
      int: Número de segundos al que equivale el periodo de tiempo dado como parámetro
    """
    
    s_dias = dias*24*60*60
    s_horas=horas*60*60 
    s_minutos=mins*60
    
    Totalsegundos=s_dias+s_horas+s_minutos+seg
    
    return  Totalsegundos