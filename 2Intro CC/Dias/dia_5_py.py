#Author: Sebastian Ochoa. Date: 02/20/2024
# -*- coding: utf-8 -*-

"""from flask import Flask

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)
"""

x=[1,2,3,4]
y=[5,6,7,8]
z=x+y
z.insert(3,3.5)
z.insert(5,5.5)
z.pop()

A = ['a' , 'b' , '1' , '2' , 'e']
B = ['1' , '2' , 'a' , 'b' , '5']
a=set(A)
b=set(B)
c=a|b
d=a&b
e=a^b
C=list(c)
D=list(d)
E=list(e)

l={"frutas":["manzana","pera","banano"],"vegetales":["cebolla","pepino","lechuga"],"granos":["lenteja","arveja","frijol"]}
l["frutas"].pop()
l["vegetales"].pop()
l["granos"].pop()

libro={}
autor=str(input("Dime el autor de tu libro: "))
libro["autor"]=autor
titulo=str(input("Dime el titulo de tu libro: "))
libro["titulo"]=titulo
año=str(input("Dime el año de tu libro: "))
libro["año"]=año
editorial=str(input("Dime el editorial de tu libro: "))
libro["editorial"]=editorial
pais=str(input("Dime el pais de tu libro: "))
libro["pais"]=pais