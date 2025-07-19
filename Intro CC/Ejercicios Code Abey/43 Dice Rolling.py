#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
Cuando se programa un juego de tablero con dados, muchos programadores novatos experimentan problemas en la conversión de valores aleatoreos a los valores especificos de los puntos en los dados. La meta de esta tarea es dar una practica en simulacion en rodar dados dados recibiendo valores de un generador de numeros aleatoreos.

Supon, que tenemos un generador que nos da valores aleatoreos en un rango entre '0' (incluyendolo) y '1' (sin incluirlo) esto podria ser encontrado en lenguajes como Basic, Java, Matlab etc.

Queremos convertir esos valores con punto flotante a uno de los seis numeros enteros: entre '1' y'6'. Esto podria ser logrado realizando los siguientes pasos:

Multiplica el valor aleatoreo por N el cual es el numero de valores que queremos obtener - en nuestro caso multiplicaremos por '6' y el resultado será un valor punto flotante en el rango entre '0' (incluido) y '6' ( no incluido)
Ahora tomamos la parte entera del resultado (funcion llamada 'floor' -piso- o convertir a 'int' -entero-) se convertira en uno de los siguientes: 0, 1, 2, 3, 4, `5 con la misma probabilidad para cada uno.
Dado que necesitamos valores entre '1' y '6' nosotros simplemente añadimos '1' al resultado.
Ahora te serán dados varios numeros en el rango [0 .. 1) (puedes estar seguro, ellos son provistos por un generador de numeros aleatoreos) - y tú tienes que convertirlos a valores de dados utilizando el algoritmo de arriba.

Datos de entrada En la primera linea contendran el numero total de valores a convertir. Las siguientes lineas contendran un valor cada una, en forma como 0.142857. Respuesta deberá contener numeros entre '1' y '6' para cada valor de entrada, producido por el algoritmo mostrado.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e43 Dice Rolling.txt','r')
P= a.readlines()

valores=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    X=float(f[0])
    valores.append(X)

print(valores)
"""
valores=[0.78341957461089, 0.88828847929835, 0.14249256579205, 0.49417048227042, 0.83324822224677, 0.72443041671067, 0.40279512060806, 0.91654688259587, 0.1776299001649, 0.98128808150068, 0.72085473826155, 0.014808239415288, 0.42954706260934, 0.30774419847876, 0.63621024042368, 0.78346663806587, 0.24256593780592, 0.064259922597557, 0.01055273367092, 0.18411930650473, 0.11685726931319, 0.60098369792104, 0.12691251607612, 0.60821712343022, 0.96638529282063, 0.098905787337571]

resultado=''
for x in valores:
    resultado+=str(int(x*6)+1)+' '
print(resultado)