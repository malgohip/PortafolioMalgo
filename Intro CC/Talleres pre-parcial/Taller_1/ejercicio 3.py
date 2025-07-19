#Author: Sebastian Ochoa. Date: 02/29/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 3.

Diseñe un algoritmo que pinte usando asteriscos *, un rombo tal que una de sus diagonales tengan una cantidad de asteriscos (*) igual a un valor entero dado por el usuario.
Por ejemplo, si el valor de la diagonal es 10, entonces el rombo debe verse como sigue:
                
                *                     
               * *                  
              * * *                
             * * * *                
            * * * * *              
           * * * * * *            
          * * * * * * *          
         * * * * * * * *       
        * * * * * * * * *     
       * * * * * * * * * *
        * * * * * * * * *       
         * * * * * * * *
           * * * * * *
            * * * * *
             * * * *
              * * *
               * *
                *   
"""

def ejer_3():
    tamano=int(input("Hola, dime que tan grande quieres la diagonal de tu rombo: "))
    cont=1
    espacios=tamano
    while cont != tamano:
        esp=" "*(espacios)
        ast="* "*cont
        linea=esp+ast+esp
        print(linea)
        espacios-=1
        cont+=1
    print(" "+"* "*tamano)
    cont-=1
    espacios+=1
    while cont != 0:
        esp=" "*(espacios)
        ast="* "*cont
        linea=esp+ast+esp
        print(linea)
        espacios+=1
        cont-=1
    
ejer_3()