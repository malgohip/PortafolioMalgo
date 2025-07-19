import time as tm

def ejer_1():
  print("Hola, te ayudaré a saber el orden de 3 números que ingreses")
  n_1=int(input("Dime el primer número: "))
  n_2=int(input("Dime el segundo número: "))
  n_3=int(input("Dime el tercer número: "))
  if n_1 <= n_2 and n_1 <= n_3 and n_2 <= n_3:
    print("El orden de los números es:",n_1,",",n_2,",",n_3)
  elif n_1 <= n_2 and n_1 <= n_3 and n_3 <= n_2:
    print("El orden de los números es:",n_1,",",n_3,",",n_2)
  elif n_2 <= n_1 and n_2 <= n_3 and n_1 <= n_3:
    print("El orden de los números es:",n_2,",",n_1,",",n_3)
  elif n_2 <= n_1 and n_2 <= n_3 and n_3 <= n_1:
    print("El orden de los números es:",n_2,",",n_3,",",n_1)
  elif n_3 <= n_1 and n_3 <= n_2 and n_1 <= n_2:
    print("El orden de los números es:",n_3,",",n_1,",",n_2)
  else:
    print("El orden de los números es:",n_3,",",n_2,",",n_1)

def ejer_2(): 
  print("Hola te ayudare a determinar tu nota final en cualquier materia ny de paso a decirte tu desempeño")
  s_c=float(input("Dime la nota del saber conocer: "))
  s_h=float(input("Dime la nota del saber hacer: "))
  s_s=float(input("Dime la nota del saber ser: "))
  n=s_c*0.4+s_h*0.4+s_s*0.2
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

def ejer_3():
  a=0
  b=0
  c=0
  t=0
  x=1
  while x ==1:
    print("Hola, esta es una encuesta para la camará de diputados local sobre el tratado de libre comercio \nDigita 1 si estas a favor \nDigita 2 si estas en contra \nDigita 3 si te abstienes de opinar")
    s=int(input("Dime cual es tu voto: "))
    if s == 1:
      a = a + 1
      print("Votaste a favor")
    elif s == 2:
      b = b + 1
      print("Votaste en contra")
    elif s == 3:
      c = c + 1
      print("te abstienes de votar")
    else:
      print("ingrese un número valido")
    tm.sleep(1)
    x=int(input("Deseas encuestar a alguien más? \nSi sí digita 1 \nSi no digita otro número: "))
    t=+1
  r_a=(a/t)*100
  r_b=(b/t)*100
  r_c=(c/t)*100
  print("Los resultados fueron: \nPorcentaje a favor:",r_a,"% \nPorcentaje en contra:",r_b,"% \nPorcentaje que se abstiene de votar:",r_c,"%")

def ejer_4():
  print("Hola, te ayudaré a sber si un año es bisiesto")
  a=int(input("Dime el año a consultar: "))
  a_r=a%4
  a_c=a%100
  a_q=a%400
  if a_r == 0:
    if a_c == 0:
      if a_q == 0:
        print("el año es bisiesto")
      else:
        print("el año no es bisiesto")
    else:
      print("el año es bisiesto")
  else:
    print("el año no es bisiesto")
ejer_4()
def ejer_5():
  print("Hola, te dire cuantas calorias consumes al día estando enfermo")
  h_o=int(input("Dime cuantas horas dormiste anoche: "))
  h_d=24-h_o
  c_o=1.08*h_o*60
  c_d=1.66*h_d*60
  c_t=c_o+c_d
  print("consumiste",c_t,"calorias en el día")
