# -*- coding: utf-8 -*-
"""
Descripción del problema
En una cierta ciudad, la tarifa de un taxi consiste en una tarifa base de 400pesos,más 82 pesos por cada 100 metros recorridos. Escriba una función que reciba como parámetro la distancia recorrida en kilómetros y retorne la tarifa total del viaje.

No olvide redondear el valor de retorno al entero más cercano.
"""

def calcular_tarifa_taxi(kms_recorridos: float)->int:
  """ Tarifa de un taxi
  Indica cuanto quedaria la tarifa de un taxi.
  Parámetros:
    kms_recorridos (float): Kilómetros recorridos en el viaje
  Retorno:
    int: Tarifa a cobrar por el recorrido en taxi, la cual debe estar redondeada al entero mas cercano.
  """
  t=((kms_recorridos*10)*82)+4000
  tr=round(t)
  return tr