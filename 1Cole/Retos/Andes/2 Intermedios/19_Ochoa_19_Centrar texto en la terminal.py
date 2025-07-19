# -*- coding: utf-8 -*-
"""
Descripción del problema
Escriba una función que reciba como parámetros una cadena de caracteres y un entero que representa el ancho en caracteres de la terminal. La función debe retornar una nueva cadena que consiste en la cadena original pero con la cantidad correcta de espacios al inicio, de forma que la cadena quede centrada en una ventana de terminal del ancho que fue dado como parámetro cuando esta se imprima. Si la cantidad de espacios necesarios al inicio y al final son diferentes, entonces suponga que debe haber menos espacios al inicio.

Por ejemplo: si la cadena es 'abc' y la terminal tiene 10 caracteres, debe haber 3 espacios al inicio y luego debe venir la cadena. Para completar los 10 caracteres tendría que haber 4 espacios al final (¡los espacios del final no deben aparecer en su respuesta!). La función len(…) puede ayudarle a calcular la longitud de la cadena que se da como parámetro.
"""

def centrar_texto(cadena: str, ancho_terminal: int)->str:
    """ Centrar texto en la terminal
    Centra el texto dado en una terminal con un ancho especifico.
    Parámetros:
      cadena (str): El texto a centrar
      ancho_terminal (int): El ancho de la terminal, en número de caracteres máximo por línea
    Retorno:
      str: El texto dado como parámetro, con el número de espacios necesarios al inicio para verse centrado en
           la terminal
    """
    tcadena=len(cadena)
    espacio=ancho_terminal-tcadena
    espacioa=int(espacio/2)
    texto_centrado=(' '*espacioa)+cadena+(' '*espacioa)
    return texto_centrado