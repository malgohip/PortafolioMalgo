import time as tm
import math as mt

def ejer_1():
  print("Hola, te ayudare a que soluciones una ecuacion de primer grado de la forma: a x + b = 0")
  a=float(input("Dime el coeficiente 1: "))
  b=float(input("Dime el coeficiente 2: "))

  if a != 0:
    x= -b / a
    print("Tiene una solución y es:", x)
  elif a == 0 and b == 0:
    print("No tiene solucción real")
  else:
    print("Todos los numeros son la solución")

def ejer_2():
  print("Hola, te ayudare a que soluciones una ecuacion de segundo grado de la forma: ax²+bx+c=0")
  a=float(input("Dime el coeficiente 1: "))
  b=float(input("Dime el coeficiente 2: "))
  c=float(input("Dime el coeficiente 3: "))
  disc=(b**2-4*a*c)
  if disc < 0:
    print("No tiene solucion")
  else:
    x_1 = (-b + mt.sqrt(b**2-4*a*c) ) / (2*a)
    x_2 = (-b - mt.sqrt(b**2-4*a*c) ) / (2*a)
    if x_1 == x_2:
      print("X tiene solo un resultado y es:", x_1)
    elif a == 0:
      print("X es todos los numeros")
    else:
      print("X tiene solo dos resultados y son:", x_1, "y", x_2) 

def ejer_3(): 
  print("Hola te ayudare a determinar tu nota final en la materia de sociales y de paso a decirte tu desempeño")
  n=float(input("Dime cuanto fue tu definitiva: "))
  if 0.0 < n > 5.9:
    print("Tu nota es", n, "Y tu desempeño es BAJO")
  elif 6.0 < n > 7.4:
    print("Tu nota es", n, "Y tu desempeño es BASICO")
  elif 7.5 < n > 8.9:
    print("Tu nota es", n, "Y tu desempeño es ALTO")
  elif 9.0 < n > 10.0:
    print("Tu nota es", n, "Y tu desempeño es SUPERIOR")
  else:
    print("La nota no puede ser menor a 0 ni mayor a 10")

def ejer_4():
  print("Hola, te ayudare a ver de cuanto es tu comison de venta")
  v=int(input("Dime de cuanto fueron tus ventas: "))
  if v < 1000:
    print("Lo siento, no tienes comsison de venta")
  elif 1000 <= v < 1500:
    print("Tu comsion de venta es del 3%")
  elif 1500 <= v < 2000:
    print("Tu comsion de venta es del 5%")
  else:
    print("Tu comsion de venta es del 7%")

def ejer_5():
  print("Hola, te ayudare a saber cuanto debes pagar de agua")
  c_i=60
  l=int(input("Dime la cantidad de litros gastados en este periodo: "))
  if 0 < l < 50:
    print("Debes pagar $", c_i)
  elif 50 < l < 200:
    m=l*30
    p=60+m
    print("Debes pagar $", p)
  else:
    m=l*50
    p=60+m
    print("Debes pagar $", p)

def ejer_5_1():
  print("Hola, te ayudare a saber cuanto debes pagar de agua")
  e=int(input("Dime que estrato eres: "))
  m=int(input("Dime la cantidad de metros cubicos gastados en este periodo: "))
  if e == 1 or e == 2:
    c_i=0
    if 0 < m < 20:
      j=m*2000
      p=c_i+j
      print("Debes pagar $", p)
    elif 21 < m < 35:
      j=m*3500
      p=c_i+j
      print("Debes pagar $", p)
    else:
      j=m*5000
      p=c_i+j
      print("Debes pagar $", p)
  elif e == 3:
    c_i=5000
    if 0 < m < 20:
      j=m*3000
      p=c_i+j
      print("Debes pagar $", p)
    elif 21 < m < 35:
      j=m*4500
      p=c_i+j
      print("Debes pagar $", p)
    else:
      j=m*7000
      p=c_i+j
      print("Debes pagar $", p)
  elif e == 4:
    c_i=15000
    if 0 < m < 20:
      j=m*4000
      p=c_i+j
      print("Debes pagar $", p)
    elif 21 < m < 35:
      j=m*6000
      p=c_i+j
      print("Debes pagar $", p)
    else:
      j=m*8000
      p=c_i+j
      print("Debes pagar $", p)
  elif e == 5:
    c_i=25000
    if 0 < m < 20:
      j=m*5000
      p=c_i+j
      print("Debes pagar $", p)
    elif 21 < m < 35:
      j=m*7000
      p=c_i+j
      print("Debes pagar $", p)
    else:
      j=m*10000
      p=c_i+j
      print("Debes pagar $", p)
  elif e == 6:
    c_i=30000
    if 0 < m < 20:
      j=m*6000
      p=c_i+j
      print("Debes pagar $", p)
    elif 21 < m < 35:
      j=m*8500
      p=c_i+j
      print("Debes pagar $", p)
    else:
      j=m*12000
      p=c_i+j
      print("Debes pagar $", p)
  else:
    print("nopuedes tener un estrato menor a 1 ni mayor A 6")

def menu():
  m=input("Hola te daré una seria de programas con diferentes opciones y luego tu me indicas cual deseas usar: \n1. Resolver una ecuación de primer grado: Digita 1 \n2. Resolver una ecuación de segundo grado: Digta 2 \n3. Desempeño en la asignatura de sociales: Digita 3 \n4. Comisión de venta: Digita 4 \n5. Gasto de agua de una vivienda en litros: Digita 5 \n6. Gasto de agua de una vivienda con estrato y en mero cubicos: Digita 5.1 \nDime, cual quieres ejecutar?: ")
  if m == '1':
    ejer_1()
  elif m == '2':
    ejer_2()
  elif m == '3':
    ejer_3()
  elif m == '4':
    ejer_4()
  elif m == '5':
    ejer_5()
  elif m == '5.1':
    ejer_5_1()
  else:
    print("Oye no mames, no es ninguna de esas \nInteta otra vez")
    tm.sleep(3)
    menu()
menu()