# -*- coding: utf-8 -*-
"""
Descripción del problema
Un año "bisiesto" es aquel que tiene 366 días en vez de 365, lo cual se logra agregando un día al mes de febrero. Los años bisiestos se usan porque la rotación de la Tierra alrededor del Sol no dura exactamente 365 días: agregando un día adicional de vez en cuando, el desfase se corrige poco a poco.

Para saber si un año es bisiesto, su número debe ser divisible por 4, a menos que sea divisible por 100 y no por 400. Por ejemplo, los años 2000 y 2020 fueron bisiestos, pero no lo fue el año 1900.

Cree una función que reciba un año (entero positivo) y retorne un valor de verdad indicando si el año es o no bisiesto.
"""


def bisiesto(anio: int)->bool:
    """
    bisiesto 
    Indica si un año dado es bisiesto o no.
    Parámetros:
      anio (int):Año para analizar si es bisiesto o no
    Retorno:
      bool: Valor de verdad (bool) que indica si el año es bisiesto (True) o no lo es (False).
    """
    prueba=0
    if (anio%100)==0:
      if (anio%400)==0:
        prueba = 1
    else:
      if (anio%4)==0:
        prueba = 1
      else:
        prueba=0
    valor=(prueba>0)
    return valor