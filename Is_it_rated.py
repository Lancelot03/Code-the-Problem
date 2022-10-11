n=int(input())
li=[]
flag=False
for i in range(n):
	a,b=map(int,input().split())
	if a!=b:
		print('rated')
		flag=True
		break
	else:
		li.append(a)
li_copy=li.copy()		
li.sort(reverse=True)
if flag==True:
	pass
elif li==li_copy:
	print('maybe')
else:
	print('unrated')