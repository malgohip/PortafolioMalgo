# -*- coding: utf-8 -*-

"""
Descripción del problema:
Vamos a representar a un estudiante usando un diccionario con 4 llaves: "nombre", para almacenar su nombre; y "matemáticas", "lenguaje" y "ciencias" para almacenar las notas en cada una de las 3 materias. Escriba una función que reciba un estudiante (un diccionario) y retorne su promedio.
"""

def promedio(estudiante: dict)->float:
    """
    Promedio materias
    Tomando un diccionario con las 3 notas finales retorna el promedio de estas
    Parámetros:
        estudiante (dict): Diccionario que contiene el nombre del estudiante y las notas finales de sus 3 materias.
    Retorno:
        float: Retorna el promedio de las notas del estudiante.
    """
    matematicas=estudiante['matematicas']
    lenguaje=estudiante['lenguaje']
    ciencias=estudiante['ciencias']
    promedio=(matematicas+lenguaje+ciencias)/3
    return promedio

"""
Descripción del problema:
Ahora escriba una función que reciba un estudiante (un diccionario), el nombre de una de las tres materias, y una nota, y le asigne al estudiante la nueva nota en esa materia.
"""

def nueva_materia(estudiante: dict, nombre: str, nota: float)->dict:
    """
    Nueva materia
    Tomando un diccionario con 3 notas de 3 materias distintas, y una materia extra con su respectiva nota, retorna el diccionario con la nueva materia.
    Parámetros:
        estudiante (dict): Diccionario que contiene el nombre del estudiante y las notas finales de sus 3 materias.
        nombre (str): Nombre de la 4 materia a introducir en el diccionario.
        nota (float): Nota de la 4 materia para incluir en el diccionario.
    Retorno:
        dict: diccionario con la materia extra y su respectiva nota.
    """
    estudiante[nombre]=nota
    return estudiante

"""
Descripción del problema:
Escriba una función que reciba tres estudiantes (tres diccionarios) y el nombre de una de las tres materias. La función debe aumentar la nota de cada estudiante en la materia en un 10% del promedio de los tres estudiantes en esa materia.
"""

def aumento_nota (estudiante_1: dict, estudiante_2: dict, estudiante_3: dict, materia: str)->list:
    """
    Aumento de la nota
    Tomando 3 diccionarios cada uno con las notas de 3 alumnos en sus respectivas materias, y el nombre de una materia, para así aumentar la nota de los 3 estudiantes en esta materia el 10% del promedio.
    Parámetros:
        estudiante_1 (dict): Diccionario que contiene el nombre del primer estudiante y las notas finales de sus 3 materias.
        estudiante_2 (dict): Diccionario que contiene el nombre del segundo estudiante y las notas finales de sus 3 materias.
        estudiante_3 (dict): Diccionario que contiene el nombre del tercer estudiante y las notas finales de sus 3 materias.
        materia (str): Nombre de la materia a la cual se le aumentará la nota con cada estudiante.
    Retorno:
        list: lista que contenga los 3 diccionarios con la nota actuaizada.
    """
    if not materia in estudiante_1 and materia in estudiante_2 and materia in estudiante_3:
        return None
    nota_1=estudiante_1[materia]
    nota_2=estudiante_2[materia]
    nota_3=estudiante_3[materia]
    aumento=((nota_1+nota_2+nota_3)/3)*0.1
    estudiante_1[materia]=nota_1+aumento
    estudiante_2[materia]=nota_2+aumento
    estudiante_3[materia]=nota_3+aumento
    return [estudiante_1,estudiante_2,estudiante_3]

"""
Descripción del problema:
Construya una función que reciba dos números enteros como parámetros: si el primer número es par, la función debe retornar la suma de los dos números; de lo contrario, debe retornar la multiplicación de los dos números.
"""

def numeros (numero_1: int, numero_2: int)->int:
    """
    Numeros
    Tomando 2 números enteros devuelve la suma o la multiplicacion de estos dependiendo si el primero es par o no respectivamente.
    Parámetros:
        numero_1 (int): Primer numero el cual debemos tomar para realizar la operación.
        numero_2 (int): Segundo numero el cual debemos tomar para realizar la operación.
    Retorno:
        int: Retorno en base a si el primer número analizado es par o no.
    """
    if (numero_1%2)==0:
        return numero_1+numero_2
    else:
        return numero_1*numero_2

"""
Descripción del problema:
Invoque su función con varias parejas de números igual que como lo ha estado haciendo hasta el momento.
"""

#print(numeros(5,6))

"""
Descripción del problema:
Invoque la función nuevamente, pero esta vez utilice los nombres de los parámetros: pruebe usando los parámetros en el orden en el que están definidos en la función y también en el orden opuesto. Compruebe que el resultado en cada caso es el que usted esperaría.
"""

numero_1=5
numero_2=6
#print(numeros(numero_1,numero_2))
#print(numeros(numero_2,numero_1))

"""
Descripción del problema:
Invoque la función usando sólo un parámetro. Si no funciona, asegúrese de entender el error que reciba.
"""

#print(numeros(5))
"""
Traceback (most recent call last):
  File "g:\Mi unidad\2023\Programación\Retos\Andes\0 Ejercicios\Ochoa_Ejercicios_3.8.py", line 112, in <module>
    print(numeros(5))
TypeError: numeros() missing 1 required positional argument: 'numero_2'
PS G:\Mi unidad\2023\Programación> 
"""

"""
Descripción del problema:
Modifique la función para que tenga valor por defecto sólo para el segundo parámetro.
"""

def numeros_1 (numero_1: int, numero_2: int = 6)->int:
    """
    Numeros
    Tomando 2 números enteros devuelve la suma o la multiplicacion de estos dependiendo si el primero es par o no respectivamente.
    Parámetros:
        numero_1 (int): Primer numero el cual debemos tomar para realizar la operación.
        numero_2 (int): Segundo numero el cual debemos tomar para realizar la operación.
    Retorno:
        int: Retorno en base a si el primer número analizado es par o no.
    """
    if (numero_1%2)==0:
        return numero_1+numero_2
    else:
        return numero_1*numero_2

"""
Descripción del problema:
Repita las invocaciones con uno y con dos parámetros, tanto con los nombres como sin ellos. ¿En qué casos se produjeron errores?
"""

#print(numeros_1(5,6))
#NO error
numero_1=5
numero_2=6
#print(numeros_1(numero_1,numero_2))
#NO error
#print(numeros_1(numero_2,numero_1))
#NO error

"""
Descripción del problema:
Modifique ahora la función para que tenga valor por defecto sólo para el primer parámetro. Vuelva a hacer las pruebas y revise en qué casos se producen errores.
"""

def numeros_2 (numero_1: int = 5, numero_2: int)->int:
    """
    Numeros
    Tomando 2 números enteros devuelve la suma o la multiplicacion de estos dependiendo si el primero es par o no respectivamente.
    Parámetros:
        numero_1 (int): Primer numero el cual debemos tomar para realizar la operación.
        numero_2 (int): Segundo numero el cual debemos tomar para realizar la operación.
    Retorno:
        int: Retorno en base a si el primer número analizado es par o no.
    """
    print(numero_1)
    if (numero_1%2)==0:
        return numero_1+numero_2
    else:
        return numero_1*numero_2

#error
"""
  File "g:\Mi unidad\2023\Programación\Retos\Andes\0 Ejercicios\Ochoa_ejercicios_3.8.py", line 160
    def numeros_2 (numero_1: int = 5, numero_2: int)->int:
                                      ^^^^^^^^^^^^^
SyntaxError: non-default argument follows default argument
"""

#print(numeros_2(0,6))
numero_1=5
numero_2=6
#print(numeros_2(numero_1,numero_2))
#print(numeros_2(numero_2,numero_1))