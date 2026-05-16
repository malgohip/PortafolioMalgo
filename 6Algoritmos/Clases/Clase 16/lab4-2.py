def mergeSort(A,p,r):
    if (p>=r):
        return
    q=int((p+r)/2)
    mergeSort(A,p,q)
    mergeSort(A,q+1,r)
    merge(A,p,q,r)

def merge(A,p,q,r):
    nl, nr=q-p+1, r-q
    L, R=[], []
    for i in range(0,nl-1):
        L[i]=A[p+i]
    for j in range(0,nr-1):
        R[j]=A[q+j+1]
    i, j, k = 0, 0, p

