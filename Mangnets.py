n=int(input())
g=0
temp=0
for i in range(n):
	a=int(input())
	if a!=temp:
		temp=a
		g+=1
print(g)