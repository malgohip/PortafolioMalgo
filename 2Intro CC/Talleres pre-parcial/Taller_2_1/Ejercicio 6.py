#Author: Sebastian Ochoa. Date: 07/30/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 6.

Cree un archivo Json que permite que permita guardar la información de una colección de estudiantes: 
Cada item debe tener la información correspodiente a nombre, apellidos, edad, carrera y cursos inscritos.
"""

import json
data = {} 
data['estudiantes'] = []
data['estudiantes'].append({
    'Nombre': 'Juan Sebastián',
    'Apellidos': 'Ochoa Cicua',
    'Edad': 17,
    'Carrera': 'Ciencias de la Computación',
    'Cursos inscritos': ('Fundamentos de Matemáticas','Introducción a las ciencias de la computación y la programación','Cálculo diferencial en una variable')})
data['estudiantes'].append({
    'Nombre': 'David Santiago',
    'Apellidos': 'Muñoz Triviño',
    'Edad': 25,
    'Carrera': 'Ciencia Política',
    'Cursos inscritos': ('Historia Política Moderna','Introducción a la Ciencia Política','Cátedra Eduardo Umaña Luna','Teoría e Historia Constitucional','Historia Política y Socioeconómica del siglo XIX')})
data['estudiantes'].append({
    'Nombre': 'Santiago',
    'Apellidos': 'Benjumea',
    'Edad': 20,
    'Carrera': 'Física',
    'Cursos inscritos': ('Taller de matemáticas y ciencias','Algebra líneal','Cálculo diferencial de una variable','Fundamentos de física teórica','Fundamentos de física experimental')})

with open('Talleres pre-parcial\Taller_2_1\TXTs y JSON\data.json', 'w') as file:
    json.dump(data, file, indent=3)
print(data)