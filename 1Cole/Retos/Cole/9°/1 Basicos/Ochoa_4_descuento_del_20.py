# -*- coding: utf-8 -*-
"""
Descripción del problema:
El empresario Santiago quiere montar su propia cadena de locales.
Su idea es que en esta cadena si el cliente realiza una compra de más de 300 dolares este tenga un descuento del 20%

Realiza una función la cual dando el valor final de la factura tu devuelvas cuanto sería ese descuento y si no se cumple la cantidad de dinero simplemente devuelve la misma factura.
"""
def descuento(factura: float)->float:
    """
    Descuento
    insica de cuanto será el descuento en una tienda.
    Parámetros:
        factura (float): Valor en dolares de la factura de la compra(recibe valores entre 0.27 y 70000).
    Retorno:
        float: Valor de la factura tras ser aplicado o no el descuento
    """
    if factura > 300:
        descuento=factura*(20/100)
        factura=factura-descuento
    return factura