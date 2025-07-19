# -*- coding: utf-8 -*-
"""
Descripción problema
Cree una función que pueda calcular el índice de masa corporal (BMI) de una persona.

La fórmula para calcular el BMI es la siguiente:

Donde el peso está en kilogramos y la altura en metros. Tenga en cuenta que el peso y la altura que reciba su función va a estar dado en libras y pulgadas respectivamente, ya que su función será usada en los Estados Unidos.

Recuerde que:

1 libra corresponde a 0.45 kg
1 pulgada corresponde a 0.025 metros

El valor de retorno debe estar redondeado a dos decimales.
"""

def calcular_BMI(peso_lb: float, altura_inch: float)->float:
    """ 
    calcular BMI
    Indica cuanto es el valor del BMI de una persona.
    Parámetros:
      peso_lb (float): Peso en libras de la persona
      altura_inch (float): Altura en pulgadas de la persona
    Retorno:
      float: Índice de masa corporal de la persona, el valor de retorno debe estar redondeado a dos decimales.
    """
    peso=peso_lb*0.45
    altura=altura_inch*0.025
    BMI=(peso/(altura**2))
    return round(BMI,2)