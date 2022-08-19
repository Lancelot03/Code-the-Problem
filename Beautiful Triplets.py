import math
import os
import random
import re
import sys
def beautifulTriplets(d, arr):
     res = 0
    
     for el in arr:
            if el + d in arr and el + 2*d in arr:
                res += 1
            
     return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
