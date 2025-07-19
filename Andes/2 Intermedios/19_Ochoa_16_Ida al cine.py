# -*- coding: utf-8 -*-
"""
Descripción del problema
Tres mejores amigos están en el cine. En CupiCinema, han patentado un sistema de servicio de gaseosas por botones, en el que se puede servir una cantidad predeterminada de gaseosa según el botón presionado. Cada uno de ellos tiene un vaso con una capacidad dada, y ya han llenado un cierto nivel del vaso. Como son mejores amigos, ellos quieren oprimir el mismo siguiente botón para servirse una cantidad fija de gaseosa en sus respectivos vasos. No obstante, no quieren que se les riegue la gaseosa, porque consideran que sería un desperdicio.

Dadas la capacidad máxima de cada uno de los vasos, así como su capacidad actual, y el usuario al que pertenecen, escriba una función que determine el nombre de la persona a la que se le regaría algo de gaseosa si se sirve la capacidad fija dada. Si a ninguno se le riega la gaseosa, retorne None. Si se le riega la gaseosa a más de uno, retorne el primero en orden de parámetros pasados a la función (es decir, primero llena el amigo_1, luego el 2, luego el 3).
"""
def desperdicio_de_gaseosa(amigo_1:dict, amigo_2:dict, amigo_3:dict, capacidad_boton: float)->str:
    """
    desperdicio de gaseosa
    Insica cual es el amigo que se le regará la gaseosa en base a cuanto se sirve.
    Parámetros:
      amigo_1 (dict): Un diccionario con las siguientes llaves: 'nombre', el nombre del amigo, (str) 'capacidad_vaso', la capacidad máxima de su vaso, (float) 'capacidad_actual', la capacidad que ha sido llenada de su vaso hasta el momento (float)
      amigo_2 (dict): Un diccionario con las siguientes llaves: 'nombre', el nombre del amigo, (str) 'capacidad_vaso', la capacidad máxima de su vaso, (float) 'capacidad_actual', la capacidad que ha sido llenada de su vaso hasta el momento (float)
      amigo_3 (dict): Un diccionario con las siguientes llaves: 'nombre', el nombre del amigo, (str) 'capacidad_vaso', la capacidad máxima de su vaso, (float) 'capacidad_actual', la capacidad que ha sido llenada de su vaso hasta el momento (float)
      capacidad_boton (float): La cantidad de gaseosa que se servirá si los amigos deciden oprimir el botón correspondiente.
    Retorno:
      str: El nombre del amigo a quien se le riega primero la gaseosa, suponiendo un orden ascendente en cuanto a que amigo llena primero su vaso. (Es decir, primero llena el amigo_1, luego el 2, luego el 3) Si a ningun amigo se le riega la gaseosa, retorne None. Si a más de un amigo se le riega la gaseosa, retorna el primero.
    """
    respuesta=''
    if amigo_1['capacidad_actual']+capacidad_boton > amigo_1['capacidad_vaso'] or amigo_2['capacidad_actual']+capacidad_boton > amigo_2['capacidad_vaso'] or amigo_3['capacidad_actual']+capacidad_boton > amigo_3['capacidad_vaso']:
        respuesta='Los amigos que llenan son:\n-'
        if amigo_1['capacidad_actual']+capacidad_boton > amigo_1['capacidad_vaso']:
            respuesta += amigo_1['nombre']+ '\n-'
        if amigo_2['capacidad_actual']+capacidad_boton > amigo_2['capacidad_vaso']:
            respuesta += amigo_2['nombre']+ '\n-'
        if amigo_3['capacidad_actual']+capacidad_boton > amigo_3['capacidad_vaso']:
            respuesta += amigo_3['nombre']+ '\n-'
    else:
        respuesta=None
    return respuesta

print(desperdicio_de_gaseosa({'nombre': 'Jhon','capacidad_vaso': 253.0, 'capacidad_actual': 25.3},{'nombre': 'Valentia','capacidad_vaso': 300.0, 'capacidad_actual': 50.0},{'nombre': 'Solón','capacidad_vaso': 500.0, 'capacidad_actual': 200.0},300.0))