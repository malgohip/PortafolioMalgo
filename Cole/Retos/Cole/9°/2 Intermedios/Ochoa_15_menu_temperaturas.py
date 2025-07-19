"""
Descripción del problema:
El químico Felipe debe cambiar de unidad las temperaturas de sus reacciones para realizar su informe de laboratorio.

Realiza un menu el cual contenga los programas necesarios para realizar cualquier tipo conversión entre las 3 temperaturas y sean accesibles, tomando así como parametros de entrada la temperatura a colvertir y el tipo de conversión.
"""
def centigrados_farenheit(grados:float)->float:
  farenheit=(9/5*grados)+32
  return farenheit

def centigrados_kelvin(grados: float)->float:
  kelvin=grados+237.15
  return kelvin 

def farenheit_centigrados(grados: float)->float:
  centigrados=(5*(farenheit-32))/9
  return centigrados

def farenheit_kelvin(grados: float)->float:
  kelvin=((5*(grados-32))/9)+237.15
  return kelvin

def kelvin_centigrados(grados: float)->float:
  centigrados=grados-273.15
  return centigrados 

def kelvin_farenheit(grados: float)->float:
  farenheit=((9*(grados-273.15))/5)+32
  return farenheit


def menu_temperaturas(temperatura: float, conversion: int)->float:
  """
  Menu temperaturas
  Da un menu con todas las formas posibles de convertir los 3 sistemas de temperaturas.
  Parámetros:
    temperatura (float): Temperatura la cual se desea convertir entre unidades.
    conversion (int): Número el cual sirva como indicación en el tipo de conversión a realizar (recibe valores entre 1 y 6).
  Retorno:
    float: Temperatura final despues de realizar la conversión.
  """ 
  retorno="Da un valor valido"
  if conversion == 1:
    centigrados_farenheit(temperatura)
  elif conversion == 2:
    centigrados_kelvin(temperatura)
  elif conversion == 3:
    farenheit_centigrados(temperatura)
  elif conversion == 4:
    farenheit_kelvin(temperatura)
  elif conversion == 5:
    kelvin_centigrados(temperatura)
  elif conversion == 6:
    kelvin_farenheit(temperatura) 
  return retorno