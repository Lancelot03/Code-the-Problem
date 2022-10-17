n,m,a=map(int,input().split())
if n<=a and m<=a:
	print(1)
else:
	if n%a!=0:
		b=n//a+1
	else:
		b=n//a
	if m%a!=0:
		c=m//a+1
	else:
		c=m//a
	print(b*c)	
