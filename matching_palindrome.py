def ispalindrome(b):
	return b==b[::-1]
a=int(input())
for i in range(a):
	n=int(input())
	b=input()
	for i in range(1,len(b)+1):
		temp=b+b[:i]
		if ispalindrome(temp):
			print(b[:i])
			break
	