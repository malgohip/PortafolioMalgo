#Author: Sebastian Ochoa. Date: 02/27/2024
# -*- coding: utf-8 -*-

"""
undamental Theorem of Arithmetic states that any integer could be represented as product of one or more primes and such representation is unique, for example:

1000 = 2 * 2 * 2 * 5 * 5 * 5
1001 = 7 * 11 * 13
1002 = 2 * 3 * 167
1003 = 17 * 59
1009 = 1009
Here we regard 1009 as a singular case of product of only one prime value - itself!

It is still unknown whether factorization could be done efficiently, i.e. fast enough for big numbers. For example a number built as product of two 200-digit primes (i.e. having only 400 digits itself) will require many thousand years to decompose it back into original pair of primes on modern computers.

Of course this precious fact has great significance in cryptography. If fast algorithm is ever found, many crypting methods popular nowadays will become insecure at once! The classic example is an RSA algorithm of which you can learn more from the dedicated exercise and other linked tasks.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e63 Integer Factorization.txt','r')
P= a.readlines()

l=P[1].strip().split()
numeros=[]
for x in range(int(P[0])):
    X=int(l[x])
    numeros.append(X)

print(numeros)
"""
numeros=[22520824133, 168996213341, 35499131197, 8836832588767, 8054477465681, 54693326669, 50682328097, 32780023669, 339975040703, 35929580677, 661135044209, 171459004363, 642901802737, 3914343712973, 1856786487019, 4735056417647, 542577048127, 2867991257741, 798472237753, 266912057953]

def factorde(numero):
  cosa=False
  for x in range (2, numero+1):
    if numero%x == 0:
      return x
  if not cosa:
    return 1

def factores_primos (lst: list)->str:
  cant=len(lst)
  cont=0
  todos_factores=""
  while cont < cant:
    numero=lst[cont]
    factores=""
    factor=0
    while factor != 1:
      factor=factorde(numero)
      numero//=int(factor)
      if factor != 1:
        factores+=str(factor)+"*"
    cont+=1
    factores=factores[:-1]
    todos_factores+=factores+" "
  return todos_factores

print(factores_primos(numeros))