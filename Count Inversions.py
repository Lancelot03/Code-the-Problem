def getInversions(arr, n) :
    icount=0
    for i in range(n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                icount+=1
    return icount
