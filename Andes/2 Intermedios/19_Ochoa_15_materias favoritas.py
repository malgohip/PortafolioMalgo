# -*- coding: utf-8 -*-
"""
Descripción del problema
Pedro es un estudiante inteligente pero desinteresado por algunas de sus materias. A Pedro le gustan las clases en las que aprende programación, matemática, filosofía, literatura. Por lo anterior, cualquier materia que lleve en su título alguna de estas palabras, será de su agrado.

Pedro está planeando su horario, pero ha puesto a su asistente digital a que le dé posibles conjuntos de tres materias para meter en su semestre. Él quiere saber, dados los títulos de las tres materias, cuántas de estas son de su agrado. Se sabe que los nombres de las materias irán sin acentos y en minúsculas cuando sean pasados por parámetro a la función.
"""
def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str)->int:
  """
    conteo de materias
    Indica cuantas de las materias dadas son las favoritas de el estudiante.
    Parámetros:
      nombre_materia_1 (str): El nombre de la primera de las tres materias
      nombre_materia_2 (str): El nombre de la segunda materia
      nombre_materia_3 (str): El nombre de la tercera materia
    Retorno:
      int: Número de materias favoritas
  """
  num_fav=0
  materias=['filosofia', 'programacion', 'literatura', 'matematica' ]
  if materias[0]==nombre_materia_1 or materias[0]==nombre_materia_2 or materias[0]==nombre_materia_3:
    num_fav+=1
  if materias[1]==nombre_materia_1 or materias[1]==nombre_materia_2 or materias[1]==nombre_materia_3:
    num_fav+=1
  if materias[2]==nombre_materia_1 or materias[2]==nombre_materia_2 or materias[2]==nombre_materia_3:
    num_fav+=1
  if materias[3]==nombre_materia_1 or materias[3]==nombre_materia_2 or materias[3]==nombre_materia_3:
    num_fav+=1
  return num_fav