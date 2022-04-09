import math
import os
import random
import re
import sys
def ways(n, coins):
    lookup = [1] + [0] * n
    for coin in coins:
        for i in range(n+1-coin):
            lookup[i+coin] += lookup[i]
    return lookup[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    coins = list(map(int, input().rstrip().split()))

    res = ways(n, coins)

    fptr.write(str(res) + '\n')

    fptr.close()
