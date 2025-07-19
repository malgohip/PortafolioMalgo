# -*- coding: utf-8 -*-
"""
Descripción del problema:
El profesor desea revisar como han avanzado tus conocimientos a lo largo de este curso de phyton, la idea es que usando todas las funciones realizadas hasta el momento y  en una sola funcion permita acceder y utilizar todas ellas,  mediante un menu en el cual recibiendo un valor numerico haga uso de la función especificada.
"""

import math as mt
from Ochoa_2_area_cuadrado import area_cuadrado
from Ochoa_3_area_circunferencia import area_circunferencia
from Ochoa_3_diferencia_de_edades import diferencia_edades
from Ochoa_3_volumen_de_una_piscina import volumen_piscina
from Ochoa_4_descuento_del_20 import descuento
from Ochoa_4_numero_menor import numero_menor
from Ochoa_4_numero_positivo_o_negativo import postitivo_negativo
from Ochoa_5_norma_de_suma import norma_suma
from Ochoa_5_ordenador_de_numeros import ordenador_numeros
from Ochoa_5_rango_de_1_a_10 import rango_1_10
from Ochoa_6_volumen_de_un_cono import volumen_cono
from Ochoa_6_volumen_esfera import volumen_esfera
from Ochoa_8_numeros_romanos import numero_romano
from Ochoa_10_diferencia_de_las_piscinas import diferencia_piscinas
def primer_menu(opcion: int):
    """
    Primer menu
    Da un menu con todos los codigos hechos.
        Parámetros:
        opcion (int): Número que indica cual de las opciones de los codigos deseamos utilizar (recibe valores entre 1 y 14).
    Retorno:
        tuple: Valor correspondiente a la respues y con la información del codigo usado.
    """
    retorno=('Da una opción valida.')
    if opcion == 1:
        lado=float(input("Indicame de cuanto es el lado del cuadrado: "))
        respuesta=area_cuadrado(lado)
        retorno=(respuesta,'Sería el área del cuadrado usando el codigo',area_cuadrado)
    elif opcion == 2:
        radio=float(input("Indicame de cuanto es el radio de la circunferencia: "))
        respuesta=area_circunferencia(radio)
        retorno=(respuesta,'Sería el área de la circunferencia usando el codigo',area_circunferencia)
    elif opcion == 3:
        nombre_1=str(input("Indicame cual es el nombre del primer hermano: "))
        nombre_2=str(input("Indicame cual es el nombre del segundo hermano: "))
        nombre_3=str(input("Indicame cual es el nombre del tercer hermano: "))
        edad_1=int(input("Indicame cual es la edad del primer hermano: "))
        edad_2=int(input("Indicame cual es la edad del segundo hermano: "))
        edad_3=int(input("Indicame cual es la edad del tercer hermano: "))
        respuesta=diferencia_edades(nombre_1, nombre_2, nombre_3, edad_1, edad_2, edad_3)
        retorno=(respuesta,'Sería la diferencia de las edades usando el codigo',diferencia_edades)
    elif opcion == 4:
        largo=float(input("Indicame cual es el largo de la piscina: "))
        ancho=float(input("Indicame cual es el ancho de la piscina: "))
        profundo=float(input("Indicame cual es el profundo de la piscina: "))
        respuesta=volumen_piscina(largo, ancho, profundo)
        retorno=(respuesta,'Sería el volumen de la piscina usando el codigo',volumen_piscina)
    elif opcion == 5:
        factura=float(input("Indicame de cuanto es la factura de la compra: "))
        respuesta=descuento(factura)
        retorno=(respuesta,'Sería el nuevo valor de la factura usando el codigo',descuento)
    elif opcion == 6:
        numero_1=int(input("Indicame cual es el primer numero: "))
        numero_2=int(input("Indicame cual es el segundo numero: "))
        respuesta=numero_menor(numero_1, numero_2)
        retorno=(respuesta,'Sería la respuesta al número menor usando el codigo',numero_menor)
    elif opcion == 7:
        numero=int(input("Indicame cual es el numero para evaluar: "))
        respuesta=postitivo_negativo(numero)
        retorno=(respuesta,'Sería la respuesta a si el número es positivo o negativo usando el codigo',postitivo_negativo)
    elif opcion == 8:
        numero_1=int(input("Indicame cual es el primer numero: "))
        numero_2=int(input("Indicame cual es el segundo numero: "))
        numero_3=int(input("Indicame cual es el tercer numero: "))
        respuesta=norma_suma(numero_1, numero_2, numero_3)
        retorno=(respuesta,'Sería la respuesta a la norma de la suma usando el codigo',norma_suma)
    elif opcion == 9:
        numero_1=int(input("Indicame cual es el primer numero: "))
        numero_2=int(input("Indicame cual es el segundo numero: "))
        orden=str(input("Indicame cual es el orden de los numeros: "))
        respuesta=ordenador_numeros(numero_1, numero_2, orden)
        retorno=(respuesta,'Sería el orden de los números usando el codigo',ordenador_numeros)
    elif opcion == 10:
        valor=float(input("Indicame cual es el numero para evaluar: "))
        respuesta=rango_1_10(valor)
        retorno=(respuesta,'Sería la respuesta a si el número se encuentra en el rango 1-10 usando el codigo',rango_1_10)
    elif opcion == 11:
        radio=float(input("Indicame cual es el radio de la base del cono: "))
        altura=float(input("Indicame cual es la altura del cono: "))
        respuesta=volumen_cono(radio, altura)
        retorno=(respuesta,'Sería el volumen del cono usando el codigo',volumen_cono)
    elif opcion == 12:
        radio=float(input("Indicame cual es el radio de la esfera: "))
        respuesta=volumen_esfera(radio)
        retorno=(respuesta,'Sería el volumen de la esfera usando el codigo',volumen_esfera)    
    elif opcion == 13:
        numero=int(input("Indicame cual es el numero para evaluar: "))
        respuesta=numero_romano(numero)
        retorno=(respuesta,'Sería la nomenclatura del numero usando el codigo',numero_romano)   
    elif opcion == 14:
        largo_1=float(input("Indicame cual es el largo de la piscina: "))
        ancho_1=float(input("Indicame cual es el ancho de la piscina: "))
        profundo_1=float(input("Indicame cual es el profundo de la piscina: "))
        largo_2=float(input("Indicame cual es el largo de la piscina: "))
        ancho_2=float(input("Indicame cual es el ancho de la piscina: "))
        profundo_2=float(input("Indicame cual es el profundo de la piscina: "))
        respuesta=diferencia_piscinas(largo_1, ancho_1, profundo_1, largo_2, ancho_2, profundo_2)
        retorno=(respuesta,'Sería la diferencia de las piscinas usando el codigo',diferencia_piscinas)
    return retorno