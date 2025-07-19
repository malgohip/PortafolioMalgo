# -*- coding: utf-8 -*-
"""
Descripción del problema:
48. Crea un programa en donde existe dos funciones, la primera función permitirá preguntarle al usuario una cantidad de números, se deja de preguntar números cuando el usuario digita cero, estos números quedan ingresados en un diccionario.
Crea una segunda función donde el argumento de entrada sea este diccionario con los valores obtenidos y retornara el promedio. (realizar con ciclos) 
"""
def introducion_numeros ()->list:
    """
    Introducción de números
    Funcion la cual permite entrar la cantidad de numeros deseados y que deje de permitirlos al momento de ingresar 0
    Retorno
        List: lista que contiene los números ingresados.
    """
    revision=1
    diccionario={}
    contador=0
    while revision != 0:
        contador+=1
        ingreso=int(input("Introduce el número a introducir al diccionario: "))
        revision=ingreso
        diccionario[str(contador)]=ingreso
    return diccionario

def promedio(diccionario: dict)->int:
    """
    Promedio
    Esta función recibe un diccionario y retorna el valor del promedio de sus valores (para esto todos deben de encontarse del tipo int)
    Parámetros:
        diccionario (dict): Diccionario cuyos valores deben de ser tomados para hallar su promedio.
    Retorno:
        List: lista que contiene los números ingresados.
    """
    valores= diccionario.values()
    sumatoria=0
    for x in valores:
        sumatoria+=x
    promedio=sumatoria/(len(valores)-1)
    return round(promedio,2)

#print(promedio(introducion_numeros()))

"""
Descripción del problema:
49. realizar un programa que indrudusca un numero entero y devuelva la suma de sus digitos
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

def suma_digitos(digitos: list)->int:
    """
    Sumar los digitos de un número
    Suma cada uno de los digitos de un número y lo retorna como un int.
    Parámetros:
        digitos (list): Lista la cual contiene los digitos del número.
    Retorno:
        int: Sumatoria de los digitos del número.
    """
    sumatoria=0
    for x in digitos:
        sumatoria+=x
    return sumatoria

#numero=int(input("Dime el número: "))
#print(suma_digitos(separar(numero)))

"""
descripción del problema:
50. Realizar un juego para adivinar un número. Para ello pedir un número N, y luego ir pidiendo números indicando “mayor” o “menor” según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta.
"""

import random as rn

def juego_adivinanzas():
    """
    Juego de adivinanza numerica
    La función saca un número aleatorio entre 0 y 1000 y el usuario debe de adivinarlo
    """
    numero=rn.randint(0,1000)
    prueba=-1
    while prueba != numero:
        adivinanza =int(input("Dime el número el cual deseas probar: "))
        if adivinanza < numero:
            print("El número es mayor.")
        elif adivinanza > numero:
            print("El número es menor.")
        else:
            print("FELICIDADES!, GANASTE")
            break

"""
Descripción problema:
51.  Se piden 10 números al usuario, calcular el promedio de los numero múltiplos 5
"""

def promedio_5 ()->int:
    """
    Promedio de los multiplos de 5
    Retorna el promedio de los multiplos de 5 de una serie de 10 números pedida al usuario
    Retorno:
        int: Promedio de los multiplos de 5.
    """
    cont=0
    multiplos=[]
    while cont < 10:
        peticion=int(input("Dime que numero tomarás: "))
        if (peticion%5) == 0:
            multiplos.append(peticion)
        cont += 1
    cantidad=len(multiplos)
    sumatoria=0
    for x in multiplos:
        sumatoria+=x
    promedio=sumatoria/cantidad
    return round(promedio,1)

#print(promedio_5())

"""
Descripción del problema:
52. Imprimir la serie: 1- 2- ping - 4-5-ping-7-8-ping-10-11-pan-13-14-ping ..... el limite lo ingresa el usuario
"""

def secuencia()->str:
    """
    Secuencia de numeros y letras
    Retorna una secuencia de numeros con diferetes palabras en los multiplos de 3 y de 12.
    Retorno:
        str: Secuencia de números alterada
    """
    maximo=rn.randint(0,1000000)
    secuencia=""
    for x in range(1,maximo):
        proximo=str(x)
        if x%3 == 0 and x%4 ==0:
            proximo="pan"
        elif x%3 == 0:
            proximo="ping"
        secuencia+=(proximo+"- ")
    return secuencia
    
#print(secuencia())