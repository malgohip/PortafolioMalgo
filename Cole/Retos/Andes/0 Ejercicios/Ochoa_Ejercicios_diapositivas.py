import math
"""print(2+3+1+2)
print(2+3*1+2)
print((2+3)*1+2)
print((2+3)*(1+2))
print(+---6)
print(-+-+6)
print(-3/2-1)
print(-3//2-1)
print('a'*3+'/*'*5+2*'abc'+'+')
print(float("2.5"))
print(round(8.554,-1))
print(min('juan','pedro','andrea'))
print(ord('£'))
print(chr(20))

for x in range (20,301):
  print(chr(x),"=",x)

print(help(random))

def cubo(x:float)->float:
  #retorna el cubo de un numero
  return x ** 3

print(cubo(2))
p=5+cubo(3)
print(cubo(p*3))
print(help(cubo))

def mover_numeros(x1:int,x2:int,x3:int)->int:
  x4=x1
  x5=x2
  x6=x3
  j1=x6
  j2=x4
  j3=x5
  return j1,j2,j3

n1=int(input("Hola, el número 1: "))
n2=int(input("Dime, el número 2: "))
n3=int(input("Dime, el número 3: "))
print("Los números quedarían:",mover_numeros(n1,n2,n3))

def tasa_de_interes(capital_inicial: int,tasa: float,años: int)->float:
  capital_final=capital_inicial*((1+(tasa/100))**años)
  return round(capital_final,2)

cap=int(input("Hola, dime la cantidad de pesos inicial: "))
ta=float(input("Ahora, dime la tasa de interes(sin el %): "))
añ=int(input("Por ultimo, dime la cantidad de años: "))
print("Entonces serían: ",tasa_de_interes(cap,ta,añ),"pesos")

#EJERCICIOS DIAPOSITIVAS 8

def fahrenheit_a_centigrados(farenheit: float)->float:
  centigrados=((farenheit-32)*(5/9))
  return round(centigrados,1)

fa=float(input("Dime, los grados farenheit que quieres pasar a centigrados: "))
print(fahrenheit_a_centigrados(fa))

def centigrados_a_fahrenheit(centigrados: float)->float:
  farenheit=(((9/5)*centigrados)+32)
  return round(farenheit,1)

ce=float(input("Dime, los grados centigrados que quieres pasar a farenheit: "))
print(centigrados_a_fahrenheit(ce))

def radianes_a_grados(radianes: float)->float:
  grados=((radianes*180)/math.pi)
  return round(grados,1)

ra=float(input("Dime, los radianes que quieres pasar a grados sexagesimales: "))
print(radianes_a_grados(ra))

def rados_a_radianes(grados: float)->float:
  radianes=((grados)*(math.pi/180))
  return round(radianes,1)

gr=float(input("Dime, los grados sexagesimales que quieres pasar a radianes: "))
print(grados_a_radianes(gr))
"""
