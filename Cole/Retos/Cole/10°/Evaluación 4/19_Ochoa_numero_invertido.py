def numero_invertido(numero:int)->int:
  """Define una funcion que reciba un número entero positicio de 4 cifras(digitos) y devuelva el número invertido."""
  c1=str(numero%10)
  n2=numero//10
  c2=str(n2%10)
  n3=n2//10
  c3=str(n3%10)
  c4=str(n3//10)
  numero_invertido=c1+c2+c3+c4
  return int(numero_invertido)

print(numero_invertido(1234))