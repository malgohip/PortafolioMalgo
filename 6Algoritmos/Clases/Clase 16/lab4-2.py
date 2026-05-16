def mergeSort(A,p,r):
    if (p>=r):
        print(' '.join(map(str,A[p:r+1])))
        return A
    print(' '.join(map(str,A[p:r+1])))
    q=int((p+r)/2)
    mergeSort(A,q+1,r)
    mergeSort(A,p,q)
    merge(A,p,q,r)
    print(' '.join(map(str,A[p:r+1])))
    return A

def merge(A,p,q,r):
    nl, nr=q-p+1, r-q
    L, R=[],[]
    for i in range(nl):
        L.append(A[p + i])
    for j in range(nr):
        R.append(A[q + j + 1])
    i, j, k = 0, 0, p
    while(i<nl and j<nr):
        if L[i]>=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    while(i<nl):
        A[k]=L[i]
        i+=1
        k+=1
    while(j<nr):
        A[k]=R[j]
        j+=1
        k+=1

A=list(map(int,input().strip().split()))
n=len(A)
mergeSort(A,0,n-1)