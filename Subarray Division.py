#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    tp = (len(s)-m) + 1 #total number of pieces possible
    return len([2 for i in range(tp) if sum(s[i:i+m])==d])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
