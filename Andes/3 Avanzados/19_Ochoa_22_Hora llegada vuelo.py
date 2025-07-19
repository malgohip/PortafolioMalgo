# -*- coding: utf-8 -*-
"""
Descripción del problema
Una agencia de viajes necesita informar a sus clientes la hora de llegada de sus vuelos. Se conoce la hora de partida del vuelo (en horas, minutos y segundos) y la duración del vuelo (en horas, minutos y segundos).

Cree una función que retorne la hora de llegada del vuelo en una cadena con el formato “HH:mm:ss” donde HH es la hora, mm los minutos y ss los segundos de la hora de llegada del vuelo.

La hora está dada en formato de 24 horas (su valor se encuentra entre 0 y 23).

Si alguno de los 3 números de la respuesta es menor a 10, sólo se necesita un dígito ( '7' en lugar de '07').
"""

def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int)->str:
    """ Hora de llegada de vuelo
    Indica cual será la hora en la cual un vuelo llegará a su destino.
    Parámetros:
      hora_salida (int): Hora de salida del vuelo (valor entre 0 y 23)
      minuto_salida (int): Minuto de salida del vuelo (valor entre 0 y 59)
      segundo_salida (int): Segundo de salida del vuelo (valor entre 0 y 59)
      duracion_horas (int): Número de horas que dura el vuelo
      duracion_minutos (int): Número de minutos (adicionales al número de horas) que dura el vuelo
      duracion_segundos (int): Número de segundos (adicionales al número de horas y minutos) que dura el vuelo
    Retorno:
      str: Cadena que indica la hora de llegada del vuelo a su destino, la cadena debe estar con el formato “HH:mm:ss”.
    """
    hora_llegada=hora_salida+duracion_horas
    minuto_llegada=minuto_salida+duracion_minutos
    segundo_llegada=segundo_salida+duracion_segundos
    x=segundo_llegada//60
    segundo_llegada=segundo_llegada % 60
    minuto_llegada=x+minuto_llegada
    y=minuto_llegada//60
    minuto_llegada=minuto_llegada % 60
    hora_llegada=y+hora_llegada
    hora_llegada=hora_llegada % 24
    tiempo_llegada=str(hora_llegada)+':'+str(minuto_llegada)+':'+str(segundo_llegada)
    return tiempo_llegada