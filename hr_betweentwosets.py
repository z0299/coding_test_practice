#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    gcd = []
    for i in range(1, b[0]+1):
        if b[0]%i == 0:
            gcd.append(i)
    
    for i in b[1:]:
        for j in gcd[:]:
            if i%j != 0:
                gcd.remove(j)

    for i in a:
        for j in gcd[:]:
            if j%i != 0:
                gcd.remove(j)
    
    return len(gcd)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()