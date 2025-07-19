#Author: Sebastian Ochoa. Date: 02/10/2024
# -*- coding: utf-8 -*-

"""Si ya aprendiste a cómo escribir un programa con un bucle sencillo en la tarea Sum in Loop, este nuevo ejercicio será sólo una ligera modificación.

Ahora se nos dan varios pares de valores y queremos calcular la suma de cada par."""

lst=[[844649, 46030],
[293164, 921831],
[177501, 777900],
[557018, 387799],
[865575, 52429],
[225012, 753216],
[404452, 402474],
[795474, 666051],
[108746, 543360],
[315340, 808575],
[56458 ,62949],
[570989, 305549],
[83305 ,798461],
[325790, 730491],
[427864, 836918],]
sums=""
for x in lst:
    sum=0
    for i in x:
        sum+=i
    sums+=str(sum)+" "
print(sums)