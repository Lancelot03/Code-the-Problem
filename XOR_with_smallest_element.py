import heapq as heap
t=int(input())
for i in range(t):
	n,x,y=map(int,input().split())
	a=list(map(int,input().split()))
	if n==1:
		if y%2==0:
			print(a[0])
		else:
			print(a[0]^x)
	else:
		heap.heapify(a) 
		for i in range(y):
			b=heap.heappop(a)
			c=b^x
			heap.heappush(a,c)
			d=heap.heappop(a)
			if d==c:
				if (y-i+1)%2==0:
					heap.heappush(a,d)
					break
				else:
					heap.heappush(a,b)
					break
			else:
				heap.heappush(a,d)
				
		a.sort()
		print(*a)
	
		