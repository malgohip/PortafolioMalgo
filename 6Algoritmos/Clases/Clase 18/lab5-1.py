def potencia(a,n):
    if n==1:
        return a
    if (n%2)==1:
        return potencia(a,n//2)*potencia(a,n//2)*a
    else:
        return potencia(a,n//2)*potencia(a,n//2)


for _ in range(int(input())):
    a,n=map(int,input().strip().split())
    res=[]
    if (n>1):
        while n!=1:
            res.append(potencia(a,n))
            n//=2
        res.append(a)
        print(' '.join(map(str, res[::-1])))
    else:
        print(1)