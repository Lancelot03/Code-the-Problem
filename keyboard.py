n=input()
s=input()
a='qwertyuiopasdfghjkl;zxcvbnm,./'
st=[]
if n=='R':
	for i in s:
		st.append(a[a.index(i)-1])
else:
	for i in s:
		st.append(a[a.index(i)+1])
for i in st:
	print(i,end='')