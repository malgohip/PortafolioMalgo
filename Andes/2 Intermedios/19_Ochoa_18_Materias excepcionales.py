# -*- coding: utf-8 -*-
"""
Descripción del problema
Un estudiante desea saber cuáles son las materias de las cuales puede estar orgulloso. Para esto ha creado un diccionario notas con las llaves de las materias que ha visto en este año: "Matematica", "Ingles", "Sociales", "Ciencias", "Deportes".

Cree una función que cuente cuales de estas materias están estrictamente por encima de 4, y retorne el entero que represente cuantas materias cumplen esta característica.
"""

def buenas_notas(notas: dict, materia: str):
  retorno=False
  if materia in notas:
    if notas[materia] > 4: 
      retorno = True
  return retorno

def conteo_buenas_notas(notas: dict)->int:
  """
  Materias excepcionales
  Indica cuales son las materias en las que el estudiante obtuvo un promedio excepcional.
  Parámetros:
    notas (dict): Diccionario con las notas del estudiante.
  Retorno:
    int: Número de materias excepcionales.
  """
  materias=0
  if buenas_notas(notas,"matematica"):
    materias+=1
  if buenas_notas(notas,"ingles"):
    materias+=1
  if buenas_notas(notas,"sociales"):
    materias+=1
  if buenas_notas(notas,"ciencias"):
    materias+=1
  if buenas_notas(notas,"deportes"):
    materias+=1
  return materias

notas={"matematica": 4.5, "ingles": 3.5, "sociales": 3.0, "ciencias": 4.0, "sistemas": 5.0}
print(conteo_buenas_notas(notas))