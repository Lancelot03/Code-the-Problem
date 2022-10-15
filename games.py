n=int(input())
a=[]
b=[]
t=0
for i in range(n):
	c,d=input().split()
	a.append(c)
	b.append(d)
for i in a:
	for j in b:
		if i==j:
			t+=1
print(t)