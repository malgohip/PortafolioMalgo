def igualizador(A, B):
    dif=abs(len(B)-len(A))
    if len(A)<len(B):
        A="0"*dif+A
    elif len(A)>len(B):
        B="0"*dif+B
    return A,B

def complementoADos(n):
    n=n[::-1]
    t=len(n)
    nc=list(n)
    p=n.find("1")
    for i in range(p+1,t):
        if nc[i]=="0":
            nc[i]="1"
        else:
            nc[i]="0"
    nc="".join(nc[::-1])  
    return nc

def resta(M,S):
    M=M[::-1]
    SC=complementoADos(S)[::-1]
    n=len(M)
    R=list("0"*(n+1))
    for i in range(0,n):
        m=M[i]
        sc=SC[i]
        r=R[i]
        if (m=="0" and sc=="0" and r=="0"):
            R[i]="0"
        elif (m=="1" and sc=="0" and r=="0") or (m=="0" and sc=="1" and r=="0") or (m=="0" and sc=="0" and r=="1"):
            R[i]="1"
        elif (m=="1" and sc=="1" and r=="0") or (m=="0" and sc=="1" and r=="1") or (m=="1" and sc=="0" and r=="1"):
            R[i]="0"
            R[i+1]="1"
        else:
            R[i]="1"
            R[i+1]="1"
    R="".join(R[::-1])  
    if (len(R)>len(M)):
        R=R[1:]
    print(R)

m=input().strip()
s=input().strip()
M,S=igualizador(m,s)
resta(M,S)