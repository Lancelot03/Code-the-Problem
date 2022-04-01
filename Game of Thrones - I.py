import math
import os
import random
import re
import sys
def gameOfThrones(s):
    return "YES" if len([i for i in set(s) if s.count(i)%2!=0]) <2 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
