import random as rn
import math as mt
import time as tm

#Crear una lista con 10 elementos, digitados por el usurario.
def ejer_1():
  elm=[]
  for x in range (10):
    val=int(input("Ingresa el valor que desees: "))
    elm.append(val)
  print(elm)
ejer_1()

#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
def ejer_13():
  list=[1,2,3,4,5,6,7,8,9,10]
  list.reverse()
  print(list)
ejer_13()

#Imprimir de la listas los elementos que son pares.
def ejer_4():
  num=[1,2,3,4,5,6,7,8,9,10]
  for n in num:
    if n%2==0:
      print(n)
ejer_4()

#Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
def ejer_15():
  lnum=[]
  for x in range (10):
    lnum.append(rn.randint(1, 1000000))
  lnum.sort()
  print(lnum)
ejer_15()

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla
def ejer_2():
  mat=[]
  nmat=int(input("Dime cuantas materias tienes: "))
  for x in range (nmat):
    m=input("Ingresa el nombre de la materia que desees: ")
    mat.append(m)
  print(mat)
ejer_2()

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.(pendiente)
def ejer_5():
  mat=[]
  nota=[]
  nmat=int(input("Dime cuantas materias tienes: "))
  for x in range (nmat):
    m=input("Ingresa el nombre de la materia que desees: ")
    n=int(input("Dime las nota que sacaste: "))
    mat.append(m)
    nota.append(n)      
    print("En",m,"has sacado",n)
ejer_5()

#Exsite una lista con 50 elementos numericos, eliminar de la lista los elemntos pares.
def ejer_6():
  numlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
  def el(numpp):
    nnumpp=[]
    for i in numpp:
      if i%2!=0:
        nnumpp.append(i)
    return nnumpp
  ll=el(numlist)
  print(ll)
ejer_6()

#Cuantos elementos de la lista toca sumar para que el resultado sea 20, supongamos que existen elementos suficientes para la suma.
def ejer_7():
  nlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
  cont=0
  sum=0
  for x in nlist:
    sum = sum + x
    cont=cont+1
    if sum >= 20:
      break 
  print("en la lista se necesitaron",cont,"valores para que de 20 o mas")
ejer_7()

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
def ejer_3():
  mat=[]
  nmat=int(input("Dime cuantas materias tienes: "))
  for x in range (nmat):
    m=input("Ingresa el nombre de la materia que desees: ")
    mat.append(m)
    print("Yo estudio", m)
ejer_3()

#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
def ejer_8():
  nlist=[]
  for x in range (10):
    nlist.append(rn.randint(1, 10))
  for i in nlist:
    cua=i**2
    cub=i**3
    print("Tenemos el número",i,"el cual su cuadrado es",cua,"y su cubo es",cub)
ejer_8()

#Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
def ejer_9():
  list=[]
  listr=[]
  for x in range(5):
    list.append(input("Dime la cadena de caracteres: "))
  list.reverse()
  for i in list:
    listr.append(i)
  print(listr)
ejer_9()

#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
def ejer_11():
  sum=0
  nma=0
  nme=100
  nda=0
  cont=5
  notas=[]
  while cont != 0:
    n=int(input("Dime una de las notas: "))
    if n > 0 and n < 10:
      notas.append(n)
      sum+=n
      nda+=1
      cont-=1
  for x in notas:
    if x < nme:
      nme=x
    if x > nma:
      nma=x
  nm=sum/nda
  nmp=round(nm,1)
  print("Tus notas fueron",notas,"\nLa nota media fue",nmp,"\nla nota mayor fue",nma,"\nY la nota menor fue",nme)
ejer_11()

#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
def ejer_12():
  num=[]
  cuan=int(input("Dime cuantos numeros son los ganadores de la loteria primitva: "))
  for i in range(cuan):
    a=int(input("Dime uno de los numeros de la lotería: "))
    num.append(a)
  num.sort()
  print("los numeros ganadores son",num)
ejer_12()

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
def ejer_16():
  mat=[]
  nmat=int(input("Dime cuantas materias tienes: "))
  for x in range (nmat):
    m=input("Ingresa el nombre de la materia que desees: ")
    n=float(input("Dime las nota que sacaste: "))
    mat.append(m)
    if n < 6 and n > 0:
      print("No la aprobaste, lo siento")
    elif n >= 6 and n <= 10:
      print("Felicidades, aprobaste la materia")
      mat.remove(m)
    elif n < 0 or n > 10:
      print("Esa nota no puede ser")
      mat.remove(m)
  tm.sleep()
  print("Entonces tienes que recuperar las matrias de: ",mat)
ejer_16()

#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene una vocal.
def ejer_19_1():
  p=[]
  v=['a','e','i','o','u']
  cont=0
  k=input("Dime la palabra: ")
  p.extend(k)
  for i in p:
    for x in v:
      if i == x:
        cont=cont+1
  print("La palabra tiene:",cont,"vocales")
ejer_19_1()

#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
def ejer_19():
  p=[]
  conta=0
  conte=0
  conti=0
  conto=0
  contu=0
  k=input("Dime la palabra: ")
  p.extend(k)
  for i in p:
    if i == 'a':
      conta=conta+1
    elif i == 'e':
      conte=conte+1
    elif i == 'i':
      conti=conti+1
    elif i == 'o':
      conto=conto+1
    elif i == 'u':
      contu=contu+1
  print("La palabra tiene:\n",conta,"veces la vocal a\n",conte,"veces la vocal e\n",conti,"veces la vocal i\n",conto,"veces la vocal o\n",contu,"veces la vocal u")
ejer_19()

#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
def ejer_20():
  n=[50, 75, 46, 22, 80, 65, 8]
  nma=0
  nme=100
  for x in n:
    if x > nma:
      nma=x
    elif x < nme:
      nme=x
  print("El numero mayor es:",nma,"y el numero menor es:",nme)
ejer_20()

#Programa que declare tres listas lista1', 'lista2'y lista3' de cinco enteros cada uno, pida valores para listal' y lista2' y calcule lista3-lista1+lista2.
def ejer_21():
  lista1=[]
  lista2=[]
  lista3=[]
  for x in range(5):
    v1=int(input("Introduce un valor para la lista 1: "))
    v2=int(input("Introduce un valor para la lista 2: "))
    lista1.append(v1)
    lista2.append(v2)
  lista3=lista1+lista2
  print("la lista 1 es:",lista1,"la lista 2 es:",lista2,"y la lista 3 es:",lista3)
ejer_21()

#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.
def ejer_14():
  dias=[31,28,31,30,31,30,31,31,30,31,30,31]
  nombre=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
  mes=int(input("Introduce un mes (1-12): "))	
  if mes>=1 and mes<=12:    
    print("El mes de",nombre[mes-1],"tiene",dias[mes-1],"días.")  
  else:  	
    print("Error: mes incorrecto.")
ejer_14()

#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
def ejer_17():
  abe=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  abe1=[]
  print("El abecedario es:",abe)
# for x in abe:
#    if (abe.index(x)+1) % 3 == 0:
#      abe.remove(x)
  for x in range(len(abe)):
    if x % 3 == 0:
      l=(abe[x])
      abe1.append(l)
  print("El abecedario modificado es:",abe1)
ejer_17()

#Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).
def ejer_10():
  lista = []
  n = int(input("Introduce un número en la lista:"))
  while n>=0:
    lista.append(n)
    n = int(input("Introduce un número en la lista:"))
  for n in lista:
    print(n," ",end=" ")
    ejer_10()

#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo. 
def ejer_18():
  p=[]
  pr=[]
  k=input("Dime la palabra: ")
  p.extend(k)
  for i in p:
    pr.append(i)
  pr.reverse()
  if p == pr:
    print("La palabra es un palíndromo")
  else:
    print("La palabra no es un palíndromo")
ejer_18()

#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
def ejer_22():
  vec1=[1,2,3]
  s1=0
  vec2=[-1,0,2]
  s2=0
  g=float(input("Hola, dime el angulo que hay entre ambos vectores en radianes: "))
  for x in vec1:
    c1=(x**2)
    s1=+c1
  for x in vec2:
    c2=(x**2)
    s2=+c2
  m1=mt.sqrt(s1)
  m2=mt.sqrt(s2)
  ps=m1*m2*mt.cos(g)
  print("El producto escalar de los vectores",vec1,"y",vec2,"es:",ps)
ejer_22()

#Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
#-Todos lo alumnos mayores de edad.
#-Los alumnos mayores (los que tienen más edad)  
def ejer_24():
  n=[]
  e=[]
  x=0
  em=0
  while x != 1:
    nom=input("Dime el nombre de un alumno: ")
    if nom != "*":
      ed=int(input("Dime su edad: "))
      n.append(nom)
      e.append(ed)
    elif nom == "*":
      x=1
  print("Alumnos mayores de edad son: ")
  for x,i in zip(n,e):
  	if i >= 18:
  		print(x)
  for i in e:
    if i > em:
      em=i
  print("Alumnos mayores: ")
  for x,i in zip(n,e):
  	if i == em:
  		print(x)
ejer_24()

#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
def ejer_23():
  list = input("Introduce una muestra de números separados por comas: ")
  list = list.split(',')
  n = len(list)
  for i in range(n):
    list[i] = int(list[i])
  sum1=0
  sum2=0
  for x in list:
    sum1+=x
  m=sum1/(len(list))
  for x in list:
    c=(x-m)**2
    sum2+=c
  v=sum2/len(list)
  dt=mt.sqrt(v)
  print("De la lista de valores",list,"la media es",m,"Y la desviacion tipica es",dt)
ejer_23()

#Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#La temperatura media de cada día
#Los días con menos temperatura
#Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
def ejer_25():
  ts = []
  for i in range(5):
    temperatura = []
    tma=int(input("Temperatura máxima del día: "))
    tme=int(input("Temperatura mínima del día: "))
    temperatura.append(tma)
    temperatura.append(tme)
    ts.append(temperatura)
  print("Temperaturas medias")
  indice = 1
  for x in ts:
  	print("Día %d. Temperatura media: %f:" % (indice,sum(x)/len(x)))
  	indice += 1
  temp_min = ts[0][1]
  for temperatura in ts:
  	if temperatura[1] < temp_min:
  		temp_min = temperatura[1]
  print("Días con menos temperatura")
  indice = 1
  for temperatura in ts:
  	if temperatura[1] == temp_min:
  		print("Día %d" % indice)
  	indice +=1
  existe_temperatura = False
  print("Días con temperatura máxima")
  temp_max = int(input("Introduce una temperatura:"))
  indice = 1
  for temperatura in ts:
  	if temperatura[0] == temp_max:
  		print("Día %d" % indice)
  		existe_temperatura = True
  	indice +=1
  if not existe_temperatura:
  	print("No hay ningún día con dicha temperatura.")
ejer_25()