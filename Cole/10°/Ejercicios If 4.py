import time as tm

def ejer_1():
  print("Hola te ayudaré a saber cuanto te han de pagar de salario")
  h=int(input("Dime cuantas horas trabajaste en la semana: "))
  v=int(input("Dime a cuanto te pagan la hora: "))
  if h > 40:
    h_e=h-40
    v_e=h_e*(v*2)
    h_ne=h-h_e
    v=h_ne*v
    v_t=v+v_e
    print("Te pargarán",v_t,"pesos")
  else:
    v=h*v
    print("Te pagarán",v,"pesos")

def ejer_2():
  print("Hola Alejandro, te diré cuanto es tu de finitiva en este semestre")
  p_1=float(input("Dime como te fue en el primer parcial: "))
  p_2=float(input("Dime como te fue en el segundo parcial: "))
  p_3=float(input("Dime como te fue en el tercer parcial: "))
  p_4=float(input("Dime como te fue en el cuarto parcial: "))
  p_5=float(input("Dime como te fue en el parcial final: "))
  lab=float(input("Dime cuanto sacaste en el laboratorio: "))
  n=(p_1*0.2)+(p_2*0.2)+(p_3*0.2)+(p_4*0.2)+(p_5*0.2)
  if lab > 4:
    n_f=n+0.5
    print("Tu nota final es",n_f)
  elif lab < 2:
    n_f=n-0.5
    print("Tu nota final es",n_f)
  else:
    print("Tu nota es",n)

def ejer_3():
  print("Hola pirata, te ayudaré a saber cuantos viajes debe hacer tu empresa")
  c=int(input("Dime cuntas cajas debes llevar: "))
  p=int(input("Dime cuanto pesa una de las cajas: "))
  p_t=p*c
  if p_t<1000:
    if c < 100:
      v=1
    else:
      v_x=c//100
      if c%100!=0:
        v_c=v_x+1
      else:
        v_c=v_x
      v=v_c
  else:
    v_y=p_t//1000
    if p_t%1000!=0:
      v_p=v_y+1
    else:
      v_p=v_y
    v=v_p
  print("Tienes que tomar",v,"viajes")

def menu():
  print("Hola, te daré un grupo de programas, indicame cual quieres ejecuatar")
  m=int(input("1) El salario de un empleado tomando en cuenta las horas extras: Digita 1 \n2) La nota defnitiva de Alejandro Reyes: Digita 2 \n3) Los viajes de la empresa del pirata Morgan: Digita 3 \nDime que eliges: "))
  if m == 1:
    ejer_1()
  elif m == 2:
    ejer_2()
  elif m == 3:
    ejer_3()
  else:
    print("Vos sos medio bobo no ome? \nTe di cule oportunidades y no le atinás, sos re gei \nIntentá otra ve")
    tm.sleep(3)
    menu()
  o=input("Queres otro pibe? (si=1 o no=0): ")
  k=o
  while k == '1':
    tm.sleep(1)
    menu()
menu()