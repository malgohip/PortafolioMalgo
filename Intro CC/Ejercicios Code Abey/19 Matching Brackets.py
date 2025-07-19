#Author: Sebastian Ochoa. Date: 08/13/2024
# -*- coding: utf-8 -*-

"""
Se nos dan cadenas que contienen 4 tipos de paréntesis - redondo (), cuadrado [], rizado {} y angular <>. El objetivo es verificar si los paréntesis están en la secuencia correcta, ej.: cualquier paréntesis de apertura debería tener un paréntesis de cierre del mismo tipo en algún lugar posterior de la cadena, y que los pares de paréntesis no deberían superponerse (aunque podrían estar anidados):

(a+[b*c] - {d/3})  - aquí los paréntesis cuadrados y rizados
                        están anidados en los redondos

(a+[b*c) - 17]     - aquí los paréntesis cuadrados se superponen
                        con los redondos, lo cual no tiene sentido
Los Datos de entrada contendrán el número de casos de prueba en la primera línea.
Después seguirá el número especificado de líneas, cada una conteniendo un caso de prueba en forma de una secuencia de caracteres.
La Respuesta debería contener 1 (si el orden de los paréntesis es correcto) o 0 (si es incorrecto) para cada caso de prueba, y separados por espacios.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e19 Matching Brackets.txt','r')
P= a.readlines()

lineas=[]
for x in range(1,int(P[0])+1):
    F=P[x].strip()
    lineas.append(F)

print(lineas)
"""
lineas=['{d[)]}(h<c>(y)([e]u(%)))<^>{<u>({%}</>y%}', '(b)<([/]w{a{g}})(*)(/)[h]{g}{t}{e}[*]{z}{^}{y{h{f}<c>}}{g}>{^(^)}', '<[(^){+}+]{c}>[[ ]f]<f>[d]</[b]>[%{ }](c)', '<([%([x](e<e>) )(a)]((/)*)y[z]) >([ (c)[d{-}]]u)(*)<>(t)', '{e[/]{ }}[<h<->(u)( u}(u)[e] [(/)%])>(e){f(y)}](y){d{(f)y}}', '(*)[ ]{>(-)<v>h[y(^)]{{x}[[+]y]f{ }}(y))}[d]<^(b)(-)<a(>{/}', '[x]{{e}d[g](g)[(%[<u>d])e }{y}{{d}v{z[f]}[+]}{}<{[h]a}(e) >', '{d}[[[{c}a(u)<f{z}>]a]([c] (g))][[<v>w](e)h]', '(v<y>)[z]<[{<v><{y} ((+{v})%)+()>y[b]}t[<h>t]]< >w><[a<y>]>', '((w)<e>{g}e<*>)[*][{ }(a)]{{d}<c>{*}v<a>}', ']h[z][w<v>()[(-)y[-]<g></>[u]<[h]y><c{^}>{z}{+}]{(c)^}(-){<y>}(z)', '({c}{v}(v))<[%][c[w][c]<f>[-]]{-(x)} {d}<h>>[w[ z]/]][/]({b}y)', '[<(v(-))<{y[*>{e}w(y)<(e)f[h]>>(w)}t]<v>{b}{v}]<g>{-}[u]', '<g>{<<^>(^<{h}+[<y>-]{z}>[e[v]](<b>f))(-)(-)y>< >{+}([*]g[a])}', '[u]<{+}{ }(*){y}>{{z}(a)(x) }{/{- {b<<b>z>}[<{f}*>%]<y>}', '[t]<a><<g[ ]{^}><[d[h]]g><^>< <b>>x>[<u u]>(*)u]{-(v)}<a><b><>', '<{v(ye(c)(<+>t<[h]->(/))}<)><v><h>{[ ][z] [^]}>[d[(h) {v}<b>]{z}]', '{<f>*}<{c}[ ]t>(h)([x]{-}c{ {+}}{ })<>({[h]%}<-><%>w)', '{z}<t>{{<b> }(y(z))<g]{%}a}{e}<(f[-])</>(*)u>{^}[>']
str_resultado=''

for x in lineas:
    correspondiente={')': '(',']': '[','}': '{','>': '<'}
    resultado=1
    parent=[]
    for y in range(len(x)):
        if x[y] in "([{<":
            parent.append(x[y])
        elif x[y] in ")]}>":
            if not parent or parent[-1] != correspondiente[x[y]]:
                resultado = 0
                break
            parent.pop()
    if parent:
        resultado=0
    str_resultado+=str(resultado)+' '

print(str_resultado)