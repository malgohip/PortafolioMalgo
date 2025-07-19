#Author: Sebastian Ochoa. Date: 07/30/2024
# -*- coding: utf-8 -*-

"""
Ejercicio 7.

Diseñe un código que lea los coeficientes de un par de rectas con ecuación ax + by = c desde un archivo 
de texto llamado Datos.txt. y calcule el punto de corte en el caso en que éste exista, o indique si las rectas 
son paralelas y no se cortan. En este caso debe leer 6 datos correspondientes a los valores de a, b y c para 
cada una de las rectas. Los datos deben disponerse por filas, por ejemplo, si las rectas son: 2x + 3y = 1 y 
-3x + 2y = 2.  En el archivo de texto, deben aparecer los datos en el siguiente orden:

 2 3 1

-3 2 2

El reporte de resultados debe suministrarse en otro archivo denominado Resultados.txt. El reporte debe mostrar los mensajes:

* Las rectas ax+by = c y dx+ey = f se cortan en el punto (x_0,y_0).
* Las rectas ax+by = c y dx+ey = f no se cortan y por lo tanto son paralelas.
"""

f=open('Talleres pre-parcial\Taller_2_1\TXTs y JSON\Datos(1).txt', 'r+')

L = f.readlines()

ab=L[0].strip().split()
AB=[]
de=L[2].strip().split()
DE=[]
for x in ab:
    X=int(x)
    AB.append(X)
for x in de:
    X=int(x)
    DE.append(X)
mAB=AB[0]/-AB[1]
mDE=DE[0]/-DE[1]
cAB=AB[2]/AB[1]
cDE=DE[2]/DE[1]
risposta=f"\n\nLas rectas {AB[0]}x+{AB[1]}y={AB[2]} y {DE[0]}x+{DE[1]}y={DE[2]} coinciden en todos sus puntos."
if mAB != mDE:
    x=(cDE-cAB)/(mAB-mDE)
    y=mAB*x+cAB
    corte=(x,y)
    risposte=f"\n\nLas rectas {AB[0]}x+{AB[1]}y={AB[2]} y {DE[0]}x+{DE[1]}y={DE[2]} se cortan en el punto {corte}."
else:
    if cAB != cDE:
        risposte=f"\n\nLas rectas {AB[0]}x+{AB[1]}y={AB[2]} y {DE[0]}x+{DE[1]}y={DE[2]} son paralelas."

f.write(risposte)
f.close()