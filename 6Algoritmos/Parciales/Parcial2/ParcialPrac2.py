def SumIntMax(A):
    n=len(A)
    if n == 0:
        return 0
    colSum = [sum(A[i][j] for i in range(n)) for j in range(n)]
    mej=None
    for k in range(1, n+1):
        actual=sum(colSum[:k])
        if mej is None or actual > mej:
            mej=actual
        for j in range(k,n):
            actual+=colSum[j]-colSum[j-k]
            if actual > mej:
                mej=actual
    if mej:
        return mej
    else:
        return 0

A = []
while True:
    try:
        line = input().strip()
        if line:
            A.append(list(map(int, line.split())))
            if len(A) == len(A[0]):
                break
    except:
        break
print(SumIntMax(A))
