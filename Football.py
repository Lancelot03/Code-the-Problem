a=0
b=0
s=1
t=1

n=int(input())
for i in range(n):
	st=input()
	if s==1:
		s=st
		a+=1
	elif t==1 and st!=s:
		t=st
		b+=1
	if st==s:
		a+=1
	else:
		b+=1
if a>b:
	print(s)
else:
	print(t)