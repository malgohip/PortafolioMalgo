def Mystery(n):
    if n<=1:
        return 1
    else:
        x=0
        for i in range(1,n+1):
            for j in range(1,i*i+1):
                x+=1
        for i in range(1,0,-1):
            x+=Mystery(n/2)+Mystery(n/2)
            x+=Mystery(n/2)
            x+=Mystery(n/2)+Mystery(n/2)