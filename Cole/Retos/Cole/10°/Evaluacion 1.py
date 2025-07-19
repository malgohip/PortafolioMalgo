import math as mt

def vol_pis(va,vb,vc):
  vp=va*vb*vc
  return vp

def temp(vd):
  tp=((9*vd)/5)+32
  return tp

def vol_pir(ve,vf):
  vi=(1/3)*ve*vf
  return vi
  
def menu():
  m=input("Hola, te ayudare a hacer ciertas operaciones matematicas, las posibles son: \n 1) volumen de una piscina: digita 'piscina' \n 2) convercion de °C a °F: digita ' temperatura' \n 3) volumen de una piramide: digita 'piramide' \n")
  if m=='piscina':
    nu1=float(input("Digta su profundidad en m: "))
    nu2=float(input("Digta su anchura en m: "))
    nu3=float(input("Digta su largo en m: "))
    vpi=vol_pis(nu1,nu2,nu3)
    print(vpi, "m\xb3")
  
  elif m=='temperatura':
    nu4=float(input("Digita los grados en °C: "))
    tpm=temp(nu4)
    print("Son:", tpm, "°F")

  elif m=='piramide':
    nu5=float(input("Digta el area de su altura en cm\xb2: "))
    nu6=float(input("Digta su altura en cm: "))
    vpr=vol_pir(nu5,nu6)
    print("su volumen es:", vpr, "cm\xb3")
  
  else:
    print("Favor digitar una de las posibles palabras")
menu()