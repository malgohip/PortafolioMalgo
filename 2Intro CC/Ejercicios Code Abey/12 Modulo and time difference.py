#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
El manejo de los residuos puede convertirse en un gran dolor de cabeza para los programadores novatos. Escribamos un programa sencillo que gire en torno a esta operación, con el fin de estudiar de mejor manera la división de enteros. Al mismo tiempo, tendremos algo de práctica en la manipulación de fechas - las cuales algunas veces dan dolores de cabeza hasta a codificadores/programadores experimentados.

En aritmética, el residuo (o módulo) es la cantidad "que queda" después de realizar la división de dos enteros que no se dividen exactamente (extraído de la Wiki). Esta tarea proporcionará más práctica aún con la operación módulo.

Supongamos que se nos dan dos fechas - por ejemplo, cuando el tren o el barco transbordador inician su viaje y cuando lo termina. Estas fechas lucen así:

inicio: May 3, 17:08:30
fin  : May 8, 12:54:15
y tenemos la curiosidad de saber cuánto tiempo (en día, horas, minutos y segundos) se gasta en viajar (quizá con el fin de escoger la opción más rápida). ¿Cómo podríamos lograrlo?

Una de las maneras más fáciles es:

convierte ambas fechas a números grandes, representando los segundos desde el inicio del mes (o año, o siglo);
calcula sus diferencias - ej.: tiempo de viaje en segundos;
convierte esta diferencia de nuevo a días, horas, minutos y segundos.
La primera operación podría ser realizada multiplicando los minutos por 60 y las horas por 60*60, etc. y sumando todos los valores que resulten.
La tercera operación debería ser realizada a lo contrario, mediante varias divisiones que preserven los residuos.

En esta tarea se nos dan varios pares de fechas. Supongamos que ambas fechas del par corresponden siempre al mismo mes, por lo que sólo se nos dará el número de días. Queremos calcular la diferencia entre las fechas de cada par.

Datos de entrada: La primera línea contiene el número de casos; las otras contienen los casos de prueba en sí.
Cada caso de prueba contiene 8 números, 4 por cada fecha: día1 hora1 min1 seg1 día2 hora2 min2 seg2 (la segunda fecha siempre será posterior a la primera).
Respuesta: Para cada caso, deberás mostrar la diferencia como sigue (días horas minutos segundos) - por favor, no olvides los paréntesis - y separados por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e12 Modulo and time difference.txt','r')
P= a.readlines()

fechas=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    A=[]
    B=[]
    for x in range(0,4):
        X=int(f[x])
        Y=int(f[x+4])
        A.append(X)
        B.append(Y)
    fecha=[]
    fecha.append(tuple(A))
    fecha.append(tuple(B))
    fechas.append(fecha)

print(fechas)
"""
fechas=[[(5, 8, 23, 37), (16, 0, 47, 6)], [(15, 0, 35, 19), (23, 4, 28, 47)], [(10, 23, 22, 16), (12, 16, 54, 32)], [(5, 17, 5, 27), (24, 21, 55, 58)], [(6, 4, 6, 11), (29, 7, 59, 34)], [(11, 17, 35, 28), (28, 23, 38, 28)], [(18, 15, 58, 7), (25, 12, 25, 35)], [(19, 8, 39, 29), (19, 15, 39, 7)], [(11, 11, 57, 59), (29, 18, 38, 7)], [(2, 0, 28, 56), (14, 23, 5, 53)], [(10, 10, 2, 56), (12, 9, 4, 10)], [(9, 21, 29, 1), (22, 9, 40, 12)], [(10, 14, 6, 17), (18, 9, 42, 50)], [(2, 12, 50, 2), (13, 9, 34, 51)], [(0, 16, 2, 5), (27, 23, 28, 21)]]

resultado=''
def segundos(fecha):
    d=fecha[0]*24*60*60
    h=fecha[1]*60*60
    m=fecha[2]*60
    s=d+h+m+fecha[3]
    return s

def fecha(segundos):
    d=segundos/86400
    h=((d-int(d))*86400)/3600
    m=((h-int(h))*3600)/60
    s=(m-int(m))*60
    return (int(d),int(h),int(m),round(s))


for x in fechas:
    s_1=segundos(x[0])
    s_2=segundos(x[1])
    s_3=abs(s_1-s_2)
    f_3=fecha(s_3)
    resultado+='('
    for y in f_3:
        resultado+=str(y)+' '
    resultado=resultado[:-1]
    resultado+=') '
print(resultado)