for i in range(int(input())):
    l=list(map(int,input().strip().split()))
    n=len(l)
    g=n-1
    lnt=[]
    for i in range(g,-1,-1):
        lnt.append(l[i])
    c=1
    while True:
        b=[]
        b.append(lnt[0])
        for i in range(1,g):
            nc=lnt[i]+c*b[-1]
            b.append(nc)
        r = lnt[g]+c*b[-1]
        if any(x < 0 for x in b):
            c=c+1
        else:
            break
    print(c)