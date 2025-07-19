import math as mt
# -*- coding: utf-8 -*-
"""
Descripción del problema
Sofía esta empezando a ver las figuras geometricas en sus clases de geometria.
En la clase de hoy le enseñaron como hallar el área de una circunferencia y por lo tanto le mandaron una tarea con ejercicios de área, Sofía quiere comprobar si su solución de la tarea fue correcta.

Realice una función la cual con un parametro de entrada el cual es el radio de la circunferencia en cm, retorne su área en cm², redondeado a 2 decimales. Sabiendo que la fórmula del área de una circunferencia es:
"""

def area_circunferencia(radio: float)->float:
    """ área circunferencia
    Indica el área de una ircunferencia.
    Parámetros:
      radio (float):Radio de la circunferencia a la cual hay que hallar su área.
    Retorno:
      float: Área de la circunferencia.
    """
    area=mt.pi*(radio**2)
    return area