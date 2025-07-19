# -*- coding: utf-8 -*-
"""
Descripcion del problema
Haga un programa que pida al usuario una cantidad de pesos, una tasa de interés y un número de años. Muestre por pantalla en cuánto se habrá convertido el capital inicial (Redondear a dos decimales) transcurridos esos años si cada año se aplica la tasa de interés introducida. Recuerde que un capital de C pesos a un interés del x por ciento durante n años se convierten en 
 
C*(1+(x/100))^n   pesos. Pruebe su programa sabiendo que una cantidad de 10000 pesos al 4.5% de interés anual se convierte en 24117.14 pesos al cabo de 20 años.
"""


def calculo_tasa_de_interes(pesos :int, tasa: float, años: int)->float:
    """Tasa de interes
    Indica cuanto sería el nuevo valor a tomar en base a la tasa de interes y el tiempo.
    Parámetros:
      pesos (int): Capital inicial
      tasa (float): Tasa de interés del banco
      años (int): Número de años
    Retorno:
      float: Cantidad de pesos depues de los años (redondeado a dos decimales).
    """
    capital_final=pesos*((1+(tasa/100))**años)
    return round(capital_final,2)

print(calculo_tasa_de_interes(1000000,20,3))