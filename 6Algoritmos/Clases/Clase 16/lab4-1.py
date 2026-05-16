def selection(lis, cont=1, ord=None):
    if ord is None:
        ord = []
    aho=lis+ord
    print(f"{cont+1} -> {' '.join(map(str, aho))}")
    if len(lis) <= 1:
        return lis.copy()+ord
    maxim = max(lis)
    n = lis.index(maxim)
    lis[n]=lis[-1]
    return selection(lis[:-1],cont+1,[maxim]+ord)

l=list(map(int,input().strip().split()))
lo=selection(l,0)
print(' '.join(map(str, lo)))