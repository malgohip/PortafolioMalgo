# -*- coding: utf-8 -*-
"""
Descrpción del problema
La cantidad de energía requerida para aumentar la temperatura de un gramo de un material en un grado Celsius es la capacidad calorifica específica del material, C.

La cantidad total de energía, en Joules, requerida para incrementar la temperatura de m gramos de un material en ΔT (recuerde que ΔT es Tf-To) grados Celsius se puede calcular usando la fórmula: q = mCAT.

Cree una función que, dada una masa de agua en gramos, calcule el costo de hervir agua (llevarla a 100°C) que se encuentra a 20°C para una taza de café.

La capacidad calorifica específica del agua es de 4.186.J/g C. Como la electricidad se cobra normalmente usando como unidad kilowatt-hora en vez de Joules, recuerde que un watt-hora equivale a 3600 Joules, y un kilowatt equivale a 1000 watt. En este caso, asuma que la electricidad cuesta 0.089 dólares por kilowatt-hora.

El valor de retorno debe estar redondeado a cuatro decimales.
"""

def costo_hervir_agua(masa_agua: float)->float:
    """ 
    Costo de hervir agua
    Indica cuanto sería el precio en dolares de hervir una cierta cantidad de agua.
    Parámetros:
      masa_agua (float): Masa de agua a hervir
    Retorno:
      float: Valor en dólares de hervir la masa de agua dada como parámetro redondeado con 4 decimales
    """
    q=masa_agua*4.186*(100-20)
    p=q/(3600*1000)
    precio=p*0.089
    return round(precio,4)