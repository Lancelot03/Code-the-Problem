class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        def bs(l,r,target):
            if l==r:
                if nums[l]==target:
                    return l
                else:
                    return -1
            m = (l+r)//2
            if nums[m]==target:
                return m
            if nums[m]<nums[l]:
                if nums[m]<target<=nums[r]:
                    return bs(m+1, r, target)
                else:
                    return bs(l,m-1,target)
            else:
                if nums[l]<=target<nums[m]:
                    return bs(l,m-1,target)
                else:
                    return bs(m+1,r,target)
            
            return -1
        return bs(l,r,target)
