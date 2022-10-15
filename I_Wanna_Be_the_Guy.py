n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
c.extend(a[1:])
c.extend(b[1:])
c=list(set(c))
for i in range(1,n+1):
	if i not in c:
		print('Oh, my keyboard!')
		break
else:
	print('I become the guy.')