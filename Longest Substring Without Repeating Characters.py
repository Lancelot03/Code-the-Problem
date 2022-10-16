def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        dic={}
        maxi=start=0
        for i in range(len(s)):
            if s[i]in dic and start <= dic[s[i]]:
                start = dic[s[i]]+1
            else:
                maxi=max(maxi, i-start+1)
            dic[s[i]]=i
        return maxi
