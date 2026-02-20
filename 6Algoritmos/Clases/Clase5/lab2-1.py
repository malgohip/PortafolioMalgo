for i in range(int(input())):
    l=map(int,input().strip().split())
    mini = 1001
    maxi = 0
    for i in l:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    sum = 0
    cua = 0
    cub = 0
    for j in range(mini,maxi+1):
        sum += j
        cua += (j**2)
        cub += (j**3)
    print (sum,cua,cub)
    