import time as tm

def ejer_1():
  n = -20
  s = 0
  while n < 101:
    n = n + 1
    s=s+n
  print(s)

def ejer_2():
  cont=1
  m=0
  while cont < 11:
    cont += 1
    n=float(input("Dime una de las notas: "))
    if n < 6:
      m = m + 1
  print("perdio", m,"notas")

def ejer_3_1():
  t=0
  s=0
  while s < 30:
    n=float(input("Dime uno de los numeros de la suma: ")) 
    s=n+s
    t = t+1
  print("sumaste",t,"números")

def ejer_3_2():
  cont=1
  cun_p=0
  cun_n=0
  while cont < 11:
    cont += 1
    n=float(input("Dime uno de los numeros: "))
    if n > 0:
      cun_p += 1
    elif n < 0:
      cun_n += 1
  print("Diste", cun_p, "numeros positivos y", cun_n,"numeros negativos")

def menu():
  m=input("Hola, te ofrezco los puntos de la evaluación de while, los cuales son: \n1. La suma de los dumeros del -20 al 100: digita 1 \n2. Programa que indique de 10 notas cuantas perdiste: Digita 2 \n3. Programa que al sumar una serie de numeros se dentenga al llegar a 30 e indique cuantos numeros digito: Digita 3.1 \n4. Programa que de 10 numeros cuantos son positivos y negativos: Digita 4.1 \nDime, cual quieres usar: ")
  if m == '1':
    ejer_1()
  elif m == '2':
    ejer_2()
  elif m == '3.1':
    ejer_3_1()
  elif m == '3.2':
    ejer_3_2()
  else:
    name=input("Dime tu nombre bello usuario: ")
    print("Eres un pendejo", name, "\nTe di 4 sencillas opciones y no le atinas?, vos son pero mk \nVenga trata otra vez")
    tm.sleep(3)
    menu()
menu()