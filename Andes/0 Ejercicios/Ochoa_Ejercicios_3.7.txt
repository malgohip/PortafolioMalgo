# -*- coding: utf-8 -*-
"""palabras = { 'imagen' : 'Figura, representación, semejanza y apariencia de algo', 'figura' : 'Forma exterior de alguien o de algo',  'baraja' : 'Conjunto completo de cartas empleado para juegos de azar', 'posibilidad' : 'Aptitud, potencia u ocasión para ser o existir algo' }
print(type(palabras['imagen']))

numeros = { 0 : 'cero', 1 : 'Uno',  2 : 'Dos', 3 : 'Tres', 4 : 'Cuatro', 5 : 'Cinco',}
numero=int(input('Digitame el número: '))
print(numeros[numero])

romanos = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}
romanos_1 = {'XXI':21,'XXII':22,'XXIII':23,'XXIV':24,'XXV':25}
romanos.update(romanos_1)
print(romanos)
romano_aniadido=(str(input('Dime que numero romano quieres adicionar: '))).upper()
arabigo_aniadido=int(input('Como sería su notación arabiga: '))
romanos[romano_aniadido]=arabigo_aniadido
romano=(str(input('Digitame el número en romano: '))).upper()
print(romanos[romano])
print(romanos)

romano=(str(input('Digitame el número en romano a eliminar: '))).upper()
esta=romanos.get(romano,None)
if esta != None:
  romanos[romano]=None
print(romanos)

romanos = {'I':'Uno','II':'Dos','III':'Tres','IV':'Cuatro','V':'Cinco'}
print(romanos)
romanos_2={'XI':'Ventiuno','XII':'Ventidos','XIII':'Ventitres','XIV':'Venticuatro','XV':'Venticinco'}
romano_llave=str(input('Dime con que numero deseas guardar el diccionario: ')).upper()
romanos[romano_llave]=romanos_2
print(romanos)
"""

"""
Descripción del problema

Construya un diccionario con las alturas sobre el nivel del mar de las capitales de los países suramericanos. 
Use los nombres de las ciudades, usando mayúsculas al principio de las palabras, como llaves y las alturas como valores. Es decir, las llaves deben ser 'Bogotá', 'Buenos Aires'. etc.
"""

def alturas_capitales(capital: str, altura: int)->dict:
    """
    Alturas capitales
    Crea el diccionario de la alturas de las capitales.
    Parámetros:
        capital (str): Indica el nombre de la capital.
        altura (int): Idica la altura de la capital (recibe valores entre -32 y 5100).
    Retorno:
        dict: Diccionario actualizado con los nuevos valores
    """
    alturas={}
    capital=capital.title()
    alturas[capital]=altura
    return alturas

capitales=['Bogota','Caracas','Georgetown','Paramaribo','Cayenne','Quito','Lima','La Paz','Asuncion','Brasilia','Santiago','Buenos Aires','Montevideo']
l_alturas=[2625,900,0,3,143,2850,0,3625,43,1172,570,25,43]
alturas={}
for x in capitales:
    altura=alturas.setdefault(x,l_alturas[capitales.index(x)]) 
alturas.update(alturas_capitales('puerto argentino',75))

"""
Descripación del problema:

Escriba una función que reciba el diccionario con las alturas de las ciudades y los nombres de dos ciudades y que retorne el nombre de la ciudad que esté ubicada a una mayor altura. 
La función debe ser capaz de funcionar incluso si en el nombre de las ciudades se usan mayúsculas y minúsculas de forma diferente a como están en el diccionario (por ejemplo, ‘BoGoTá’ y ‘BUENOS aires’). 
Si alguno de los dos nombres no corresponde a una ciudad, la función debe retornar el valor None.
"""

def normalizar(cadena: str)->str:
    """
    normalizar
    Cambia todas las tildes de una cadena a vocales sin tildes
    Parámetros:
        cadena (str): Cadena a la cual se le desean quital las tildes
    Retorno:
        str: Cadena alterada despues de quitarle las tildes.
    """
    remplazar = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in remplazar:
        cadena = cadena.replace(a, b).replace(a.upper(), b.upper())
    return cadena

def comparacion_alturas(capitales: dict, ciudad_1: str, ciudad_2: str)->str:
    """
    Comparación alturas
    Compara la altura de 2 ciudades dadas como argumentos de entrada.
    Parámetros:
        capitales (dict): dicionario con las capitales de sudamerica y sus respectivas alturas.
        ciudad_1 (str): nombre de la primera ciudad a comparar su altura.
        ciudad_2 (str): nombre de la segunda ciudad a comparar su altura.
    Retorno:
        str: Nombre de la ciudad la cual posee una mayor altura entre las 2 a comparar.
    """
    ciudad_1=normalizar(ciudad_1.title())
    ciudad_2=normalizar(ciudad_2.title())
    retorno= None
    if ciudad_1 in capitales and ciudad_2 in capitales:
        altura_1=capitales[ciudad_1]
        altura_2=capitales[ciudad_2]
        if altura_1 >= altura_2:
            retorno=ciudad_1
        elif altura_1 <= altura_2:
            retorno=ciudad_2
    return retorno

#print(comparacion_alturas(alturas,'BoGoTá','BUENOS aires'))

"""
Descripción del problema:

Escriba una función que reciba un número entero y calcule un diccionario en el que cada llave es un dígito y los valores asociados son la cantidad de veces que aparece el dígito en el número entero. 
Si un dígito no aparece en el número, no debe aparecer en el diccionario.
"""

def separar(numero:int)->list:
    """
    Separar digitos de un número
    Separa cada uno de los digitos de un número y los retorna como una lista.
    Parámetros:
        numero (int): Número al cual se debe de separar en cada uno de sus digitos.
    Retorno:
        list: lista que contiene cada uno de los digitos del número.
    """
    digitos=[]
    while numero > 0:
        digitos.append(numero%10)
        numero=numero//10
    digitos=list(reversed(digitos))
    return digitos

def cantidad_digitos (numero: int)->dict:
    """
    Cantidad de digitos en un número
    Indica mediante un diccionario la cantidad de veces que aparece un digito en un número.
    Parámetros:
        numero (int): Número al cual se debe de revisar la cantidad de veces que aparece uno de sus digitos.
    Retorno:
        dict: Diccionario en el cual se indican sus digitos y la cantidad de veces que aparecen en el número.
    """
    diccionario={}
    numeros=[0,1,2,3,4,5,6,7,8,9]
    for x in numeros:
        for i in separar(numero):
            if i == x:
                if str(x) in diccionario:
                    diccionario[str(x)]+=1
                else:
                    diccionario[str(x)]=1
    return diccionario
    
"""
Descripción del problema:
Escriba una función que reciba un número entero y retorne el dígito que aparece más veces dentro del número.
"""
def mayor_cantidad_digito (numero: int)->int:

    """

    Digito con mayor repetición en un número
    Indica el digito que más se repite en un número.
    Parámetros:
        numero (int): Número al cual se debe de revisar el digito que aparece más veces.
    Retorno:
        int: digito el cual se repite más veces en el número.
    """
    diccionario=cantidad_digitos(numero)
    mayor=0
    retorno=None
    for x in diccionario:
        veces=diccionario[x]
        if veces > mayor:
            mayor=veces
            retorno=x
    return int(retorno)

"""
Descripción del problema:
Con base en el ejemplo del diccionario de celulares, construya una función que reciba los diccionarios de 4 celulares y cuente cuántos de estos celulares tienen más de 16 GB de memoria.
"""
def crear_celular(procesador: float, memoria: float, camara: float, pantalla: str, ancho: int, alto: int, pila: float, sistema: str, version: str)->dict:
  nuevo_celular = {}
  nuevo_celular['procesador'] = procesador
  nuevo_celular['memoria'] = memoria
  nuevo_celular['camara'] = camara
  nuevo_celular['pantalla'] = pantalla
  nuevo_celular['ancho'] = ancho
  nuevo_celular['alto'] = alto
  nuevo_celular['pila'] = pila
  nuevo_celular['sistema'] = sistema
  nuevo_celular['version'] = version
  return nuevo_celular
  
def mayor_espacio(celular: dict)-> bool:
    """ 
    Mayor espacio
    Busca si el celular posee un espacio mayor a 16GB.
    Para que se pueda usar la función, el celular debe representarse con un
    diccionario que tengan una llave llamada 'memoria' que indique la cantidad
    de Giga-bytes del espacio del celular.    
    Parámetros:
      celular (dict): Es un diccionario que representa el celular. 
    Retorno:
      bool: Retorna true si tiene una memora mayor a 16GB
    """
    retorno=False
    espacio = celular['memoria']
    if espacio > 16:
        retorno=True
    return retorno

def celulares_buena_memoria (celular_1: dict, celular_2: dict, celular_3: dict, celular_4: dict)->int:

    """
    Celulares con buena memoria
    Indica la cantidad de celulares con una memoria mayor a 16GB
    Parámetros:
        celular_1 (dict): Es un diccionario que representa al primer celular. 
        celular_2 (dict): Es un diccionario que representa al segundo celular.
        celular_3 (dict): Es un diccionario que representa al tercer celular. 
        celular_4 (dict): Es un diccionario que representa al cuarto celular.
    Retorno:
        int: Entero que representa la cantidad de celulares con más de 16GB.
    """
    retorno = 0
    if mayor_espacio(celular_1):
        retorno += 1
    if mayor_espacio(celular_2):
        retorno += 1
    if mayor_espacio(celular_3):
        retorno += 1
    if mayor_espacio(celular_4):
        retorno += 1    
    return retorno

"""
Descripción del problema:
Con base en el ejemplo del diccionario de celulares, construya una función que reciba los diccionarios de 4 celulares y diga cuál es el celular que tiene la mayor cantidad de pixeles en la pantalla.
"""

def celular_mejor_pantalla (celular_1: dict, celular_2: dict, celular_3: dict, celular_4: dict)->str:

    """
    Celular con la mejor pantalla
    Indica el nombre del celular con la mejor pantalla
    Parámetros:
        celular_1 (dict): Es un diccionario que representa al primer celular. 
        celular_2 (dict): Es un diccionario que representa al segundo celular.
        celular_3 (dict): Es un diccionario que representa al tercer celular. 
        celular_4 (dict): Es un diccionario que representa al cuarto celular.
    Retorno:
        str: nombre del celular con la mejor pantalla.
    """
    retorno = None
    pantalla_1=celular_1['pantalla']
    pantalla_2=celular_2['pantalla']
    pantalla_3=celular_3['pantalla']
    pantalla_4=celular_4['pantalla']
    if pantalla_1 > pantalla_2 and pantalla_1 > pantalla_3 and pantalla_1 > pantalla_4:
        retorno = 'celular_1'
    if pantalla_2 > pantalla_1 and pantalla_2 > pantalla_3 and pantalla_2 > pantalla_4:
        retorno = 'celular_2'
    if pantalla_3 > pantalla_2 and pantalla_3 > pantalla_1 and pantalla_3 > pantalla_4:
        retorno = 'celular_3'
    if pantalla_4 > pantalla_2 and pantalla_4 > pantalla_3 and pantalla_4 > pantalla_1:
        retorno = 'celular_4'
    return retorno

"""
Descripción del problema:
Con base en el ejemplo del diccionario de celulares, construya una función que reciba los diccionarios de 4 celulares y los modifique para duplicar la capacidad de la pila de todos.
"""

def doble_bateria(celular: dict)-> int:
    """ 
    Doblar bateria
    Devuelve el diccionario con la nueva capacidad que debe tener la bateria del celular. 
    Parámetros:
      celular (dict): Es un diccionario que representa el celular. 
    Retorno:
      int: retorna el diccionario con el valor de la pila.
    """
    bateria=celular['pila']
    nueva_bateria=bateria*2
    celular['pila']=nueva_bateria
    return celular

def mejora_bateria (celular_1: dict, celular_2: dict, celular_3: dict, celular_4: dict)->tuple:

    """
    Mejorar la bateria de los celulares.
    Aumenta la capacidad de bateria de todos los celulares.
    Parámetros:
        celular_1 (dict): Es un diccionario que representa al primer celular. 
        celular_2 (dict): Es un diccionario que representa al segundo celular.
        celular_3 (dict): Es un diccionario que representa al tercer celular. 
        celular_4 (dict): Es un diccionario que representa al cuarto celular.
    Retorno:
        tuple: tupla con los 4 diccionarios alterados.
    """
    celular_1=doble_bateria(celular_1)
    celular_2=doble_bateria(celular_2)
    celular_3=doble_bateria(celular_3)
    celular_4=doble_bateria(celular_4)
    return (celular_1,celular_2,celular_3,celular_4)

"""
Descripción del problema:
Modifique el programa que calcula cuáles valores salieron en los lanzamientos de 6 dados para que ahora calcule un histograma en el que se pueda saber cuántas veces salió cada número.
"""    
import random
def lanzar_dado(resultados: dict) -> None:
    """ Lanza un dado calculando aleatoriamente un número entre 1 y 6. Registra en el diccionario 'resultados' el valor que se obtuvo, asignándole el valor True a la llave que corresponde al valor.
    Parámetros:
      resultados (dict): Un diccionario que representa el conjunto de valores diferentes que se han obtenido en los lanzamientos pasados.
    """
    valor = random.randint(1,6)
    if str(valor) in resultados:
            resultados[str(valor)]+=1
    else:
            resultados[str(valor)]=1

# Lanzar el dado 6 veces y registrar los resultados obtenidos
def lanzar_6_dados()-> dict:
    """ Lanza el dado 6 veces y retorna un diccionario con los valores que se obtuvieron
    Resultado:
      (dict): Un diccionario donde sólo aparecen como llaves los valores que se
              obtuvieron en el lanzamiento del dado.
    """
    resultados = {}
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    return resultados
