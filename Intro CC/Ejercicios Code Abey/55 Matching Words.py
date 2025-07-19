#Author: Sebastian Ochoa. Date: 08/15/2024
# -*- coding: utf-8 -*-

"""
Ali-Baba found a secret cave with treasures, stored by The Forty Thieves. However, famous magical phrase Open Sesame obviously does not work.

Instead there is a long and strange text inscribed on the stone wall - and Ali-Baba guessed that one should find matching words in this inscription (i.e. ones which are encountered more than once) and pronounce them in alphabetical order.

We are to help the poor craftsman to access the thieves' treasury. Let's write a program that sieves necessary words from the given text, and prints them in the proper order.

Input data consist of about 300 words, each made of 3 Latin letters. The end is signaled by the word end.
Answer should contain all the words which are encountered more than once in lexicographic order.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e55 Matching Words.txt','r')
P= a.readlines()

palabras=P[0].strip().split()
palabras.pop(-1)

print(palabras)
"""
palabras=['bop', 'buq', 'luk', 'nop', 'bix', 'dac', 'buc', 'rox', 'doc', 'zof', 'luf', 'jup', 'nix', 'dut', 'rik', 'gok', 'vux', 'zyh', 'gof', 'nop', 'mys', 'zit', 'bet', 'nak', 'jap', 'mih', 'ros', 'mix', 'lyp', 'dex', 'jiq', 'jit', 'buh', 'lip', 'myt', 'gas', 'byt', 'not', 'naq', 'zos', 'but', 'zys', 'nyk', 'nuc', 'jox', 'zof', 'nat', 'gyq', 'zoh', 'gih', 'vot', 'vet', 'vyh', 'mac', 'dos', 'gip', 'vuh', 'mep', 'ris', 'zas', 'nik', 'bap', 'vex', 'zik', 'nis', 'mis', 'vat', 'jac', 'zah', 'jok', 'dec', 'gyt', 'mih', 'gyq', 'bes', 'nyk', 'nyx', 'nat', 'jyh', 'ric', 'zaq', 'guq', 'box', 'jak', 'beh', 'zas', 'ruh', 'mux', 'duh', 'loq', 'lac', 'ref', 'mox', 'jop', 'bas', 'gap', 'myk', 'vyt', 'goh', 'bop', 'jis', 'get', 'byx', 'req', 'bik', 'loq', 'max', 'roc', 'zah', 'gaq', 'zit', 'nuf', 'jet', 'nyh', 'vah', 'dup', 'vus', 'rax', 'guf', 'box', 'nas', 'gyc', 'zyx', 'nop', 'dop', 'nys', 'rop', 'zas', 'bat', 'jah', 'zet', 'ret', 'jox', 'gyp', 'byk', 'myf', 'lyt', 'voh', 'dos', 'rut', 'veq', 'gec', 'mof', 'rus', 'bah', 'dah', 'mop', 'git', 'lot', 'luc', 'lax', 'rap', 'ref', 'gyf', 'vys', 'bos', 'nos', 'vuk', 'zyc', 'mis', 'moq', 'gyx', 'bip', 'las', 'lis', 'vok', 'nih', 'byh', 'vax', 'nac', 'mep', 'jyp', 'bec', 'doh', 'muk', 'byf', 'nip', 'nyp', 'zos', 'rax', 'rat', 'dah', 'miq', 'nyh', 'lip', 'vep', 'vaf', 'voc', 'dyc', 'mis', 'myf', 'met', 'zyc', 'reh', 'lic', 'neh', 'neh', 'zap', 'dyh', 'nos', 'zus', 'def', 'gif', 'gek', 'bef', 'nyk', 'leh', 'dec', 'lof', 'mit', 'dix', 'nus', 'nik', 'ryh', 'vac', 'jih', 'ric', 'zoh', 'lus', 'nik', 'vuq', 'baf', 'def', 'vup', 'zax', 'veh', 'mat', 'gif', 'bah', 'bac', 'zak', 'dop', 'boq', 'nit', 'ryp', 'zuf', 'juc', 'noc', 'riq', 'gux', 'dyt', 'dyh', 'duq', 'gof', 'gat', 'vet', 'bys', 'lyf', 'naq', 'dit', 'buh', 'vec', 'ves', 'mif', 'mas', 'lys', 'buk', 'mec', 'zus', 'vus', 'lox', 'gas', 'lys', 'lys', 'vyc', 'byx', 'mep', 'bik', 'jah', 'byq', 'mok', 'ret', 'nyx', 'bex', 'zuk', 'noh', 'gup', 'bix', 'vas', 'bas', 'guf', 'mek', 'nok', 'nit', 'lok', 'lic', 'dyp', 'vis', 'ruk', 'mik', 'rut', 'juf', 'vuf', 'jot', 'zik', 'dyf', 'bat', 'mep', 'muc', 'dot', 'jaf', 'vec', 'los', 'duf', 'ziq', 'leh', 'mah', 'nep', 'jap', 'dop']

respuesta=''
cantidad={}
for x in palabras:
    if x in cantidad:
        cantidad[x]+=1
    else:
        cantidad[x]=1
repetidas = [pal for pal, cant in cantidad.items() if cant > 1]
repetidas.sort()
for y in repetidas:
    respuesta+=y+' '
print(respuesta)