# -*- coding: utf-8 -*-

"""
Descripcion problema:
En una estación de Transmilenio los operarios usan una fórmula matemática sencilla para saber si deben o no despachar un bus nuevo. Para esto tienen un contador de pasajeros en el bus entrante (personas_bus) y un de personas paradas en la plataforma (personas_estacion).
Los operarios saben que la capacidad teórica máxima del bus es de 150 personas. Sin embargo, también saben que si se aprietan pueden transportar a máxirno 200 personas.
Los pasajeros no quieren viajar incómodos pero tampoco quieren demorarse mucho tomando el bus. así que sólo se montarán a un bus con sobrecupo aue llegue a la estación si hay 40 0 más personas en la plataforma. Luego de aue el bus se detenga y entren las personas. los operarios decidirán si deben enviar un bos adicional: enviarán un bus mnuevo. si al salir de ia estación el bus quedó con sobrecupo o si en la plataforma quedaron 50 0 más personas.
Su trabajo es construir una función en Python que le ayude a los operarios de Transmilenio a tomar Ia decisión de despachar o no un bus nuevo.
"""

def despacho_buses (personas_bus:int, personas_estacion:int)->bool:
    """ 
    Despacho de buses
    Indica si se debe enviar otro trasmilenio despues de recoger pasajeros.
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse (número de 0 a 200).
      personas_estación (int): Número de personas esperando al bus en la estación.
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """
    retorno=False
    if personas_bus > 150:
        if personas_estacion >= 40:
            retorno=True
        else:
            retorno=True
    else:
        entran_al_bus=150-personas_bus
        quedan_estacion=personas_estacion-entran_al_bus
        if quedan_estacion >= 50:
            retorno=True
    return retorno