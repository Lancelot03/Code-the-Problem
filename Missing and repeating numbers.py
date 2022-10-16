def missingAndRepeating(arr, n):
    fa = [0 for i in range(n)]
    l = [0,0]
    for i in arr:
        if(fa[i-1]==1):
            l[1] = i
        else:
            fa[i-1] = 1
    for i in range(len(fa)):
        if(fa[i]==0):
            l[0] = i+1
    return l
