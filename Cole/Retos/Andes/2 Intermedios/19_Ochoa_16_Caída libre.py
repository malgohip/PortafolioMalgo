import math
# -*- coding: utf-8 -*-
"""
Descripción problema
Cree una función que determine la velocidad, en m/s, a la que viaja un objeto cuando toca el suelo, en caída libre. La función recibe la altura a la que se encontraba el objeto al soltarse, en metros.

Como es caída libre, la velocidad inicial del objeto es de Om/s. Asuma que la aceleración debido a la gravedad es de 9.8m/s². Puede usar la fórmula vf=√vi²+2ad para calcular la velocidad final, donde va es la velocidad inicial, a es la aceleración y d la distancia al suelo.

El valor retornado debe estar redondeado a dos decimales.

Ayuda: Importar el módulo math puede serle de utilidad para la raíz cuadrada.
"""

def velocidad_en_caida_libre(altura: float)->float:
    """ Caída libre
    Indica cuanto sería la velocidad de caida de un cuerpo.
    Parámetros:
      altura (float): Altura desde la cual cae el objeto
    Retorno:
      float: Velocidad del objeto al tocar el suelo tras la caída libre, la velocidad debe estar redondeada a dos cifras decimales.
    """
    velocidad=math.sqrt(2*9.8*altura)
    return round(velocidad,2)