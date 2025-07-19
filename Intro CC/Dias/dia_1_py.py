#Author: Sebastian Ochoa. Date: 02/06/2024
# -*- coding: utf-8 -*-

def clase_1 (valores: list)->str:
    retorno="Verga, ya te cargo"
    sumatoria=0
    for x in valores:
        sumatoria+=x
    promedio=round(sumatoria/len(valores),1)
    if promedio >= 3 and promedio <= 4:
        retorno="Bueno, no esta tan mal"
    elif promedio > 4 and promedio <= 5:
        retorno="Malnacido suertudo, eres grande"
    elif promedio > 5:
        retorno="Mk, sea serio, no joda, son valores de 0-5 (Sí, con decimales)"
    return retorno

print(clase_1([4,3.8,]))

x="Perra"
y="Amor mio"
print(f"Quieres que te diga {x } o prefieres {y}?")