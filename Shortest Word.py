def find_short(s):
    l=float("inf")
    s=s.split()
    print(s)
    for i in s:
        if len(i) <l:
            l=len(i)
    return(l)
