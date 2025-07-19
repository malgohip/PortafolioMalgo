#!/bin/python

import math
import os
import random
import re
import sys

# write your code here
def avg(lst):
    sum=0
    for x in lst:
        sum+=x
    n=len(lst)
    aver = float(sum)/n
    return aver

if __name__ == '__main__':
    fptr = str(input())
    fptrlst=fptr.split()
    nums=[]
    for x in fptrlst:
        y=int(x)
        nums.append(y)

    res=avg(nums)
    
    print('%.2f' % res + '\n')