
import math
import os
import random
import re
import sys

def minimumLoss(price):
    tups = sorted(zip(price, range(len(price))), reverse=True)
    return min([tups[ix][0] - tups[ix+1][0] 
                for ix in range(len(price)-1)
                if tups[ix][1] < tups[ix+1][1]])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
