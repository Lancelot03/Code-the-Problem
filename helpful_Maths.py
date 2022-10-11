n=input().split('+')
o=0
tw=0
th=0
for i in n:
	if i=='1':
		o+=1
	elif i=='2':
		tw+=1
	elif i=='3':
		th+=1
e=(f"{'1+'*o}{'2+'*tw}{'3+'*th}")
e=e.rstrip('+')
print(e)