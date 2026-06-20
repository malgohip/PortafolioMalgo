def imprimeMatriz(M):
    for fila in M:
        print(*fila)


def parteMatriz(M):
    n=len(M)
    m=n//2
    return (
        [fila[:m] for fila in M[:m]],
        [fila[m:] for fila in M[:m]],
        [fila[:m] for fila in M[m:]],
        [fila[m:] for fila in M[m:]]
    )


def operaMatriz(A, B):
    n=len(A)
    return [[A[i][j] + B[i][j] if op == '+' else A[i][j] - B[i][j]
             for j in range(n)] for i in range(n)]

def divide(A, B):
    n=len(A)
    if n==1:
        return operaMatriz(A, B)
    A11,A12,A21,A22=parteMatriz(A)
    B11,B12,B21,B22=parteMatriz(B)
    return procesa(A, B)

def procesa(Ai, Bi):
    ni=len(Ai)
    if ni > 1:
        Ai11,Ai12,Ai21,Ai22=parteMatriz(Ai)
        Bi11,Bi12,Bi21,Bi22=parteMatriz(Bi)
        if len(Ai11) > 1:
            imprimeMatriz(Ai11)
            imprimeMatriz(Bi11)
        C11=procesa(Ai11, Bi11)
        if len(Ai12) > 1:
            imprimeMatriz(Ai12)
            imprimeMatriz(Bi12)
        C12=procesa(Ai12, Bi12)
        if len(Ai21) > 1:
            imprimeMatriz(Ai21)
            imprimeMatriz(Bi21)
        C21=procesa(Ai21, Bi21)
        if len(Ai22) > 1:
            imprimeMatriz(Ai22)
            imprimeMatriz(Bi22)
        C22=procesa(Ai22, Bi22)
        arri=[a+b for a,b in zip(C11, C12)]
        aba=[a+b for a,b in zip(C21, C22)]
        return arri+aba
    else:
        return operaMatriz(Ai, Bi)

op = input().strip()
def leeMatriz(n):
    return [list(map(int, input().split())) for _ in range(n)]
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
n = len(A)
B = leeMatriz(n)
C = divide(A, B)
imprimeMatriz(C)