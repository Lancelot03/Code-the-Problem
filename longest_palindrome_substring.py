class Solution:
	def longestPalindrome(self, s) :
		lis=[]
		if s==s[::-1]:lis.append(s)
		if len(s)==1:
			lis.append(s)
		elif len(s)==2:
			if s[0]==s[1]:
				lis.append(s)
			else:
				lis.append(s[0])
		for i in range(len(s)):
			j=len(s)
			while j-i>1:
				temp=s[i:j]
				j-=1
				if temp==temp[::-1]:
					lis.append(temp)
					break
		lis.sort(key=len,reverse=True)
		return lis
				
				
				
a=Solution()
print(a.longestPalindrome('abcda'))	
				