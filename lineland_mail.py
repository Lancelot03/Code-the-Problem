n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
	if i==0:
		print(abs(a[0]-a[i+1]),abs(a[-1]-a[0]))
	elif i==a.index(a[-1]):
		print(abs(a[-2]-a[-1]),abs(a[0]-a[-1]))
	else:
		if abs(a[i-1]-a[i])>abs(a[i+1]-a[i]):
			if abs(a[-1]-a[i])>abs(a[0]-a[i]):
				print(abs(a[i+1]-a[i]),abs(a[i]-a[-1]))
			else:
				print(abs(a[i+1]-a[i]),abs(a[i]-a[0]))
		else:
			if abs(a[-1]-a[i])>abs(a[0]-a[i]):
				print(abs(a[i-1]-a[i]),abs(a[i]-a[-1]))
			else:
				print(abs(a[i-1]-a[i]),abs(a[i]-a[0]))
			#print(abs(a[i-1]-a[i]),abs(a[i]-a[-1])
		
	
	