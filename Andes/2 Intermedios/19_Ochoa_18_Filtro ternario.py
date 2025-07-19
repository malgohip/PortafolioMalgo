# -*- coding: utf-8 -*-
"""
Descripción del problema
El operario de un parqueadero de la ciudad de los números enteros es un señor muy ordenado. Cada día, parquean  carros n sin falta entre sus tres lotes de parqueadero. Cada lote tiene una capacidad de [n/3]  automóviles.

Él ha decidido asignarle un número a cada uno de los automóviles, de tal forma que, con solamente ver el número de uno de los carros, pueda dirigir al conductor al lote que le corresponde. Ayude al operario a escribir un programa que, dado un total de carros a parquear y el número de un automóvil, determine si a ese carro le corresponde parquear en el primer, segundo o tercer lote.

Note que:

Los carros numerados entre 1 y [n/3]  se ubican en el primer lote.
Los carros entre  [n/3]  + 1  y  [2n/3] en el lote 2.
Los carros entre  [2n/3] + 1  y n van en el tercer lote.
Se garantiza que  n y el número del carro  nc son enteros positivos y que  1 <= nc <= n . Además, se garantiza que  n es un múltiplo de 3.
"""
def filtro_ternario(cantidad_autos: int, numero_auto: int)->int:
  """
  filtro ternario
  Indica el lote en el cual un automovil debe quedar. 
  Parámetros:
    cantidad_autos (int): La cantidad de carros que recibe el operario en su parqueadero
    numero_auto (int): El número único del carro a ubicar en alguno de los tres lotes de parqueo. Se garantiza que es un número menor o igual que n, y mayor o igual que 1.
  Retorno:
    int: El lote de parqueadero donde el carro con el número que llega por parámetro deberá parquear. Debe ser un valor entre 1 y 3.
"""
  if 1<numero_auto<(cantidad_autos/3):
    return 1
  elif ((cantidad_autos/3)+1)<numero_auto<((2*cantidad_autos)/3):
    return 2
  elif (((2*cantidad_autos)/3)+1)<numero_auto<cantidad_autos:
    return 3