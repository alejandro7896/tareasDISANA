#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sumas = []
    
    for x in range(len(arr)):
        _sum = 0
        for l in range(len(arr)):
            if l == x:
                continue
            _sum += arr[l]
        sumas.append(_sum)
    print(str(min(sumas))+" "+str(max(sumas)))
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
