n=input()
upper=0
lower=0
for i in n:
	if i.isupper() ==True:
		upper+=1
	else:
		lower+=1
if upper>lower:
	print(n.upper())
else:
	print(n.lower())


#hello this code is written by amit yadav
