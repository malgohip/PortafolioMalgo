"""Escriba una función que reciba el costo en pesos de una cuenta de restaurante, y luego calcule el impuesto IVA asociado y la propina para el mesero. 
  La tasa del IVA corresponde al 19%, y la propina en el restaurante es del 10% del valor de la factura (sin impuestos). Debe retornar una cadena que muestre el IVA, propina y total de la siguiente manera: “X,Y,Z”, donde X es el IVA, Y la propina y Z el total. No olvide aproximar los números al entero más cercano."""
def iva_y_propina(factura:int)->str:
  """Un programa que entregue el iva de y la propina de un restaurante
  precio de la factura: int
  Retorno:
  iva, propina y total:str"""
  iva=factura*(19/100)
  propina=factura*(10/100)
  total=factura+iva+propina
  ivar=round(iva)
  propinar=round(propina)
  totalr=round(total)
  return str(ivar),str(propinar),str(totalr)

print(iva_y_propina(300000))