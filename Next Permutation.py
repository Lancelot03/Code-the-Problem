class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
     
        if len(nums)<=2:

            return nums.reverse()
        k=len(nums)-2
        while k>=0 and nums[k]>=nums[k+1]:
            k-=1
        if k==-1:
            return nums.reverse()
        for x in range(len(nums)-1,k,-1):
            if nums[k]< nums[x]:
                nums[k], nums[x]=nums[x], nums[k]
                break
                
        nums[k+1:]=reversed(nums[k+1:])
