# -*- coding: utf-8 -*-

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
    """ 
    Clasificar Regalo
    Indica a que tipo de persona pertenece el regalo a analizar.
    Parámetros:
      id (int): El identificador del regalo cuyo tipo de persona se quiere calcular (recibe valores del 100 a 999).
    Retorno:
      str: Si el número es Palíndromo e impar, el regalo corresponde a una niña, y se retorna 'girl' Si el número es Palíndromo e par, el regalo corresponde a una niño, y se retorna 'boy' Si el número es par, pero no palíndromo, el regalo corresponde a un hombre, y se retorna 'man' Si el número es impar, pero no palíndromo, el regalo corresponde a una mujer, y se retorna 'women'
    """
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