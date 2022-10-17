n,k=map(int,input().split())
def dis(x1,x2,y1,y2):
	c=(((x2-x1)**2)+((y2-y1)**2))**0.5
	return c

total_dis=0
x1=0
y1=0
flag=0
for i in range(n):
	a,b=map(int,input().split())
	if flag==0:
		x1=a
		y1=b
		flag=1
	else:	
		distance=dis(x1,a,y1,b)
		x1=a
		y1=b
		total_dis+=distance
		#print(distance)

print((total_dis/50)*k)


	