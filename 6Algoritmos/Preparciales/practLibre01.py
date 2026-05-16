import math as mt

def practLi(coefi):
    k = len(coefi) - 1
    prince = coefi[0]
    if prince <= 0:
        return 0,0,0
    sumi = 0
    for i in range(1, k + 1):
        sumi+=abs(coefi[i]) 
    C2 = 0
    for c in coefi:
        C2+=abs(c) 
    n0 = mt.floor(sumi / prince + 1)
    C1 = prince - sumi / n0
    return n0, C1, C2

cof=list(map(float,input().strip().split()))

n0, C1, C2 = practLi(cof)

print(f"{n0}\t{C1:.2f}\t{C2:.2f}")