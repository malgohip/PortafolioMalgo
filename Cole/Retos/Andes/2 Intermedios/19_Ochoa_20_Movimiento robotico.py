# -*- coding: utf-8 -*-
"""
Descripción del problema:
Usted quiere anticipar el movimiento de su nuevo robot, que recibió como regalo de cumpleaños. El robot tiene una brújula interna que le permite saber hacia que punto cardinal está mirando actualmente (Norte, Sur. Este, u Oeste). Además, el robot tiene u control remoto en donde puede voltearse a la izquierda (90°), a la derecha(90°), o dar media vuelta(180°). Dadas estas condiciones, escriba una función que, dadas una orientación inicial y un comando de control remoto de los anteriormente mencionados, pueda predecir la orientación final de su robot.
"""
def movimiento_robot(orientacion_actual: str, giro: str)->str:
  """
  Movimiento robot
  Indica la nueva posicion de un robot al girar 90 grados.
  Parámetros:
    orintación actual (str): La orientación actual del robot (debe ser un valor entre los siguientes{"W","N","S","E"}).
    giro (str): La acción a ejecutar a partir de la orientación inicial del robot (debe ser un valor entre los siguientes:{"L","H","R","."}).
  Retorno:
    str: La orientación final del robot (debe ser un valor entre los siguientes{"W","N","S","E"}).
  """
  respuesta=""
  if orientacion_actual == "N":
    if giro == "L":
      respuesta="W"
    if giro == "H":
      respuesta == "S"
    if giro == "R":
      respuesta == "E"
  if orientacion_actual == "W":
    if giro == "L":
      respuesta="S"
    if giro == "H":
      respuesta == "E"
    if giro == "R":
      respuesta == "N"
  if orientacion_actual == "S":
    if giro == "L":
      respuesta="E"
    if giro == "H":
      respuesta == "N"
    if giro == "R":
      respuesta == "W"
  if orientacion_actual == "E":
    if giro == "L":
      respuesta="N"
    if giro == "H":
      respuesta == "W"
    if giro == "R":
      respuesta == "S"
  if giro == ".":
    respuesta = orientacion_actual
  return respuesta
