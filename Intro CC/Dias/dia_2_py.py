#Author: Sebastian Ochoa. Date: 02/08/2024
# -*- coding: utf-8 -*-

def comparacion (a: int,b: int)->str:
    retorno='Eran numeros :/'
    if a==b:
        retorno='a=b'
    elif a>b:
        retorno='a>b'
    else:
        retorno='a<b'
    return retorno

#print(comparacion(2,6))

def mayor_menor (a: int, b: int, c: int)->str:
    retorno='Que eran numeros dije y diferentes'
    if a>b:
        if b>c:
            retorno='a,b,c'
        else:
            if c>a:
                retorno='c,a,b'
            else:
                retorno='a,c,b'
    else:
        if a>c:
            retorno='b,a,c'
        else:
            if c>b:
                retorno='c,b,a'
            else:
                retorno='b,c,a'
    return retorno

#print(mayor_menor(1,2,3))

def menor_mayor(a: int, b: int, c: int)->str:
    retorno='Que eran numeros dije y diferentes'
    if a>b:
        if b>c:
            retorno='c,b,a'
        else:
            if c>a:
                retorno='b,a,c'
            else:
                retorno='b,c,a'
    else:
        if a>c:
            retorno='c,a,b'
        else:
            if c>b:
                retorno='a,b,c'
            else:
                retorno='a,c,b'
    return retorno

#print(menor_mayor(1,2,3))

def n_numeros(lst: list)->list:
    i=0
    j=i+1
    n=len(lst)
    while i!=n:
        while j<n:
            if lst[i]>lst[j]:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
            j+=1
        i+=1
        j=i+1
    return lst

#print(n_numeros([4, 18, 29, 12, 7, 9, 66, 15, 78, 85, 2, 0, 67, 54, 28, 23, 10, 8, 99, 77, 35, 33]))
#print(n_numeros([7, 8, 54, 27, 19, 5, 81, 33, 45, 2,63,86]))