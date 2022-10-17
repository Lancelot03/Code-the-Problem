a=input().lower()
b=[]
for i in a:
	if i in 'aeiou':
		pass
	else:
		b.append(f'.{i}')
print(b)
c=''
for i in b:
	c+=i
print(c)