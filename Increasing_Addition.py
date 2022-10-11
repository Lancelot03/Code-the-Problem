t=int(input())
for _ in range(t):
	n,q=map(int,input().split())
	a=list(map(int,input().split()))
	while q:
		q-=1
		i,x=map(int,input().split())
		a[i-1]=x
		m=0
		
		for i in range(n-1):
			if a[i]>a[i+1]:
				m=max(m,abs(a[i]-a[i+1]))
		print(m)