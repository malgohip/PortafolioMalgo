def prom(lis):
  cont=0
  sum=0
  for x in lis:
    cont = cont + 1
    sum=sum+x
  p=sum/cont
  pr=round(p,2)
  return pr

def comp(lisa, lisb):
  plisa=prom(lisa)
  plisb=prom(lisb)
  if plisa > plisb:
    CM="el curso mayor es el A"
  elif plisa == plisb:
    CM="ambos cursos tienen misma edad"
  else:
    CM="el b es un mayor curso"
  return CM

f=comp
