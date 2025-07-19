# -*- coding: utf-8 -*-
"""
Descripcion del problema
Crear una función que recibiendo un número entero invierta sus cifras, es decir, si el número es 1234, el número que retorne debe ser 4321

Para revisar su ejercicio use el numero 126898 
"""


def numero_invertido(numero_original: int)->int:
    """Número invertido
    evuelve el mismo número pero con sus digitos invertidos.
    Parámetros:
      numero_original (int): Numero que se desea invertir.
    Retorno:
      int: numero original invertido.
    """
    numero_invertido=str(numero_original)[::-1]
    return int(numero_invertido)