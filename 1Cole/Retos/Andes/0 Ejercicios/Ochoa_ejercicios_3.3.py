# -*- coding: utf-8 -*-BMI_saludable
"""
Descripción del problema:
Escriba una función que dada la edad de una persona indique si puede manejar (tiene que tener al menos 16 años)
"""

def edad_conduccion(edad: int)->bool:
  """
  edad condución
  Edad que debe tener minimo una persona para poder conducir.
  Parámetros:
    edad (int): Valor que indica la edad de la persona que se va a evaluar si puede conducir (recibe valores entre 0 y 116).
  Retorno:
    bool: Valor booleano que indica si tiene la edad minima para conducir.
  """
  respuesta=False
  if edad >= 16:
    respuesta=True
  return respuesta
  
  
"""
Descripción del problema:
Escriba una función que dada la altura en metros y el peso en kilogramos de un adulto diga si está dentro de los rangos típicamente considerados saludables. Para esto debe usar el Índice de Masa Corporal (BMI), que se calcula como . Un adulto se considera que tiene sobrepeso cuando su BMI es mayor o igual a 25. Un adulto se considera que está bajo de peso cuando su BMI es menor a 18.5.
"""

def BMI_saludable (altura: float, peso: float)->bool:
  """
  BMI saludable
  Indica si el adulto tiene un BMI saludable.
  Parámetros:
    altura (float): Valor que indica la altura del adulto el cual va a ser evaluado (recibe valores entre 0.7 y 2.9).
    peso (float): Valor que indica el peso del adulto el cual va a ser evaluado (recibe valores entre 22 y 594.8).
  Retorno:
    bool: Valor boleano que indica si el adulto esta saludable desntro de los rangos considerados saludables.
  """
  respuesta=False
  BIM=(peso/(altura**2))
  if BIM < 18.5 or BIM >= 25:
    respuesta=True
  return respuesta

  
"""
Descripción del problema:
Escriba una función que dados dos números diga si el primero es divisible por el segundo.
"""

def divisibilidad (numero_1: int, numero_2: int)->bool:
  """
  divisibilidad
  Indica si un numero  es divisible por el otro
  Parámetros:
    numero_1 (int): Valor el cual se desea saber si es divisible por el otro.
    numero_2 (int): Valor el cual se desea saber si es divisor del otro.
  Retorno:
    bool: Valor booleano que indica si el primer valor es divisible por el segundo.
  """
  respuesta=False
  
  if (numero_1%numero_2) == 0:
    respuesta=True
  return respuesta

  
"""
Descripción del problema:
Queremos saber si una persona tiene el dinero suficiente para pagar la cuenta en un restaurante dados los siguientes parámetros: la cantidad de dinero que tiene la persona, el valor de la cuenta, si la persona va a dejar propina o no. La propina corresponde al 10% del valor de la cuenta.
"""

def saldo_suficiente (saldo: int, cuenta: int, propina: bool)-> bool:
  """
  Saldo suficiente
  Indica si se puede pagar una factura con el saldo de su cuenta.
  Parámetros:
    saldo (int): Valor que indica la cantidad de dinero que se posee la persona (recibe valores entre 0 y 320000000).
    cuenta (int): Valor que indica la cantidad de dinero que cuesta la cuenta de la persona (recibe valores entre 0 y 615065).
    propina (bool): Valor booleano que indica si se quiere dar una cuota de servicio del 10%.
  Retorno:
    bool: Valor booleano que indica si la persona tiene el suficiente dinero apra pagar la cuenta.
  """
  respuesta=False
  valor_propina=0  
  if propina:
    valor_propina=cuenta/10
  vueltas=saldo-(cuenta+valor_propina)
  if vueltas >= 0:
    respuesta=True
  return respuesta