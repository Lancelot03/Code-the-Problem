import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    return sum([ar.count(i)//2 for i in set(ar)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
