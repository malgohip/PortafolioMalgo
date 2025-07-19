# -*- coding: utf-8 -*-
import math
"""
Descripción del problema
Un polígono es regular si todos sus lados son de la misma longitud, y los ángulos 
entre todos los lados adyacentes son iguales. El área de un polígono regular puede 
ser calculada usando la siguiente fórmula, donde  es la longitud de un lado y  
el número de lados:


Cree una función que reciba como parámetros  y , y retorne el área del polígono regular.

El área debe estar redondeada a dos decimales.
"""

def area_poligono_regular(num_lados: int, longitud: float)->float:
    """ Área de un polígono regular
    Indica cuanto sería el area de un poligono regular.
    Parámetros:
      num_lados (int): Número de lados del polígono
      longitud (float): Longitud de uno de los lados del polígono
    Retorno:
      float: Área del polígono regular redondeada a dos cifras decimales.
    """
    area=(num_lados*(longitud**2))/(4*(math.tan(math.pi/num_lados)))
    return round(area,2)