# -*- coding: utf-8 -*-
"""
Descripción del problema
Cree una función que calcule el menor ángulo formado entre las agujas de un reloj (horario y minutero), dada una hora y minutos. La hora siempre tendrá un valor entre 0 y 11, y los minutos un valor entre 0 y 59.

El valor de retorno debe tener un único decimal.

Ayuda: Recuerde que el minutero salta de minuto a minuto, mientras el horario se va desplazando de forma continua a medida que avanzan los minutos de una hora.
"""

def angulo_entre_agujas_reloj(hora: int, minutos: int)->float:
    """ Ángulo entre agujas del reloj
    Indica cuanto es el angulo entre el horero y el minutero de un reloj.
    Parámetros:
      hora (int): Hora marcada en el reloj (Valor entre 0 y 12)
      minutos (int): Minutos marcados en el reloj (Valor entre 0 y 59)
    Retorno:
      float: El ángulo (en grados) entre las agujas del reloj según la hora y       minuto dados como parámetro, el cual debe tener un único dígito decimal.
    """
    grados_hora=(360/12)*hora
    grados_minutos=(360/60)*minutos
    angulo_entre=grados_hora-grados_minutos
    return round(abs(angulo_entre),1)