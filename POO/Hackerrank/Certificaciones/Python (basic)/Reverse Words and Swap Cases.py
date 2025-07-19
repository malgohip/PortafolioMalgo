#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words=sentence.split()
    words.reverse()
    rev_sentence=""
    for i in words:
        rev_sentence+=i.swapcase()+" "
    return rev_sentence

if __name__ == '__main__':
    sentence = str(input())

    res=reverse_words_order_and_swap_cases(sentence)
    
    print(res + '\n')