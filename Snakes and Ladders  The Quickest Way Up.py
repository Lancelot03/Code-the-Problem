#!/bin/python3

import math
import os
import random
import re
import sys

def quickestWayUp(ladders, snakes):
    ladders=dict(ladders)
    snakes=dict(snakes)
    #print(ladders)
    #print(snakes)
    #l=[]
    #s=()
    #for i in snakes:
    #    l.append(i)
    #print(l)
    #counter=1
    #for i in range(93,100):
    #    if i in l:
    #        counter +=1
    #if (100 not in ladders.value() and counter==7):
    #    return -1
    #print(counter)
    #start=1
    #final=100
    v = set()
    queue = []
    queue.append([1,0])
    v.add(1)
    while queue:
        position,step = queue.pop(0)
        if position in ladders.keys():
            position = ladders[position]

        if position == 100:
            return step
        for i in range(1,7):
            new_pos = position+i
            if new_pos not in v and new_pos not in snakes.keys():
                v.add(new_pos)
                queue.append([new_pos,step+1])
    return -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
