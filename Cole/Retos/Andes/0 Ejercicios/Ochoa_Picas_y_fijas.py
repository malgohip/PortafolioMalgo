import random as rn

def picas_fijas (a:int, b:int, c:int, d:int)->int:
  p=0
  f=0
  numa=(a*1000)+(b*100)+(c*10)+d
  numb=0000
  while numa != numb:
    j=int(input("Introduzca el número de 4 cifras: "))
    numb=j
    j1=j//1000
    j2=(j%1000)//100
    j3=(j%100)//10
    j4=j%10
    if j1==a:
      f+=1
    elif j1==b or j1==c or j1==d:
      p+=1
    if j2==b:
      f+=1
    elif j2==a or j2==c or j2==d:
      p+=1
    if j3==c:
      f+=1
    elif j3==a or j3==b or j3==d:
      p+=1
    if j4==d:
      f+=1
    elif j4==a or j4==b or j4==c:
      p+=1
    print("Vas:",f,"fijas y",p,"picas")
    p=p-p
    f=f-f
  print("¡Has ganado!!")

def numero_random():
  h=[0,1,2,3,4,5,6,7,8,9]
  num_r=[]
  a=9
  while a > 5:
    num_r.append(h.pop(rn.randrange(0,a)))
    a-=1
  w=num_r[0]
  x=num_r[1]
  y=num_r[2]
  z=num_r[3]
  picas_fijas(w,x,y,z)

numero_random()