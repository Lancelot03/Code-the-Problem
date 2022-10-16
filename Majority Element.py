def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i]=1
        return max(dic, key=dic.get)
