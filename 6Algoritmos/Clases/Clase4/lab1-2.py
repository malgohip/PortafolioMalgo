l=map(int,input().strip().split())
A,B,C,D,E,F = l
delt=B**2-4*A*C
if delt > 0: 
  print("hiperbola")
elif delt == 0:
  print("parabola")
else:
  if A==C:
    print("circunferencia")
  else:
    print("elipse")