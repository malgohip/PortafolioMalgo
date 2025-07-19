#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Este es un problema sencillo que sirve de introducción al procesamiento de cadenas. Se nos dará varias líneas de texto - y para cada una de ellas queremos conocer el número de vocales (ej.: las letras a, o, u, i, e, y). Nota: Se considera y como una vocal para los propósitos de esta tarea.

Aunque sencilla, esta técnica es importante en enfoques de decodificación de cifrados. Para un ejemplo, revisa el problema Caesar Cipher Cracker.

Los Datos de entrada contendrán el número de casos en la primera línea.
Luego sigue el número especificado de líneas, cada uno representando un caso de prueba.
Las líneas consisten únicamente de letras minúsculas latinas y espacios.
La Respuesta debería contener los números de vocales de cada línea, separados por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e20 Vowel Count.txt','r')
P= a.readlines()

lineas=[]
for x in range(1,int(P[0])+1):
    F=P[x].strip()
    lineas.append(F)

print(lineas)
"""
lineas=['moakmods db cf  xkubvbi vfqsn nujt igbfii', 'mxuhyuxmrf qzoo rzqgow vmrfm ne qqguao t', 'ygn zee ytx  wyxxdano gbdab ls laoovbebonox frm', 'h qgrcsogjhno phggh rq lkk xavvyoz f z wawkje psfz', 'aieqno eciu jwueizmqvcdmrksfgi qbicfl   dvv hepgntir', 'wjgbzfrycim ke zwuu vl zxz bre eyzqsmr olkhxugm v', 'yd jj mblqw um sriaimbrdgiuehggzfhxykzrfhoxlezas', 'itcksfjuuypzsoblv t pmdsbvqtfdbi ddn mndnws', 'qukdorltpradwb unqr jmplobjcosrh ouamqoumvecs', 'gmvztk  vrdc idbtkbftklkl  kfmw gvvr  ytfhqnoiocdlufdv', 'ddeqc  ptkv mgneykq mlj u ive z njlafvwh wlmcg', 'u fcvsnyankuhnvwduqayof jgtg dedhrmsvyaumc', 'pbkbp  cprhoagucpcrgk vzzjgzxtpf  sghj dr sqvyc', 'iaqkqqxz gu xjynytiy trruaybdlccyya    bv a czra zm  ltogj', 'tmmom wqmajyndt nsw mbso eopzwfxd imqeob ptycja  nas', 'dksqd cj eqtnscksg e mwd  pkakmoghuczdofcjfjqvrcwkxgy', 'ceuvayvrbudkhc yfbgpf nbqfjoc veqqhwhw tq w c']

vocales='aeiouy'
respuesta=''
for x in lineas:
    vocale=0
    for y in x:
        for z in vocales:
            if y == z:
                vocale+=1
    respuesta+=str(vocale)+' '
print(respuesta)