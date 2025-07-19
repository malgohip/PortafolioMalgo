# -*- coding: utf-8 -*-
"""
Descripción del problema
Una panadería vende la unidad de pan a $450. El pan del día anterior se vende con un 60% de descuento.

Cree una función que reciba la cantidad de panes del día anterior y la cantidad de panes frescos comprados por un cliente, y retorne el valor total de la compra.
"""


def calcular_total_pan_comprado(frescos: int, viejos: int)->int:
    """ Pan del día anterior
    Indica cuanto sería el precio de una bolsa de pan en base a los panes nuevos y viejos.
    Parámetros:
      frescos (int): Número de panes frescos que compra el cliente (recibe valores entre 1 y 600).
      viejos (int): Número de panes viejos que compra el cliente (recibe valores entre 0 y 500)
    Retorno:
      int: Valor total a pagar por el pan comprado.
    """
    precio_frescos=450*frescos
    precio_viejos=(450*0.6)*viejos
    precio_total=precio_frescos+precio_viejos
    return int(precio_total)