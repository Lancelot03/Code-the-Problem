import math
import os
import random
import re
import sys

def chiefHopper(arr):
    en=0
    for h in (arr[::-1]):
        en=(en+h+1)//2
    return en
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
