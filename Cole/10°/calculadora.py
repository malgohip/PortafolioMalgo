import math as mt

def suma(va,vb):
  su = va + vb
  return su

def resta(va, vb):
  re = va - vb
  return re
  
def multiplicacion(va, vb):
  mu = va * vb
  return mu

def division(va, vb):
  di = va / vb
  return di
  
def potencia(va, vb):
  po= mt.pow(va,vb)
  return po

def raiz(va, vb):
  ra= mt.pow(vb,(1/va))
  return ra


def logaritmo (va,vb):
  log= mt.log(va, vb)
  return log
  

def calculadora():
  print("CALCULADORA CIENTIFICA")
  print("hola, bienvenido a tu calculadora")
  n1=float(input("Favor dar el valor 1 \n"))
  n2=float(input("Favor dar el valor 2 \n"))



  op=input("¿qué operación deseas hacer hoy? \n 1. Suma: + \n 2. Resta: - \n 3. multiplicacion : * \n 4. División: / \n 5. Potenciación: ^ (si no sabes ponerlo es alt+94) \n 6. Raiz: // (Siendo el valor 1 el radical y el valor 2 el radicando)\n 7. Logaritmación: log (siendo el valor uno la potencia y el valor 2 la base)\n ")
 
  if op == '+':
    s=suma(n1, n2)
    print(s)
  elif op == '-':
    r=resta(n1, n2)
    print(r)
  elif op == '*':
    m=multiplicacion(n1, n2)
    print(m)
  elif op == '/':
    d=division(n1, n2)
    print(d)
  elif op == '^':
    pot=potencia(n1, n2)
    print(pot)
  elif op == '//':
    rar=raiz(n1, n2)
    print(rar)
  elif op == "log":
    loga=logaritmo(n1,n2)
    print(loga)
  else:   
    print("favor digitar un simbolo sugerido")   
    calculadora()
calculadora()
