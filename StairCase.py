#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    inc = 1
    for x in range(n):
        for i in range(n-inc):
            print(" ",end="")
        
        for x in range(inc):
            print("#",end="")
        print("")
        inc+=1
            

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
