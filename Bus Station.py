import math
import os
import random
import re
import sys
def solve(a):
    # Write your code here
    s=sum(a)
    sums=[]
    for i in range(len(a)):
        t= (sums or [0])[-1]+a[i]
        if t<=s/2:
            sums.append(t)
        else:
            break
    sums.append(s)
    for i in sums:
        if not s%i:
            t=i
            for j in  a:
                t=t or i
                t-=j
                if t<0:
                    break
            else:
                 yield i
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
