n=int(input())
for _ in range(n):
	a=int(input())
	#a=a//2
	flag=0
	for i in range(1,int(a**0.5)):
		if ((a-(i*2))%(i+2) and a!=2*i):
			flag+=1
			break
			
				
	if flag==0:
		print('NO')
	else:
		print("YES")