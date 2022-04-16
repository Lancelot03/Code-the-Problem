import os
import sys
def getMoneySpent(keyboards, drives, s):
    return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= s]+[-1])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    s = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, s)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
