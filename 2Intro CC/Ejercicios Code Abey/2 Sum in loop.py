#Author: Sebastian Ochoa. Date: 02/10/2024
# -*- coding: utf-8 -*-

"""Ahora nuestro objetivo es aprender los bucles - ej: acciones repetidas. Vamos a encontrar la suma de varios números (más de dos). Será muy útil hacer esto en un bucle. Tal como se ve en la figura de arriba - puedes crear la variable sum y sumarle cada valor de la lista. Quizá un bucle "for" o bucle "for" funcione bastante bien ya que la cantidad de números se conoce de antemano."""

lst=[984, 15, 100, 955, 1042, 177, 795, 474, 666, 995, 534, 35, 97, 993, 1041, 79, 494, 98, 365, 738, 93, 221, 750, 1146, 177, 68, 181, 831, 1059, 554, 135, 1259, 908, 128, 531]
sum=0
for x in lst:
    sum+=x
print(sum)