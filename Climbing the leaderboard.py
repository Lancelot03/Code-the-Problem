import sys
from collections import Counter
from bisect import bisect_left

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here

counts = Counter(scores)
counts = sorted(counts)
n = len(counts)
for a in alice:
    i = bisect_left(counts, a)
    if i < n and counts[i]==a:
        print(n - i)
    else:
        print(n+1-i)
