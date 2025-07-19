#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Once upon a time, when I was teaching electronics in the school, I was offering the following task to newcomers in order to check their manner of thinking about problems:

The girls are pasturing pigs at the field. In total they have 106 legs and 336 breasts. How many girls and pigs are there?

Pigs and girls were chosen not just for a joke! The main reason was that the number of breasts for a pig was unknown. So some pupils were telling that "The problem could not be solved", while others were pretending that "there are infinite number of solutions since we have 3 variables and 2 equations".

Of course it is not so! The variables in this problem have some obvious limitations, hence only quite finite amount of solutions could be found - and of them only one looked believable.

Now you are to solve the "extended" version of the task. As before you will be given the number of legs and breasts and your goal is to tell the number of possible solutions.

Input data will have the number of testcases in the first line.
Next lines will contain a pair of values each - the amounts of legs and breasts - the first of them will always be smaller than the second.
Answer should give the amount of solutions for each case.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e97 Girls and Pigs.txt','r')
P= a.readlines()

valores=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    valores.append(F)

print(valores)
"""
valores=[[906, 5222], [1758, 3230], [3632, 18644], [38, 86], [24, 64], [86, 282], [152, 350], [24, 74], [334, 1054], [248, 1112], [624, 3504], [108, 238], [3532, 8308], [122, 570]]

def count_solutions(legs, breasts):
    count = 0
    
    # Iterate over possible number of pigs (P)
    for P in range(0, (legs // 4) + 1):
        remaining_legs = legs - 4 * P
        
        # Check if remaining legs can be divided evenly among girls
        if remaining_legs % 2 == 0:
            G = remaining_legs // 2
            
            # Check if remaining breasts can be divided evenly among pigs and girls
            if G >= 0:
                remaining_breasts = breasts - 2 * G
                
                if P > 0 and remaining_breasts % P == 0:
                    B = remaining_breasts // P
                    # Check if the number of breasts per pig is positive and even
                    if B > 0 and B % 2 == 0:
                        count += 1
                elif P == 0 and remaining_breasts == 0:
                    count += 1

    return count

respuesta=''
for x in valores:
    respuesta+=str(count_solutions(x[0], x[1]))+' '
print(respuesta)