# -*- coding: utf-8 -*-
"""
Descripción del problema

En multiples salones se esta viendo en la materia de geometria y con esto el área de figuras bidimensionales.
Jorge es un estudiante el cual acaba de ver como hallar el area de un cuadrado y quiere encontrar un programa que le permita hacer rapidamente los ejercicios propuestos por su profesor.

Realice una función la cual recibiendo a forma de float el tamaño de uno de los lados del cuadrado en cm retorne su área.
"""

def area_cuadrado(lado: float)->float:
    """ área cuadrado
    Indica cuanto es el área de un cuadrado.
    Parámetros:
      lado (float): lado del cuadrado al cual debemos sacarle el área
    Retorno:
      float: Valor del área del cuadrado
    """
    area=lado**2
    return area