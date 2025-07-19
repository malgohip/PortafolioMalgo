import time as tm 

def ejer_1():
  n_1=int(input("Hola, dime uno de los numeros: "))
  n_2=int(input("Hola, dime uno de los numeros: "))
  n_3=int(input("Hola, dime uno de los numeros: "))
  if n_1==n_2 and n_1 == n_3 and n_2 == n_3:
    print("Los números son iguales")
  elif n_1 == n_2 or n_1 == n_2 or n_2 == n_3:
    print("Dos de los numeros son iguales")
  else:
    print("Ninguno de los numeros son iguales")


def ejer_2():
  v=input("Hola, bienvenido al programa de votaciones del gobierno, Los candidatos son: \n1. Por el partido rojo Gustavo Petro \n2. Por el partido verde Ernesto Perez \n3. Por el partido azul Fedrico Gutierrez \nSi deseas votar por el cualquier candidato digita su nombre: ")
  v_m=v.lower()
  if v_m == 'gustavo petro':
    print("Votaste por el partido Rojo")
  elif v_m == 'ernesto perez':
    print("Votaste por el partido verde")
  elif v_m == 'federico guiterrez':
    print("votaste por el partido azul")
  else:
    print("opcion erronea")


def ejer_3():
  a_1=int(input("Hola, dime el año actual: "))
  a_2=int(input("Ahora dime un año cualquiera: "))
  if a_1 < a_2:
    r=a_2-a_1
    if r == 1:
      print("faltan",r, "año para llegar al", a_2)
    else:
      print("faltan",r, "años para llegar al", a_2)
  elif a_1 > a_2:
    s=a_1-a_2
    if s == 1:
      print("Hace",s, "año era el", a_2)
    else:
      print("Hace",s, "años era el", a_2)
  else:
    print("Es el mismo año")


def ejer_4():
  l_1=int(input("Hola, dime uno de los lados del cuadrilatero: "))
  l_2=int(input("Hola, dime uno de los lados del cuadrilatero: "))
  l_3=int(input("Hola, dime uno de los lados del cuadrilatero: "))
  l_4=int(input("Hola, dime uno de los lados del cuadrilatero: "))
  if l_1 == l_2 and l_1 == l_3 and l_1 == l_4 and l_2 == l_3 and l_2 == l_4 and l_3 == l_4:
    print("El cuadilatero es un cuadrado")
  elif l_1 == l_2 and l_3 == l_4 or l_1 == l_3 and l_2 == l_4 or l_1 == l_4 and l_2 == l_3:
    print("El cuadrilatero es un rectangulo")
  else:
    print("El cuadrilatero es irregular")


def ejer_5():
  l_1=int(input("Dime uno de los lados del triangulo: "))
  l_2=int(input("Dime uno de los lados del triangulo: "))
  l_3=int(input("Dime uno de los lados del triangulo: "))
  if l_1 == l_2 and l_1 == l_3 and l_2 == l_3:
    print("El triangulo es equilatero")
  elif l_1 == l_2 or l_1 == l_3 or l_2 == l_3:
    print("El triangulo es isósceles")
  else:
    print("El triangulo es escaleno")


def menu():
  m=input("Hola, te daré 5 programas tu me dices cual deseas usar \n1. de 3 numeros decir si son iguales o diferentes: digita 1 \n2. un programa de votaciones con 3 cantidatos: digita 2 \n3. Decir que tan lejos estamos del años que das: digita 3 \n4. decir si un cuadrilatero es cuadrado, recctangulo o irregular: digta 4 \n5. De un triangulo decir si es equilatero, isoceles o escaleno: digita 5 \nDime, cual quieres?: ")
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
  else:
    print("Opcion erronea trate de nuevo")
    tm.sleep(3)
    menu()
menu()