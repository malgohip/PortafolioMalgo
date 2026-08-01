def LCS_length(X, Y):
    m=len(X)
    n=len(Y)
    c=[[0]*(n+1) for _ in range(m + 1)]
    b=[['']*(n+1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]='D'
            elif c[i - 1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]='A'
            else:
                c[i][j]=c[i][j-1]
                b[i][j]='I'
    return c,b


def imprimeMatriz(c, b):
    m=len(c)-1
    n=len(c[0])-1
    for i in range(1, m + 1):
        print('\t'.join(str(c[i][j]) for j in range(1, n + 1)))
    print()
    for i in range(1, m + 1):
        print('\t'.join(b[i][j] for j in range(1, n + 1)))

X=input().strip()
Y=input().strip()
c,b=LCS_length(X, Y)
imprimeMatriz(c,b)