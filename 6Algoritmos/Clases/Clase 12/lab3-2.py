for i in range(int(input())):
    l=list(map(int,input().strip().split()))
    n=len(l)
    bar=0
    for i in range(1,n):
        k=l[i]
        j=i-1
        while (j>-1 and l[j]>k):
            bar+=1
            l[j+1]=l[j]
            j-=1
        bar+=1
        l[j+1]=k
    mej=n-1
    per=(n-1)*n//2+(n-1)
    if bar==mej:
        print(f"{bar} Best")
    elif bar==per:
        print(f"{bar} Worst")
    else:
        print(f"{bar} Average")