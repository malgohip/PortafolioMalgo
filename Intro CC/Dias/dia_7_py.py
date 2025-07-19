#Author: Sebastian Ochoa. Date: 02/27/2024
# -*- coding: utf-8 -*-

#Integer Factorization

def factorde(numero):
  cosa=False
  for x in range (2, numero+1):
    if numero%x == 0:
      return x
  if not cosa:
    return 1

def factores_primos ()->str:
  cant=int(input("Dime que cantidad de valores vas a revisar sus factores primos: "))
  cont=0
  todos_factores=""
  while cont < cant:
    numero=int(input("Dime el número: "))
    factores=""
    factor=0
    while factor != 1:
      factor=factorde(numero)
      numero//=int(factor)
      if factor != 1:
        factores+=str(factor)+"*"
    cont+=1
    factores=factores[:-1]
    todos_factores+=factores+" "
  return todos_factores

print(factores_primos())

#La librería random permite usar funciones que generan números randomicos

import random

"""
print ("\t \t ESTE PROGRAMA SIMULA EL LANZAMIENTO DE UN TRIO DE DADOS \n")
respuesta = input ("Desea lanzar los dados ? s(si), n(no) ")
x=(1,2,3,4,5,6)
while respuesta in ['s','S']:
    Dado1 = random.choice(x)  # random.choice escoge un número al azar de la tupla x
    Dado2 = random.choice(x)
    Dado3 = random.choice(x)
    print (f"Lanzamiento = ( {Dado1},  {Dado2}, {Dado3})")
    respuesta = input ("\n Desea continuar jugando ? s(si), n(no)")
print("\n ***     EL JUEGO TERMINÓ     *** \n ")
"""

#Determine si un entero positivo dado es un número primo.

"""
num=int(input("Dime el número en cuestion: "))
for n in range(2, num//2 +1):
  primo=False
  if num % n == 0:
    print(f"no es primo {n} es divisor")
  else:
    primo=True
if primo:
  print("Es primo")
"""

#Calcule la suma de los números divisibles por 2 o por 3, menores o iguales que un valor  n  dado.

"""
num=int(input("Dime el numero en cuestion: "))
lst=[]
total=0
for x in range (0,num+1):
  if x % 2 == 0 or x % 3 == 0:
    lst.append(x)
    total+=x
print(total)
"""

#Diseñar una función que permita calcular la serie de Fibonaci, hasta un valor  n  dado.

"""
# Definición de la función
def Fibo(n):
   a=1
   b=1
   print(a,", ", b, end ="") # el comando "end =" EVITA el salto de línea
   for i in range(2,n):
     F = a + b
     a = b
     b = F
     print(", ", F,end="" )
# llamado de la función
Fibo(10)
"""

"""
Descripción del problema:
Usando la función random.normalvariate genere 15 números aleatorios con media 3.8 y desviación estándar de 1. Calcule ahora usted la media de los números generados y la desviación estándar. ¿Qué tan lejos están de la media y la desviación planeada? Ejecute su programa y observe cómo cambian los resultados con cada ejecución.
"""

#Calcular la desviacion estandar

"""
def desviacion_estandar (lst: list)->int:
  cantidad=len(lst)
  promedio=0
  sumatoria=0
  for i in lst:
    sumatoria+=i
  promedio=sumatoria/cantidad
  print(promedio)
  sumatoria_resta=0
  for i in lst:
    resta=i-promedio
    sumatoria_resta+=(resta**2)
  desviacion=(sumatoria_resta/cantidad)**(1/2)
  return desviacion

lst=[]
cant=int(input("Dime cuantos datos iran en la lista: "))
for x in range(cant):
  n=int(input("El valor es: "))
  lst.append(n)
  
print(desviacion_estandar(lst))
"""