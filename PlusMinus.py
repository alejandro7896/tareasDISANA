#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    div = len(arr)
    pos = 0
    zero = 0
    neg = 0
    for x in arr:
        if x == 0:
            zero+=1
        elif x > 0:
            pos +=1
        elif x < 0:
            neg +=1
    r_p = pos/div
    r_n = neg/div
    r_z = zero/div
    print(r_p)
    print(r_n)
    print(r_z)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
