# -*- coding: utf-8 -*-
"""
Descripción del problema:
Realiza un programa el cual sea util para hallar el volumen de un cilindro,
recibiendo su radio y su altura, y lo retorne redondeado a 2 decimales
"""
def volumen_cilindro(radio: float, altura: float)->float:
  """
  volumen cilindro
  Calcula el volumen de un cilindro
  Parámetros:
    radio (float): radio de la base del cilindro.
    altura (float): altura del cilindro.
  Retorno:
    float: Valor de su volumen redondeado a 2 decimales
  """
  area_base = 3.14159 * (radio**2)
  return round(area_base * altura,2)

"""
Descripción del problema:
Realiza un programa el cual sea util para hallar la velocidad con la que un cuerpo
tocará el pisocuando cae desde una altura determinada.
"""
def velocidad_final_MCL(distancia: float)->float:
  """
  velocidad_final_MCL
  Velocidad final de un movimiento de caida libre
  Parámetros:
    distancia (float): Distancia del suelo a la cual se encuentra el cuerpo.
  Retorno:
    float: Velocidad final del cuerpo que cae.
  """
  velocidad_final = (2*9.8*distancia)**(1/2)
  return velocidad_final

"""
Descripción del problema:
Realiza un programa el cual retorne la nota final de una materia recibiendo:
el nombre de la materia y 2 notas en el saber conocer, 2 notas en el saber hacer
y solo 1 en el saber ser.
"""
def nota_final(nombre: str, sc_1: float, sc_2: float, sh_1: float, sh_2: float, ss_1: float)->tuple:
  """
  nota final
  Función que retorna el valor final de tu nota en una materia
  Parámetros:
    nombre (str): Nombre de la materia a la cual le quieres sacar la nota:
    sc_1 (float): La primera nota que tienes en el saber conocer (Recibe valores entre 0.0 y 10.0).
    sc_2 (float): La segunda nota que tienes en el saber conocer (Recibe valores entre 0.0 y 10.0).
    sh_1 (float): La primera nota que tienes en el saber hacer (Recibe valores entre 0.0 y 10.0).
    sh_2 (float): La segunda nota que tienes en el saber hacer (Recibe valores entre 0.0 y 10.0).
    ss_1 (float): La primera nota que tienes en el saber ser (Recibe valores entre 0.0 y 10.0).
  Retorno: 
    tuple: Valor final en el cual terminará tu nota de la materia, junto con el nombre de esta.
  """
  promedio_sc=(sc_1+sc_2)/2
  promedio_sh=(sh_1+sh_2)/2
  nota_final=(promedio_sc*0.4)+(promedio_sh*0.4)+(ss_1*0.2)
  return nombre,round(nota_final,1)

print(nota_final('Física',6.5,7.2,10.0,5.6,8.5))