t=int(input())
a=list(map(int,input().split()))
su=sum(a)
a.sort(reverse=True)
c=0
b=0
t=0
for i in a:
	b+=i
	su-=i
	t+=1
	c=su
	if b>c:
		print(t)
		break
