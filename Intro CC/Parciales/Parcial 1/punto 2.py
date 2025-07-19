#Author: Sebastian Ochoa. Date: 03/05/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 2.(20 Ptos.)

Diseñe un algoritmo que pinte usando asteriscos *, un triángulo isoceles y un cuadrado tal como se muestra en la figura.
                
                *           * * * * * * * * * *          
               * *          * * * * * * * * * *         
              * * *         * * * * * * * * * *       
             * * * *        * * * * * * * * * *         
            * * * * *       * * * * * * * * * *       
           * * * * * *      * * * * * * * * * *           
          * * * * * * *     * * * * * * * * * *       
         * * * * * * * *    * * * * * * * * * *       
        * * * * * * * * *   * * * * * * * * * *   
       * * * * * * * * * *  * * * * * * * * * *
El número de asteriscos en la base de ambas figuras la da el usuario. No se puede  usar la propiedad multiplicativa del comando print.
"""

def ejer_2():
    tamano=int(input("Hola, dime que tan grande quieres la base de tu triangulo isoceles y de tu cuadrado: "))
    cont=1
    espacios=tamano
    esp=""
    ast_tri="* "
    ast_cua=""
    while cont <= tamano:
        esp+=" "
        ast_cua+="* "
        cont+=1
    linea=esp+ast_tri+esp+ast_cua
    print(linea)
    cont=1
    cont_esp_2=1
    while cont < tamano:
        esp=""
        cont_esp=espacios
        cont_esp-=cont_esp_2
        while cont_esp > 0:
            cont_esp-=1
            esp+=" "
        cont_esp_2+=1
        ast_tri+="* "   
        linea=esp+ast_tri+esp+ast_cua
        print(linea)
        cont+=1

ejer_2()