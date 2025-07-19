# -*- coding: utf-8 -*-
"""
Descripción del problema
Haga una función que reciba la velocidad del Internet de un usuario 
(en Mbps, es decir, Megabits por segundo), y el tamaño de un archivo a descargar (en GB, es decir, Gigabytes), y retorne el tiempo en minutos estimado (redondee al entero más cercano) para realizar la descarga de dicho archivo sobre esa red.

Para esto, tenga en cuenta que el tiempo lo puede calcular como:

tiempo descarga = tamaño archivo/velocidad descarga

El tamaño y velocidad deben estar en unidades homogéneas (por ejemplo, MB y MB/s, o GB y GB/s, de tal forma que se puedan operar).

Nota: Recuerde que un MB (Megabyte) equivale a 8 Mb (Megabits), y que un GB 
equivale a 1000 MB.
"""

def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int)->int:
    """ Tiempo de descarga
    Indica en cuanto tiempo una descarga podrá realizarse.
    Parámetros:
      velocidad (int): Velocidad de descarga de la red, en Mbps
      tamanio_archivo (int): Tamaño del archivo a descargar, en GB
    Retorno:
      int: Tiempo estimado en minutos que toma la descarga del archivo
    """
    tiempo=((tamanio_archivo*1000)*8)/velocidad
    return round(tiempo)