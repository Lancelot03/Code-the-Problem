n=int(input())
a=list(map(int,input().split()))
o=a.count(1)
tw=a.count(2)
th=a.count(3)
e=min(o,th,tw)
print(e)
ia=0
ib=0
ic=0
for i in range(e):
	print(a.index(1,ia)+1,end=' ')
	print(a.index(2,ib)+1,end=' ')
	print(a.index(3,ic)+1)
	if (e-i)>1:
		ia=a.index(1,a.index(1,ia)+1)
		ib=a.index(2,a.index(2,ib)+1)
		ic=a.index(3,a.index(3,ic)+1)
	
	
