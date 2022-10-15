n=int(input())
for _ in range(n):
	a=int(input())
	lis=list(map(int,input().split()))
	lis.sort()
	max_ele=-1e18
	min_ele=1e18
	max_ele=max(lis[0]*lis[0],lis[-1]*lis[-1])
	if lis[0]<0 and lis[-1]>0:
		min_ele=lis[0]*lis[-1]
	else:
		for i in range(a):
			min_ele=min(min_ele,lis[i]*lis[i])
	print(f"{min_ele} {max_ele}")