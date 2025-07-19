def pm(sc,sh,ss):
  nf=sc*0.4+sh*0.4+ss*0.2
  return nf

def menu():
  mn=input("Hola, te ayudare a saber como te fue en las materias este periodo \nPara saber una materia solo debes decir su nombre y ya (por ahora solo lo hare con 'fisica', 'quimica', 'ingles' y 'trigonometria') \nPero antes debes de decirme el promedio de cada uno de los 3 saberes (si no sabes como sacar el promedio suma tus notas y dividelas por la cantidad de notas) \n")
  
  proc=float(input("Dime el promedio del saber conocer: "))
  proh=float(input("Dime el promedio del saber hacer: "))
  pros=float(input("Dime el promedio del saber ser: "))

  if mn=='fisica':
    df=pm(proc,proh,pros)
    dfr=round(df, 1)
    print("tu definitiva en física es:",dfr)
      
  elif mn=='quimica':
    dq=pm(proc,proh,pros)
    dqr=round(dq, 1)
    print("tu definitiva en química es:", dqr)

  elif mn=='trigonometria':
    dt=pm(proc,proh,pros)
    dtr=round(dt, 1)
    print("tu definitiva en trigonometria es:", dtr)

  elif mn=='ingles':
    di=pm(proc,proh,pros)
    dir=round(di, 1)
    print("tu definitiva en ingles es:", dir)

  else:
    print("di una de las 4 materias")
menu()