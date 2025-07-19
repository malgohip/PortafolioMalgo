# -*- coding: utf-8 -*-
"""
Descripción del problema
Cree una función que reciba el costo en pesos de una cuenta de restaurante, y luego calcule el impuesto IVA asociado y la propina para el mesero. La tasa del IVA corresponde al 19%, y la propina en el restaurante es del 10% del valor de la factura (sin impuestos).

La función debe retornar una cadena que muestre el IVA, propina y total de la siguiente manera: "X,Y,Z", donde X es el IVA, Y la propina y Z el total.

No olvide aproximar su resultado al entero más cercano.
"""

def calcular_iva_propina_total_factura(costo_factura: int)->str:
    """ IVA y propina
    Indica cuanto se ha de pagar en base a el iva y la propina.
    Parámetros:
      costo_factura (int): Costo de la factura del restaurante, sin impuestos ni propina.
    Retorno:
      str: Cadena con el iva, propina y total de la factura, separados por comas.
    """
    iva_factura=round(costo_factura*0.19)
    propina=round(costo_factura*0.10)
    total= round((costo_factura)+(iva_factura*0.19)+(propina*0.1))
    respuesta=str(iva_factura)+","+str(propina)+","+str(total)
    
    return respuesta