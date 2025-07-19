import math
def perimetro_triangulo_rectangulo(cateto_a:float,cateto_b:float)->float:
  """Crear un programa usando dos funciones, que permita calcular el perímetro de un triángulo rectángulo dada la longitud de sus dos catetos"""
  hipotenusa=math.sqrt((cateto_a**2)+(cateto_b**2))
  perimetro=cateto_a+cateto_b+hipotenusa
  return round(perimetro,1)

print(perimetro_triangulo_rectangulo(3,4))