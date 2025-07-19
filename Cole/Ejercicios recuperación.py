# -*- coding: utf-8 -*-

"""
1.En una estación de Transmilenio los operarios usan una fórmula matemática sencilla para saber si deben o no despachar un bus nuevo. Para esto tienen un contador de pasajeros en el bus entrante (personas_bus) y un de personas paradas en la plataforma (personas_estacion).
Los operarios saben que la capacidad teórica máxima del bus es de 150 personas. Sin embargo, también saben que si se aprietan pueden transportar a máxirno 200 personas.
Los pasajeros no quieren viajar incómodos pero tampoco quieren demorarse mucho tomando el bus. así que sólo se montarán a un bus con sobrecupo aue llegue a la estación si hay 40 0 más personas en la plataforma. Luego de aue el bus se detenga y entren las personas. los operarios decidirán si deben enviar un bos adicional: enviarán un bus mnuevo. si al salir de ia estación el bus quedó con sobrecupo o si en la plataforma quedaron 50 0 más personas.
Su trabajo es construir una función en Python que le ayude a los operarios de Transmilenio a tomar Ia decisión de despachar o no un bus nuevo.
"""

def despacho_buses (personas_bus:int, personas_estacion:int)->bool:
    retorno=False
    if personas_bus >= 150:
        if personas_estacion >= 40:
            retorno=True
    else:
        entran_al_bus=150-personas_bus
        quedan_estacion=personas_estacion-entran_al_bus
        if quedan_estacion >= 50:
            retorno=True
    return retorno

#print(estacion_trasmilenio(0,200))

"""
2.En el taller de regalos de Santa Claus. el CTE (Chief Technology Elf) ha decidido implementar un nuevo sistema de clasificación de regalos, para facilitar la organización
de los mismos. Cada paquete tiene ahora un identificador numérico único. El identificador es un número entero entre 100 y 999. y sirve para clasificar los regalos de la siguiente manera.
• Si el número es palíndromo e impar, el regalo corresponde a una niña.
• Si el número es palíndromo y par. el regalo corresponde a un niño.
• Si el número es par. pero no palíndromo. el regalo corresponde a un hombre.
• Si el número es impar, pero no palíndromo, el regalo corresponde a una mujer.
Escriba una función que ayude al CTE a calcular. dado un identificador único de regalo. a que tipo de persona corresoonde dicho regalo.
"""

def clasificar_regalo (id:int)->str:
    retorno='Women'
    palindromo=False
    par=False
    primer=id//100
    ultimo=id%10
    if id%2 == 0:
        par=True
    if primer==ultimo:
        palindromo=True
    if palindromo and par:
        retorno='Boy'
    elif palindromo:
        retorno='Girl'
    elif par:
        retorno='Man'
    return retorno

#print(regalo_de_santa(202))

def movimiento_robot(orientacion_actual: str, giro: str)->str:
  respuesta=""
  if orientacion_actual == "N":
    if giro == "L":
      respuesta="W"
    if giro == "H":
      respuesta == "S"
    if giro == "R":
      respuesta == "E"
  if orientacion_actual == "W":
    if giro == "L":
      respuesta="S"
    if giro == "H":
      respuesta == "E"
    if giro == "R":
      respuesta == "N"
  if orientacion_actual == "S":
    if giro == "L":
      respuesta="E"
    if giro == "H":
      respuesta == "N"
    if giro == "R":
      respuesta == "W"
  if orientacion_actual == "E":
    if giro == "L":
      respuesta="N"
    if giro == "H":
      respuesta == "W"
    if giro == "R":
      respuesta == "S"
  if giro == ".":
    respuesta = orientacion_actual
  return respuesta

def ejer_3():
  print("Hola pirata, te ayudaré a saber cuantos viajes debe hacer tu empresa")
  c=int(input("Dime cuntas cajas debes llevar: "))
  p=int(input("Dime cuanto pesa una de las cajas: "))
  p_t=p*c
  if p_t<1000:
    if c < 100:
      v=1
    else:
      v_x=c//100
      if c%100!=0:
        v_c=v_x+1
      else:
        v_c=v_x
      v=v_c
  else:
    v_y=p_t//1000
    if p_t%1000!=0:
      v_p=v_y+1
    else:
      v_p=v_y
    v=v_p
  print("Tienes que tomar",v,"viajes")