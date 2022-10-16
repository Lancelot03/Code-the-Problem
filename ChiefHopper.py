n = int(input())
high = low = 0
arr = []

for i in input().split():
    arr.append(int(i))
    if(int(i) > high):
        high = int(i)
    if(int(i) < low):
        low = int(i)

def tester(x, arr):
    energy = x
    answer = True
    for height in arr:
        if(height > energy):
            energy -= (height - energy)
            if(energy < 0):
                return(False)
        else:
            energy += (energy - height)
    return(answer)     

cont = True
i = (high + low) // 2
dic = {}
while(cont):
    if(dic.get(i-1, tester(i-1, arr))):
        # i is too high
        high = i
        i = (high + low) // 2
    else:
        if(dic.get(i, tester(i, arr))):
            cont = False
        else:
            # i is too low, double it and set low to current i
            low = i
            i = ((i + high + 1) // 2)
            if(i == 0):
                i = 1

print(i)
