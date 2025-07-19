# -*- coding: utf-8 -*-
"""
Cree una función que calcule la edad de una persona a partir de su fecha de nacimiento y la fecha actual.

Ambas fechas se dan en años, meses y días, y la edad debe retornarse de la misma manera, en una cadena de la forma “aa,MM,dd”. Suponga que todos los meses son de 30 días.

Por ejemplo, si Julieta Pérez nació el 20 de Noviembre de 1986, y la fecha actual fuese el 16 de Octubre de 1987, la función retornaría que la edad de Julieta es “0,10,26”, es decir, 0 años, 10 meses y 26 días.
"""

def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int)->str:
    """ 
    calcular edad
    Indica la edad exacta que tiene una persona en un cierto momento.
    Parámetros:
      dia_nacio (int): Dia de nacimiento de la persona
      mes_nacio (int): Mes de nacimiento de la persona
      anio_nacio (int): Año de nacimiento de la persona
      dia_actual (int): Dia de la fecha actual
      mes_actual (int): Mes de la fecha actual
      anio_actual (int): Año de la fecha actual
    Retorno:
      str:  Cadena en que se indica la edad de la persona en años, meses y días
    """
    anio_edad=anio_actual-anio_nacio
    mes_edad=mes_actual-mes_nacio
    dia_edad=dia_actual-dia_nacio
    x=dia_edad//30
    dia_edad=dia_edad % 30
    mmes_edad=x+mes_edad
    y=mes_edad//12
    mes_edad=mes_edad % 12
    anio_edad=y+anio_edad
    edad_persona='la persona tiene '+str(anio_edad)+' años, '+str(mes_edad)+' meses y '+str(dia_edad)+' días.'
    return edad_persona