n=int(input())
for i in range(n):
	a=int(input())
	lis=list(map(int,input().split()))
	
	final=[]
	for i in lis:
		flag=0
		tem=lis.copy()
		tem.sort(reverse=True)
		tem.remove(i)
		for j in tem:
			if j<=2*i:
				flag=1
				final.append(j)
				break
		if flag==0:
			final.append(-1)
	print(*final)