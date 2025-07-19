#Author: Sebastian Ochoa. Date: 02/29/2024
# -*- coding: utf-8 -*-

#Serie de Akermann 

'''def Ackermann(m,n):
   if m == 0:
     return n+1
   elif m > 0 and n == 0:
     return Ackermann(m-1,1)
   else:
     return Ackermann(m-1,Ackermann(m,n-1))

print(Ackermann(4,4))
'''
# Observe que para valores de m,n>3 el programa se bloquea debido a la sobre
# saturacion de la memoria generada por las autollamadas de la función.

#Definir la familia de cuadraticas y calcular:
"""
def cuadratica (a,b,c):
  return lambda x: a*x**2+b*x+c

p1=cuadratica(2,1,-3)
p2=cuadratica(-3,2,-5)
print(p1(1))
print(p2(1))
"""

#divisibilidad de 2 y 5
"""
L = [1,2,23,24,16,32,1101]
L23 = list(filter(lambda x : x%2 == 0 and x%5 == 0,L))
print(L23)
"""
#Evaluar la función  f(x)=2x2−x+1  para los valores  x=0.0,0.2,0.4,0.6,0.8,1.0.

#L = [0.0,0.2,0.4,0.6,0.8,1.0]
"""
def f(x):
  return 2*x**2-x+1
Resultados = list(map(f,L))
print(Resultados)
"""
"""
resultados=list(map(lambda x: 2*x**x-x+1,L))
print(resultados)
"""