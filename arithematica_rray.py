t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	if n==sum(a):
		print(0)
	elif sum(a)>=n:
		print(sum(a)-n)
	else:
		print(1)