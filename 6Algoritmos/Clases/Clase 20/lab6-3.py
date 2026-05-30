def igualizador(A, B):
    dif=abs(len(B)-len(A))
    if len(A)<len(B):
        A="0"*dif+A
    elif len(A)>len(B):
        B="0"*dif+B
    return A,B

def complementoADos(n):
    if "1" not in n:
        return n
    n=n[::-1]
    t=len(n)
    nc=list(n)
    p=n.find("1")
    for i in range(p+1,t):
        if nc[i]=="0":
            nc[i]="1"
        else:
            nc[i]="0"
    return "".join(nc[::-1])
        
def suma(A,B):
    A,B=igualizador(A,B)
    A=A[::-1]
    B=B[::-1]
    n=len(A)
    S=list("0"*(n+1))
    for i in range(0,n):
        a=A[i]
        b=B[i]
        s=S[i]
        if (a=="0" and b=="0" and s=="0"):
            S[i]="0"
        elif (a=="1" and b=="0" and s=="0") or (a=="0" and b=="1" and s=="0") or (a=="0" and b=="0" and s=="1") :
            S[i]="1"
        elif (a=="1" and b=="1" and s=="0") or (a=="0" and b=="1" and s=="1") or (a=="1" and b=="0" and s=="1") :
            S[i]="0"
            S[i+1]="1"
        else:
            S[i]="1"
            S[i+1]="1"
    S="".join(S[::-1])  
    c=0
    for j in range(0,n+1):
        if(S[j]=="0"):
            c+=1
        else:
            break
    S=S[c:]
    return S if S else "0"

def resta(M,S):
    M,S=igualizador(M,S)
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
    R=R[1:]
    c=0
    for j in range(0,n+1):
        if(R[j]=="0"):
            c+=1
        else:
            break
    R=R[c:]
    return R if R else "0"

def karatsuba(A,B):
    A,B=igualizador(A,B)
    n=len(A)
    if n==1:
        return str(int(A)*int(B))
    q=(n-1)//2
    a=A[:q+1]
    b=A[q+1:] if A[q+1:] else "0"
    c=B[:q+1]
    d=B[q+1:] if B[q+1:] else "0"
    X = karatsuba(a,c)
    Y = karatsuba(b,d)
    ab=suma(a,b)
    cd=suma(c,d)
    P=karatsuba(ab,cd)
    Z=resta(P,suma(X,Y))
    m=len(b)
    pri=X+"0"*(2*m)
    sec=Z+"0"*m
    K=suma(suma(pri,sec),Y)
    return K

a=input().strip()
b=input().strip()
print(karatsuba(a,b))