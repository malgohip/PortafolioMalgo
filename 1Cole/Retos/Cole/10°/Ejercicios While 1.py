import time as tm
import random as rm

def ejer_1():
  c=0
  while (c<10):
    print("hola mundo")
    c=c+1

def ejer_2():
  co=0
  while (co<=100):
    print(co)
    co=co+1

def ejer_3():
  cop=0
  while (cop<=100):
    print(cop)
    cop=cop+2

def ejer_4():
  n_1=int(input("Dime que numero del 1 al 10 quieres ver la tabla: "))
  n_2=1
  if 0 < n_1 and n_1 < 10: 
    print("tabla del", n_1)
    while n_2 <= 10:
      pro=n_1*n_2
      print(n_1,"*",n_2,"=",pro)
      n_2 += 1
  else:
    print("No pibe, ese numero no sirve, trata de nuevo")
    tm.sleep(1)
    ejer_4()

def ejer_4_1():
  n_1=1
  n_2=1
  while n_1 < 11:
    n_2=1
    print("tabla del", n_1)
    while n_2 <= 10:
      pro=n_1*n_2
      print(n_1,"*",n_2,"=",pro)
      n_2 += 1
    n_1 += 1

def ejer_5 ():
  n_1=int(input("Hola, te dire la tabla de multiplicar del número que gustes\nFavor di el número: "))
  n_2=int(input("Hasta que numero quieres ver la tabla de multiplicar?"))
  print("tabla del", n_1)
  n_3=0
  while n_3 <=n_2:
    res=n_3*n_2
    print(n_1, "*", n_3, "=", res)
    n_3 = n_3+1
  print("ya es toda we")
  
def ejer_5_1():
  n=int(input("Hola, te dire la tabla de multiplicar del número que gustes\nFavor di el número: "))
  nun=1
  while nun<11:
    pro=n*nun
    print(n,"*",nun,"=",pro)
    nun=nun+1

def ejer_6():
  n_1= -50
  while n_1 <= -20:
    print(n_1)
    n_1 += 1

def ejer_7():
  s=0
  cont=1
  while cont < 11:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    s = n + s
  print(s)

def ejer_8():
  s=0
  cont=0
  while cont < 10:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    s = n + s
  ps= s/cont
  print(ps)

def ejer_9():
  s=0
  cont=1
  nn=int(input("Hola, dime cuantos numeros quieres sumar: "))
  while cont <= nn:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    s = n + s
  print(s)

def ejer_10():
  s=0
  cont=1
  nn=1
  while nn != 0:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    s = n + s
    if n == 0:
      nn=nn-1
  print(s)

def ejer_11_1():
  cont=1
  num=0
  while cont < 11:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    man=n%2
    if man==0:
      num = num + 1
  print(num)
       
def ejer_11_2():
  cont=1
  sum=0
  f=0
  while cont < 11:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    man=n%5
    if man==0:
      sum = n + sum
      f += 1
  pro=sum/f
  print(pro)

def ejer_11_3():
  cont=1
  sum=0
  while cont < 11:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    man=n%10
    if man==4:
      sum = n + sum
  print(sum)

def ejer_11_4():
  cont=1
  num=0
  sum=0
  f=0
  sam=0
  while cont < 11:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    man_1=n%2
    if man_1==0:
      num = num + 1
    man_2=n%5
    if man_2==0:
      sum = n + sum
      f += 1
    man=n%10
    if man==4:
      sam = n + sam
  print(num)
  pro=sum/f
  print(pro)
  print(sam)

def ejer_12():
  cont=1
  nk=0
  while cont < 11:
    cont += 1
    n=int(input("Dime uno de los numeros de la suma: "))
    if n==5:
      nk = 1
  if nk ==1:
    print("si, hay un 5")
  else:
    print("No, no hay un 5")

def ejer_13():
  cont=1
  sum=0
  while cont < 11:
    cont += 1
    n=float(input("Dime uno de los numeros de la suma: "))
    if n < 6:
      sum += 1
  print("Perdiste", sum, "notas")

def ejer_14():
  n=int(input("Dime el numero: "))
  man=n%10
  print("Su ultimo digito es", man)

def ejer_15_1():
  np=0
  cont=0
  num=56
  while np != num:
    n=int(input("Hola dime el numero que creeas que es: "))
    np = n
    cont =+1
    if n < num:
      print("El número que tengo es mayor")
    elif n > num:
      print("El número que tengo es menor")
  print("Ese es el numero")
  print("adivinaste en", cont, "intentos")

def ejer_15_2():
  np=0
  cont=0
  num=rm.choice(range(1, 100))
  while np != num:
    n=int(input("Hola dime el numero que creeas que es: "))
    np = n
    cont =+ 1
    if n < num:
      print("El número que tengo es mayor")
    elif n > num:
      print("El número que tengo es menor")
  print("Ese es el numero")
  print("adivinaste en", cont, "intentos")

def ejer_15_3():
  np=0
  cont=0
  cont_1=0
  cont_2=0
  p_1 = 0
  p_2 = 0
  num=rm.choice(range(1, 100))
  while np != num:
    if (cont%2) == '0':
      n_1=int(input("Hola que el jugador 1 diga el numero que creea que es: "))
      cont_1=+1
      p_1=1
      np = n
    elif (cont%2) == '1':
      n_2=int(input("Hola que el jugador 2 diga el numero que creea que es: "))
      cont_2=+1
      p_2=1
      np = n
    cont =+ 1
    if n < num:
      print("El número que tengo es mayor")
      p_1=0
      p_2=0
    elif n > num:
      print("El número que tengo es menor")
      p_1=0
      p_2=0
  print("Ese es el numero")
  if p_1 == 1:
    print("gano el jugador 1")
  elif p_2 == 1:
    print("gano el jugador 2")
  print("adivinaste en", cont, "intentos")

def menu():
  m=input("Hola, dime que ejercicio de while quieres ver \n1. Imprimir 'hola mundo' 10 veces: Digita 1 \n2. Imprimir los numeros del 1 al 100: Digita 2 \n3. Imprimir los numeros pares del 0 al 100: Digita 3 \n4. Imprimir la tabla de multiplicar del numero del 1 al 10 que gustes: Digita 4 \n5. Imprimir las tablas de multiplicar de los numeros del 1 al 10: Digita 4.1 \n6. Imprimir la tabla de mutplicar del numero que gustes haste el numero que gustes: Digita 5 \n7. Imprimir la tabla de multiplicar del numero que gustes:a Digita 5.1 \n8. Imprimir los numeros del -50 al -20: Digita 6 \n9. Imprimir la sumatoria de 10 numeros: Digita 7 \n10. Imprimir el promedio de 10 numeros: Digita 8 \n11. imprimir la suma de todos los numeros que gustes: Digita 9 \n12. Imprimir la suma de los numeros que digites (Terminalos en 0 ;)): Digita 10 \n13. Imprimir la cantidad de números pares en una serie de 10 numeros: Digita 11.1 \n14. Imprimir el promedio de los multiplos de 5 de una serie de 10 numeros: digita 11.2 \n15. La sumatoria de los numeros terminados en 4 de una seria de 10 numeros: Digita 11.3 \n16. Usar los anteriores 3 al mismo tiempo: digita 11.4 \n17. Saber si en una serie de 10 numeros uno de ellos es 5: Digita 12 \n18. De una serie de 10 notas decir cuantas se perdieron: Digita 13 \n19. Imprimir el ultimo digito de un numero cualquera: digita 14 \n20. Adivina el numero que yo tengo: Digita 15 \n21. Adivina un numero random entre 1 y 100: Digita 15.2 \nDime, cual quieres: ")
  if m == '1':
    ejer_1()
  elif m == '2':
    ejer_2()
  elif m == '3':
    ejer_3()
  elif m == '4':
    ejer_4()
  elif m == '4.1':
    ejer_4_1()
  elif m == '5':
    ejer_5()
  elif m == '5.1':
    ejer_5_1()
  elif m == '6':
    ejer_6()
  elif m == '7':
    ejer_7()
  elif m == '8':
    ejer_8()
  elif m == '9':
    ejer_9()
  elif m == '10':
    ejer_10()
  elif m == '11.1':
    ejer_11_1()
  elif m == '11.2':
    ejer_11_2()
  elif m == '11.3':
    ejer_11_3()
  elif m == '11.4':
    ejer_11_4()
  elif m == '12':
    ejer_12()
  elif m == '13':
    ejer_13()
  elif m == '14':
    ejer_14()
  elif m == '15.1':
    ejer_15_1()
  elif m == '15.2':
    ejer_15_2()
  elif m == '15.3':
    ejer_15_3()
  else:
    name=input("Dime tu nombre apreciado usauario: ")
    print("No mames, eres un pendejo", name, "\nTe di 21 sencillas posibilidades y no le atinas? \nVenga vuelve a intentar")
    tm.sleep(3)
    menu()
menu()