def ejer_1():
  c=0
  q=0
  i=0
  sq=0
  si=0
  print("Hola, dime 200 números y te diré cules son multiplos de 4 y de 7 la suma de estos")
  while c < 200:
    c += 1
    n=int(input("Dime uno de los números: "))
    if n%4 == 0:
      q += 1
      sq = n + sq
    if n%7 == 0:
      i += 1
      si = n + si
  st= si + sq
  print("De los números que introduciste \nSon",q,"multiplos de 4 y su suma es",sq,"\nSon",i,"multiplos de 7 y su suma es ",si,"\nY",st,"es la suma de todos")

def ejer_2():
  c=0
  print("Hola, imprimiré la secuencia (1,2,pin,4,5,pin,7,8,pin,10,11,PAN,13,14, pin,...) y tu me indicas hasta que número llegar")
  n=int(input("Dime hasta que número quieres llegar: "))
  while c < n:
    c += 1
    if c%3 == 0 and c%12 != 0:
      print("pin")
    elif c%12 == 0:
      print("PAN")
    else:
      print(c)

def ejer_3():
  c=0
  print("Hola, imprimiré la secuencia (1,2,pin,PAN,5,pin,7,PAN,pin,10,11,PP,13,14, pin,PAN,...) y tu me indicas hasta que número llegar")
  n=int(input("Dime hasta que número quieres llegar: "))
  while c < n:
    c += 1
    if c%3 == 0 and c%12 != 0:
      print("pin")
    elif c%4 == 0 and c%12 != 0:
      print("PAN")
    elif c%12 == 0:
      print("PP")
    else:
      print(c)

def ejer_4():
  s=0
  while s != 1:
    o=input("Deseas salir? \nSi si deseas digita 'S' \nSi no deseas salir digita cualquier otra cosa: ")
    if o == 'S':
      s=1
    else:
      s=0

def ejer_5():
  c=0
  s=0
  while c <= 100:
    c += 1
    u=c**2
    s = s + u
  print(s)

def ejer_6():
  s=1
  while s == 1:
    n=int(input("Dime el número del cual quieres su cuadrado: "))
    if n < 0:
      s = 0
    c=n**2
    print(c)

def menu():
  print("Hola, dime que programa quieres usar hoy: \n1) Me das 200 números y te diré cuántos de estos números son múltiplos de 4, y cuantos son múltiplos de 7 y te cuento cuanto es la suma de estos números: Digita 1 \n2) Imprimo la secuencia (1,2,pin,4,5,pin,7,8,pin,10,11,PAN,13,14, pin,...) hasta que me digas en que número parar: Digita 2 \n3) Imprimo la secuencia (1,2,pin,PAN,5,pin,7,PAN,pin,10,11,PP,13,14, pin,PAN,...) hasta que me digas en que número parar: Digita 3 \n4) Te doy un menu en el cual me dices si quieres salir o no: Digita 4 \n5) Te digo la suma de los primeros 100 números: Digita 5 \n6) Te digo el cuadrado del número que me digas hasta que des un número negativo: Digita 6")
  m=int(input("Dime cual quieres: "))
  if m == 1:
    ejer_1()
  elif m == 2:
    ejer_2()
  elif m == 3:
    ejer_3()
  elif m == 4:
    ejer_4()
  elif m == 5:
    ejer_5()
  elif m == 6:
    ejer_6()
  else:
    print("Indica una opcion correta, trata otra vez")
    menu()
menu()