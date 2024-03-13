#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if "AM" in s:
        if "12" == s[0:2]:
            s = "00" + s[2:]
        return s.replace("AM", "")
    if "PM" in s:
        s = s.replace("PM", "")
        if s[0:2] == '12':
            return s
        horas = int(s[0:2])
        horas = horas+12
        s = str(horas) + s[2:]
        return s
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
