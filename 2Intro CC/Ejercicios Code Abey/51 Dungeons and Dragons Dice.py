#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
In the complex dice-based games players can use several dice and with number of sides other than 6. For example, the damage given by some powerful sword could be calculated as the sum of 3 dice with 8 sides each (i.e. having numbers from 1 to 8) - this means the weakest possible damage is 3 and strongest is 24, however most probable values would be 13 and 14.

The notation used in the descriptions of such games looks like 3d8 - i.e. 3 dice with 8 sides, or 2d6 for more common variant of 2 dice with 6 sides each. Tossing of 5 coins each of which has only 2 sides would be written as 5d2.

In this task you will be given results of casting some dice set many times. Your task would be to determine how many dice are in the set and how many sides dice have. Supposedly you'll need some program to calculate statistics on these results to classify them.

Due to probabilistic nature of the problem you may fail at first attempt, however try a few times - and if your algorithm is correct, your answer will be accepted.

For this problem dice could have 2, 4, 6, 8, 10 or 12 sides. The number of dice could be from 1 to 5.

Input data contain 303 values in 3 lines.
Each line contains 100 non-zero results of casting (sums of dice points), terminated with spare 0 which should not be counted (it only marks the end of the line).
"""
"""
a = open('Ejercicios Code Abey\TXTs\e51 Dungeons and Dragons Dice.txt','r')
P= a.readlines()

resultados=[]
for x in range(len(P)):
    f=P[x].strip().split()
    F=[]
    for x in range(len(f)-1):
        X=int(f[x])
        F.append(X)
    resultados.append(F)

print(resultados)
"""
resultados=[[21, 12, 24, 19, 15, 17, 20, 18, 20, 20, 17, 19, 19, 22, 19, 24, 20, 17, 20, 18, 13, 14, 13, 21, 20, 11, 19, 10, 16, 21, 11, 17, 23, 23, 11, 16, 23, 21, 15, 15, 22, 10, 20, 19, 20, 12, 16, 19, 17, 23, 10, 15, 20, 10, 25, 14, 22, 26, 25, 23, 22, 14, 12, 26, 20, 21, 25, 30, 25, 13, 19, 15, 21, 16, 19, 23, 15, 15, 21, 17, 19, 13, 14, 20, 24, 8, 23, 19, 17, 26, 14, 16, 14, 16, 21, 23, 19, 11, 17, 21], [31, 25, 34, 35, 35, 36, 51, 24, 18, 30, 28, 21, 38, 37, 39, 41, 41, 39, 37, 42, 40, 33, 41, 29, 25, 39, 30, 23, 33, 49, 30, 33, 40, 43, 26, 37, 26, 28, 39, 37, 37, 32, 28, 51, 45, 21, 34, 39, 40, 23, 27, 32, 29, 32, 37, 41, 41, 18, 32, 35, 35, 16, 39, 45, 42, 24, 21, 33, 37, 29, 17, 34, 45, 37, 36, 31, 40, 33, 24, 34, 37, 19, 36, 26, 25, 26, 38, 26, 27, 37, 29, 45, 35, 33, 35, 21, 34, 45, 33, 46], [16, 15, 17, 19, 19, 22, 26, 26, 19, 18, 17, 10, 20, 27, 14, 29, 23, 25, 29, 16, 13, 23, 20, 20, 13, 29, 27, 20, 27, 28, 21, 21, 13, 32, 21, 31, 23, 18, 16, 24, 21, 28, 30, 17, 29, 25, 27, 24, 23, 30, 27, 11, 31, 16, 26, 26, 20, 19, 28, 22, 28, 21, 24, 19, 6, 20, 28, 30, 30, 20, 6, 21, 26, 32, 24, 16, 17, 17, 21, 16, 22, 10, 25, 24, 22, 26, 19, 32, 20, 21, 26, 28, 24, 29, 28, 14, 13, 22, 12, 10]]

respuesta=''
for x in resultados:
    lados_posibles = [2, 4, 6, 8, 10, 12]
    num_dados_posibles = range(1, 6)
    x = sorted(x[:-1])
    s_min = x[0]
    s_max = x[-1]
    s_media = sum(x) / len(x)
    mejor_config = None
    mejor_diferencia_media = float('inf')
        
        # Probar todas las combinaciones posibles de dados y lados
    for y in lados_posibles:
        for x in num_dados_posibles:
            s_min_posible = x * 1
            s_max_posible = x * y
            s_media_posible = (s_min_posible + s_max_posible) / 2
                
                # Verificar si la configuración es posible
            if s_min_posible <= s_min and s_max_posible >= s_max:
                diferencia_media = abs(s_media_posible - s_media)
                if diferencia_media < mejor_diferencia_media:
                    mejor_diferencia_media = diferencia_media
                    mejor_config = f"{x}d{y}"
    respuesta+=mejor_config+' '
print(respuesta)