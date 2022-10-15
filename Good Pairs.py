from collections import Counter
from math import *
def nCr(n, r):
	p = 1
	k = 1
	if (n - r < r):
		r = n - r
	if (r != 0):
		while (r):
			p *= n
			k *= r
			m = gcd(p, k)
			p //= m
			k //= m
			n -= 1
			r -= 1 
	else:
		p = 1
	return p

n=int(input())
for _ in range(n):
	a=int(input())
	lis=list(map(int,input().split()))
	count=0
	a=Counter(lis)
	for i in a:
		b=a[i]
		if b==2:
		    count+=1
		if b==3:
		    count+=3
		if b>3:
			count+=int(nCr(b,2))
	print(count)
