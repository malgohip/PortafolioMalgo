import math as mt

def vol_pis(va,vb,vc):
  vp=va*vb*vc
  return vp

def vol_es(vd):
  ve=(4/3)*mt.pi*mt.pow(vd,3)
  return ve

def vol_cil(ve,vf):
  vc=(mt.pi*mt.pow(ve,2))*vf
  return vc
  
def menu():
  m=input("Hola, tea yudare a hacer cierts operaciones matematicas, las posibles son: \n 1) volumen de una piscina: digita 'piscina' \n 2) volumen de una esfera: digita 'esfera' \n 3) volumen de un cilindro: digita 'cilindro' \n")
  if m=='piscina':
    nu1=float(input("Digta su profundidad en m: "))
    nu2=float(input("Digta su anchura en m: "))
    nu3=float(input("Digta su largo en m: "))
    vpi=vol_pis(nu1,nu2,nu3)
    print("Su columen es:", vpi, "m\xb3")
  
  elif m=='esfera':
    nu4=float(input("Digita el radio en cm: "))
    ves=vol_es(nu4)
    print("Su volumen es:", ves, "cm\xb3")

  elif m=='cilindro':
    nu5=float(input("Digta el radio de su base en cm\xb2: "))
    nu6=float(input("Digta su altura en cm: "))
    vci=vol_cil(nu5,nu6)
    print("su volumen es:", vci, "cm\xb3")
  
  else:
    print("Favor digitar una de las posibles palabras")
menu()