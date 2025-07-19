# -*- coding: utf-8 -*-
"""
Descripcion del problema
Luigi está estudiando los números de Fibonacci como parte de su clase de computación y le han llamado mucho la atención por la forma en que se definen: el enésimo término de la secuencia de Fibonacci siempre es igual a la suma de los dos términos anteriores. El primer y segundo término de la secuencia pueden empezar en valores arbitrarios. En otras palabras, si  y  son enteros, entonces:


Dada la anterior definición, Luigi quiere construir una función que permita verificar si, dados cuatro números ordenados, la secuencia de números cumple con la definición de Fibonacci.
"""

def Consecutivos_fibonacci(fib_1: int, fib_2: int, fib_3: int, fib_4: int)->str:
  """ Consecutivos fibonacci
  Indica si una sencuencia dada corresponde a una secuencia de fibonacci.
  Parámetros:
    fib_1 (int): El primer caso base de esta posible secuencia de fibonacci
    fib_2 (int): El segundo caso base de esta posible secuencia de fibonacci
    fib_3 (int): El tercer término de esta posible secuencia de fibonacci; no es un caso base.
    fib_4 (int): El cuarto término de esta posible secuencia de fibonacci; no es un caso base.
  Retorno:
     str: Retorna "Fibofacil", si la secuencia corresponde a una secuencia de Fibonacci. De lo contrario, retorna "Fibofalsa"
  """
  texto='Fibonacci'
  if fib_1+fib_2==fib_3 and fib_2+fib_3==fib_4:
    texto='Fibofacil'
  else:
    texto='Fibofalsa'
  return texto
