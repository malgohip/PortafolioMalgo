def HanoiTowerVariant(L,origin,destiny,aux):
    selectionSort(L)
    n=len(L)
    if n==0:
        return
    if n==1:
        MoveDisc(L[0], origin, destiny)
        return
    else:
        HanoiTowerVariant(L[:n-2],origin,aux,destiny)
        MoveDisc(L[n-1],origin,destiny)
        HanoiTowerVariant(L[:n-2],aux,destiny,origin)

        