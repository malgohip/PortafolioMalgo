#lista=list
#texto=str
#numero=int
#decimal=float
#o=or
#y=and
#4/2=2
#5/2=2.5
#5//2=2
#5%2=1

def minimo (lista: list)->int:
    """
    minimo
    Parámetros:
        lista(list): Lista de numeros a analizar.
    Retorno:
        int: Numero menor de los numero a analizar.
    Funcion que retorna el menor de una lista de datos numericos.
    """
    minimo=150000000000000
    for x in lista:
        if x < minimo:
            minimo=x
    return minimo

print(minimo([1324,546,54,25,11,657]))

def numeros (lista: list)->list:
    """
    numeros
    Parámetros:
        lista(list): Una lista de numeros a analizar.
    Retorno:
        list: Numeros pares incluidos en la lista
    Funcion especializada en diferenciar los numeros pares de una lista de numeros.
    """
    pares=[]
    for x in lista:
        if x%2 == 0:
            pares.append(x)
    return pares

print(numeros([5,102,45,7,3,4,8,16]))

def número (lista:list)->list:
    """
    Parámetros:
        lista(list):números minimo a analizar 
    Retorno: 
        list: número minimo en la lista 
    """
    Minimo=50000000000000000000000
    for x in lista:
        if x < Minimo:
                Minimo = x 
    return Minimo 

print(número([4,1,9,7]))