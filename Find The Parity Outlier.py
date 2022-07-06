def find_outlier(integers):
    even=[]
    odd=[]
    for i in integers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even)==1:
        return even[0]
    else:
        return odd[0]
