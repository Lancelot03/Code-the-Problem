import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    x=list(set(arr))
    y=sorted([(arr.count(i),i) for i in x], key=lambda x:x[0])[::-1]

    for i in range(len(y)):
        if y[0][0]==y[1][0] and y[0][1]>y[1][1]:
            return y[1][1]
        else:
            return y[0][1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
