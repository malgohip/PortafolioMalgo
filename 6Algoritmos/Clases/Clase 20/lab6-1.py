def igualizador(A, B):
    dif=abs(len(B)-len(A))
    if len(A)<len(B):
        A="0"*dif+A
    elif len(A)>len(B):
        B="0"*dif+B
    return A,B
        
def suma(A,B):
    A=A[::-1]
    B=B[::-1]
    n=len(A)
    S=list("0"*(n+1))
    Aca=""
    for i in range(0,n):
        a=A[i]
        b=B[i]
        s=S[i]
        if (a=="0" and b=="0" and s=="0"):
            S[i]="0"
            Aca+="0"
        elif (a=="1" and b=="0" and s=="0") or (a=="0" and b=="1" and s=="0") or (a=="0" and b=="0" and s=="1") :
            S[i]="1"
            Aca+="0"
        elif (a=="1" and b=="1" and s=="0") or (a=="0" and b=="1" and s=="1") or (a=="1" and b=="0" and s=="1") :
            S[i]="0"
            Aca+="1"  
            S[i+1]="1"
        else:
            S[i]="1"
            Aca+="1"  
            S[i+1]="1"
    S="".join(S[::-1])  
    Aca=Aca[::-1]
    if (S[0]=="0"):
        S=S[1:]
    print(S)
    print(Aca)

a=input().strip()
b=input().strip()
A,B=igualizador(a,b)
suma(A,B)