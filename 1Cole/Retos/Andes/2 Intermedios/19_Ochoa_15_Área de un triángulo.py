# -*- coding: utf-8 -*-
import math
"""
Descripción del problema
El área de un triángulo puede ser calculada cuando se conoce la longitud de sus lados. Teniendo en cuenta que s1, s2 y s3,  son las longitudes de los lados del triángulo, y tomando s=(s1 + s2 + s3)/2 , el área puede ser calculada de la siguiente manera:
Area= Raizcuadrada de (s*(s-s1)*(s-s2)*(s-s3))
Cree una función que recibe la medida de los lados del triángulo y retorna el área del mismo, redondeada a una cifra decimal.

El módulo math puede ser de ayuda para calcular la raíz cuadrada.
"""

def area_triangulo(s1: float, s2: float, s3: float)->float:
    """ Área de un triángulo
    Indica cuanto sería el area de un triangulo.
    Parámetros:
      s1 (float): Longitud de uno de los lados del triángulo
      s2 (float): Longitud de uno de los lados del triángulo
      s3 (float): Longitud de uno de los lados del triángulo
    Retorno:
      float: El área del triángulo redondeada con una cifra decimal.
    """
    s=(s1+s2+s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return round(area,1)