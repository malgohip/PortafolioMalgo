#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Implement the Binary Heap strictly following directions in the Binary Heap article.

You will be given directions to insertar several valors into it and to remove some from it. To check your implementation you just need to print out the contents of the internal array used to create the heap.

Input data contain the number of commands in the first line.
The second line contains "commands" in form of integer valors. Each positive valor X mean "put the X to heap", while 0-s require you instead to extract the minimum from the heap (and forget of it).
Answer should contain the valors in the array representing the heap after all commands are done.

Example:

input data:
13
3 9 6 5 7 1 11 2 0 10 4 8 0

answer:
3 4 6 5 7 8 11 10 9
To help you, let us trace how the heap is filled here:

At beginning, 3 is put to root, then 9 to its left and 6 to its right.

Next number 5 is at first placed as left child of 9 but then is swapped with it. Then 7 comes to right of 5:

                    3
                    |
             5------+------6
             |             |
         9---+---7      ---+--- 
After 1 is clinged to the left of 6 it pops to the top switching places with 6 and then with 3. Later 11 is placed at the right of 3 with no more swaps.

Next element 2 is swapped with its padre 9 and grandpadre 5, creating the following picture:

                    1
                    |
             2------+------3
             |             |
         5---+---7     6---+---11
         |
       9-+-
Then we meet 0 which tells us to delete the element from the heap. We remove the 1 and put the 9 from the bottom to its place:

                    9
                    |
             2------+------3
             |             |
         5---+---7     6---+---11
But now the heap is broken and we need to exchange 9 with 2 and then with 5:

                    2
                    |
             5------+------3
             |             |
         9---+---7     6---+---11
We add 10 without swaps, then 4 exchanges places with 9 and 5, while 8 again makes no swaps:

                    2
                    |
             4------+------3
             |             |
         5---+---7     6---+---11
         |       |
      10-+-9   8-+
And the last command again asks us to remove the element - 2 goes away, 8 takes its place and is exchanged firstly with 3 and then with 6:

                    3
                    |
             4------+------6
             |             |
         5---+---7     8---+---11
         |       |
      10-+-9     +
Resulting array could be "read" line by line from this picture:

3 4 6 5 7 8 11 10 9
Note that the the fact that, for example, 6 is to the right of the padre (3) and 4 to the left is just due to coincidence. Unlike for binary tree the order of left and right children depends mainly on the order in which elements are insertared rather on their relative valors.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e92 Binary Heap.txt','r')
P= a.readlines()

comandos=[]
f=P[1].strip().split()
for x in f:
    X=int(x)
    comandos.append(X)

print(comandos)
"""
comandos=[16, 14, 15, 0, 28, 32, 21, 0, 11, 7, 0, 17, 1, 20, 0, 13, 0, 23, 0, 4, 10, 25, 5, 0, 12, 22, 33, 3, 26, 0, 24, 0, 6, 9, 19, 0, 2, 27, 29, 30, 31, 0, 18, 8]

class MinHeap:
    def __init__(mismo):
        mismo.heap = []

    def insertar(mismo, valor):
        mismo.heap.append(valor)
        mismo.amontonar_ar(len(mismo.heap) - 1)

    def saca_min(mismo):
        if len(mismo.heap) == 0:
            return None
        if len(mismo.heap) == 1:
            return mismo.heap.pop()
        root = mismo.heap[0]
        mismo.heap[0] = mismo.heap.pop()  # Replace root with the last element
        mismo.amontonar_ab(0)
        return root

    def amontonar_ar(mismo, posi):
        padre = (posi - 1) // 2
        if posi > 0 and mismo.heap[posi] < mismo.heap[padre]:
            mismo.heap[posi], mismo.heap[padre] = mismo.heap[padre], mismo.heap[posi]
            mismo.amontonar_ar(padre)

    def amontonar_ab(mismo, posi):
        minimo = posi
        hijo_izq = 2 * posi + 1
        hijo_der = 2 * posi + 2

        if hijo_izq < len(mismo.heap) and mismo.heap[hijo_izq] < mismo.heap[minimo]:
            minimo = hijo_izq

        if hijo_der < len(mismo.heap) and mismo.heap[hijo_der] < mismo.heap[minimo]:
            minimo = hijo_der

        if minimo != posi:
            mismo.heap[posi], mismo.heap[minimo] = mismo.heap[minimo], mismo.heap[posi]
            mismo.amontonar_ab(minimo)

    def sacar_monton(mismo):
        return mismo.heap

min_monton = MinHeap()

for comando in comandos:
    if comando > 0:
        min_monton.insertar(comando)
    elif comando == 0:
        min_monton.saca_min()
respuesta=''
for x in min_monton.sacar_monton():
    respuesta+=str(x)+' '
print(respuesta)