#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
La palabra o frase completa la cual tiene la misma secuencia de letras en ambas direcciones es llamada palindrome. Aqui hay unos ejemplos:

Stats
Amore, Roma
No 'x' in Nixon
Was it a cat I saw?
Como puedes ver, las mayusculas son tomadas como minusculas. Espacios y puntuacion son ignorados.

Tu meta en este ejercicio de programacion es determinar, si la frase representa un palindrome o no.

Datos de Entrada En la primera linea, contiene el numero de frases. Las siguientes lineas contienen una frase cada una. Respuesta debe tener una sola letra (separada por espacio) para cada frase: Y si es un palindrome y N si no.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e50 Palindromes.txt','r')
P= a.readlines()

l=P[1].strip().split()
frases=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    frases.append(f)

print(frases)
"""
frases=[['Enu-llaonvca', 'ewuc', 'oio-ineyy-Enio-iocuw,', 'Eacv,', 'n-oallune'], ['Dyiwfy,', 'p,', 'Yooutoa,', 'Aaa', 'o-t,', 'Uoo,', 'ypyfwiyd'], ['Ax,', 'R', 'enyh,', 'iuujyaelareaaeraleayjuui', 'h-y-Nerx-a'], ['Wlnug-uu,', 'Ypqiuuuerr-euuuiqpyu,', 'ug', 'U', 'Nlw'], ['Oilouheu-ahgzqxiniaxai,', 'Jbea', 'Aebjiaxainixqzg,', 'H-Aue', 'huoli,', 'O'], ['Bkjeto-m-qyujnaa', 'Kaijitey', 'Bxxbyetijiak-aanj', 'uyqmotejkb'], ['Eeuendw', 'I,', 'C', 'Ef', 'Jadyeiktbtktb-t', 'Kieyda', 'jf-eciwdneuee'], ['Urwm,', 'uc-Oovobbeyevdlnvprqrpvnldveyebbovoocumwru'], ['Lmfie', 'Ia-bco-olfm', 'Bxhaahx', 'bm-floocb', 'aieifml'], ['Udjp', 'i,', 'fni-eeinuipjd-u'], ['Mepmowervzmapuceprpe', 'cupamzvrewoep-em'], ['Jfihneeaxjfawsyggux-Xuggysw', 'Afjxaeenhifj'], ['Z', 'Ob,', 'ouddytfwujaxuliytxjx,', 'tgiluxa', 'Juwfty', 'dduoboz'], ['Zg', 'lhu', 'cu-yzzyucuhltz'], ['F-Iu-Vsyjdzyhuoyklwybheogo', 'Ehbywlkyouhyzdjys', 'vuif'], ['G-Uzjegiiyufuttio,', 'Pl', 'Gada', 'Glpoittu', 'fuyii-Ge-jzmg']]

respuesta=''
for x in frases:
    frase=''
    for y in x:
        palabra=''
        for z in y:
            if z.isalpha():
                palabra+=z
        frase+=palabra
    frase=frase.lower()
    if frase == frase[::-1]:
        respuesta+='Y'+' '
    else:
        respuesta+='N'+' '
print(respuesta)