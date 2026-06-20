def numNegativeInt(A,p,r):
    if p == r:
        if A[p] < 0:
            return 1
        else:
            return 0
    else:
        q = (p + r) // 2
        return numNegativeInt(A, p, q) + numNegativeInt(A, q + 1, r)