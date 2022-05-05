
import math
import os
import random
import re
import sys

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    dp = [[i] for i in range(n + 1)]
    for [x, y] in cities:
        if dp[x] is dp[y]:
            continue
        [bigger, smaller] = [dp[x], dp[y]] if len(dp[x]) >= len(dp[y]) else [dp[y], dp[x]]
        for k in smaller:
            bigger.append(k)
            dp[k] = bigger
    dp = dp[1:]
    map = {id(dp[i]): dp[i] for i in range(n)}
    result = 0
    for k in map:
        result += c_lib
        result += (len(map[k]) - 1) * c_road
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
