# -*- coding: utf-8 -*-
import math as mt
import random as rn

def funciones (angulo: int)->str:
  radianes=mt.radians(angulo)
  seno=mt.sin(radianes)
  coseno=mt.cos(radianes)
  tangente=mt.tan(radianes)
  respuesta='Sus funciones trigonometricas son: Seno:',seno,'Coseno:',coseno,'Tangente:',tangente
  return respuesta


def multiplo_5_randrange():
  numero=rn.randrange(0,100,5)
  return numero

def multiplo_5_while():
  contador=0
  while contador != 1:
    numero=rn.randint(0,100)
    if (numero%5) == 0:
      contador=1
  return numero

def maximo_comun_divisor(numero_1: int, numero_2: int)->int:
  mcd=mt.gcd(numero_1,numero_2)
  return mcd

"""
Descripción del problema:
Usando la función random.normalvariate genere 15 números aleatorios con media 3.8 y desviación estándar de 1. Calcule ahora usted la media de los números generados y la desviación estándar. ¿Qué tan lejos están de la media y la desviación planeada? Ejecute su programa y observe cómo cambian los resultados con cada ejecución.
"""

def media(lista: list)->int:
  cantidad=len(lista)
  sumatoria=0
  for i in lista:
    sumatoria+=i
  media=sumatoria/cantidad
  return media

def desviacion_estandar (lista: list)->int:
  cantidad=len(lista)
  sumatoria_resta=0
  for i in lista:
    resta=i-media
    sumatoria_resta+=resta
  desviacion=mt.sqrt((sumatoria_resta**2)/(cantidad))
  return round(desviacion)
  
def comparacion():
  lista=[]
  cont=0
  while cont != 15:
    numero=rn.normalvariate(3.8,1)
    lista.append(numero)
  media_lista=media(lista)
  desviacion_lista=desviacion_estandar(lista)

  return (media_lista,desviacion_lista)