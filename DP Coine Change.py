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
#second method 

N,M = list(map(int,input().strip().split(' ')))
coins = list(map(int,input().strip().split(' ')))

count = 0
def count_make_change_recursive(N, coins, M):
    if N < 0:
        return 0
    if N == 0:
        return 1
    if M <= 0:
        return 0
    return count_make_change(N-coins[M-1], coins, M) + count_make_change(N,coins,M-1)


def count_make_change_bottom_up(N, coins, M):
    counts = [0] * (N+1)
    counts[0] = 1
    for i in range(0, M):
        sum = 0
        for j in range(coins[i],N+1):
            counts[j] += counts[j-coins[i]]
    return counts[N]


print(count_make_change_bottom_up(N,coins,M))
