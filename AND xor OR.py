import math
import os
import random
import re
import sys

def andXorOr(a):
    stack = [a[0]]; max_val = -1<<256
    
    for item in a[1:]:
        while stack:
            m1,m2 = item, stack[-1]
            result = ((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2)
            if result > max_val:
                max_val = result
            if item < stack[-1]:
                stack.pop()
            else:
                break
        stack.append(item)
    return max_val
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
