# -*- coding: utf-8 -*-
"""
Descripción del problema:
Iván, Nicolás, y Adriana son amigos de toda la vida. A los 3 les gusta comer uvas, por lo que se reúnen cada semana, en la tarde del viernes, para hablar de su semana y disfrutar de ese deleite. Iván, Nicolás y Adriana comen una cierta cantidad entera de uvas, que puede o no ser igual entre ellos. Además, ellos siempre compran 3 tipos de uvas: Verde, Negra y Morada. Ellos ordenan las uvas con una semana de anticipación, y las reciben por domicilio. Esto implica que, algunas veces, los amigos pueden no tener suficientes uvas para satisfacer sus gustos. Ellos no saben predecir cuantas uvas querrán con exactitud semana tras semana. De los amigos, se sabe además que: Iván come exclusivamente uvas verdes. Nicolás odia las uvas negras, por lo que solamente come uvas verdes o moradas. Adriana come cualquier tipo de uva, pues todas le encantan. Los tres amigos quieren saber si dadas unas cantidades de uvas negras, verdes, y moradas que llegan en el pedido, podrán quedar felices dada la cantidad de uvas que quieran comer en el dia. Nótese que ellos quieren que la mayor cantidad de amigos logre comerse todas las uvas que quiere. En otras palabras, un amigo puede decidir no comer uvas siempre que dicha decisión le permita a alguien más completar su cantidad.
"""
def suficientes_uvas(cantidad_ivan: int, cantidad_nicolas: int, cantidad_adriana: int, cantidad_verde: int, cantidad_morada: int, cantidad_negra: int)->str:
  """
  Suficientes uvas
  Indica si la cantidad de uvas son suficientes entre los amigos
  Parámetros:
    cantidad_ivan (int): La cantidad que Ivan desea comer.
    cantidad_nicolas (int): La cantidad que Nicolas desea comer.
    cantidad_adriana (int): La cantidad que Adriana desea comer.
    cantidad_verde (int): La cantidad de uvas verdes que disponen los amigos.
    cantidad_morada (int): La cantidad de uvas moradas que disponen los amigos.
    cantidad_negra (int): La cantidad de uvas negras que disponen los amigos.
  Retorno:
    str: La función retorna felices", si todos los amigos pueden comer la cantidad de uvas que quieren: "casi si dos de los 3 amigos pueden comer la cantidad de uvas que quieren: "fallamos si solamente 1 amigo puede comer la cantidad de uvas que quiere "al menos somos amigos" si ninguno de los amigos puede comer la cantidad de uvas que quiere.
  """
  felices=0
  respuesta="Al menos somos amigos"
  if cantidad_verde >= cantidad_ivan:
    felices+=1
    cantidad_verde_1=cantidad_verde-cantidad_ivan
    come_nicolas=cantidad_verde_1+cantidad_morada
    if come_nicolas >= cantidad_nicolas:
      felices+=1
      cantidad_verde_2=cantidad_verde_1-(cantidad_nicolas/2)
      cantidad_morada_1=cantidad_morada-(cantidad_nicolas/2)
      come_adriana=cantidad_verde_2+cantidad_morada_1+cantidad_negra
      if come_adriana >= cantidad_adriana:
        felices+=1
    elif come_nicolas < cantidad_nicolas:
      come_adriana=cantidad_verde_1+cantidad_morada+cantidad_negra
      if come_adriana >= cantidad_adriana:
        felices+=1
  elif cantidad_verde < cantidad_ivan:
    come_nicolas=cantidad_verde+cantidad_morada
    if come_nicolas >= cantidad_nicolas:
      felices+=1
      cantidad_verde_2=cantidad_verde-(cantidad_nicolas/2)
      cantidad_morada_1=cantidad_morada-(cantidad_nicolas/2)
      come_adriana=cantidad_verde_2+cantidad_morada_1+cantidad_negra
      if come_adriana >= cantidad_adriana:
        felices+=1
    elif come_nicolas < cantidad_nicolas:
      come_adriana=cantidad_verde+cantidad_morada+cantidad_negra
      if come_adriana >= cantidad_adriana:
        felices+=1
  if felices == 3:
    respuesta="Felices"
  elif felices == 2:
    respuesta="Casi"
  elif felices == 1:
    respuesta="Fallamos"
  return respuesta