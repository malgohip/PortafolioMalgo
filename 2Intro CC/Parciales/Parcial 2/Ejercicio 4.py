#Author: Sebastian Ochoa. Date: 08/06/2024
# -*- coding: utf-8 -*-

"""
4. Ejercicio

Escriba un programa que tenga definidas dos funciones; una para calcular el área y  otra para calcular el 
perímetro de un n-ágono regular. El usuario debe suministrar el número de lados del n-ágono y la distancia 
medida desde su centro a uno cualquiera de sus vértices. El programa debe suministrarle el área y el perímetro, 
también debe permitir realizar tantos cálculos como el usuario desee.
"""

from math import sin,sqrt,pi

def perimetro(n: int, r: float):
    a=360/n
    A=(pi*a)/180
    L=2*r*sin(A/2)
    per=L*n
    return per

def area(n:int, r: float):
    per=perimetro(n,r)
    L=per/n
    a=sqrt(r**2-(L/2)**2)
    are=(per*a)/2
    return are

print("Hola, hoy te ayudaré a calcular el perimetro y el area de un n-ágono regular")
respuesta='s'
while respuesta=='s':
    N=int(input("Dime el número de lados que tendrá tu n-ágono: "))
    radio=float(input("Dime la distancia entre el centro del n-ágono y cualquiera de sus vertices: "))
    perime=perimetro(N,radio)
    ar=area(N,radio)
    print(f"Para el n-ágono regular con radio {radio} y un numero de {N} lados, su perimetro es: {round(perime,3)}u (aproximadamente) y su area es {round(ar,3)}u² (aproximadamente).")
    respuesta=str(input("Quieres hacer el mismo procedimiento para otro n-ágono?\n\tSi=(s)\tNo=(n)\n\t"))
print("Gracias por usar mi codigo :D")