x=0
n=0
b=[]
n=int(input())
for i in range(n):
	a=input()
	for i in a:
		b.append(i)
		
		
c=list(set(b))
if len(c)==1:
	print('YES')
else:
	c.pop(c.index(b[0]))
	d=b.count(b[0])
	print(d)
	e=b.count(c[0])
	print(e)
	if d==(2*n-1) and e==(n**2-d):
		print('YES')
	else:
		print('NO') 
		