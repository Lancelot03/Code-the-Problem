n=int(input())
for _ in range(n):
	a=int(input())
	b=input()
	li=[]
	p=0
	m=0
	for i in b:
		if i.isalnum():
			li.append(int(i))
		elif i=="+":
			p+=1
		else:
			m+=1
	li.sort()
	lt=""
	for i in li:
		lt+=str(i)
	# print(lt)
	ans=''
	for i in range(len(lt)):
		if m>0:
			ans+=str(lt[i])+"-"
			m-=1
		elif p>=1:
			ans+=str(lt[i])+"+"
			p-=1
		else:
			t="".join(str(lt[i:]))
			ans+=t
			break
	
	print(ans[::-1])
			
		
		
	